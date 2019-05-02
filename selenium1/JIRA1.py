from selenium import webdriver
from selenium.webdriver.common.by import By
from jira.client import JIRA
import datetime

driver = webdriver.Chrome()
driver.implicitly_wait(10)

def run():
    """
    login confluence
    :return: None
    """
    driver.get(confluence_url)
    login()
    click_key('#space-menu-link')
    driver.find_element_by_partial_link_text('data center').click()
    click_key('#plusminus3773763-0')
    click_key('#plusminus3774539-0')
    click_key('#plusminus3774542-0')
    click_key('#plusminus13533496-0')
    current_time = datetime.datetime.now().strftime("%Y%m%d")
    try:
        result = driver.find_element_by_partial_link_text('NSTS （{}）'.format(current_time))
    except:
        result = None
    if result is None:
        create_new_page(0)
    else:
        result.click()
        click_key('#editPageLink')
    fill_data()
    click_key('#rte-button-publish')

def login():
    """
    Keep the login status alive
    :return: None
    """
    result = driver.find_element(By.CSS_SELECTOR, '#loginButton')
    if result:
        input_key('#os_username', username)
        input_key('#os_password', password)
        click_key('#loginButton')

def input_key(css_path, content):
    """
    Enter information into the input box.
    :param css_path: Locate the input box.
    :param content: Information for the input box.
    :return: None
    """
    driver.find_element(By.CSS_SELECTOR, css_path).clear()
    driver.find_element(By.CSS_SELECTOR, css_path).send_keys(content)

def click_key(css_path):
    """
    Click the corresponding button
    :param css_path: Button path
    :return: None
    """
    driver.find_element(By.CSS_SELECTOR, css_path).click()

def create_new_page(days):
    """
    Add a daily page if it is missing
    :param days: Daily's interval days
    :return: None
    """
    days += 1
    page_time = datetime.datetime.now() + datetime.timedelta(days=days)
    page_time = page_time.strftime("%Y%m%d")
    result = driver.find_element_by_partial_link_text('NSTS （{}）'.format(page_time))
    if len(result) == 0:
        create_new_page(days)
    else:
        result.click()
        click_key('#action-menu-link')
        click_key('#action-copy-page-link')
        click_key('#copy-dialog-next')
        current_time = datetime.datetime.now().strftime("%Y%m%d")
        input_key('#content-title', 'NSTS （{}）'.format(current_time))
        input_key('#tinymce>h2', '{}日报'.format(current_time))

def jira_statistics(status=None, priority=None, severity=None):
    """
    Today's statistics of jira
    :return: The result of today's jira statistics
    """
    jira = JIRA(server=jira_url, basic_auth=(username, password))
    priority = 'and priority={}'.format(priority) if priority else ''
    severity = 'and 严重级别={}'.format(severity) if severity else ''
    if status:
        status = '({}, reopened)'.format(status) if status == 'open' else '({})'.format(status)
        issues_in_proj = jira.search_issues('project=NSTS  and status in {status} and issuetype="故障" and updated >= "-24H" {priority} {severity}'.format(status=status, priority=priority, severity=severity),
                                            maxResults=100)
    else:
        issues_in_proj = jira.search_issues('project=NSTS  and status in (open, reopened) and issuetype="故障" and updated < "-24H" {priority} {severity}'.format(priority=priority, severity=severity), maxResults=100)
    return len(issues_in_proj)

def jira_result():
    """
    Summary the statistics of jira
    :return: Summary result
    """
    result = []
    # Different priority bug statistics
    dif_pri_bugs = []
    # Different severity bug statistics
    dif_sev_bugs = []
    # Covariance item
    covariance_item = ['open', 'resolved', 'closed', None]
    # Covariance item of priority
    cov_item_of_pri = ['P0-Highest', 'P1-High', 'P2-Medium', 'P3-Low', 'P4-Lowest', None]
    # Covariance item of severity
    cov_item_of_sev = ['S0-Blocker', 'S1-Major', 'S2-Normal', 'S3-Minor', 'S4-Enhancement', None]
    for k, v in enumerate(covariance_item):
        dif_pri_bug = []
        for x, y in enumerate(cov_item_of_pri):
            dif_pri_bug.append(jira_statistics(status=v, priority=y))
        dif_pri_bugs.append(dif_pri_bug)
        dif_sev_bug = []
        for i, j in enumerate(cov_item_of_sev):
            dif_sev_bug.append(jira_statistics(status=v, severity=j))
        dif_sev_bugs.append(dif_sev_bug)
    result.append(dif_pri_bugs)
    result.append(dif_sev_bugs)
    return result

def fill_data():
    """
    Fill the statistical results of jira into the table
    :return: None
    """
    results = jira_result()
    driver.switch_to.frame('wysiwygTextarea_ifr')
    for index, result in enumerate(results):
        for i, j in enumerate(result):
            for x, y in enumerate(j):
                first_child = 15 if index == 0 else 18
                sencond_child = i + 1
                third_child = x + 2
                # fill data into bugfix table
                init_js = 'document.querySelector(\'#tinymce > table:nth-child({}) > tbody > tr:nth-child({}) > td:nth-child({})\').innerText={}; '.format(first_child, sencond_child, third_child, y)
                driver.execute_script(init_js)
    driver.switch_to.default_content()

if __name__ == '__main__':
    run()
    driver.quit()
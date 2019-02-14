import requests
image_url = "https://www.python.org/static/community_logos/python-logo-master-v3-TM.png"

r = requests.get(image_url) # create HTTP response object

with open("python_logo.png",'wb') as f:
    f.write(r.content)
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

archive_url = "http://www-personal.umich.edu/~csev/books/py4inf/media/"

def get_video_links():
    r = requests.get(archive_url)
    soup = BeautifulSoup(r.content, 'html5lib')
    links = soup.findAll('a')
    video_links = [archive_url + link['href'] for link in links if link['href'].endswith('mp4')]
    #print video_links#
    return video_links

def download_video_series(video_links):
    for link in video_links:
	    #u'http://www-personal.umich.edu/~csev/books/py4inf/media/PY4INF-13-Webservices-01.mp4'里面的第一项内容，前缀u表示是unicode的内容类型
        file_name = link.split('/')[-1]
        print("Downloading file:%s" % file_name)
        r = requests.get(link, stream=True)
        # download started
        with open(file_name, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024 * 1024):
                if chunk:
                    f.write(chunk)
        print("%s downloaded!\n" % file_name)
    print("All videos downloaded!")
    return

if __name__ == "__main__":
    video_links = get_video_links()
    download_video_series(video_links)
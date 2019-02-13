#http://python.jobbole.com/88325/
from wordcloud import WordCloud
import PIL
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import codecs

'''
Note:Following 3 lines are for the problem of Chinese Font display
'''

from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False

def wordcloudplot(txt):

    '''
        Note：一定要加上以下三行代码。
           最早把这三行注释掉，ubuntu系统缺少matplotlib支持中文字体
            生成的标签云中文显示为口，查了很多材料，都没有明确说明这个问题
            最好加上这三行，或者自己添加为自己喜欢的字体！！！
    '''

    path='msyh.ttf'
    path=unicode(path, 'utf8').encode('gb18030')
    alice_mask = np.array(PIL.Image.open('air.jpg'))
    wordcloud = WordCloud(font_path=path,
                          background_color="white",
                          margin=5,
                          width=1800,
                          height=800,
                          mask=alice_mask,
                          max_words=2000,
                          max_font_size=60,
                          random_state=42)
    #wordcloud = wordcloud.generate(txt)
    wordcloud = wordcloud.fit_words(txt)
    wordcloud.to_file('output.png')
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()

def main():
    a=[]
    f=open(r'android.txt','r').readlines()
    for line in f:
        tempArr = line.strip().split("  ")
        #tempArr[0] = tempArr[0].decode("utf-8")
        tempArr[1] = int(tempArr[1])
        a.append(tempArr)
    wordcloudplot(a)

if __name__=='__main__':
    main()
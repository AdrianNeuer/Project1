import pandas as pd 
import numpy as np 
from wordcloud import WordCloud,STOPWORDS,ImageColorGenerator
import jieba
import matplotlib.pyplot as plt
from PIL import Image


DF_STANDARD=pd.read_excel('知乎用户.xlsx')
STOP_WORDS_FILE_PATH='zhihustop.txt'

def makewc(x):
    d=DF_STANDARD[x].dropna(axis=0)
    mytext=' '.join(d)
    image=np.array(Image.open(x+'.jpg'))
    image_color=ImageColorGenerator(image)
    wc = WordCloud( 
                scale=3,
                background_color = 'white',  # 设置背景颜色
                #mask = backgroud_Image,      # 设置背景图片
                max_words = 50,            # 设置最大现实的字数
                stopwords = STOP_WORDS_FILE_PATH,       # 设置停用词
                font_path = 'SIMLI.TTF',    # 设置字体格式，如不设置显示不了中文
                max_font_size = 60,          # 设置字体最大值
                color_func=image_color,             #设置关键字的字体颜色
                random_state = 42,           # 设置有多少种随机生成状态，即有多少种配色方案
                mask=image
                    ).generate(mytext)
    plt.imshow(wc)
    plt.axis('off')
    wc.to_file(x+'.png')

if __name__ =='__main__':
    # worldcloud绘制
    makewc('学校')
    makewc('专业')
    makewc('所在行业')
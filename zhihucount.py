import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from pyecharts import options as opts
from pyecharts.charts import Pie
from pyecharts.globals import ThemeType



df=pd.read_excel('知乎用户.xlsx')

#plt画图太丑
'''plt.rcParams['font.sans-serif']=['SimHei']
explode = (0.05, 0, 0, 0, 0)  # 0.1为第二个元素凸出距离
colors = ['tomato', 'lightskyblue', 'goldenrod', 'green', 'y']
# 饼图绘制函数
plt.figure(figsize=(8, 6))
plt.pie(sizes, explode=explode, labels=labels, colors=colors, 
        autopct='%1.1f%%', shadow=False, pctdistance=1.3, 
        startangle=90, textprops={'fontsize': 16, 'color': 'w'})
plt.title('知乎用户粉丝数量分布图')
plt.axis('equal')
plt.legend(loc='best')
#plt.savefig('age.png', dpi=600)
plt.show()'''

#知乎用户粉丝数量分布图
labels1 = ['0-100', '100-1000', '1000-5000', '5000-10000', '10000-100000','100000以上']
sizes1 = [len(df[(df['粉丝'] <= 100)]), 
         len(df[(df['粉丝'] >= 100) & (df['粉丝'] < 1000)]), 
         len(df[(df['粉丝'] >= 1000) & (df['粉丝'] < 5000)]), 
         len(df[(df['粉丝'] >= 5000) & (df['粉丝'] < 10000)]), 
         len(df[(df['粉丝'] >= 10000) & (df['粉丝'] < 100000)]),
         len(df[(df['粉丝'] >= 100000)])]
print(sizes1)

c = (
    Pie(init_opts=opts.InitOpts(theme=ThemeType.VINTAGE))
    .add(
        "",
        [list(z) for z in zip(labels1, sizes1)]
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="知乎用户粉丝数量分布图",pos_bottom='center'),
        legend_opts=opts.LegendOpts(pos_left="15%"), 
    )
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {d}%"))
)
c.render("知乎用户粉丝数量分布图.html")


#知乎用户获赞数分布图
labels2 = ['0-100', '100-1000', '1000-5000', '5000-10000', '10000-100000','100000以上']
sizes2 = [len(df[(df['获赞'] <= 100)]), 
         len(df[(df['获赞'] >= 100) & (df['获赞'] < 1000)]), 
         len(df[(df['获赞'] >= 1000) & (df['获赞'] < 5000)]), 
         len(df[(df['获赞'] >= 5000) & (df['获赞'] < 10000)]), 
         len(df[(df['获赞'] >= 10000) & (df['获赞'] < 100000)]),
         len(df[(df['获赞'] >= 100000)])]
print(sizes2)


e = (
    Pie(init_opts=opts.InitOpts(theme=ThemeType.MACARONS))
    .add(
        "",
        [list(z) for z in zip(labels2, sizes2)],
        radius=["40%", "75%"],
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="知乎用户获赞数分布图"),
        legend_opts=opts.LegendOpts(
            orient="vertical", 
            pos_top="15%",
            pos_left="2%"),
    )
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {d}%"))
)
e.render("知乎用户获赞数分布图.html")

#知乎用户关注数分布图
labels3 = ['0-10', '10-50', '50-100', '100-500', '500-1000','1000以上']
sizes3 = [len(df[(df['获赞'] <= 10)]), 
         len(df[(df['获赞'] >= 10) & (df['获赞'] < 50)]), 
         len(df[(df['获赞'] >= 50) & (df['获赞'] < 100)]), 
         len(df[(df['获赞'] >= 100) & (df['获赞'] < 500)]), 
         len(df[(df['获赞'] >= 500) & (df['获赞'] < 1000)]),
         len(df[(df['获赞'] >= 1000)])]
print(sizes3)
f = (
    Pie(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
    .add(
        "",
        [list(z) for z in zip(labels3, sizes3)],
        radius=["30%", "75%"],
        rosetype="radius",
    )

    .set_global_opts(title_opts=opts.TitleOpts(title="知乎用户关注数分布图"))    
)
f.render("知乎用户关注数分布图.html")



#知乎用户感谢数分布图
labels4 = ['0-100', '100-1000', '1000-5000', '5000-10000', '10000-100000','100000以上']
sizes4 = [len(df[(df['感谢'] <= 100)]), 
         len(df[(df['感谢'] >= 100) & (df['感谢'] < 1000)]), 
         len(df[(df['感谢'] >= 1000) & (df['感谢'] < 5000)]), 
         len(df[(df['感谢'] >= 5000) & (df['感谢'] < 10000)]), 
         len(df[(df['感谢'] >= 10000) & (df['感谢'] < 100000)]),
         len(df[(df['感谢'] >= 100000)])]
print(sizes4)
g = (
    Pie(init_opts=opts.InitOpts(theme=ThemeType.MACARONS))
    .add(
        "",
        [list(z) for z in zip(labels4, sizes4)],
        radius=["30%", "80%"]
    )
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {d}%"))
    .set_global_opts(title_opts=opts.TitleOpts(title="知乎用户感谢数分布图",pos_bottom='center'))    
)
g.render("知乎用户感谢数分布图.html")
    
#知乎用户收藏数分布图
labels5 = ['0-100', '100-1000', '1000-5000', '5000-10000', '10000-100000','100000以上']
sizes5 = [len(df[(df['收藏'] <= 100)]), 
         len(df[(df['收藏'] >= 100) & (df['收藏'] < 1000)]), 
         len(df[(df['收藏'] >= 1000) & (df['收藏'] < 5000)]), 
         len(df[(df['收藏'] >= 5000) & (df['收藏'] < 10000)]), 
         len(df[(df['收藏'] >= 10000) & (df['收藏'] < 100000)]),
         len(df[(df['收藏'] >= 100000)])]
print(sizes5)

h = (
    Pie(init_opts=opts.InitOpts(theme=ThemeType.WESTEROS))
    .add(
        "",
        [list(z) for z in zip(labels5, sizes5)],
        radius=["40%", "75%"],
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="知乎用户收藏数分布图"),
        legend_opts=opts.LegendOpts(
            orient="vertical", 
            pos_top="15%",
            pos_left="2%"),
    )
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {d}%"))
)
h.render("知乎用户收藏数分布图.html")

#知乎用户回答数分布图
labels6 = ['0-10', '10-50', '50-100', '100-500', '500以上']
sizes6= [len(df[(df['回答数'] <= 10)]), 
         len(df[(df['回答数'] >= 10) & (df['回答数'] < 50)]), 
         len(df[(df['回答数'] >= 50) & (df['回答数'] < 100)]), 
         len(df[(df['回答数'] >= 100) & (df['回答数'] < 500)]), 
         len(df[(df['回答数'] >= 500)])]
print(sizes6)
f = (
    Pie(init_opts=opts.InitOpts(theme=ThemeType.PURPLE_PASSION))
    .add(
        "",
        [list(z) for z in zip(labels6, sizes6)],
        radius=["30%", "75%"],
        rosetype="area",
    )

    .set_global_opts(title_opts=opts.TitleOpts(title="知乎用户回答数分布图"))    
)
f.render("知乎用户回答数分布图.html")
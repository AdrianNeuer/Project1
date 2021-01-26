import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
from pyecharts.charts import Bar
from pyecharts import options as opts
from pyecharts.globals import ThemeType 

df=pd.read_excel('知乎用户.xlsx')
p=df.sort_values(by='粉丝',ascending=False)
p=p.reset_index(drop=True)
q=p.iloc[:20,:]
print(q)

x=list(q['名字'])
y1=list(q['粉丝'])
y2=list(q['回答数'])
y3=list(q['感谢'])
y4=list(q['收藏'])
y5=list(q['获赞'])
print(x,y1,y2,y3,y4)
'''
bar1=(
    Bar(init_opts=opts.InitOpts(theme=ThemeType.VINTAGE))
        .add_xaxis(x)
        .add_yaxis("", y1)
        .set_global_opts(title_opts=opts.TitleOpts(title="知乎用户粉丝Top20"),
        xaxis_opts=opts.AxisOpts(name="名字", axislabel_opts={"rotate": 30})
        )
    )
bar1.render('知乎用户粉丝Top20.html')
bar2=(
    Bar(init_opts=opts.InitOpts(theme=ThemeType.MACARONS))
        .add_xaxis(x)
        .add_yaxis("", y2)
        .set_global_opts(title_opts=opts.TitleOpts(title="知乎用户回答数Top20"),
        xaxis_opts=opts.AxisOpts(name="名字", axislabel_opts={"rotate": 70})
        )
    )
bar2.render('知乎用户回答数Top20.html')
bar3=(
    Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
        .add_xaxis(x)
        .add_yaxis("", y3)
        .set_global_opts(title_opts=opts.TitleOpts(title="知乎用户感谢Top20"),
        xaxis_opts=opts.AxisOpts(name="名字", axislabel_opts={"rotate": 30})
        )
    )
bar3.render('知乎用户感谢Top20.html')
bar4=(
    Bar(init_opts=opts.InitOpts(theme=ThemeType.WESTEROS))
        .add_xaxis(x)
        .add_yaxis("", y4)
        .set_global_opts(title_opts=opts.TitleOpts(title="知乎用户收藏Top20"),
        xaxis_opts=opts.AxisOpts(name="名字", axislabel_opts={"rotate": 50})
        )
    )
bar4.render('知乎用户收藏Top20.html')'''
bar5=(
    Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
        .add_xaxis(x)
        .add_yaxis("", y5)
        .set_global_opts(title_opts=opts.TitleOpts(title="知乎用户获赞Top20"),
        xaxis_opts=opts.AxisOpts(name="名字", axislabel_opts={"rotate": 50})
        )
    )
bar5.render('知乎用户获赞Top20.html')

# 绘制散点图  数据过于聚集作废
'''# 设置图表大小df=df[df['获赞']<=30000]
df=df[df['回答数']>=30]
df['index']=range(len(df))
df=df.reset_index(drop=True)
x=df['回答数']
y1=df['获赞']
y2=df['感谢']
#figsise = opts.InitOpts(width='800px',height='600px')
scatter = Scatter(init_opts=opts.InitOpts(theme=ThemeType.VINTAGE))
# 添加数据
scatter.add_xaxis(xaxis_data=x)
scatter.add_yaxis(series_name='获赞/回答散点图'#图例名称
                  ,y_axis=y1#数据
                  ,label_opts=opts.LabelOpts(is_show=False)#数据不显示
                  ,symbol_size=10#设置散点的大小
                  ,symbol='triangle'#设置散点的形状（cricle,rect,pin,triangle）
                  )
scatter.add_yaxis(series_name='感谢/回答散点图'#图例名称
                  ,y_axis=y2#数据
                  ,label_opts=opts.LabelOpts(is_show=False)#数据不显示
                  ,symbol_size=10#设置散点的大小
                  ,symbol='circle'#设置散点的形状（cricle,rect,pin,triangle）
                  )

# 设置标题
scatter.set_global_opts(title_opts=opts.TitleOpts("获赞/感谢与回答图像"))

# 显示图片
scatter.render("scatter.html")'''
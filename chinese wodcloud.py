from pyecharts import Line, Bar, Pie, EffectScatter
# 数据
attr =["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
v1 =[5, 20, 36, 10, 10, 100]
v2 =[55, 60, 16, 20, 15, 80]

# 普通折线图
line = Line('折线图')
line.add('商家A', attr, v1, mark_point=['max'])
line.add('商家B', attr, v2, mark_point=['min'], is_smooth=True)
line.show_config()
line.render(path='./data/01-04折线图.html')

# 阶梯折线图
line2 = Line('阶梯折线图')
line2.add('商家A', attr, v1,  is_step=True, is_label_show=True)
line2.show_config()
line2.render(path='./data/01-05阶梯折线图.html')

# 面积折线图
line3 =Line("面积折线图")
line3.add("商家A", attr, v1, is_fill=True, line_opacity=0.2,   area_opacity=0.4, symbol=None, mark_point=['max'])
line3.add("商家B", attr, v2, is_fill=True, area_color='#a3aed5', area_opacity=0.3, is_smooth=True)
line3.show_config()
line3.render(path='./data/01-06面积折线图.html')

from pyecharts import Pie
pie =Pie('各类电影中"好片"所占的比例', "数据来着豆瓣", title_pos='center')
pie.add("", ["剧情", ""], [25, 75], center=[10, 30], radius=[18, 24], label_pos='center', is_label_show=True, label_text_color=None, )
pie.add("", ["奇幻", ""], [24, 76], center=[30, 30], radius=[18, 24], label_pos='center', is_label_show=True, label_text_color=None, legend_pos='left')
pie.add("", ["爱情", ""], [14, 86], center=[50, 30], radius=[18, 24], label_pos='center', is_label_show=True, label_text_color=None)
pie.add("", ["惊悚", ""], [11, 89], center=[70, 30], radius=[18, 24], label_pos='center', is_label_show=True, label_text_color=None)
pie.add("", ["冒险", ""], [27, 73], center=[90, 30], radius=[18, 24], label_pos='center', is_label_show=True, label_text_color=None)
pie.add("", ["动作", ""], [15, 85], center=[10, 70], radius=[18, 24], label_pos='center', is_label_show=True, label_text_color=None)
pie.add("", ["喜剧", ""], [54, 46], center=[30, 70], radius=[18, 24], label_pos='center', is_label_show=True, label_text_color=None)
pie.add("", ["科幻", ""], [26, 74], center=[50, 70], radius=[18, 24], label_pos='center', is_label_show=True, label_text_color=None)
pie.add("", ["悬疑", ""], [25, 75], center=[70, 70], radius=[18, 24], label_pos='center', is_label_show=True, label_text_color=None)
pie.add("", ["犯罪", ""], [28, 72], center=[90, 70], radius=[18, 24], label_pos='center', is_label_show=True, label_text_color=None, is_legend_show=True, legend_top="center")
pie.show_config()
pie.render(path='./data/01-多个饼图.html')
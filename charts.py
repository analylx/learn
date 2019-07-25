from pyecharts import Funnel, Gauge, Graph
from pyecharts import Map, Geo
from pyecharts import Liquid, Polar, Radar
from pyecharts import WordCloud
import os
#pip install pyecharts==0.1.9.4 
#指定安装旧版的，新的1.2.1无法成功import
# 世界地图数据
value = [95.1, 23.2, 43.3, 66.4, 88.5]
attr= ["China", "Canada", "Brazil", "Russia", "United States"]

map0 = Map("世界地图示例", width=1200, height=600)
map0.add("世界地图", attr, value, maptype="world",  is_visualmap=True, visual_text_color='#000')
map0.render(path="./data/04-00世界地图.html")

# 仪表盘
gauge = Gauge("仪表盘")
gauge.add('业务指标', '完成率', 66.66)
gauge.show_config()
gauge.render(path="./data/02-02仪表盘.html")
"""
# 关系图
nodes =[{"name": "结点1", "symbolSize": 10}, {"name": "结点2", "symbolSize": 20}, {"name": "结点3", "symbolSize": 30}, {"name": "结点4", "symbolSize": 40}, {"name": "结点5", "symbolSize": 50}, {"name": "结点6", "symbolSize": 40}, {"name": "结点7", "symbolSize": 30}, {"name": "结点8", "symbolSize": 20}]
links =[]
for i in nodes:
    for j in nodes:
        links.append({"source": i.get('name'), "target": j.get('name')})

print(links)
print(nodes)
graph =Graph("关系图-环形布局示例")
graph.add("", nodes, links, is_label_show=True, repulsion=8000,     layout='circular', label_text_color=None)
graph.show_config()
graph.render(path="./data/02-03关系图.html")
"""
# 水球图
liquid =Liquid("水球图")
liquid.add("Liquid", [0.6])
liquid.show_config()
liquid.render(path='./data/03-01水球.html')

# 圆形水球
liquid2 =Liquid("水球图示例")
liquid2.add("Liquid", [0.6, 0.5, 0.4, 0.3], is_liquid_outline_show=False)
liquid2.show_config()
liquid2.render(path='./data/03-02圆形水球.html')

# 菱形水球
liquid3 =Liquid("水球图示例")
liquid3.add("Liquid", [0.6, 0.5, 0.4, 0.3], is_liquid_animation=False, shape='diamond')
liquid3.show_config()
#os.mknod('./data/03-03菱形水球.html')  #这个方法只能在linux下使用
#f=open('./data/03-03菱形水球.html','w')
#f.close()
liquid3.render(path='./data/03-03菱形水球.html')

# 极坐标
radius =['周一', '周二', '周三', '周四', '周五', '周六', '周日']
polar =Polar("极坐标系-堆叠柱状图示例", width=1200, height=600)
polar.add("A", [1, 2, 3, 4, 3, 5, 1], radius_data=radius, type='barRadius', is_stack=True)
polar.add("B", [2, 4, 6, 1, 2, 3, 1], radius_data=radius, type='barRadius', is_stack=True)
polar.add("C", [1, 2, 3, 4, 1, 2, 5], radius_data=radius, type='barRadius', is_stack=True)
polar.show_config()
polar.render(path='./data/03-04极坐标.html')

# 雷达图
schema =[ ("销售", 6500), ("管理", 16000), ("信息技术", 30000), ("客服", 38000), ("研发", 52000), ("市场", 25000)]
v1 =[[4300, 10000, 28000, 35000, 50000, 19000]]
v2 =[[5000, 14000, 28000, 31000, 42000, 21000]]
radar =Radar()
radar.config(schema)
radar.add("预算分配", v1, is_splitline=True, is_axisline_show=True)
radar.add("实际开销", v2, label_color=["#4e79a7"], is_area_show=False)
radar.show_config()
radar.render(path='./data/03-05雷达图.html')

"""
#支持保持成各种格式,但是会有问题
bar = Bar("我的第一个图表", "这里是副标题")
bar.add("服装", ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"], [5, 20, 36, 10, 75, 90])
# bar.print_echarts_options()
bar.render(path='snapshot.html')
bar.render(path='snapshot.png')
bar.render(path='snapshot.pdf')
"""

name =['Sam S Club', 'Macys', 'Amy Schumer', 'Jurassic World', 'Charter Communications', 'Chick Fil A', 'Planet Fitness', 'Pitch Perfect', 'Express', 'Home', 'Johnny Depp', 'Lena Dunham', 'Lewis Hamilton', 'KXAN', 'Mary Ellen Mark', 'Farrah Abraham', 'Rita Ora', 'Serena Williams', 'NCAA baseball tournament', 'Point Break']
value =[10000, 6181, 4386, 4055, 2467, 2244, 1898, 1484, 1112, 965, 847, 582, 555, 550, 462, 366, 360, 282, 273, 265]
wordcloud =WordCloud(width=1300, height=620)
wordcloud.add("", name, value, word_size_range=[20, 100])
wordcloud.show_config()
wordcloud.render(path='./data/05-01权重词云.html')


wordcloud2 =WordCloud(width=1300, height=620)
wordcloud2.add("", name, value, word_size_range=[30, 100], shape='diamond')
wordcloud2.show_config()
wordcloud2.render(path='./data/05-02变形词云.html')
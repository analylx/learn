from urllib import urlopen  
from reportlab.graphics.shapes import *  
from reportlab.graphics.charts.lineplots import LinePlot  
#from reportlab.graphics.charts.textlabels import Label  
from reportlab.graphics import renderPDF  
 
URL = 'http://analylx.tk/index.php?user/publicLink&fid=e666IrgAgOuWWhHAOgBCdVO8bh8xlmupAnGSFbInJmziENVSoCYuiOoeBbqMxwVfNDEcgp3wpZF58xfxVcUKmdpvmJIomg-SdXY8twcxgQPzsXSDjpbue5PWvQ&file_name=/float.txt'  
COMMENT_CHARS = '#:'  
 
drawing = Drawing(400, 200)  
data = []  
for line in urlopen(URL).readlines():  
        if not line.isspace() and not line[0] in COMMENT_CHARS: 
                #print line 
                data.append([float(n) for n in line.split()])
                #print data  

pred = [row[2] for row in data]  
high = [row[3] for row in data]  
low = [row[4] for row in data]  
times = [row[0] + row[1]/12.0 for row in data]  
lp = LinePlot()  
lp.x = 50  
lp.y = 50  
lp.height = 125  
lp.width = 300  
lp.data = [zip(times, pred),zip(times,high),zip(times, low)]  
lp.lines[0].strokeColor = colors.blue  
lp.lines[1].strokeColor = colors.red  
lp.lines[2].strokeColor = colors.green  
 
drawing.add(lp)  
drawing.add(String(250,150, 'Sunspots',fontSize=14,fillColor=colors.red))  
renderPDF.drawToFile(drawing, 'report3.pdf','Sunspots')
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
from matplotlib import style


style.use('ggplot')    
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
def animate(i):
    pullData = open("twitter_res.txt","r").read()
    lines = pullData.split('\n')
    xar = []
    yar = []
    x =0
    y =0 
    for line in lines:
        x+=1
        if line == 'pos'  :
            y+=1
        elif line == 'neg' :
            y-=1
        xar.append(x)# x axis: contains the number of tweets containing the specific (keyword) that have been classified 
        yar.append(y )# y axis: net positive or negative sentiment adding up every successive tweet
    ax1.clear()
    ax1.plot(xar,yar)
ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()

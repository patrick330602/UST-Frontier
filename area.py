from collections import namedtuple
import random
Rectangle = namedtuple('Rectangle', 'xmin ymin xmax ymax')

def rectangle(X1,Y1,width1,height1,X2,Y2,width2,height2):
    ra = Rectangle(X1,Y1,X1+width1,Y1+height1)
    rb = Rectangle(X2,Y2,X2+width2,Y2+height2)
    dx = min(ra.xmax, rb.xmax) - max(ra.xmin, rb.xmin)
    dy = min(ra.ymax, rb.ymax) - max(ra.ymin, rb.ymin)
    return width1*height1-dx*dy
    
def square(X1,Y1,width1,height1,X2,Y2,width2):
    ra = Rectangle(X1,Y1,X1+width1,Y1+height1)
    rb = Rectangle(X2,Y2,X2+width2,Y2+width2)
    dx = min(ra.xmax, rb.xmax) - max(ra.xmin, rb.xmin)
    dy = min(ra.ymax, rb.ymax) - max(ra.ymin, rb.ymin)
    return width1*height1-dx*dy
    
def circle(X1,Y1,width1,height1,X2,Y2,radius):
    cnt = 0
    N= 10000000
    x_min, x_max = X1, X1+width1
    y_min, y_max = Y1, Y1+height1
    for i in range(N) :  
        x = random.uniform(x_min, x_max)  
        y = random.uniform(y_min, y_max)  
          
        if (x-X2)*(x-X2)+(y-Y2)*(y-Y2) <= radius * radius:  
            cnt += 1  
    ratio = cnt / N
    area = width1 * height1 * (1-ratio)
    return area
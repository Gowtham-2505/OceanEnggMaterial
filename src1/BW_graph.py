import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = 12,7

cw = 8 #m #crest width
tw = 3 #m # toe width
th = 2 #m # toe height
bwh = 10 #m #total breakwater height
at = 0.5 #m #armour thickness
de = np.arctan(1/2) # breakwater slope

p3x = -(bwh-th)/np.tan(de)
p2x = p3x-tw+at/np.sin(de)
p1x = p2x - th/np.tan(de)
p4x = 0
p5x = cw
p5y = bwh
p4y = bwh
p3y = th
p2y = th
p1y = 0

px = np.array([p3x,p4x,p5x,cw-p3x]) #Armour layer
py = np.array([p3y,p4y,p5y,p3y])    #Armour layer

p11x = -((bwh - th - at)/np.tan(de)- at/np.tan(de))
p22x = at/np.tan(de)
p33x = cw - p22x
p44x = cw - p11x
p11y = p44y = th
p22y = p33y = bwh - at

px1 = [p1x,p2x,p11x,p22x,p33x,p44x,cw-p2x,cw-p1x,p1x]   #underlayer1 
py1 = [p1y,p2y,p11y,p22y,p33y,p44y,p2y,p1y,p1y]         #underlayer1
# for checking points
print(px1)
print(py1)

plt.plot(px,py,px1,py1)
plt.show()
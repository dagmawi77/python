import matplotlib.pyplot as pt
import numpy as num

ypoint = num.array([3,8,1,10])

# pt.plot(ypoint,marker='o')
# pt.plot(ypoint,marker='*')
# pt.plot(ypoint,marker='+')
# pt.plot(ypoint,marker='H')
# pt.plot(ypoint,marker='P')
pt.plot(ypoint,'o:g',ms=20,mec='r',mfc='b')
pt.plot(ypoint, marker = 'o', ms = 20, mec = '#4CAF50', mfc = '#4CAF50')
pt.plot(ypoint, marker = 'o', ms = 20, mec = 'hotpink', mfc = 'hotpink')
pt.plot(ypoint,ls=':')


pt.show()
'''
CO2 effect on earth mean temp.
Need to get sources for parameters.
Institute for Earth Science Research and Education [IESRE]
http://www.instesre.org/Solar/SimpleGreenhouseModel.html
print(dir())
print(dir('matplotlib'))
'''
import math,cmath
import matplotlib.pyplot as plt
#h ow does emisivity vary with ghg?
def c2f(x):
 return (9/5)*x+32
f='{:.1f}'
f0='{:.2e}'
s0=1360 # solar watts/m**2
alpha=.29 # albedo # IESRE
r=6.3781e6# earth radius meters # Wikipedia
solarRadiation=s0*math.pi*r**2
print('solarRadiation global watts',f0.format(solarRadiation))
sigma=5.675e-8# Bolzmans constant
c0=278 # ppm. pre-industrial CO2 concentration
# no athmospher temp, IESRE # wikipedia Idealized_greenhouse_model
te=(s0*(1-alpha)/(4*sigma))**.25
print('No athmosphere temp earth','K=',f.format(te),'C=',f.format(te-273),'F=',f.format(c2f(te-273)))
temps=[];cs=[]
for c in range(275,800,20):
    #c= 405 # ppm. Current
    fCO2=5.35 * math.log(c/c0) # effect of CO2
    print(c/c0,fCO2)
    te=(.25*(s0+fCO2)*(1-alpha)/sigma)**.25
    #print('Athmosphere GHG ',c,f.format(te),f.format(te-273),f.format(c2f(te-273)))
    epsilon=.765
    epsilon=.782
    epsilon=.83333
    #epsilon=5.35*math.log(c/c0) #athmospheric emisivity LHG Hyp
    #at te = 15C epsilon=.782 #IESRE
    # epsilon=2*
    ts=te/(1-epsilon/2)**.25 # temp at surface old???
    ts=ts.real
    #ts=(s0*(1-alpha)/(4*sigma*(1-epsilon/2)))**.25
    temps.append(c2f(ts-273));cs.append(c)
    print('Athmosphere CO2=',c,
          'SurfTemp K=',f.format(ts),'C=',f.format(ts-273),'F=',f.format(c2f(ts-273)),end='  ')
    print('Temp delta due to CO2', fCO2)
# West Linn OR summer average high temperature
#plt.plot(cs,temps)
tempsWL=[(83-59)+x for x in temps]
plt.plot(cs,tempsWL)
plt.ylabel('Global avg Temp F')
plt.ylabel('West Lin OR July avg High Temp F')
plt.xlabel('CO2 PPM')
plt.grid()
plt.show()


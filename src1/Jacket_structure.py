#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


D = 1000 #mm
t = 25 #mm
d = D-2*t  #mm
I = (np.pi/64)*(pow(D,4)-pow(d,4)) #mm^4
A = (np.pi/4)*(pow(D,2)-pow(d,2)) #mm^2
r = np.sqrt(I/A)  #mm
l = 8000 #mm
#In Jacket structures 
k = 0.8
klr = k*l/r
#Axial force given
P = 350  #KN
fa = P/A*1e+03 #N/mm^2
rho = 1e+03/(1e+03**3) #Kg/mm^3
g = 9.81 #m/s^2
depth = 70 #m


# In[3]:


fy = 345      #In N/mm^2
if D/t <= 60:
    Fy = fy      
elif D/t>60 and D/t<300:
    C = 0.3
    Fxe = 2*C*E*t/D  #N/mm^2
    Fxc = fy*(1.64-0.23*pow(D/t,0.25))
    Fy = min(Fxe,Fxc)
E = 2.0e+05   #In N/mm^2
cc = np.sqrt(2*(np.pi**2)*E/Fy)
#given moment along yy and zz
myy = 780 #Kn-m
mzz = 560 #KN-m


# In[4]:


#Allowable compressive Axial stress Fa

klrcc = klr/cc
if klr<cc:
    Fa = ((1-pow(klrcc,2)/2)*Fy)/(5/3 + (3*klrcc)/8 - pow(klrcc,3)/8) #N/mm^2  
elif klr>=cc:
    Fa = (12*np.pi**2*E)/(23*pow(klrcc,2))    #N/mm^2 
print('I: ',I)
print("A: ",A)
print("r: ",r)
print("d: ",d)
print("kl/r: ",klr)
print("Cc = ",cc)
print("Axial stress given: ",fa) # in N/mm^2
print("Fa: ",Fa)
print('-----------------------------------------------')
if Fa>fa:
    print("Member is suitable for compressive stress")
else:
    print("Member is not suitable for compressive stress")


# In[5]:


#Max Load carrying capacity if only axial applied
print("Max Load carrying capacity if only axial applied: ",Fa*A)


# In[6]:


#Allowable Tensile stress
Ft = 0.6*Fy
if Ft>fa:
    print("Ft: ",Ft)
    print('Member is suitable for tensile stress')
else:
    print('Member is not suitable for tensile stress')


# In[7]:


#check for Bending
fb = np.zeros(2)
fb[0] = (myy*(D/2)*1e+06)/I  #N/mm^2
fb[1] = (mzz*(D/2)*1e+06)/I  #N/mm^2
print("Applied bending stresses ",fb)


# In[8]:


if D/t <= 10340/Fy:
    Fb = 0.75*Fy
elif 10340/Fy < D/t and D/t<20680/Fy:
    Fb = (0.84-1.74*((Fy*D)/(E*t)))*Fy    #N/mm^2
else:
    Fb = (0.72-0.58*((Fy*D)/(E*t)))*Fy    #N/mm^2
print("Fb :",Fb)
if Fb>fb[0] and Fb>fb[1]:
    print("Safe in inplane and outplane bending")
elif Fb>fb[0] and Fb<fb[1]:
    print("Safe in inplane but not in outplane bending")
elif Fb<fb[0] and Fb>fb[1]:
    print("Safe in outplane but not in inplane bending")
else:
    print("Not safe by any bending")


# In[13]:


#Check for hydrostatics
p = rho*g*depth*1e+03 #N/mm^2
fh = p*D/(2*t)
M = (l/D)*np.sqrt(2*D/t)
if M >= 1.6*D/t:
    ch = 0.44*t/D
elif 0.825*D/t<= M and M< 1.6*D/t:
    ch = 0.44*t/D + (0.21*pow(D/t,3))/(pow(M,4))
elif 3.5<= M and M< 0.825*D/t:
    ch = 0.736/(M-0.636)
elif 1.5<=M and M< 3.5:
    ch = 0.755/(M-0.559)
elif M<1.5:
    0.8
Fhe = 2*ch*E*t/D #N/mm^2
if Fhe <= 0.55*Fy:
    Fhc = Fhe
elif 0.55*Fy < Fhe and Fhe<= 1.6*Fy:
    Fhc = 0.45*Fy + 0.18*Fhe
elif 1.6*Fy < Fhe and Fhe <6.2*Fy:
    Fhc = (1.31*Fy)/(1.15 + (Fy/Fhe))
else:
    Fhc = Fy
print("M :",M)
print("Ch :",ch)
print("p: ",p)
print("fh :",fh)
print("Fhc :",Fhc)
print("Fhe :",Fhe)


# In[53]:


#To find SFh , API RP 2A,Pg 44,3.3.5
#during normal loads 
SFh = 2 #Hoop comp using basic allowable stress
# during stormy condition
#SFh = 1.5
FHS = Fhc/SFh   #N/mm^2
if FHS>fh:
    print('Safe against Hydrostatic pressure')
else:
    print('Not safe against Hydrostatic pressure')
print("Fhc/SFh :",FHS)


# In[54]:


#combined axial compression and bending
if fa/Fa > 0.15:
    print("Check Manually")
elif fa/Fa <= 0.15:
    if (fa/Fa) + np.sqrt(fb[0]**2+fb[1]**2)/(Fb) <= 1.0:
        print("expression value: ",(fa/Fa) + np.sqrt(fb[0]**2+fb[1]**2)/(Fb))
        print('Safe in axial compression and bending')
    else:
        print("expression value: ",(fa/Fa) + np.sqrt(fb[0]**2+fb[1]**2)/(Fb))
        print('Not safe in axial compression and bending')


# In[ ]:





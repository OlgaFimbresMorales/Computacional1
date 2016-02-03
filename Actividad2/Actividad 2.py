
# coding: utf-8

# In[9]:

from math import sqrt
print("Problema 1)
h = float(input("Proporciona la altura de la torre en metros: "))
t = sqrt(2*h/9.81)
print("El tiempo en que la pelota llega al suelo son",t,"segundos")


# In[10]:

T = 60*float(input("Proporciona el periodo minutos: "))
print (T)


# In[66]:

from math import sqrt, pi
print ("Problema 2")
T = 60*float(input("Proporciona el periodo de un satélite en minutos: "))
G = 6.67e-11
M = 5.97e24
R = 6371000.
h = (((G*M*T**2)/(4*pi**2))**(1.0/3.0))- R
print ("Su altura debe ser de", h, "metros")


# In[4]:

from math import sin,acos,pi, atan, sqrt
print ("Problema 3")
print ("Especifica las coordenadas cartesianas del punto:")
x = float(input("Introduce x: "))
y = float(input("Introduce y: "))
z = float(input("Inytoduce z: "))
r = sqrt(x**2 + y**2 + z**2)
theta = acos(z/r)
phi = atan(y/x)
print ("Las coordenas esféricas correspondientes son:")
print("r =",r,"theta =",theta,"phi =",phi)
 


# In[7]:

print ("Problema 4a")
n = int(input("Ingrese un número: "))
if n%2==0:
     print("Par")
else:
     print("Impar")
        


# In[11]:

print ("Problema 4b")
print("Ingrese dos número, uno par y uno impar:")
m = int(input("Ingrese el primer número: "))
n = int(input("Ingrese el segundo número: "))
while (m+n)%2==0:
    print("Uno debe ser par y el otro impar.")
    m = int(input("Ingrese el primer número: "))
    n = int(input("Ingrese el segundo número: "))
print("Los números que escogió son",m,"y",n)


# In[12]:

print("Problema 5.1")
f1,f2 = 1,1
while f2<1000:
      print(f2)
      f1,f2 = f2,f1+f2


# In[25]:

from math import factorial
print("Problema 5.2")
f1,f2 = 1,1
while f2<=10:
      print(f2)
      f1,f2 = f2,f1+f2


# In[35]:

def factorial(x,n):
	if(n>0):
		# Se va llamando a ella misma mientras el valor sea superior a 0
		x=factorial(x,n-1)
		x=x*n
	else:
		x=1
	return x
 
try:
	numero = int(raw_input("inserta un numero "))
 
	# Ejecutamos la función recusiva para el calculo
	calculo=factorial(1,numero)
	print "El factorial de %s es %s" % (numero,calculo)
except:
	print "\nTiene que ser un valor numerico"


# In[59]:

x ,n = 1, 1
if(n>0)
   
    
    


# In[ ]:




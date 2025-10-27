import random
import math


def gaussianbis(m,s):
    r=random.random()
    u=random.random()
    return m+math.sqrt(s)*math.sqrt(-2*math.log(r))*math.cos(2*math.pi*u)

'the funcion below calculates the price of an Asian Call option'
'It takes as parameter the list of times needed to calculate the price of the Asian Call option'

def asiancalloption(listoftimes,S0,K,T,mu,sigma,n):
    m=len(listoftimes)
    'we add 0 to the list of times in the line below to initiate the process at t=0'
    listoftimes = [0] + listoftimes 
    brownianlist=[]
    geometricbrownianlist=[]
    for j in range(0,m+1):
        brownianlist.insert(0,0)
        geometricbrownianlist.insert(0,0)
    Asiantotalsum=0
    geometricbrownianlist[0]=S0
    for k in range(0,n): 
        Asiansum=0
        for i in range(1,m+1):
            brownianlist[i]=brownianlist[i-1]+gaussianbis(0,listoftimes[i]-listoftimes[i-1])
            geometricbrownianlist[i]=S0*math.exp((mu-sigma**2/2)*listoftimes[i]+sigma*brownianlist[i])    
            Asiansum=Asiansum+geometricbrownianlist[i]
        if (1/m)*Asiansum-K>0:    
            Asiantotalsum = Asiantotalsum+(1/m)*Asiansum-K
    return (1/n)*Asiantotalsum*math.exp(-mu*T)

from matplotlib import pyplot as plt
import random
import math


def gaussianbis(m,s):
    r=random.random()
    u=random.random()
    return m+math.sqrt(s)*math.sqrt(-2*math.log(r))*math.cos(2*math.pi*u)


'simulation of the geometric brownian motion'

def geometricbrownian(listoftimes,S0,mu,sigma):
    n=len(listoftimes)
    brownianlist=[]
    for j in range(0,n):
        brownianlist.insert(0,0)
    geometricbrownianlist=[]
    for j in range(0,n):
        geometricbrownianlist.insert(0,0)
    for i in range(1,n):
        brownianlist[i]=brownianlist[i-1]+gaussianbis(0,listoftimes[i]-listoftimes[i-1])
    geometricbrownianlist[0]=S0
    for l in range(1,n):
        geometricbrownianlist[l]=S0*math.exp((mu-sigma**2/2)*listoftimes[l]+sigma*brownianlist[l])    
    #return brownianlist, geometricbrownianlist
    plt.plot(listoftimes, geometricbrownianlist)

'Archives: '
def pricegeometricbrownianmotionatT(T,S0,mu,sigma,n):
    sumprices=0
    for i in range(0,n):
        geometricbrownian= S0*math.exp((mu-sigma**2/2)*T+sigma*gaussianbis(0, T))
        sumprices = sumprices + geometricbrownian
    return sumprices/n

def europeancalloption(S0,K,T,mu,sigma,n):
    count=0
    for k in range(0,n):
        ST=S0*math.exp((mu-sigma**2/2)*T+sigma*gaussianbis(0, T))
        if ST>K:
            count = count + (ST-K)*math.exp(-mu*T)
    return count/n
    

    

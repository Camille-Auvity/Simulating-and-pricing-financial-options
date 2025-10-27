import random
import math

def gaussianbis(m,s):
    r=random.random()
    u=random.random()
    return m+math.sqrt(s)*math.sqrt(-2*math.log(r))*math.cos(2*math.pi*u)


def europeancalloption(S0,K,T,mu,sigma,n):
    count=0
    for k in range(0,n):
        ST=S0*math.exp((mu-sigma**2/2)*T+sigma*gaussianbis(0, T))
        if ST>K:
            count = count + (ST-K)*math.exp(-mu*T)
    return count/n

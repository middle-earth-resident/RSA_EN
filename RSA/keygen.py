import sys
sys.path.append('')
from PrimePackage import primeproduct
from PrimePackage import primegen 
import random
from fractions import gcd

prpro=primeproduct()
select_random=random.SystemRandom()
earr=[]
class keygen():
	n=prpro.primeprod

#keep phi privaate	
	def phi():
		p2=prpro.p1-1
		q2=prpro.q1-1
		if p2>q2:
			greater=p2
		else:
			greater=q2
		while(True):
			if((greater%p2==0) and (greater%q2==0)):
				lcm=greater
				break
			greater+=1
				
		return lcm

	
		
	for i in range(1,phi(),1):
		if gcd(i,phi())==1:	
			earr.append(i)
	e=select_random.choice(earr)
	fi=phi()
	print(e,"is E")
        print (n, "is N")
	print(fi,"is phi")

        def modinv(fi,e):
            #naive method to find modular multiplicative inverse of e under modulus phi(n)
		m0=fi
		
		y=0
		x=1
		if(fi==1):
			return 0
		while(e>1):
			q=e//fi
			t=fi
			fi=e%fi
			e=t
			t=y
			y=x-q*y
			x=t
		if(x<0):
			x=x+m0
		return x
	print(modinv(fi,e),"Is d")	
							
			

	
        

		




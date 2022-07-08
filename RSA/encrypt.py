#from convert import convert
enc=[]
s=""
m=[]
import pickle
class encrypt:
	with open('text.txt','r') as myfile:
		s=myfile.read().replace('\n','')
	
	e=int(raw_input("ENTER the key e"))
	n=int(raw_input("Enter the value for n"))
	
		
	for i in s:
		ip=ord(i)
		
		c=pow(ip,e,n)
		enc.append(c)
	with open('encrypted','wb') as fp:
		pickle.dump(enc,fp)
	
		
		
	"""def power(i,e,n):
			x=1
			bits="{0:b}".format(e)
			for j,bit in enumerate(bits):
				if bit=='1':x=(((x**2)*j)%n)
				elif bit=='0':x=((x**2)%n)
			
			print x%n
	power(i,e,n)"""




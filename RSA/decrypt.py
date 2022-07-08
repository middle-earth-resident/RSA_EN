import pickle
mprime=[]
enc=[]
dec=""
class decrypt():
	with open('encrypted','rb') as fp:
		enc=pickle.load(fp)
	d=int(raw_input("Enter key d"))
	n=int(raw_input("ENTER n"))
	
	
	for i in enc:
		m=pow(i,d,n)
		mprime=str(unichr(m))	
		dec=dec+mprime
	with open('decrypted.txt','a') as the_file:
			the_file.write(dec)	
	"""for i in c:
		iprime=int(i)
		m=pow(iprime,d,n)
		mprime.append(m)
		
	print mprime"""
		
	

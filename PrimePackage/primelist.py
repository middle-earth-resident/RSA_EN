#pYthon program to check if number is prime or not
arr=[]
class primelist:

	
	def primelists(self):
		#ch='y'
		#while (ch=='y') or (ch=='Y'): 
    		num=int(input("Enter a NUmber"))
    		for j in range(1,num):


		    	for i in range(2,j):
			    	if(j%i)==0:
					#print (num ,"is not a prime number")
					#print (i,"times",num//i,"is",num)
					break
		    	else:
        	                arr.append(j)
	
        	return arr

#p=primetest()
#print p

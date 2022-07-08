from primelist import primelist
import random
prlist=primelist()
primenum=prlist.primelists()
class primegen:
	
	
	def primegen():
		system_choice= random.SystemRandom()
		return system_choice.choice(primenum)
	p=primegen()
	q=primegen()
	print p
	print q

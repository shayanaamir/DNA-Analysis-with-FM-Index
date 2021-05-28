class RollingHash:
	def __init__(self, string, size):
		self.str  = string
		self.hash = 0  #For the pattern
		self.init = 0
		self.end  = size

		for i in range(0, size):
			self.hash += ord(self.str[i])

	def update(self):
		if self.end <= len(self.str) -1:
			self.hash -= ord(self.str[self.init])
			self.hash += ord(self.str[self.end])
			self.init += 1
			self.end  += 1
			
	def digest(self):
		return self.hash

	def text(self):
		return self.str[self.init:self.end]

def rabin_karp(substring, string):
	lst = []
	if substring == None or string == None or substring == "" or string == "" or len(substring) > len(string):
		return lst
	hs 	 = RollingHash(string, len(substring))
	hsub = RollingHash(substring, len(substring))
	hsub.update()
	for i in range(len(string)-len(substring)+1):						
		if hs.digest() == hsub.digest():
			if hs.text() == substring:
				lst.append(i)
		hs.update()
	print(lst)
	return lst

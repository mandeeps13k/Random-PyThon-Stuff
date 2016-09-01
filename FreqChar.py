freqs = { }
file = open("testfile.txt",'r')
for line in file.readlines():
	for char in line:
		if char in freqs:
			freqs[char] = freqs[char]+1
		else:
			freqs[char] = 1

print freqs

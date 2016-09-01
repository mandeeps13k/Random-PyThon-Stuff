file = open("testfile.txt",'r')
for line in file.readlines():
	for word in line.split():
		if word[: :-1] == word :
			print " %s is in In Palindrome" %word
		else :
			print "%s not in Palindrome " %word



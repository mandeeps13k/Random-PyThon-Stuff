import sys


lines = 0
wordCount = 0
mostWordsInLine = 0

with open(sys.argv[1],'r') as myfile:
	for line in myfile.readlines():
		lines = lines+1
		print line
		wordCount = len(line)
		if(wordCount > mostWordsInLine):
			mostWordsInLine = wordCount
		print ("Word Count : " + str(wordCount))

avgWords = wordCount/lines

print "Average Words per line : %d " %avgWords
print "Most words in a single Line : %d " %mostWordsInLine

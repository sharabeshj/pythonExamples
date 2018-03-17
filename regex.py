'''
Identifiers
	\d any number
	\D anything but a number
	\s space
	\S anything but a space
	\w any character
	\W anything but a character
	. ~ . any character , except for a new line 
	\b the white space around words
	\. a period

Modifiers:
	{1,3} we're expecting 1-3
	+ match 1 or more
	? match 0 or 1
	* match 0 or more
	$ match the end of a string
	^ matching the beginning of a string
	| either or 
	[] range or variance
	{x} expecting x amount

White Space characters:
	\n new line
	\s space
	\t tab
	\e escape
	\f form feed
	\r return

DONT FORGET:
	. + * ? [] $ ^ () {} | \ -use these escape these
'''

import re

exampleString='''
Jesicca is  15 years old, and Daniel is 27 years old.
Edward is 97, and his grandfather, Oscar, is 102.
'''
ages = re.findall(r'\d{1,3}',exampleString)
names=re.findall(r'[A-Z][a-z]*',exampleString)

print(ages)
print(names)
x=0
ageDict={}
for eachName in names:
	ageDict[eachName]=ages[x]
	x+=1

print(ageDict)
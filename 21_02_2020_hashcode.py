import sys
import random
import time

random.seed(time.clock())

a=1

f=str(a)


abc=f+'.txt'
xyz=f+'_sol.txt'

sys.stdin=open(abc,'r')
sys.stdout=open(xyz,'w')

numberOfBooks,numberOfLibrary,daysAvailable=map(int,raw_input().split())
scoreOfBooks=list(map(int,raw_input().split()))

booklists=[]
customScoreList=[]

for i in range(numberOfLibrary):
	numberOfBook,numberOfDaysForSignup,perDayLimit=map(int,raw_input().split())
	
	booklist=list(set(list(map(int,raw_input().split()))))

	y=[scoreOfBooks[x] for x in booklist]
	s=sum(y)

	customScore=(numberOfBook+s+random.randint(-1000,1000))/(perDayLimit+random.randint(-100,1000)+1)


	zippy=zip(y,booklist)
	booklist=[j for i,j in sorted(zippy)]
	booklist.reverse()

	booklists.append(booklist)
	customScoreList.append(customScore)

libraryIndex=list(range(0,numberOfLibrary))
zippy=zip(customScoreList,libraryIndex)
libraryOrderToUse=[j for i,j in sorted(zippy)]
libraryOrderToUse.reverse()
#print(libraryOrderToUse)

x=[]

x=[0]*numberOfBooks
answer=[]

for library in libraryOrderToUse:
	y=[]
	for book in booklists[library]:
		if(x[book]==0):
			y.append(book)
			x[book]=1
	if(len(y)>0):
		answer.append([library,len(booklists[library])])
		answer.append(booklists[library])

x=len(answer)//2
print(x)
for i in range(0,len(answer),2):
	print(" ".join(str(x) for x in answer[i]))
	print(" ".join(str(x) for x in answer[i+1]))



	
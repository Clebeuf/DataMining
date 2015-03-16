import sys

iFile=open(sys.argv[1], 'r')
k=sys.argv[1].find('.')
out1 = sys.argv[1][:k]+"_freshness.txt"
out2 = sys.argv[1][:k]+"_score.txt"
oFile1=open(out1, 'w')
oFile2=open(out2, 'w')
movieIDB=freshnessB=scoreB=quoteB=False

grade_array=["F","D","C-","C","C+","B-","B","B+","A-","A","A+"]
criticList={}

line = iFile.readline()
while(not (line=="")):
	i=line.find(':')
	if(not(i==-1)):
		cat=line[:i]
		cat=cat.strip()
		if(cat[0]=='\"'):
			cat=cat[1:]
		#end if
		if(cat[-1]=='\"'):
			cat=cat[:-1]
		#end if
		#print cat
		value=line[i+1:]
		value=value.strip()
		if(value[-1]==','):
			value=value[:-1]
		#end if
		if(value[-1]=='\"'):
			value=value[:-1]
		#end if
		if(value[0]=='\"'):
			value=value[1:]
		#end if
		#print value
		if(cat=="links"):
			start=value.find('{')
			value=value[start+1:]
			while(value.find('}')==-1):
				value=iFile.readline()	
			#end while
		elif(cat=="movieID"):
			movieID = value
			movieIDB=True
		#elif(cat=="publication"):
		#	tup += value + ','
		elif(cat=="quote"):
			quote = '\"' + value + '\"'
			quoteB=True
		elif(cat=="freshness"):
			freshness = '\"' + value + '\"'
			freshnessB=True
		elif(cat=="critic"):
			
			if(value in criticList):
				critic=str(criticList[value])
			else:
				newval=len(criticList)
				criticList.update({value:newval})
				critic=str(newval)
			#end if

			if(movieIDB and freshnessB and quoteB and not(quote=='\"\"') and not(freshness=="\"none\"") and not(critic=='\"\"')):			
				if(not scoreB):
					score="NONE"
				#end if
				tup=movieID+','+critic+','+freshness+','+score+','+quote+'\n'
				#print tup.strip()
				oFile1.write(tup)
			#end if
			if(movieIDB and scoreB and quoteB and not(quote=='\"\"') and not critic=='\"\"' and not score=="INVALID"):
				if(not freshnessB):
					freshness="\"none\""
				#end if
				tup=movieID+','+critic+','+freshness+','+score+','+quote+'\n'
				#print tup.strip()
				oFile2.write(tup)
			#end if
			movieIDB=freshnessB=scoreB=quoteB=False
		elif(cat=="original_score"):
			scoreB=True
			spot=value.find('/')
			divisor=numerator=-1
			if(spot==-1):
				divisor = 10
				j=0
				while(j<11):
					if(value==grade_array[j]):
						numerator=j
						break
					#end if
					j+=1;
				#end while
			else:
				strNumerator = value[:spot].strip()
				strDivisor = value[spot+1:].strip()
				valid=True
				for c in strNumerator:
					if(not(c.isdigit() or c == '.')):
						valid=False
					#end if
				#end for
				for c in strDivisor:
					if(not(c.isdigit() or c=='.')):
						valid=False
					#end if
				#end for
				if(valid):
					numerator=float(strNumerator)
					divisor=float(strDivisor)
				#end if
			#end if
			if(numerator == -1 or divisor == 0):
				score = "INVALID"
			else:
				percent = numerator/divisor
				score = str(percent)
			#end if
		#end if
	#end if
	line = iFile.readline()
#end while
oFile1.close()
oFile2.close()
iFile.close()

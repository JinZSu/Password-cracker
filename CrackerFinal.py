import hashlib

def main():
	print("Main")
	Eharmony()   #MD5	
	#Linkedin(0)   #SHA1 Pepper
	#formspring() #SHA256 salt

def passhashsearch(hash1,mode):
	if(mode=="MD5"):
		filepointerr = open("realhuman_phillMD5.txt")
	elif(mode=="SHA1"):
		filepointerr = open("realhuman_phillSHA1.txt")
	elif(mode=="SHA256"):
		filepointerr = open("realhuman_phillSHA256.txt")
	temp = filepointerr.readline().strip("\r\n").split(':')

	linehash = temp[0]
	password = temp[1]
	while(temp!=['']):
		if(linehash==hash1):
			print("FOUND")
			filepointerr.close()
			return password
		temp = filepointerr.readline().strip("\r\n").split(':')
		if(len(temp)==2):
			linehash = temp[0]
			password = temp[1]
	filepointerr.close()
	return "HashNotFound"

def Eharmony():
	counter = 0
	count = 0
	print("Initializing MD5")
	filepointerr = open("eharmony passwords.txt")
	filepointerw = open("eharmony_updaterealhuman_phill.txt","w")
	linehash=filepointerr.readline().strip("\r\n")
	while(linehash):
		print(counter, "COUNTER")
		print(linehash)
		search = passhashsearch(linehash,"MD5")
		if(search ==linehash):
			filepointerw.write(search+":"+linehash+"\n")
			print(search+":"+linehash+"\n")
			count+=1
		linehash=filepointerr.readline().strip("\r\n")
		counter+=1
	filepointerr.close()	
	filepointerw.close()
	print(count)
	print("Finished MD5")

def formspring():
	count = 0
	print("Initializing SHA256")
	filepointerr = open("formspring.txt")
	filepointerw = open("formspringupdaterealhuman_phill.txt","w")
	linehash=filepointerr.readline().strip("\r\n")
	while(linehash):
		search = passhashsearch(linehash,"SHA256")
		if(search !="HashNotFound"):
			filepointerw.write(search+":"+linehash+"\n")
		linehash=filepointerr.readline().strip("\r\n")
	filepointerr.close()	
	filepointerw.close()
	print("Finished SHA256")



def Linkedin(state1):
	count = 0
	counter=0
	if(state1):
		Remover()
	else:
		print("Initializing SHA1")
	filepointerr = open("updatedlinkedin.txt")
	filepointerw = open("linkedinrealhuman_phill.txt","w")
	linehash=filepointerr.readline().strip("\r\n")
	while(linehash):
		print(counter, "COUNTER")
		print(linehash)
		search = passhashsearch(linehash,"SHA1")
		if(search !="HashNotFound"):
			filepointerw.write(search+":"+linehash+"\n")
			count+=1
		linehash=filepointerr.readline().strip("\r\n")
		counter+=1
	filepointerr.close()	
	filepointerw.close()
	print("Finished SHA1")
	print("LINKDIN COUNT",count)


def Remover(): #I saw that there are ones that begin with 0, which doesn't look natural
	count=0
	filepointerr = open("linkedin.txt")
	filepointerw = open("updatedlinkedin.txt","w")
	content = filepointerr.readline()
	while(content):
		if(content[:5]=="0000"):
			print("found")
		else:
			filepointerw.write(content)
			count+=1
		content=filepointerr.readline()
	filepointerr.close()
	filepointerw.close()
	print("REMOVER REMOVED: ",count)

if __name__ == '__main__':
	main()
	print("processed")
	

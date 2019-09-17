import hashlib


def main():
	Linkdein()   #SHA1 Pepper
	Eharmony()   #MD5
	formspring() #SHA256 salt

def word2hash(string1,mode):
	if(mode=="MD5"):
		result=hashlib.md5(str.encode())
	elif(mode=="SHA1"):
		result=hashlib.sha1(str.encode())
	elif(mode=="SHA256"):
		result=hashlib.sha256(str.encode())
	return result.hexdigest()

def Eharmony():
	count = 0
	filepointerr = open("eharmony\ passwords.txt")
	print(filepointerr.readline)
def formspring():
	count = 0


def Linkedin(state1):
	count = 0
	if(state1):
		Remover()
	else:
		fp = open("updatedlinkedin.txt")
		content = fp.readline()

	print "LINKDIN COUNT",count 
	
def formspring():
	count = 0

def Remover(): #I saw that there are ones that begin with 0, which doesn't look natural
	count=0
	filepointerr = open("linkedin.txt")
	filepointerw = open("updatedlinkedin.txt","w")
	content = filepointerr.readline()
	while(content):
		if(content[:5]=="0000"):
			print "found"
		else:
			filepointerw.write(content)
			count+=1
		content=filepointerr.readline()
	filepointerr.close()
	filepointerw.close()
	print "REMOVER REMOVED: ",count

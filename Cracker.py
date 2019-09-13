def main():
	Linkdein()
	Eharmony()
	formspring()

def Eharmony():
	count = 0

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

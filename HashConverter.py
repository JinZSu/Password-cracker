import hashlib

def main():
	print("Main")
	#passhashsearch("MD5")
	#passhashsearch("SHA1")
	passhashsearch("SHA256")

def word2hash(string1,mode):
	if(mode=="MD5"):
		result=hashlib.md5(string1.encode())
	elif(mode=="SHA1"):
		result=hashlib.sha1(string1.encode())
	elif(mode=="SHA256"):
		result=hashlib.sha256(string1.encode())
	return result.hexdigest()

def passhashsearch(mode):
	filepointerr = open("10million.txt")
	filepointerw = open("10millionSHA256.txt","w")
	linepass = filepointerr.readline().strip("\r\n")
	while(linepass):
		hash = word2hash(linepass,mode)
		filepointerw.write(hash + ":" + linepass+"\n")
		linepass = filepointerr.readline().strip("\r\n")
	filepointerr.close()
	filepointerw.close()
if __name__ == '__main__':
	main()
	print("processed")
	

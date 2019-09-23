import hashlib

def main():
	print("Main")
	#passhashsearch("MD5")
	passhashsearch("SHA1")
	#passhashsearch("SHA256")

def word2hash(string1,mode):
	if(mode=="MD5"):
		result=hashlib.md5(string1.encode(encoding='utf-8',errors='ignore'))
	elif(mode=="SHA1"):
		result=hashlib.sha1(string1.encode(encoding='utf-8',errors='ignore'))
	elif(mode=="SHA256"):
		result=hashlib.sha256(string1.encode(encoding='utf-8',errors='ignore'))
	return result.hexdigest()

def passhashsearch(mode):
	filepointerr = open("realhuman_phill.txt", 'r',encoding="Latin-1")
	filepointerw = open("realhuman_phillSHA1.txt","w")
	linepass = filepointerr.readline().strip("\n")
	while(linepass):
		print(linepass)
		hash = word2hash(linepass,mode)
		filepointerw.write(hash + ":" + linepass+"\n")
		linepass = filepointerr.readline().strip("\n")
	filepointerr.close()
	filepointerw.close()
if __name__ == '__main__':
	main()
	print("processed")

import hashlib

def main():
	print("Main")
	#passhashsearch("MD5")
	#passhashsearch("SHA1")
	passhashsearch("SHA256")

def passhashsearch(mode):
	BASE58 = '0123456789abcdefghijkmnopqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ' 
	filepointerr = open("realhuman_phill.txt", 'r',encoding="Latin-1")
	filepointerw = open("realhuman_phillSHA256.txt","w")
	linepass = filepointerr.readline().strip("\r\n")
	while(linepass):
		print(linepass)
		for i in BASE58:
			for x in BASE58:
				temp1 = str(i+x+linepass)
				temp2 = str(linepass+i+x)
				fsalt = hashlib.sha256(temp1.encode()).hexdigest()
				bsalt = hashlib.sha256(temp2.encode()).hexdigest()
				print(fsalt,bsalt)
				print(type(fsalt),type(temp1))
				filepointerw.write(fsalt + ":" + temp1 +"\n")
				filepointerw.write(bsalt + ":" + temp2 +"\n")
		linepass = filepointerr.readline().strip("\n")
	filepointerr.close()
	filepointerw.close()
if __name__ == '__main__':
	main()
	print("processed")

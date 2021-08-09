import string
import random
import base64
import colorsys
import os

#@X.DASH.666
#DASH COPY RIGHT
#YOU CAN EDIT THE TOOL BUT DONT REMOVE THE COPY RIGHTS plz

red="\033[31m"
green="\033[32m"
yellow="\033[33m"
blue="\033[34m"
purple="\033[35m"
cyan="\033[36m"
white="\033[37m"
cl=[red,green,yellow,blue,purple,cyan,white]
class encrypt:
	
	def caesar_encrypt(self):
		print("\n")
		message=str(input("ENTER MESSAGE TO ENCRYPT: "))
		while True:
			try:
				print("\n")
				shift=int(input("SHIFT: "))
				break
			except ValueError as ve:
				print("\n")
				print("PLEASE ENTER NUMBERS ONLY")
				print("debug: ",ve)
		alphabet=string.ascii_lowercase
		shifted_alphabet=alphabet[shift:]+alphabet[:shift]
		caesar_encrypt_table=str.maketrans(alphabet,shifted_alphabet)
		
		encrypted_message=message.translate(caesar_encrypt_table)
		
		print("\n"+encrypted_message)
		
		input("\npress enter to continue")
	def caesar_decrypt(self):
		print("\n")
		message=str(input("ENTER MESSAGE TO DECRYPT: "))
		while True:
			try:
				print("\n")
				shif=int(input("SHIFT: "))
				shift=26-shif
				shift%=26
				break
			except ValueError as ve:
				print("\n")
				print("PLEASE ENTER NUMBERS ONLY")
				print("debug: ",ve)
		alphabet=string.ascii_lowercase
		shifted_alphabet=alphabet[shift:]+alphabet[:shift]
		caesar_decrypt_table=str.maketrans(alphabet,shifted_alphabet)
		print("\n")
		decrypted_message=message.translate(caesar_decrypt_table)
		
		print(decrypted_message)
		input("\npress enter to continue")
	def DSA_encrypt(self):
		message=input("ENTER YOUR MESSAGE: ")
		print("\n")
		opreation=input("OPREATION (*,/,+,-): ")
		print("\n")
		opreation_num=int(input("THE OPRETION NUMBER: "))
		print("\n")


		alphabet=string.ascii_lowercase
		new_alphabet=""
		numeric_password=[]

		for i in range(26):
			new_alphabet_char=random.choice(alphabet)
			new_alphabet+=new_alphabet_char

		DSA_table=str.maketrans(alphabet,new_alphabet)

		enc_message_raw=message.translate(DSA_table)

		enc_message=""
		for i in enc_message_raw:
			ascii_num_raw=ord(i)
			if opreation=="*":
				ascii_num=ascii_num_raw*opreation_num
			elif opreation=="/":
				ascii_num=ascii_num_raw/opreation_num
			elif opreation=="+":
				ascii_num=ascii_num_raw+opreation_num
			elif opreation_num=="-":
				ascii_num=ascii_num_raw-opreation_num
			enc_message+=chr(ascii_num)
			

		print("encrypted message: ",enc_message)
		print("alphabet password: ",new_alphabet)
		input("\npress enter to continue")

class encode:
	def base64_encode(self):
		message=input("MESSAGE: ").encode()
		encoded_message=base64.b64encode(message)
		print(encoded_message.decode())
		input("\npress enter to continue")
	def base64_decode(self):
		message=input("ENCODED MESSAGE: ")
		decoded_message=base64.b64decode(message)
		print(decoded_message.decode())
		input("\npress enter to continue")


rc=random.choice(cl)
print(rc)

banner="""
 /$$$$$$$  /$$$$$$$$ /$$$$$$$$
| $$__  $$| $$_____/| $$_____/
| $$  \ $$| $$      | $$      
| $$  | $$| $$$$$   | $$$$$   
| $$  | $$| $$__/   | $$__/   
| $$  | $$| $$      | $$      
| $$$$$$$/| $$$$$$$$| $$$$$$$$
|_______/ |________/|________/
 
 beta 1.1                             
                              
                              
"""

choices="""
1>>>caesar encrypt
2>>>caesar decrypt
3>>>DSA encrypt
4>>>BASE64 encode
5>>>BASE64 decode
6>>>exit
"""
encr=encrypt()
enco=encode()
while True:
	os.system("clear")
	print(banner)
	print(choices)
	
	choice=input("ENTER YOUR CHOICE: ")
	choice.replace(" ","")
	if choice=="1":
		encr.caesar_encrypt()
	elif choice=="2":
		encr.caesar_decrypt()
	elif choice=="3":
		encr.DSA_encrypt()
	elif choice=="4":
		enco.base64_encode()
	elif choice=="5":
		enco.base64_decode()
	elif choice=="6":
		exit()
	else:
		print("THATS NOT A CHOICE!")
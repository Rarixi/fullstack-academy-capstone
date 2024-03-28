from cryptography.fernet import Fernet
#Generates encryption key 

key = Fernet.generate_key()
file = open("encyption_key.txt", "wb")
file.write(key)
file.close()
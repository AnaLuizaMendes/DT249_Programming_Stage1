# The program that can encrypt and decrypt strings using a simple algorithm
# To encrypt a string, we reverse it and add 1 to the ASCII code for each character

# Encrypt

message = input("Please enter the message here: ")
encrypt = ""

for letter in message:
    encrypt = chr(ord(letter) + 1) + encrypt

print(encrypt)
print("\n")


# Decrypt

string = input("Please enter the encrypt message here: ")

new_string = ""

for letter in string:
    new_string = chr(ord(letter) - 1) + new_string

print(new_string)

# Password Generator
import random
len_of_passwd = int(input("Enter the length of password that you want?\n"))
num_of_symbols = int(input("How many symbols would you like?\n"))
num_of_numbers = int(input("How many numbers would you like?\n"))
letters = []
numbers = []
symbols = ['!', '@', '#', '$', '%', '&', '*', '_', '+']
passwd = list()

for j in range(97 , 123):
    letters.append(chr(j))
for i in range(65 , 91):
    letters.append(chr(i))
for a in range(0, 10):
    numbers.append(str(a))
if len_of_passwd < (num_of_symbols+num_of_numbers):
    print("Wrong input, number of symbols + number of numbers is more than the length of pass")
else:
    for i in range(0, num_of_numbers):
        passwd.append(numbers[random.randint(0, 9)])
    for i in range(0, num_of_symbols):
        passwd.append(symbols[random.randint(0, len(symbols)-1)])
    for i in range(0, len_of_passwd - num_of_numbers - num_of_symbols):
        passwd.append(letters[random.randint(0, len(letters)-1)])
    
    # print(passwd)
    strong_passwd = ""
    for i in range(0, len_of_passwd):
        temp = random.randint(0, len(passwd)-1)
        strong_passwd = strong_passwd + passwd[temp]
        passwd.pop(temp)
        # print(strong_passwd)
    print(strong_passwd)

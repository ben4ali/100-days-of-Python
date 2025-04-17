import random

print("Welcome to the PyPassword Generator!")

letters = int(input("How many letters would you like in your password?\n"))
symbols = int(input("How many symbols would you like?\n"))
numbers = int(input("How many numbers would you like?\n"))

letter_bank = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
symbol_bank = ['!','@','#','$','%','?','&','*','(',')','-','+','_','=']
number_bank = ['1','2','3','4','5','6','7','8','9','0']

bank = [letter_bank,symbol_bank,number_bank]
password_length = letters+symbols+numbers
generated_password = ""

for i in range(password_length):
    bank_choice = random.randint(0,2)
    character=bank[bank_choice][random.randint(0,len(bank[bank_choice])-1)]
    if bank_choice == 0:
        upper = random.randint(0,1)
        if upper == 0:
            character = character.upper()
    generated_password+=character

print("Password generated:")
print(generated_password)


print("Welcome to caesar cipher")

LETTERS = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def process_cipher(process_choice,shift,message_to_process):
    new_message = ""
    for i in range(len(message_to_process)):
        for j in range(len(LETTERS)):
            if LETTERS[j] == message_to_process[i]:
                processed_shift_number = j + shift
                if process_choice =="decode":
                    processed_shift_number = j - shift
                    new_message += LETTERS[processed_shift_number]
                    continue
                if processed_shift_number >= len(LETTERS):
                    processed_shift_number-=26
                new_message+= LETTERS[processed_shift_number]
    return new_message

def take_input():
    input_message = input("Type your message:\n")
    input_shift_number = int(input("Type the shift number:\n"))
    return input_message,input_shift_number

choice = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
while choice.lower() != "no":
    message, shift_number = take_input()
    result_message = process_cipher(choice,shift_number,message)
    print(f"Here's the {choice}d message: {result_message}")
    choice = input("Type 'encode' or 'decode' if you want to go again. Otherwise type 'no'.\n")
print("Goodbye")
# colect user preference 
# lenght
# should contain Uppercase
# should contain special
# should contain digits
# get all available charaacters
# randomly pick characters up to lenght
# ensure we have at least one of each charcter type
# ensure lenght is valid


import random
import string # give us the access to alist of the character that are lowercase, uppercase, digits, or special charcters

def generate_password():
    length = int(input("Enter the desired password lenght: ").strip())
    include_uppercase = input("Include Uppercase chatracter ? (yes/no): ").strip().lower()
    include_special = input("Include Special chatracter ? (yes/no): ").strip().lower()
    include_digits= input("Included digits? (yes/no): ").strip().lower()

    if length < 4:
        print("Password lenght must be at least 4 charcters.")
        return
    lower = string.ascii_lowercase
    uppercase = string.ascii_uppercase if include_uppercase == "yes" else ""
    special = string.punctuation if include_special == "yes" else ""
    digits = string.digits if include_digits == "yes" else ""
    all_merge_charcters = lower + uppercase + special + digits
    
    required_charcters = []
    if include_uppercase == "yes":
        required_charcters.append(random.choice(uppercase))
    if include_special == "yes":
        required_charcters.append(random.choice(special))
    if include_digits == "yes":
        required_charcters.append(random.choice(digits))
    remaining_lenght = length - len(required_charcters)
    password = required_charcters

    for _ in range(remaining_lenght):
        chracters = random.choice(all_merge_charcters)
        password.append(chracters)
    random.shuffle(password)
    str_password = "".join(password)
    print(str_password)
generate_password()
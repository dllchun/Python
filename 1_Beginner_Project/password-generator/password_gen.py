import random
import string

number = [1,2,3,4,5,6,7,8,9]
alphabet = [i for i in string.ascii_letters]
full_list = number + alphabet


def generate_password():
    bin = input('How many digit of password do you need? ')
    volumn = input('How many password do you need? ')
    for i in range(int(volumn)):
        password_list = []
        while int(bin) > len(password_list):
            random_num = random.randint(0,len(full_list)-1)
            password_item = full_list[random_num]
            password_list.append(str(password_item))
        print(str(i+1)+': '+ ''.join(password_list))

if __name__ == '__main__':
    generate_password()

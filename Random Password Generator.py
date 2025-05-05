#GenerateRandomPassword

import random
import string
import pyperclip


def GenerateRandomPassword(length,u_letters,u_digits,u_symbols):
    combletters = ''
    if not any([u_letters,u_digits,u_symbols]):
        return 'You must choose at least one character type'
    if u_letters:
        combletters+=string.ascii_letters
    if u_digits:
        combletters+=string.digits
    if u_symbols:
        combletters+=string.punctuation
    password = ''.join(random.choice(combletters) for i in range(0,length))
    pyperclip.copy(password)
    return password
   
          
def UserBooleanInputs(st):
    while True:
        answer = input(st + ' (y/n): ').strip().lower()
        if answer in ['y','yes']:
            return True
        elif answer in ['n','no']:
            return False
        else:
            print('Invalid input. Please enter y or n.')

def main():
    print('=== Random Password Generator ===')
    try:
        le = int(input('Enter your password length: '))
        if le<=0:
            print('Password length should be greater than zero')
            return
    except ValueError:
        print('Please Enter a Valid Number')
        return
    use_l = UserBooleanInputs ('Include letters')
    use_d = UserBooleanInputs ('Include digits')
    use_s = UserBooleanInputs ('Include symbols')
    res = GenerateRandomPassword(le,use_l,use_d,use_s)
    
    print()
    print('*'*43)
    print(f'Generated Password: {res}'.center(43))
    print('Password has been copied to your clipboard!')
    print('*'*43)

if __name__ == '__main__':
    main()

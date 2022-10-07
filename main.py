# Import the password generator module
from tkinter import Tk
from pass_gen.pass_gen import password_gen

# Defining main function
def main():
    while True:
        length_input = input("Input the length of the password to be generated.\nLeave blank for standard length password (8 characters) ")
        
        if length_input == "":
            password = password_gen()
        else:
            password = password_gen(int(length_input))
        
        # This workaround is in place because Tkinter
        # ships with python in every OS
        # this is done to no mess around with OS specific
        # clipboard codes
        dummy_window = Tk()
        dummy_window.withdraw()
        dummy_window.clipboard_clear()
        dummy_window.clipboard_append(password)
        dummy_window.update()
        dummy_window.destroy()
        
        print(50 * "=")
        print("Password copied to the clipboard.")
        print(50 * "=", "\n")
        
        user_option = input("Would you like to generate another password? (Y/N) ").lower()
        
        if user_option == "n":
            break
        continue

# Driver code
if __name__ == '__main__':
    main()
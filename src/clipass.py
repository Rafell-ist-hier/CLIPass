import os
import io
from pathlib import Path
from contextlib import chdir

print("
   ____ _     ___ ____
  / ___| |   |_ _|  _ \ __ _ ___ ___
 | |   | |    | || |_) / _` / __/ __|
 | |___| |___ | ||  __/ (_| \__ \__ \_
  \____|_____|___|_|   \__,_|___/___(_)
/n")
print("A Python-Programmed CLI Tool for quickly but/n")
print("not so safely storing Passwords in Text files.\n")
print("Made by Rafell.")

print("Type a Key name:")
keyname = input()
print("Type a password:")
password = input()
print("Write your File name:")
file_name = input()

if (os.path.isdir("clipass_passwords") == True):
        with chdir("clipass_passwords"):
                with open(file_name + ".txt", "w") as password_file:
                        password_file.write(keyname)
                        password_file.write(password)
else:
        os.mkdir("clipass_passwords")
        print("Missing folder has been created./n")
        print("Please try creating your Password file again.")
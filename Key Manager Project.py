from fileinput import filename
import os.path
import random
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

while True:
    print("[C]reate or [F]ind File?")
    path = input("-->")
    if path == "C":                     # Choice 1
        file_name = input("File Name:")
        fileCat = file_name + ".txt"
        crt = open(fileCat, "a")
        break
    elif path == "F":                   # Choice 2
        print("Select File:")
        print(Fore.YELLOW + "-"*30)
        l1st = os.listdir()
        l2st = "\n".join(l1st)
        print(l2st)
        print(Fore.YELLOW + "-"*30 + "\n")
        f_sel = input("sf>")
        if os.path.exists(f_sel):
            fileCat = f_sel
            crt = open(fileCat, "a")
            break
        elif f_sel == "q":
            print(Back.LIGHTRED_EX + Fore.WHITE + "\n### You can't run this program without a file ###\n")
        else:
            print(Fore.RED + "\n\n!!No such file exists!!\n\n")
    elif path == "q":                   # Choice 3
        quit()
    else:
        print(Fore.RED + "\n!!Error: Command not recognized!!\n")
    

def help_screen():
    print("")
    print(Fore.GREEN + "Help:")
    print(Fore.YELLOW + "-" * 25)
    print("? %21s" % "Shows Commands")  # 14 long
    print("q %21s" % "Closes Program")
    print("ff %19s" % "Look for File")
    print("gn %21s" % "Create a String")
    print(Fore.YELLOW + "-" * 25)
    print("")


def file_find():
    while True:
        def ff_help():
            print("")
            print(Fore.GREEN + "File Finder Help:")
            print(Fore.YELLOW + "-" * 25)
            print("ed %20s" % "Make Changes to File")
            print("rd %20s" % "Read Content of File")
            print(Fore.YELLOW + "-" * 25)
            print("")

        def ff_edit():      #Edit Keys and Stuff!!!
            # wr1te = open(fileCat, "r")
            # print(wr1te.read())
            # d = {}
            # for line in wr1te:
                # k, v = line.strip().split('-')
                # d[k.strip()] = v.strip()
            # wr1te.close()
            # print(d)
            print("W.I.P")

        def ff_read():
            try:
                reed = open(str(fileCat), 'r')
                print(Fore.YELLOW + "-" * 63)
                print(reed.read())
                print(Fore.YELLOW + "-" * 25, Fore.YELLOW + "End of Text", Fore.YELLOW + "-" * 25)
            except NameError:
                print(Back.LIGHTRED + "!!No file detected!!\nIn order to view a file, one must exist in directory"
                      "\n\nClosing Program...")
                input("Press Enter to Exit")
                quit()

        mission = input("ff> ")
        if mission == "?":
            ff_help()
        if mission == "ed":
            ff_edit()
        if mission == "rd":
            ff_read()
        if mission == "q":
            break


def gen():              # Key Generator
    phrase = []         # Adding the letters and numbers
    label = {}          # User Input Name for Key
    try:
        f = open(str(fileCat), 'a')
        print(Fore.LIGHTMAGENTA_EX + "=" * 10, Fore.LIGHTBLUE_EX + "Key Generator", Fore.LIGHTMAGENTA_EX + "=" * 10)
        while True:
            print("What will this key be called?")
            name = input("gn> ")
            for chen in range(1, 5):
                num = random.randint(1, 9)
                let_1 = chr(random.randint(33, 122))
                let_2 = chr(random.randint(33, 122))
                phrase.append(num)
                phrase.append(let_1)
                phrase.append(let_2)
            random.shuffle(phrase)
            newt = ''.join(str(e) for e in phrase)
            label[name] = newt
            print("")
            print(Fore.LIGHTMAGENTA_EX + "=" * 25)
            print(name, ":", *phrase, sep='')
            print(Fore.LIGHTMAGENTA_EX + "=" * 25)
            print("")
            for key, value in label.items():
                f.write('%s: %s\n' % (key, value))
            print("Generate Another Key?")
            hamster = input("y/n: ")
            if hamster == "y":
                print("\n\n")
                gen()
                break
            elif hamster == "n":
                f.close()
                print(Back.WHITE + Fore.BLACK + "\n\n!!Exiting Key Generator!!\n\n")
                break
            else:
                print("Error")
                break
    except NameError:
        print("!!No file detected!!\nIn order to create keys, A text file must exist in directory"
              "\n\nClosing Program...")
        input("Press Enter to Exit")
        quit()


def selection(choice):
    while True:
        if choice == "?":
            help_screen()
            break
        if choice == "q":
            quit()
        if choice == "ff":
            file_find()
            break
        if choice == "gn":
            print(Back.LIGHTCYAN_EX + Fore.BLACK + "Start Key Generator?")
            confirm = input("y/n: ")
            if confirm == "y":
                print("\n\n")
                gen()
                break
            elif confirm == "n":
                break
            else:
                break
        else:
            print(Fore.RED + "\n\n!!ERROR: Enter '?' for help on commands!!\n\n")
            break


def main():
    print("\n\n" + Fore.LIGHTBLUE_EX + "#"*30)
    print(Fore.GREEN + "Welcome to Key Manager!")
    print(Fore.GREEN + "Type '?' for help on commands")
    print(Fore.LIGHTBLUE_EX + "#"*30)
    while True:
        mission = input("--> ")
        selection(mission)
        crt.close()               # Close and Save the File


if __name__ == '__main__':
    main()


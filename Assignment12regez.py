# Michael Suter
# Regex tutorials - using regular expressions
# 4/23/20
import re

print("""
    Type 1 to check if your input has a 'q'
    Type 2 to check if your input contains 'the'
    Type 3 to check if your input has a '*'
    Type 4 to check if your input contains a digit
    Type 6 to check if your input contains a period
    Type 6 to check if your input has at least 2 consecutive vowels
    Type 7 to check if your input contains white space
    Type 8 to check if your input has any letters that repeat three times
    Type 9 to check if your input starts with Hello
    Type 10 to check if your input contains an email address 
    Type 11 to quit
    """)


def menu():
    answer = int(input(">"))
    while answer <= 1 >= 11:
        menu()
    if answer == 1:
        print("You chose to check if the string contains a q. This will return True if it is, else it will return False.")
        response = input("Enter your string>")
        if bool(re.search("q", response)):
            print(True)
        else:
            print(False)
        return menu()
    elif answer == 2:
        print("You chose to check if the string contains 'The', This will return True if it is, else it will return False.")
        response = input("Enter your string>")
        if bool(re.search("The", response)):
            print(True)
        else:
            print(False)
        return menu()
    elif answer == 3:
        print("You chose to check if the string contains a *, This will return True if it is, else it will return False. ")
        response = input("Enter your string>")
        if bool(re.match('\*', response)):
            print(True)
        else:
            print(False)
        return menu()
    elif answer == 4:
        print("You chose to check if the string contains a digit, This will return True if it is, else it will return False")
        response = input("Enter your string>")
        if bool(re.match(r'\d', response)):
            print(True)
        else:
            print(False)
        return menu()
    elif answer == 5:
        print("You chose to check if the string contains a period '.' , This will return True if it is, else it will return False.")
        response = input("Enter your string>")
        if bool(re.search('\.', response)):
            print(True)
        else:
            print(False)
        return menu()
    elif answer == 6:
        print("You chose to check if the string contains 2 consecutive vowels, This will return True if it is, else it will return False.")
        response = input("Enter your string>")
        if response is bool(re.search(r'[aeiou]{2}', response)):
            print(True)
        else:
            print(False)
        return menu()
    elif answer == 7:
        print("You chose to check if the string contains a white space, This will return True if it is, else it will return False.")
        response = input("Enter your string>")
        if response is bool(re.match(' ', response)):
            print(True)
        else:
            print(False)
        return menu()
    elif answer == 8:
        print("You chose to check if the string contains any letters that repeat 3 times, This will return True if it is, else it will return False.")
        response = input("Enter your string>")
        if response is bool(re.match('a{1,3}', response)):
            print(True)
        else:
            print(False)
        return menu()
    elif answer == 9:
        print("You chose to check if the string Starts with 'Hello' , This will return True if it is, else it will return False.")
        response = input("Enter your string>")
        if response is bool(re.match("Hello", response)):
            print(True)
        else:
            print(False)
        return menu()
    elif answer == 10:
        print("You chose to check if the string is an email address, This will return True if it is, else it will return False.")
        response = input("Enter your string>")
        if response is bool(re.search('.com', response)):       # stumped on this and 9, I make no excuse
            print(True)
        else:
            print(False)
        return menu()
    else:
        if answer == 11:
            exit("Goodbye")


menu()

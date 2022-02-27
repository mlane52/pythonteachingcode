def str_analysis(string):
    if string.isdigit(): 
        string = int(string) 

        if string > 99: 
            return str(string) + ": That's a big number."
        else:
            return str(string) + ": That's small number."
    else: 
        if string.isalpha(): 
            return string + ": uses all alpha characters."
        else: 
            return string + ": neither all alpha nor digit."

print("StringTester\n") 

while True:
    user_input = input("Input string for testing: ") 
    if user_input == "": 
        print("No input detected.")
    else: 
        print(str_analysis(user_input)) 
        break  
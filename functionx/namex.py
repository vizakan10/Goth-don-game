output=''

def intro():
    prompt=('''\t\t\t"Welcome to DON game"\n\n\\\\\\\tYou should choose a lower value than your life score to fight\t\\\\\\
    \t\t\t\tGood Luck:)\n--------------------------------------------------------------------------------''')
    print(prompt)
    output=prompt
    name = input('Enter a user name [should start with an alphabet]:-- ')

    while name == '' or not name[0].isalpha():
        print("Start the name with an alphabet, try again\n")
        name = input('Enter a user name [should start with an alphabet]:- ')
    
    name = name.capitalize()
    return name,output







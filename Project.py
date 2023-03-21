def start():
    global name
    global r
    print("..............................................................................................................................")
    print("                                             WELCOME TO THE ARENA!!!   " )                                                   
    print("                                  Get your favourite movie recommendations here\n")
    print("                                                           - By Aaditya Sharma and Aaditya Bhalla")
    print("..............................................................................................................................")
    name=input("Enter your name: ")
    print("Welcome! " + name)
    
def movie():
    lang=int(input("Please select your recommended language: \n1. English\n2. Hindi\n"))
    print(".......................................................................................................................")
    if lang==1:
        print("You have selected English.\n")
        r=int(input("Type 1 to continue\nType 2 to switch language\nType anything else to exit\n"))
        print("..........................................................................................................................")
        if r==1:
            genre_e()
        elif r==2:
            movie()
        else:
            print("Thank you!! "+name+" See you soon.")
            exit()
        print("..............................................................................................................................")
    elif lang==2:
        print("You have selected Hindi.\n")
        r=int(input("Type 1 to continue\nType 2 to switch language\nType anything else to exit\n"))
        print(".........................................................................................................................")
        if r==1:
            genre_h()
        elif r==2:
            movie()
        else:
            print("Thank you!! "+name+" See you soon.")
            exit()
        print("..........................................................................................................................")
    else:
        print("Enter correct input!!")
        movie()

def genre_h():
    genre=int(input("Please select your recommended genre: \n1. Action\n2. Horror\n3. Adventure\n4. Comedy\n5. Science Fiction\n6. Romance\n"))
    if genre==1:
        action_h()
    elif genre==2:
        horror_h()
    elif genre==3:
        ad_h()
    elif genre==4:
        comedy_h()
    elif genre==5:
        scifi_h()
    elif genre==6:
        rom_h()
    else:
        print("\nEnter correct input!!")
        genre_h()
        
    
def genre_e():
    genre=int(input("Please select your recommended genre: \n1. Action\n2. Horror\n3. Adventure\n4. Comedy\n5. Science Fiction\n6. Romance\n"))
    print("..................................................................................................................")
    if genre==1:
        action_e()
    elif genre==2:
        horror_e()
    elif genre==3:
        ad_e()

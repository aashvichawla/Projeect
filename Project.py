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
    elif genre==4:
        comedy_e()
    elif genre==5:
        scifi_e()
    elif genre==6:
        rom_e()
    else:
        print("\nEnter correct input!!")
        genre_e()    

def action_e():
    act=int(input("\nPlease select the movie to see description: \n1. BOYKA: UNDISTPUTED\n2. RAMBO\n3. OPERATION RED SEA\n4. UNCHARTED\n5. PREDATOR\n"))
    print("..................................................................................................................")
    if act==1:
        print("\nDescription:\nWhen he finds out the wife of the man he accidentally killed is in trouble,\nBoyka offers to fight in a series of impossible battles to free her from a life of servitude.\n\nCast:\nScott Adkins\nMartyn Ford\nTeodora Duhovnikova\nAlon Abutbul\n\nReviews: 4.7/5\n\n")
        print("Trailer link:")
        print("https://youtu.be/KQtB3-NMfnU")
    
    elif act==2:
        print("\nDescription:\nHaving long-since abandoned his life as a lethal soldier, John Rambo\n(Sylvester Stallone) lives a solitary life near the Thai border. Two weeks after guiding a missionary\n(Julie Benz) and her comrades into Burma, he gets an urgent call for help.\n\nCast:\nSylvester Stallone\nYvette Monreal\nRichard Crenna\nSean Albertson\n\nReviews: 4.5/5\n\n")
        print("Trailer link:")
        print("https://youtu.be/2CRjdwRYQbU")
    
    elif act==3:
        print("\nDescription:\nThe film was loosely based on the evacuation of the 225 foreign nationals\nand almost 600 Chinese citizens from Yemen's southern port of Aden during the 2015 Yemeni\nCivil War in late March.\n\nCast:\nJiang Luxia\nHusang Johnny\nHai-Qing\nFang Yin\n\nReviews: 3.9/5\n\n")
        print("Trailer link:")
        print("https://youtu.be/w2dbIXyB5yY")
    
    elif act==4:
        print("\nDescription:\nStreet-smart Nathan Drake (Tom Holland) is recruited by seasoned treasure hunter Victor 'Sully' Sullivan (Mark Wahlberg) to recover a fortune amassed by Ferdinand Magellan and lost 500 years ago by the House of Moncada\n\nCast:\nTom Holland\nSophia Ali\nMark Wahlberg\nTati Gabrielle\n\nReviews:3.2/5\n\n")
        print("Trailer link:")
        print("https://youtu.be/eHp3MbsCbMg")
    
    elif act==5:
        print("\nDescription:\nIt stars Arnold Schwarzenegger as the leader of an elite paramilitary rescue team on a mission to save hostages in guerrilla-held territory in a Central American rainforest, who encounter the deadly Predator (Kevin Peter Hall), a skilled, technologically advanced alien who stalks and hunts them down\n\nCast:\nArnold Schwarzenegger\nCarl Weathers\nKevin Peter Hall\n\nReviews:4.1/5\n\n")
        print("Trailer link:")
        print("https://youtu.be/WaG1KZqrLvM")
    
    else:
        print("\nEnter correct input!!")
        action_e()
        
        
    
def action_h():
    act=int(input("\nPlease select the movie to see description: \n1. RRR\n2. K.G.F: CHAPTER 1\n3. BAAHUBALI: THE BEGINNING\n4. TIGER ZINDA HAI\n5. URI: THE SURGICAL STRIKE\n"))
    print("..................................................................................................................")
    if act==1:
        print("\nDescription:\nSet in the 1920s, the plot explores the undocumented period in their lives when\nboth the revolutionaries chose to go into obscurity before they began the fight for their country.\n\nCast:\nRam Charan\nN.T Rama Rao Jr.\nAjay Devgan\nAliabhatt\n\nReviews: 4.8/5\n\n")
        print("Trailer link:")
        print("https://youtu.be/GY4BgdUSpbE")
        
    elif act==2:
        print("\nDescription:\nIn the 1970s, a gangster goes undercover as a slave to assassinate the owner of\na notorious gold mine. Edit Report This. The movie dates back to 1951. Here, two incidents take place;\nThe birth of the hero and other in the Kolar Gold Fields (K.G.F) they get gold.\nThe hero is brought up in poverty.\n\nCast:\nYash\nSrinidhi Shetty\nRamchandra Raju\nAnant Nag\n\nReviews: 4.4/5\n\n")
        print("Trailer link:")
        print("https://youtu.be/Qah9sSIXJqk")    
    
    elif act==3:
        print("\nDescription:\nThe first of two cinematic parts, the film follows Sivudu, an adventurous young man who\nhelps his love Avantika rescue Devasena, the former queen of Mahishmati who is now a prisoner under the\ntyrannicalrule of king Bhallaladeva. The story concludes in Baahubali 2: The Conclusion.\n\nCast:\nPrabhas\nRana Daggubati\nRamya Krishnan\nAnushka Shetty\n\nReviews: 4.3/5\n\n")
        print("Trailer link:")
        print("https://youtu.be/sOEg_YZQsTI")
    
    elif act==4:
        print("\nDescription:\nWhen a group of Indian and Pakistani nurses are held hostage in Iraq by a terrorist organization, a secret agent is drawn out of hiding to rescue them. Inspired by real events, Tiger Zinda Hai is a sequel to the blockbuster Ek Tha Tiger, and an espionage action thriller that follows a daring rescue mission in Iraq\n\nCast:\nSalman Khan\nKtrina Kaif\nParesh Rawal\n\nReviews:3.7/5\n\n")
        print("Trailer link:")
        print("https://youtu.be/ePO5M5DE01I")    
    
    elif act==5:
        print("\nDescription:\nIndian army special forces execute a covert operation, avenging the killing of fellow army men at their base by a terrorist group. Divided over five chapters, the film chronicles the events of the surgical strike conducted by the Indian military against suspected militants in Pakistan occupied Kashmir\n\nCast:\nVicky Kaushal\nYami Gautam\nParesh Rawal\nMohit Raina\n\nReviews:4.4/5\n\n")
        print("Trailer link:")

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
        print("https://youtu.be/Tqlvm-iCerg")    
    
    else:
        print("\nEnter correct input!!")
        action_h()
    
def horror_e():
    hor=int(input("\nPlease select the movie to see description: \n1. THE EXORCIST (1973)\n2. THE SHINING\n3. THE CONJURING (2013)\n4.THE INVITATION\n5.THE RING\n"))

    print("..................................................................................................................")
    if hor==1:
        print("\nDirector:\nWilliam Friedkin\n\nWriter:\nWilliam Peter Braddy\n\nCast:\nEllen Burstyn\nMax Von Sydow\nLinda Blair\n\nDescription:\nIt stars Ellen Burstyn, Max von Sydow, Lee J. Cobb, Kitty Winn, Jack MacGowran (in his final\nfilm role), Jason Miller and Linda Blair. It follows the demonic possession of a young girl and\nher mother&#39;s attempt to rescue her through an exorcism conducted by a pair of Catholic\npriests.\n\nReviews:3.8/5\n\n")
        print("Trailer link")
        print("https://youtu.be/NbNhVAA2d_k")
    elif hor==2:
        print("\nDirector:\nStanley Kubric\n\nWriter:\nStephen King\n\nCast:\nJack Nicholson\nShelly Duvall\nDanny Lloyd\n\nDescription:\nA family heads to an isolated hotel for the winter where a sinister presence influences the\nfather into violence, while his psychic son sees horrific forebodings from both past and\nfuture.\n\nReviews:3.9/5\n\n")
        print("Trailer link")
        print("https://youtu.be/S014oGZiSdI")
    elif hor==3:
        print("\nDirector:\nJames Wan\n\nWriter:\nChad Heyes and Carey W. Hayes\n\nCast:\nPatric Wilson\nVera Farmiga\nRon Livingston\n\nDescription:\nParanormal investigators Ed and Lorraine Warren work to help a family terrorized by a dark\npresence in their farmhouse. In 1971, Carolyn and Roger Perron move their family into a\ndilapidated Rhode Island farm house and soon strange things start happening around it with\nescalating nightmarish terror.\n\nReviews:4.2/5\n\n")
        print("Trailer link")
        print("https://youtu.be/k10ETZ41q5o")
    elif hor==4:
        print("\nDescription:\n A young woman is courted and swept off her feet, only to realize a gothic conspiracy is afoot. \n\nCast:\n Nathalie Emmanuel\n Thomas DohertySean\n Pertwee See\n\nReviews: 4.2/5\n\n")
        print("Trailer link")
        print("https://youtu.be/5bL1ftuxgOE")
    elif hor==5:
        print("\nDescription:\nA journalist must investigate a mysterious videotape which seems to cause the death of anyone one week to the day after they view it. Rachel Keller is a journalist investigating a videotape that may have killed four teenagers (including her niece).\n\nCast:\n Naomi Watts\n Martin Henderson\n Brian Cox\n\nReviews: 4.7/5\n\n")
        print("Trailer link")
        print("https://youtu.be/yzR2GY-ew8I")
              
    else:
        print("\nEnter correct input!!")
        horror_e()
        
def horror_h():
    hor=int(input("Please select the movie to see description: \n1. TUMBBAD\n2. PARI\n3. PIZZA (2013)\n4.LAXMII\n5.STREE\n"))
    print("...................................................................................................................")
    if hor==1:
        print("\nDirector:\nRahi Anil Barve, Anand Gandhi, Adesh Prasad\n\nWriter:\nMitesh Shah\n\nCast:\nSohum Shah\nJyoti Malshe\nAnita Date-Kelkar\nRonjini Chakraborty\n\nDescription:\nA mythological story about a goddess who created the entire universe. The plot revolves\naround the consequences when humans build a temple for her first-born.\n\nReviews:3.2/5\n\n")
        print("Trailer link")
        print("https://youtu.be/ZjuhALyNgss")         
    elif hor==2:
        print("\nDirector:\nProsit Roy\n\nCast:\nAnushka Sharma\nParambrata Chattopadhyay\nRajat Kapoor\nRitabhari Chakraborty\n\nDescription:\nArnab tries to help Ruksahana, who is found under mysterious circumstances in a house. He\nlets her stay at his home until he discovers something strange about her.\n\nReviews:4.1/5\n\n")
        print("Trailer link")      
        print("https://youtu.be/PQKu78NnyvU")
    elif hor==3:
        print("\nDirector:\nKartthik Subbaraj\n\nCast:\nVijay Sethupathi\nRamya Nambeeshan\nAadukalam Naren\n\nDescription:\nA pizza delivery boy lands in a mysterious circumstance and it works a dramatic change in\nhis life.\n\n")
        print("Trailer link")
        print("https://youtu.be/i5GtgmlWTXE")
    elif hor==4:
        print("\nDescription:\n Aasif visits his wife's parents' house and happens to go to a ground that is supposedly haunted. However, he is soon possessed by the spirit of a transgender who is out for revenge.\n\nCast:\n Akshay Kumar\n Kiara Advani\n Sharad Kelkar\n\nReviews: 4.4/5\n\n")
        print("Trailer link")
        print("https://youtu.be/AzTYIiRYmv0")
    elif hor==5:
        print("\nDescription:\n in the small town of Chanderi, the menfolk live in fear of an evil spirit named 'Stree' who abducts men in the night. Based on the urban legend of 'Nale Ba' that went viral in Karnataka in the 1990s. \n\nCast:\n Ashish Chhipa \n Rajkummar Rao \n Shraddha kapoor\n\nReviews: 4.7/5\n\n")
        print("Trailer link")
        print("https://youtu.be/gzeaGcLLl_A")
    
    else:
        print("\nEnter correct input!!")
        horror_h()

        
def ad_e():
    ad=int(input("Please select the movie to see description: \n1. UNCHARTED\n2. JURASSIC PARK\n3. JOURNEY 2: THE MYSTERIOUS ISLAND\n4.JUNGLE CRUISE\n5.JACK THE GIANT SLAYER\n"))
    print("...............................................................................................................")
    if ad==1:
        print("\nDirector:\nRuben Fleischer\n\nCast:\nTom Holland\nMark Wahlberg\nAntonio Banderas\n\nDescription:\nStreet-smart Nathan Drake is recruited by seasoned treasure hunter Victor Sully Sullivan to \nrecover a fortune amassed by Ferdinand Magellan, and lost 500 years ago by the House of Moncada.\n\nReviews: 4.8/5\n\n")
        print("Trailer link")
        print("https://youtu.be/eHp3MbsCbMg")
    elif ad==2:
        print("\nDirector:\nSteven Spielberg\n\nCast:\nSam Neill\nLaura Dern\nJeff Goldblum\n\nDescription:\nA pragmatic paleontologist touring an almost complete theme park on an island in Central America\nis tasked with protecting a couple of kids after a power failure causes the park's cloned dinosaurs to run loose.\n\nReviews: 4.3/5\n\n")
        print("Trailer link")
        print("https://youtu.be/lc0UehYemQA")
    elif ad==3:
        print("\nDirector:\nBrad Peyton\n\nCast:\nJosh Hutcherson\nDwayne Johnson\nMichael Caine\n\nDescription:\nSean Anderson partners with his mom's husband on a mission to find his grandfather, who is thought\nto be missing on a mythical island.\n\nReviews: 4.4/5\n\n")
        print("Trailer link")
        print("https://youtu.be/qdFCjwcK8IE") 
    elif ad==4:
        print("\nDescription:\n Based on Disneyland's theme park ride where a small riverboat takes a group of travelers through a jungle filled with dangerous animals and reptiles but with a supernatural element.. \n\nCast:\n Dwayne Johnson\n Emily Blunt\n Edgar Ramírez \n\nReviews: 4.8/5\n\n")
        print("Trailer link")
        print("https://youtu.be/RPkFU1CUb6s")
    elif ad==5:
        print("\nDescription:\n The ancient war between humans and a race of giants is reignited when Jack, a young farmhand fighting for a kingdom and the love of a princess, opens a gateway between the two worlds. \n\nCast:\n Nicholas Hoult \n Stanley Tucci \n Ewan McGregor \n\nReviews: 4.7/5\n\n")
        print("Trailer link")
        print("https://youtu.be/ng9rjC8MOgU")
              
     
    else:
        print("\nEnter correct input!!")
        ad_e()

    
def ad_h():
    ad=int(input("Please select the movie to see description: \n1. RA.ONE\n2. TIGER ZINDA HAI\n3. ZINDAGI NA MILEGI DOBARA\n4.THE JUNGLE BOOK\n5.THUGS OF HINDOSTAN\n"))
    print("................................................................................................................")
    if ad==1:
        print("\nDirector:\nAnubhav Sinha\nBazin bs\n\nCast:\nShah Rukh Khan\nArjun Rampal\nKareena Kapoor\n\nDiscription:\nWhen the titular antagonist of an action game takes on physical form, it's only the game's less powerful\nprotagonist who can save his creator's family.\n\nReviews: 4/5\n\n")
        print("Trailer link")
        print("https://youtu.be/d9PlHc_qVKw")
    elif ad==2:
        print("\nDirector:\nAli Abbas zafar\n\nCast:\nSalman Khan\nKatrina Kaif\nParesh Rawal\n\nDescription:\nWhen a group of Indian and Pakistani nurses are held hostage in Iraq by a terrorist organization,\na secret agent is drawn out of hiding to rescue them.\n\nReviews:3.9/5\n\n")
        print("Trailer link")
        print("https://youtu.be/ePO5M5DE01I")
    elif ad==3:
        print("\nDirector:\nZoya Akhtar\n\nCast:\nHrithik Roshan\nFarhan Akhtar\nAbhay deol\n\nDescription:\nThree friends decide to turn their fantasy vacation into reality after one of their friends gets engaged.\n\nReviews: 4.1/5\n\n")
        print("Trailer link")
        print("https://youtu.be/FJrpcDgC3zU")
    elif ad==4:

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
        print("\nDescription:\n After a threat from the tiger Shere Khan forces him to flee the jungle, a man-cub named Mowgli embarks on a journey of self discovery with the help of panther Bagheera and free-spirited bear Baloo.\n\nCast:\nNeel Sethi\nBill Murray\nBen Kingsley\n\nReviews: 4.8/5\n\n")
        print("Trailer link")
        print("https://youtu.be/C4qgAaxB_pc")   
    elif ad==5:
        print("\THUGS OF HINDOSTAN\nDescription:\nRecruited by the East India Company, a local thug infiltrates a troop of patriotic bandits who plan to overthrow the British regime and reclaim their independence. \n\nCast:\n Amitabh Bachchan\n Aamir Khan \n Lloyd Owen \n\nReviews: 4/5\n\n")
        print("Trailer link")
        print("https://youtu.be/zI-Pux4uaqM")
    
    else:
        print("\nEnter correct input!!")
        ad_h()

def comedy_e():
    comedy=int(input("Please select the movie to see description: \n1. CENTRAL INTELLIGENCE\n2. HOME ALONE\n3. JOHNY ENGLISH\n4.THE INVENTION OF LYING\n5.THE HANGOVER\n"))
    print("....................................................................................................................")
    if comedy==1:
        print("\nDirector:\nRawson Marshall Thurber\n\nCast:\nDwayne johnson\nKevin Hart\nDanielle Nicolet\n\nDescription:\nAfter he reconnects with an awkward pal from high school through Facebook, a mild-mannered accountant\nis lured into the world of international espionage.\n\n")
        print("Trailer link")
        print("https://youtu.be/MxEw3elSJ8M")       
    elif comedy==2:
        print("\nDirector:\nChris Columbus\n\nCast:\nMacaulay Culkin\nJoe Pesci\nDaniel Stern\n\nDescription:\nAn eight-year-old troublemaker must protect his house from a pair of burglars when he is accidentally\nleft home alone by his family during Christmas vacation.\n\n")
        print("Trailer link")
        print("https://youtu.be/0iNmVVlmmv8")
    elif comedy==3:
        print("\nDirector:\nPeter Howwit\n\nCast:\nRowan Akinson\nJohn Malkovich\nNatalie Imbruglia\n\nDescription:\nAfter a sudden attack on MI5, Johnny English, Britain's most confident, yet unintelligent spy, becomes Britain's only spy.\n\n")
        print("Trailer link")
        print("https://youtu.be/-Qv6p6pTz5I")
    elif comedy==4:
        print("\nDescription:\nA comedy set in a world where no one has ever lied, until a writer seizes the opportunity for personal gain. \n\nCast:\n Ricky Gervais \n Jennifer Garner \n Jonah Hill \n\nReviews: 4.5/5\n\n")
        print("Trailer link")
        print("https://youtu.be/RhRnmyBjOLs")
    elif comedy==5:
        print("\nDescription:\nThree buddies wake up from a bachelor party in Las Vegas, with no memory of the previous night and the bachelor missing. They make their way around the city in order to find their friend before his wedding. \n\nCast:\n Zach Galifianakis \n Bradley Cooper\n Justin Bartha \n\nReviews: 4.7/5\n\n")
        print("Trailer link")
        print("https://youtu.be/tcdUhdOlz9M")      
    else:
        print("\nEnter correct input!!")
        comedy_e()

def comedy_h():
    comedy=int(input("Please select the movie to see description: \n1. PHIR HERA PHERI\n2. DESI BOYZ\n3. HOUSEFULL\n4.DHAMAAL\n5.DHAMAAL\n"))
    print("..........................................................................................................................")
    if comedy==1:
        print("\nDirector:\nNeeraj Vora\n\nCast:\nAkshay Kumar\nSuniel Shetty\nParesh Rawal\n\nDescription:\nBaburao, Raju and Shyam are living happily after having risen from rags to riches. Still, money brings the joy of riches\nand with it the greed to make more money. And so, with a don as an unknowing investor, Raju initiates a new game.\n\nReviews:4/5\n\n")
        print("Trailer link")
        print("https://youtu.be/1rJQQCZcq2s")
    elif comedy==2:
        print("\nDirector:\nRohit Dhawan\n\nCast:\nAkshay Kumar\nJohn Abraham\nDeepika Padukone\n\nDescription:\nTwo friends lose their jobs, then part bitterly after they get exposed as male strippers.\n\nReviews:3.9/5\n\n")
        print("Trailer link")
        print("https://youtu.be/wOcisXA4z4")
    elif comedy==3:
        print("\nDirector:\nSajid Khan\n\nCast:\nAkshay Kumar\nDeepika Padukone\nRiteish Deshmukh\n\nDescription:\nBelieving himself to be jinxed, a man attempts to find true love, but instead gets caught in a web of lies.\n\nReviews:4/5\n\n")
        print("Trailer link")
        print("https://youtu.be/oqPZHVekBZ0")      
    elif comedy==4:
        print("\nDescription:\nFour lazy slacker conmen buddies who are jobless, homeless and broke learn about the secret of a hidden treasure from a dying thief and later embark on a race against time to find the mobster's buried treasure and claim it while being pursued by a determined police inspector who is hellbent to get the treasure all by himself. \n\nCast:\n Sanjay Dutt \n Riteish Deshmukh \n Arshad Warsi \n\nReviews: 4.6/5\n\n")
        print("Trailer link")
        print("https://youtu.be/LZX2NAR_QlY")
    elif comedy==5:
         print("\nDescription:\nTwo friends are searching for their long lost companion. They revisit their college days and recall the memories of their friend who inspired them to think differently, even as the rest of the world called them 'idiots'. \n\nCast:\n  Aamir Khan\n Madhavan\n Sharman Joshi \n kareena Kapoor\n Boman Irani \n\nReviews: 4.8/5\n\n")
         print("Trailer link")
         print("https://youtu.be/K0eDlFX9GMc")   
        
    
    else:
        print("\nEnter correct input!!")
        comedy_h()

def scifi_e():
    scifi=int(input("Please select the movie to see description: \n1. THE TERMINATOR\n2. INTERSTELLAR\n3. DUNE\n4. INCEPTION\n5. THE MARTIAN\n"))
    print(".........................................................................................................................")
    if scifi==1:
        print("\nDescription:\nThe Terminator is a formidable robotic assassin and soldier, designed by the\nmilitary supercomputer Skynet for infiltration and combat duty, towards the ultimate goal of exterminating\nthe Human Resistance.\n\nCast:\nArnold Schwarzenegger\nLinda Hamilton\Bill Paxton\nWilliam Wisher Jr.\n\nReviews: 4.1/5\n\n")
        print("Trailer link:")
        print("https://youtu.be/k64P4l2Wmeg")  
        
    elif scifi==2:
        print("\nDescription:\nInterstellar is about Earth's last chance to find a habitable planet before a lack of\nresources causes the human race to go extinct. The film's protagonist is Cooper (Matthew McConaughey),\na former NASA pilot who is tasked with leading a mission through a wormhole to find a habitable planet in\nanother galaxy.\n\nCast:\nMatthew McConaughey\nJessica Chastain\nAnne Hathaway\nMatt Damon\n\nReviews: 3.7/5\n\n")
        print("Trailer link:")
        print("https://youtu.be/zSWdZVtXT7E")      
    
    elif scifi==3:
        print("\nDescription:\nA mythic and emotionally charged hero's journey, Dune tells the story of Paul\nAtreides, a brilliant and gifted young man born into a great destiny beyond his understanding,\nwho must travel to the most dangerous planet in the universe to ensure the future of his family and his people.\n\nCast:\nTimothee Chalamet\nZendaya\nJason Momoa\nOscar Issac\n\nReviews: 3.5/5\n\n")
        print("Trailer link:")
        print("https://youtu.be/8g18jFHCLXk")      
    
    elif scifi==4:
        print("\nDescription:\nInception centres on brooding “extractor” Dom Cobb (played by Leonardo DiCaprio)—a thief who invades targets' dreams through a chemical-induced shared dream state in order to steal valuable information\n\nCast:\nLeonardo DiCaprio\nJoseph Gordon Levitt\nTom Hrady\n\nReviews:4.6/5\n\n")
        print("Trailer link:")
        print("https://youtu.be/YoHD9XEInc0")  
        
    elif scifi==5:
        print("\nDescription:\nAn astronaut becomes stranded on Mars after his team assume him dead, and must rely on his ingenuity to find a way to signal to Earth that he is alive and can survive until a potential rescue\n\nCast:\nMatt Damon\nJessica Chastain\nChiwetel Ejiofor\nKate Mara\n\nReviews:4/5\n\n")
        print("Trailer link:")
        print("https://youtu.be/ej3ioOneTy8")  
    
    else:
        print("\nEnter correct input!!")
        scifi_e()

        
        
def scifi_h():
    scifi=int(input("Please select the movie to see description: \n1. MISSION MANGAL\n2. ROBOT\n3. KOI... MIL GAYA\n4. RA.ONE\n5. KRRISH 3\n"))
    if scifi==1:
        print("\nDescription:\nMangalyaan was India's first interplanetary mission. The indigenously-built\nspace probe has been in the Martian orbit since September 24, 2014. The mission made India the first\nAsian country, and the fourth in the world after Roscosmos, NASA, and the European \nSpace Agency, to get to the planet.\n\nCast:\nAkshay Kumar\nVidya Balan\nSonakshi Sinha\nSharman Joshi\n\nReviews: 4.1/5\n\n")
        print("Trailer link:")
        print("https://youtu.be/q10nfS9V090")      
    
    elif scifi==2:
        print("\nDescription:\nVasigaran (Rajnikanth) builds a perfect replica of himself, a super-robot he \naffectionately dubs Chitti. Dr. Vasi has noble plans of donating Chitti to the Indian army, \nbut when Chitti suddenly develops feelings for Dr. Vasi's fiancee, Sana (Aishwarya Rai Bachchan), things get awkward\n\nCast:\nRajnikanth\nAishwarya Rai Bachchan\nSanthanam\nDanny Denzongpa\n\nReviews: 3.6/5\n\n")
        print("Trailer link:")
        print("https://youtu.be/RprCwSsUe5E")  
    
    elif scifi==3:
        print("\nDescription:\nKoi... Mil Gaya focuses on Rohit (Hrithik Roshan), a developmentally\ndisabled man who contacts an extraterrestrial being with his late father Sanjay's (Rakesh Roshan) \ncomputer. The film followshis relationship with Nisha (Zinta), Rohit's friend, who falls in love with him.\n\nCast:\nHrithik Roshan\nPreity Zinta\nPrem Chopra\nMukesh Rishi\n\nReviews: 3.2/5\n\n")
        print("Trailer link:")
        print("https://youtu.be/VxDudRIMKrc")      
    
    elif scifi==4:
        print("\nDescription:\nOne (also played by Khan). The former escapes from the game's virtual world and enters the real world; his aim is to kill Lucifer, the game ID of Shekhar's son and the only player to have challenged Ra. One's power. Relentlessly pursued, the family is forced to bring out G\n\nCast:\nShah Rukh Khan\nKreena Kapoor\nRajnikanth\nAmitabh Bachchan\nPriyanka Chopra\n\nReviews:2.8/5\n\n")
        print("Trailer link:")
        print("https://youtu.be/d9PlHc_qVKw")  
        
    elif scifi==5:
        print("\nDescription:\nKrrish and his scientist father must save the world and their own family from an evil man named Kaal and his gang of mutants, led by the ruthless Kaya. After defeating the villainous Dr. Siddhant Arya and bringing his father Rohit back from the dead, Krrish continued fighting against evil and saving innocent lives\n\nCast:\nHrithik Roshan\nKangana Ranaut\nPriyanka Chopra\n\nReviews:2.4/5\n\n")
        print("Trailer link:")
        print("https://youtu.be/_6Ix1VF_yWM")  
        
    else:
        print("\nEnter correct input!!")
        scifi_h()
        
        
def rom_e():
    rom=int(input("Please select the movie to see description: \n1. PRIDE & PREJUDICE\n2. AFTER\n3. THE NOTEBOOK\n4. THE VOW\n5. THE LUCKY ONE\n"))
    print(".........................................................................................................................")
    if rom==1:
        print("\nDescription:\nSparks fly when spirited Elizabeth Bennet meets single, rich, and proud Mr. Darcy. But\nMr. Darcy reluctantly finds himself falling in love with a woman beneath his class. Can each \novercome their own pride and prejudice?\n\nCast:\nKeira Knightley\nMathew Macfadyen\nCarey Mulligan\nRosamund Pike\n\nReviews: 4.0/5\n\n")
        print("Trailer link:")
        print("https://youtu.be/Ur_DIHs92NM")  
    
    elif rom==2:
        print("\nDescription:\nBased on the novel by Anna Todd. Based on Anna Todd's novel, AFTER follows Tessa\n(Langford), a dedicated student, dutiful daughter, and loyal girlfriend to her high-school sweetheart,\nas she enters her first semester in college armed with grand ambitions for her future.\n\nCast:\nJosephine Langford\nAnna Todd\nSelma Blair\nHero Fiennes\n\nReviews: 3.9/5\n\n")
        print("Trailer link:")
        print("https://youtu.be/g99KPOpqZ4Q")     
    
    elif rom==3:
        print("\nDescription:\nThe Notebook is an achingly tender story about the enduring power of love, a story of\nmiracles that will stay with you forever. Set amid the austere beauty of coastal North Carolina in 1946,\nThe Notebook begins with the story of Noah Calhoun, a rural Southerner returned home from World War II.\n\nCast:\nRyan Gosling\nRachel McAdams\nJames Garner\nSam Shepard\n\nReviews: 3.3/5\n\n")
        print("Trailer link:")
        print("https://youtu.be/FC6biTjEyZw")  
        
    elif rom==4:
        print("\nDescription:\nInspired by a true story, The Vow is the tale of a love that refuses to be forgotten. Leo (Channing Tatum, Dear John ) is devastated when a car accident plunges his wife Paige (Rachel McAdams, The Notebook ) into a deep coma. She miraculously recovers – but the last five years of her memories have vanished\n\nCast:\nRachel McAdams\nChanning Tatum\nJessica Lange\nJoe Cobden\n\nReviews:2.4/5\n\n")
        print("Trailer link:")
        print("https://youtu.be/PcL24s-S6ns")  
        
    elif rom==5:
        print("\nDescription:\nIt is an adaptation of Nicholas Sparks' 2008 novel of the same name. The film stars Zac Efron as Logan Thibault, a US Marine who finds a photograph of a young woman while serving in Iraq, carries it around as a good luck charm, and later tracks down the woman, with whom he begins a relationship\n\nCast:\nZac Efron\nTaylor Schilling\nJoe Chrest\n\nReviews:3.1/5\n\n")
        print("Trailer link:")
        print("https://youtu.be/9w8lE83oYeM")  
        
    else:
        print("\nEnter correct input!!")
        rom_e()
        
        
def rom_h():
    rom=int(input("Please select the movie to see description: \n1. RAABTA\n2. DHADAK\n3. SANAM RE\n4. GEHRAIYAAN\n5. AASHIQUI 2\n"))
    print("...........................................................................................................................")
    if rom==1:
        print("\nDescription:\nRaabta is a story of Shiv and Saira, long lost lovers who have to fight the same \nhurdles that they did centuries back that drifted them apart. Shiv (Rajput) and Saira (Sanon) fall for\neach other. However, Saira experiences certain nightmares. She then comes across Zack (Sarbh) and feels\nthe same connection with him.\n\nCast:\nSushant Singh Rajput\nKriti Sanon\nRajkumar Rao\nDeepika Padukone\n\nReviews: 2.4/5\n\n")
        print("Trailer link:")
        print("https://youtu.be/YXjYfpqg8Z0")
    
    elif rom==2:
        print("\nDescription:\nSet in Rajasthan, this love story explores how the protagonists deal with issues\nlike differences between castes and honor killings.\n\nCast:\nJhanvi Kapoor\nIshaan Khattar\nAshutosh Rana\nAnkit Bisht\n\nReviews: 2.7/5\n\n")
        print("Trailer link:")
        print("https://youtu.be/TIE92mUvSsw")
        
    elif rom==3:
        print("\nDescription:\nA man focused on his career finds solace when he reunites with his childhood sweetheart\n\nCast:\nDivya Khosla\nYami Gautam\nUrvashi Rautela\nRishi Kapoor\n\nReviews: 2.2/5\n\n")
        print("Trailer link:")
        print("https://youtu.be/fvQZkpnb764")
        
    elif rom==4:
        print("\nDescription:\nAlisha (Deepika Padukone), a yoga instructor, believes that her personal and professional lives are in shambles. She's having trouble finding an investor for her fitness software, and her six-year relationship with Karan, a struggling writer, has reached a stalemate\n\nCast:\nDeepika Padukone\nSiddhant Chaturvedi\nRajat Kapoor\n\nReviews:3.2/5\n\n")
        print("Trailer link:")
        print("https://youtu.be/Yy8SKJygKD4")
        
    elif rom==5:
        print("\nDescription:\nHe meets Arohi in a bar in Goa, where she works to earn a living. Impressed by her singing, he promises her to take her to Mumbai and make her a star, where they fall in love with each other. Aashiqui 2 is a musical love story of these lovers who goes through love and hate, fame and failure in their lives\n\nCast:\nAditya Roy Kapur\nShraddha Kapoor\nShaad Randhawa\nMahesh Thakur\n\nReviews:3.2/5\n\n ")
        print("Trailer link:")
        print("https://youtu.be/FyXXgpPqe6w")
        
    else:
        print("\nEnter correct input!!")
        rom_h()


start()
movie()

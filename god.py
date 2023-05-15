import random

class items:
    def __init__(self, name, belongsTo, rarity, type):
        self.self = self
        self.name = name # what gets outputted
        self.belongsTo = belongsTo # whose is it
        self.rarity = rarity # e.g TETH/HE, 00/000
        self.type = type # EGO or Identity or Trash(0s)


 # intended but it doesn't work FSR therefore nothing for identities also
class MainSim: 
    # Set up a lot of foundation so i can do a lot more with this later, some things planned:
    # next: draw until you have specific thing
    # statistics of pulls: etc, how much of a session was EGO, 3 stars, Etc
    # statistics of % drawn of each sinner 
    # GUI which will make it more than a command to be run
    # extra line when EGO/000 drops 
    # extra line when 00 drops
    # extra line for duplicates
    # EGO cannot be drawn twice in a session feature
    # if draw 0 or 00 just make it output onestar or twostar
    # interact to keep drawing instead of all at once
    # some sort of database??
    # actual luck vs calculated chance
    # draw until you have specific thing
    # target extraction like banners, 000 guaranteed tickets
    # luck with respect to one specific item that you wish for
    # daily 4 pulls
    # ^ I realized that that would need numerous different banner informations other than the standard so unless that can be automated I'm not doing that
    # sort results_str 
    # put same stuff into vars 
    # code below 

    ### big list of everything in the game (probably a better way to do it)
    # shorten
    trashtype = "Trash"
    idtype = "Identity"
    egotype = "EGO"
    threestar = "B"
    twostar = "C"
    onestar = "D"
    Zayin = "A-ZAYIN"
    Teth = "A-TETH"
    He = "A-HE"
    ### LCB sinners aka 0 stars, this is all pointless crap for flavor
    LCB_Sinner_YiSang = items("LCB Sinner Yi Sang", "Yi Sang", onestar, trashtype)
    LCB_Sinner_Knows_Everything = items("LCB Sinner Faust", "Faust", onestar, trashtype)
    LCB_Sinner_DQte = items("LCB Sinner Don Quixote", "Don Quixote", onestar, trashtype)
    LCB_Sinner_R_S = items("LCB Sinner Ryoshu", "Ryoshu", onestar, trashtype)
    LCB_Sinner_Meursault = items("LCB Sinner Meursault", "Meursault", onestar, trashtype)
    LCB_Sinner_Hong = items("LCB Sinner Hong Lu", "Hong Lu", onestar, trashtype)
    LCB_Sinner_Heathcliff = items("LCB Sinner Heathcliff", "Heathcliff", onestar, trashtype)
    LCB_Sinner_Ishmael = items("LCB Sinner Ishmael", "Ishmael", onestar, trashtype)
    LCB_Sinner_Rodya = items("LCB Sinner Rodion", "Rodion", onestar, trashtype)
    LCB_Sinner_Shinculairu = items("LCB Sinner Sinclair", "Sinclair", onestar, trashtype)
    LCB_Sinner_Outis = items("LCB Sinner Outis", "Outis", onestar, trashtype)
    LCB_Sinner_Gregor = items("LCB Sinner Gregor", "Gregor", onestar, trashtype)
    ### 2 stars, 00s
    Seven_YiSang = items("Seven Section 6 Yi Sang", "Yi Sang", twostar, idtype)
    L_Faust = items("Lobotomy Corp. Remnant Faust", "Faust", twostar, idtype)
    W_Faust = items("W Corp. Cleanup Agent Faust", "Faust", twostar, idtype)
    Shi_Don = items("Shi Section 5 Director Don Quixote", "Don Quixote", twostar, idtype)
    N_Don = items("N Corp. Mittelhammer Don Quixote", "Don Quixote", twostar, idtype)
    Seven_R_S = items("Seven Section 6 Ryoshu", "Ryoshu", twostar, idtype)
    Liu_Meursault = items("Liu Section 6 Meursault", "Meursault", twostar, idtype)
    Kuro_Hong = items("Kurokumo Wakashu Hong Lu", "Hong Lu", twostar, idtype)
    Hong_Liu = items("Liu section 5 Hong Lu", "Hong Lu", twostar, idtype)
    Shi_Cliff = items("Shi Section 5 Heathcliff", "Heathcliff", twostar, idtype)
    N_Cliff = items("N Corp. Kleinhammer Heathcliff", "Heathcliff", twostar, idtype)
    Shi_Mael = items("Shi Section 5 Ishmael", "Ishmael", twostar, idtype)
    LCCB_Mael = items("LCCB Assistant Manager Ishmael", "Ishmael", twostar, idtype)
    LCCB_Rodya = items("LCCB Assistant Manager Rodion", "Rodion", twostar, idtype)
    N_Rodya = items("N Corp. Mittelhammer Rodion", "Rodion", twostar, idtype)
    Mexiclair = items("Jefe de los Marachis Sinclair", "Sinclair", twostar, idtype)
    Zweiclair = items("Zwei Section 6 Sinclair", "Sinclair", twostar, idtype)
    Blade_Outis = items("Blade Lineage Cutthroat Outis", "Outis", twostar, idtype)
    G_Outis = items("G Corp. Head Manager Outis", "Outis", twostar, idtype)
    Liu_Gregor = items("Liu Section 6 Gregor", "Gregor", twostar, idtype)
    ### 3 stars, 000s
    V_50 = items("Blade Lineage Salsu Yi Sang", "Yi Sang", threestar, idtype)
    Grip = items("The One Who Grips Faust", "Faust", threestar, idtype)
    W_Don = items("W Corp. Cleanup Agent Don Quixote", "Don Quixote", threestar, idtype)
    Kuro_R_S = items("Kurokumo Wakashu Ryoshu", "Ryoshu", threestar, idtype)
    Chef_R_S = items("R.B Chef de Cuisine Ryoshu", "Ryoshu", threestar, idtype)
    W_Meur = items("W Corp. Cleanup Agent Meursault", "Meursault", threestar, idtype)
    N_Meur = items("N Corp. Großhammer Meursault", "Meursault", threestar, idtype)
    TT_Lu = items("Tingtang Gangleader Hong Lu", "Hong Lu", threestar, idtype)
    Rabbit = items("R Corp. 4th Pack Rabbit Heathcliff", "Heathcliff", threestar, idtype)
    Reindeer = items("R Corp. 4th Pack Reindeer Ishmael", "Ishmael", threestar, idtype)
    Kuro_Rodya = items("Kurokumo Henchwoman Rodion", "Rodion", threestar, idtype)
    N_Sinclair = items("The One Who Shall Grip Sinclair", "Sinclair", threestar, idtype)
    Blade_Sinclair = items("Blade Lineage Salsu Sinclair", "Sinclair", threestar, idtype)
    Seven_Outis = items("Seven Section 6 Director Outis", "Outis", threestar, idtype)
    G_regor = items("G Corp. Manager Corporal Gregor", "Gregor", threestar, idtype)
    ### Obtainable EGOs
    Rocks = items("Wishing Cairn - Yi Sang", "Yi Sang", Teth, egotype)
    # Dimensional Ripper Yi Sang here
    Dog1 = items("Telepole - Faust", "Faust", He, egotype)
    Bear = items("Hex Nail - Faust", "Faust", Teth, egotype)
    Dog2 = items("Telepole - Don Quixote", "Don Quixote", He, egotype)
    God = items("Pursuance - Meursault", "Meursault", He, egotype)
    # Dimensional Ripper Hong Lu here
    I_Am_Fiiire = items("Ardor Blossom Star - Ishmael", "Ishmael", He, egotype)
    Stew = items("Lifetime Stew - Sinclair", "Sinclair", Teth, egotype)
    Nihil = items("Ya Sunyata Tad Rupam - Outis", "Outis", Teth, egotype)
    Bad = items("Lantern - Gregor", "Gregor", Teth, egotype)
    EGO = [
        Rocks,
        Dog1,
        Bear,
        Dog2,
        God,
        I_Am_Fiiire,
        Stew,
        Nihil,
        Bad
    ]
    OOO = [
        V_50,
        Grip,
        W_Don,
        Kuro_R_S,
        Chef_R_S,
        W_Meur,
        N_Meur,
        TT_Lu,
        Rabbit,
        Reindeer,
        Kuro_Rodya,
        N_Sinclair,
        Blade_Sinclair,
        Seven_Outis,
        G_regor
    ]
    OO = [
        Seven_YiSang,
        L_Faust,
        W_Faust,
        Shi_Don,
        N_Don,
        Seven_R_S,
        Liu_Meursault,
        Kuro_Hong,
        Hong_Liu,
        Shi_Cliff,
        N_Cliff,
        Shi_Mael,
        LCCB_Mael,
        LCCB_Rodya,
        N_Rodya,
        Mexiclair,
        Zweiclair,
        Blade_Outis,
        G_Outis,
        Liu_Gregor
    ]
    O = [
        LCB_Sinner_Gregor,
        LCB_Sinner_DQte,
        LCB_Sinner_Heathcliff,
        LCB_Sinner_Hong,
        LCB_Sinner_Ishmael,
        LCB_Sinner_Knows_Everything,
        LCB_Sinner_YiSang,
        LCB_Sinner_Shinculairu,
        LCB_Sinner_Meursault,
        LCB_Sinner_R_S,
        LCB_Sinner_Outis,
        LCB_Sinner_Rodya
    ]
    # unused area for now, various information
    BPEGONumPaid = 5
    BPEGONumFree = 8
    BPEGONumSum = BPEGONumFree + BPEGONumPaid
    EventId = 1
    EventEGO = 1
    EGOTotal = EventEGO + BPEGONumSum + int(len(EGO))
    IdTotal = EventId + int(len(OOO)) + int(len(OO))
    results_str = []
    results = []

    ### now comes the actual things
    # ways to make it actually draw the class instead of .name:
    # 1.somehow get the class not in a list and then print its name - convert single item list into that item
    # 2.namedtuple or something
    # --------------------------------------
    def pullone(): # Standard extraction
        pull = random.choices([MainSim.EGO[random.randint(0, 8)], MainSim.OOO[random.randint(0, 14)], MainSim.OO[random.randint(0, 19)], MainSim.O[random.randint(0, 11)]], 
                              [1.2996, 2.8995, 12.8, 83.0004], k=1)
        drop = pull[0] # i was fucking stupid literally just take the index 0 oh my god
        MainSim.results.append(drop)
        return drop.name, drop.rarity, drop.belongsTo, drop.type # for later
    #footnote: k is the amount of variables it wants to output
    def tenth(): # 10th pull 
        pull = random.choices([MainSim.EGO[random.randint(0, 8)], MainSim.OOO[random.randint(0, 14)], MainSim.OO[random.randint(0, 19)]], 
                              [1.2996, 2.8995, 95.8009], k=1)
        drop = pull[0]
        MainSim.results.append(drop)
        return drop.name, drop.rarity, drop.belongsTo, drop.type 
    # --------------------------------------
    # testing area
    """ def test1(): # testing lists
        listhere = []
        listhere.append(random.choices([egotype, "OOO", "OO"], [1.2996, 2.8995, 95.8009], k=1))
        print(listhere)
    def test2(): # testing taking info from objects in a class
        ee = 0
        while ee < 10:
            MainSim.results_str.append(MainSim.OOO[0].name) # this is exactly how i want to do the thing 
            # nvm that wasnt, that would only take name value and I wouldn't be able to log anything else
            ee += 1
        print(MainSim.results_str)
    def try1(): # just trying out
        counterily = 10 # there is nothing wrong with this function. i fucked up the class assignment(items.name instead of self.name). FUN!!!! !  
        while counterily > 0:
            pulled = random.choices([MainSim.OO[random.randint(0, 19)].name, MainSim.O[random.randint(0, 11)].name], [12.8, 83.0004], k=1)
            MainSim.results_str.append(pulled)
            pulled = []
            counterily -= 1
        print(MainSim.results_str) """
    # using the defined functions
    def draw10(count): # perform 9 1draws, and a special draw
        while count > 0: # the number of 10 extracts to sim
            pulls = 10
            while pulls > 1:
                MainSim.pullone() # standard extraction for the first 9 times
                pulls -= 1
            MainSim.tenth() # guaranteed 2star extraction
            count -= 1
        draws = int(len(MainSim.results)) - 1
        while draws > -1:
            MainSim.results_str.append(MainSim.results[draws].name)
            draws -= 1
        random.shuffle(MainSim.results_str)
        print(MainSim.results_str) 
    def draw1(count):
        while count > 0: # the number of 10 extracts to sim
            MainSim.pullone() # standard extraction for the first 9 times
            count -= 1
        print(MainSim.results_str)
    def sorted10(count): # need to sort by value items.rarity instead of .name alphabetical - maybe return values from pullone() or tenth()?
        while count > 0: # the number of 10 extracts to sim
            pulls = 10
            while pulls > 1:
                MainSim.pullone() # standard extraction for the first 9 times
                pulls -= 1
            MainSim.tenth() # guaranteed 2star extraction
            count -= 1
        draws = int(len(MainSim.results)) - 1 # how many items were drawn 
        results1 = sorted(MainSim.results, key=lambda self: self.rarity, reverse=True)   # sort by rarity
        while draws > -1:
            MainSim.results_str.append(results1[draws].name)
            draws -= 1 
        print(MainSim.results_str)

    # changes:
    # updated tenth() to be in line with pullone() because that was directly appending into result_str and messing with sorted pulls
    # 2 lists, one for the actual items and one for their names to be outputted 
    # sort results_str by rarity
    # actual words instead of just outputting pull results_str
    # put the tenth pull somewhere random
    # draw once

# MainSim.sorted10(1) # sort by rarity
# MainSim.draw10(1) # draw 10 randomly
# MainSim.draw1(1) # draw 1 randomly

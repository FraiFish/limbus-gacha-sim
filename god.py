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
    # statistics of pulls: etc, how much of a session was EGO, 3 stars, Etc
    # statistics of % drawn of each sinner 
    # GUI which will make it more than a command to be run
    # actual words instead of just outputting pull results_str 
    # extra line when EGO/000 drops 
    # extra line when 00 drops
    # extra line for duplicates
    # EGO cannot be drawn twice in a session feature
    # if draw 0 or 00 just make it output "0" or "00"
    # interact to keep drawing instead of all at once
    # some sort of database??
    # actual luck vs calculated chance
    # draw until you have specific thing
    # draw once(implemented)
    # target extraction like banners, 000 guaranteed tickets
    # luck with respect to one specific item that you wish for
    # daily 4 pulls
    # ^ I realized that that would need numerous different banner informations other than the standard so unless that can be automated I'm not doing that
    # sort results_str 
    # put the tenth pull somewhere random(implemented)
    # code below 

    ### big list of everything in the game (probably a better way to do it)
    ### LCB sinners aka 0 stars, this is all pointless crap for flavor
    LCB_Sinner_YiSang = items("LCB Sinner Yi Sang", "Yi Sang", "0", "Trash")
    LCB_Sinner_Knows_Everything = items("LCB Sinner Faust", "Faust", "0", "Trash")
    LCB_Sinner_DQte = items("LCB Sinner Don Quixote", "Don Quixote", "0", "Trash")
    LCB_Sinner_R_S = items("LCB Sinner Ryoshu", "Ryoshu", "0", "Trash")
    LCB_Sinner_Meursault = items("LCB Sinner Meursault", "Meursault", "0", "Trash")
    LCB_Sinner_Hong = items("LCB Sinner Hong Lu", "Hong Lu", "0", "Trash")
    LCB_Sinner_Heathcliff = items("LCB Sinner Heathcliff", "Heathcliff", "0", "Trash")
    LCB_Sinner_Ishmael = items("LCB Sinner Ishmael", "Ishmael", "0", "Trash")
    LCB_Sinner_Rodya = items("LCB Sinner Rodion", "Rodion", "0", "Trash")
    LCB_Sinner_Shinculairu = items("LCB Sinner Sinclair", "Sinclair", "0", "Trash")
    LCB_Sinner_Outis = items("LCB Sinner Outis", "Outis", "0", "Trash")
    LCB_Sinner_Gregor = items("LCB Sinner Gregor", "Gregor", "0", "Trash")
    ### 2 stars, 00s
    Seven_YiSang = items("Seven Section 6 Yi Sang", "Yi Sang", "00", "Identity")
    L_Faust = items("Lobotomy Corp. Remnant Faust", "Faust", "00", "Identity")
    W_Faust = items("W Corp. Cleanup Agent Faust", "Faust", "00", "Identity")
    Shi_Don = items("Shi Section 5 Director Don Quixote", "Don Quixote", "00", "Identity")
    N_Don = items("N Corp. Mittelhammer Don Quixote", "Don Quixote", "00", "Identity")
    Seven_R_S = items("Seven Section 6 Ryoshu", "Ryoshu", "00", "Identity")
    Liu_Meursault = items("Liu Section 6 Meursault", "Meursault", "00", "Identity")
    Kuro_Hong = items("Kurokumo Wakashu Hong Lu", "Hong Lu", "00", "Identity")
    Hong_Liu = items("Liu section 5 Hong Lu", "Hong Lu", "00", "Identity")
    Shi_Cliff = items("Shi Section 5 Heathcliff", "Heathcliff", "00", "Identity")
    N_Cliff = items("N Corp. Kleinhammer Heathcliff", "Heathcliff", "00", "Identity")
    Shi_Mael = items("Shi Section 5 Ishmael", "Ishmael", "00", "Identity")
    LCCB_Mael = items("LCCB Assistant Manager Ishmael", "Ishmael", "00", "Identity")
    LCCB_Rodya = items("LCCB Assistant Manager Rodion", "Rodion", "00", "Identity")
    N_Rodya = items("N Corp. Mittelhammer Rodion", "Rodion", "00", "Identity")
    Mexiclair = items("Jefe de los Marachis Sinclair", "Sinclair", "00", "Identity")
    Zweiclair = items("Zwei Section 6 Sinclair", "Sinclair", "00", "Identity")
    Blade_Outis = items("Blade Lineage Cutthroat Outis", "Outis", "00", "Identity")
    G_Outis = items("G Corp. Head Manager Outis", "Outis", "00", "Identity")
    Liu_Gregor = items("Liu Section 6 Gregor", "Gregor", "00", "Identity")
    ### 3 stars, 000s
    V_50 = items("Blade Lineage Salsu Yi Sang", "Yi Sang", "000", "Identity")
    Grip = items("The One Who Grips Faust", "Faust", "000", "Identity")
    W_Don = items("W Corp. Cleanup Agent Don Quixote", "Don Quixote", "000", "Identity")
    Kuro_R_S = items("Kurokumo Wakashu Ryoshu", "Ryoshu", "000", "Identity")
    Chef_R_S = items("R.B Chef de Cuisine Ryoshu", "Ryoshu", "000", "Identity")
    W_Meur = items("W Corp. Cleanup Agent Meursault", "Meursault", "000", "Identity")
    N_Meur = items("N Corp. Großhammer Meursault", "Meursault", "000", "Identity")
    TT_Lu = items("Tingtang Gangleader Hong Lu", "Hong Lu", "000", "Identity")
    Rabbit = items("R Corp. 4th Pack Rabbit Heathcliff", "Heathcliff", "000", "Identity")
    Reindeer = items("R Corp. 4th Pack Reindeer Ishmael", "Ishmael", "000", "Identity")
    Kuro_Rodya = items("Kurokumo Henchwoman Rodion", "Rodion", "000", "Identity")
    N_Sinclair = items("The One Who Shall Grip Sinclair", "Sinclair", "000", "Identity")
    Blade_Sinclair = items("Blade Lineage Salsu Sinclair", "Sinclair", "000", "Identity")
    Seven_Outis = items("Seven Section 6 Director Outis", "Outis", "000", "Identity")
    G_regor = items("G Corp. Manager Corporal Gregor", "Gregor", "000", "Identity")
    ### Obtainable EGOs
    Rocks = items("Wishing Cairn - Yi Sang", "Yi Sang", "TETH", "EGO")
    # Dimensional Ripper Yi Sang here
    Dog1 = items("Telepole - Faust", "Faust", "HE", "EGO")
    Bear = items("Hex Nail - Faust", "Faust", "TETH", "EGO")
    Dog2 = items("Telepole - Don Quixote", "Don Quixote", "HE", "EGO")
    God = items("Pursuance - Meursault", "Meursault", "HE", "EGO")
    # Dimensional Ripper Hong Lu here
    I_Am_Fiiire = items("Ardor Blossom Star - Ishmael", "Ishmael", "HE", "EGO")
    Stew = items("Lifetime Stew - Sinclair", "Sinclair", "TETH", "EGO")
    Nihil = items("Ya Sunyata Tad Rupam - Outis", "Outis", "TETH", "EGO")
    Bad = items("Lantern - Gregor", "Gregor", "TETH", "EGO")
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
    def pullone(): # Standard extraction
        pull = random.choices([MainSim.EGO[random.randint(0, 8)], MainSim.OOO[random.randint(0, 14)], MainSim.OO[random.randint(0, 19)], MainSim.O[random.randint(0, 11)]], [1.2996, 2.8995, 12.8, 83.0004], k=1)
        drop = pull[0] # i was fucking stupid literally just take the index 0 oh my god
        MainSim.results_str.append(drop.name)
    #footnote: k is the amount of variables it wants to output
    def tenth(): # 10th pull 
        pull = random.choices([MainSim.EGO[random.randint(0, 8)], MainSim.OOO[random.randint(0, 14)], MainSim.OO[random.randint(0, 19)]], [1.2996, 2.8995, 95.8009], k=1)
        drop = pull[0]
        MainSim.results_str.append(drop.name)
    # testing area
    def test1(): # testing lists
        listhere = []
        listhere.append(random.choices(["EGO", "OOO", "OO"], [1.2996, 2.8995, 95.8009], k=1))
        print(listhere)
    def test2(): # testing taking info from objects in a class
        ee = 0
        while ee < 10:
            MainSim.results_str.append(MainSim.OOO[0].name) # this is exactly how i want to do the thing 
            # nvm that wasnt, that would only take name value and I wouldn't be able to log anything else
            ee += 1
        print(MainSim.results_str)
    def try1(): # just trying out
        counterily = 10 # there is nothing wrong with this function. i fucked up the class assignment. FUN!!!! !   aaa
        while counterily > 0:
            pulled = random.choices([MainSim.OO[random.randint(0, 19)].name, MainSim.O[random.randint(0, 11)].name], [12.8, 83.0004], k=1)
            MainSim.results_str.append(pulled)
            pulled = []
            counterily -= 1
        print(MainSim.results_str)
    # using the defined functions
    def draw10(count): # perform 9 1draws, and a special draw
        while count > 0: # the number of 10 extracts to sim
            pulls = 10
            while pulls > 1:
                MainSim.pullone() # standard extraction for the first 9 times
                pulls -= 1
            MainSim.tenth() # guaranteed 2star extraction
            count -= 1
        random.shuffle(MainSim.results_str)
        print(MainSim.results_str) 
    def draw1(count):
        while count > 0: # the number of 10 extracts to sim
            MainSim.pullone() # standard extraction for the first 9 times
            count -= 1
        print(MainSim.results_str)
    def sorted10(count):
        while count > 0: # the number of 10 extracts to sim
            pulls = 10
            while pulls > 1:
                MainSim.pullone() # standard extraction for the first 9 times
                pulls -= 1
            MainSim.tenth() # guaranteed 2star extraction
            count -= 1
        random.shuffle(MainSim.results_str)
        print(MainSim.results_str)
    

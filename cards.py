import random

SUITS = 'schd'
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
CHIPS = 500
TURN  = True

def takeCards(num):
    x = random.sample(deck, num)
    for i in x:
        deck.remove(i)
    return x

def takeChips(user, amount):
    return (user.chips - amount)

def tableStatus():
    print "\n\nThe current pot size is: ", table.chips
    print "\nYour chip count     : ", ME.chips
    print "The AI's chip count : ", AI.chips
    print "\nYour cards:   ",
    for i in ME.cards:
        print i.rep,
    if (table.cards != ""):
        print "\n\nTable cards:  ",
        for i in table.cards:
            print i.rep,

class card(object):
    def __init__(self, value, suit):
        self.rank = RANKS[value]
        self.suit = suit
        self.value = value+2 if value < 9 else 10+(value == 12) # such a hack
        self.rep = self.rank+suit # assuming both text

class user(object):
    def __init__(self, chips):
        self.chips = chips
        self.cards = takeCards(2)

class pot(object):
    def __init__(self, lb, bb, dealer):
        self.lb = lb
        self.bb = bb
        self.dealer = dealer
        self.chips = 0
        self.cards = ""


#create deck
deck = [card(x, y) for x in range(13) for y in SUITS]

#create user chips and cards
ME = user(CHIPS)

#create computer chips and cards
AI = user(CHIPS)

#init table blinds and dealer
table = pot(25, 50, AI)

#main loop
while(ME.chips >= 0 and AI.chips >= 0):
    table.chips += table.lb +table.bb

    if (ME == table.dealer):
        ME.chips -= table.bb
        AI.chips -= table.lb
    else:
        ME.chips -= table.lb
        AI.chips -= table.bb

    if (table.dealer == AI):
        print "\nYou are the LITTLE BLIND"
    else:
        print "\nYou are the DEALER and BIG BLIND"

    tableStatus()

    if (table.dealer == AI):
        while(TURN == True):
            bet = raw_input("\nWould you like to call the blind (C), raise (R), or fold (F)?: ")
            if (bet == 'C'):
                print "You called"
                ME.chips -= table.lb
                TURN = False
            elif (bet == 'R'):
                cond = True
                while(cond == True):
                    newbet = raw_input('What would you like to raise?: ')
                    try:
                        test = int(newbet)
                    except ValueError:
                        print "That's not a number!"
                        break
                    if (newbet <= table.lb):
                        print "Please bet at least the little blind"
                    else:
                        print "You raised", newbet
                        ME.chips -= int(newbet)
                        add = (table.lb + int(newbet) - table.bb)
                        AI.chips -= add
                        print "The AI calls you raise of ", add
                        cond = False
                        TURN = False
            elif (bet == 'F'):
                print "You fold."
                TURN = False
                break
            else:
                print "Please enter a valid response"

    elif (table.dealer == ME):
        print "\nYou are the dealer"
        deal = raw_input("pls fix")

    flop = takeCards(3)
    table.cards = flop

    tableStatus()

    if (table.dealer == AI):
        while (TURN == False):
            flopDec = raw_input("\n\nWould you like to bet (B) or check (C): ")
            if (flopDec == 'B'):
                condf = True
                while(condf == True):
                    flopBet = raw_input("What would you like to bet?: ")
                    try:
                        flopTest = int(flopBet)
                    except ValueError:
                        print "That's not a number!"
                        break
                    if (flopBet <= table.lb):
                        print "Please bet at least the little blind"
                    else:
                        print "You raised", flopBet
                        ME.chips -= int(flopBet)
                        AI.chips -= int(flopBet)
                        print "The AI calls you raise of ", flopBet
                        condf = False
                        TURN = True
            elif (flopDec == 'C'):
                print "You Check"
                print "The AI also checks"
                TURN = True
            else:
                print "Please enter a valid response"

    turnC = takeCards(1)
    table.cards = flop + turnC

    tableStatus()

    if (table.dealer == AI):
        while (TURN == True):
            turnDec = raw_input("\n\nWould you like to bet (B) or check (C): ")
            if (turnDec == 'B'):
                condt = True
                while(condf == True):
                    turnBet = raw_input("What would you like to bet?: ")
                    try:
                        turnTest = int(turnBet)
                    except ValueError:
                        print "That's not a number!"
                        break
                    if (turnBet <= table.lb):
                        print "Please bet at least the little blind"
                    else:
                        print "You raised", turnBet
                        ME.chips -= int(turnBet)
                        AI.chips -= int(turnBet)
                        print "The AI calls you raise of ", turnBet
                        condt = False
                        TURN = False
            elif (turnDec == 'C'):
                print "You Check"
                print "The AI also checks"
                TURN = False
            else:
                print "Please enter a valid response"

    riverC = takeCards(1)
    table.cards = flop + turnC + riverC

    tableStatus()

    if (table.dealer == AI):
        while (TURN == False):
            riverDec = raw_input("\n\nWould you like to bet (B) or check (C): ")
            if (riverDec == 'B'):
                condr = True
                while(condr == True):
                    riverBet = raw_input("What would you like to bet?: ")
                    try:
                        riverTest = int(riverBet)
                    except ValueError:
                        print "That's not a number!"
                        break
                    if (riverBet <= table.lb):
                        print "Please bet at least the little blind"
                    else:
                        print "You raised", riverBet
                        ME.chips -= int(riverBet)
                        AI.chips -= int(riverBet)
                        print "The AI calls you raise of ", riverBet
                        condr = False
                        TURN = True
            elif (turnDec == 'C'):
                print "You Check"
                print "The AI also checks"
                TURN = True
            else:
                print "Please enter a valid response"

    print "\nThe AI had :",
    for i in AI.cards:
        print i.rep,

    replay = raw_input("\n\nWould you like to play again? (Y/N)")
    if (table.dealer == AI):
        table.dealer = ME
    else:
        table.dealer = AI

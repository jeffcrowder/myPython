import random
from PrintColors import PrintColors

class GameBoard:
    c = PrintColors()

    guessList = [ \
            ['O','O','O','O'],['O','O','O','O'], \
            ['O','O','O','O'],['O','O','O','O'], \
            ['O','O','O','O'],['O','O','O','O'], \
            ['O','O','O','O'],['O','O','O','O'], \
            ['O','O','O','O'],['O','O','O','O']]

    clueList = [ \
            ['*','*','*','*'],['*','*','*','*'], \
            ['*','*','*','*'],['*','*','*','*'], \
            ['*','*','*','*'],['*','*','*','*'], \
            ['*','*','*','*'],['*','*','*','*'], \
            ['*','*','*','*'],['*','*','*','*']]

    colorList = [ \
            [c.CBLACK,c.CBLACK,c.CBLACK,c.CBLACK ],[c.CBLACK,c.CBLACK,c.CBLACK,c.CBLACK ], \
            [c.CBLACK,c.CBLACK,c.CBLACK,c.CBLACK ],[c.CBLACK,c.CBLACK,c.CBLACK,c.CBLACK ], \
            [c.CBLACK,c.CBLACK,c.CBLACK,c.CBLACK ],[c.CBLACK,c.CBLACK,c.CBLACK,c.CBLACK ], \
            [c.CBLACK,c.CBLACK,c.CBLACK,c.CBLACK ],[c.CBLACK,c.CBLACK,c.CBLACK,c.CBLACK ], \
            [c.CBLACK,c.CBLACK,c.CBLACK,c.CBLACK ],[c.CBLACK,c.CBLACK,c.CBLACK,c.CBLACK ]]
    
    clueColorList = [\
            [c.CBLACK,c.CBLACK,c.CBLACK,c.CBLACK ],[c.CBLACK,c.CBLACK,c.CBLACK,c.CBLACK ], \
            [c.CBLACK,c.CBLACK,c.CBLACK,c.CBLACK ],[c.CBLACK,c.CBLACK,c.CBLACK,c.CBLACK ], \
            [c.CBLACK,c.CBLACK,c.CBLACK,c.CBLACK ],[c.CBLACK,c.CBLACK,c.CBLACK,c.CBLACK ], \
            [c.CBLACK,c.CBLACK,c.CBLACK,c.CBLACK ],[c.CBLACK,c.CBLACK,c.CBLACK,c.CBLACK ], \
            [c.CBLACK,c.CBLACK,c.CBLACK,c.CBLACK ],[c.CBLACK,c.CBLACK,c.CBLACK,c.CBLACK ]]

    thisGuess = [c.CBLACK,c.CBLACK,c.CBLACK,c.CBLACK]
    thisClue = [c.CBLACK,c.CBLACK,c.CBLACK,c.CBLACK]

    winFlag = False
    
    answer = [c.CBLACK,c.CBLACK,c.CBLACK,c.CBLACK]
    CBLACKBG = c.CBLACKBG
    ENDC = c.ENDC

    numRows = 10
    guessCount = 10
    
    def build_secret_code(self):
        #print "this is where I will build the secret code"
        possibleColors = [ self.c.CWHITE,  self.c.CGREEN, self.c.CRED, \
                           self.c.CYELLOW, self.c.CBLUE , self.c.CCYAN ]
        self.answer = random.sample(possibleColors, 4)


    def update_guess(self, colors):
        self.thisGuess = colors
        self.guessCount -= 1
        for i in range(4):
            self.colorList[self.guessCount][i] = colors[i]
    
    def update_clueColorList(self,numColors,numLocations):
        # add the white pegs
        for i in range(numColors):
            self.clueColorList[self.guessCount][i] = self.c.CWHITE
        # now change to green
        for i in range(numLocations):
            self.clueColorList[self.guessCount][i] = self.c.CGREEN
        
    def user_guess(self):
        print ""
        print "---------------------------------------------------------------------"
        print "Enter your guess for the four colors and position of the secret code."
        print "Please choose four of the six following colors: " 
        print self.c.CWHITE  + "   w =white" + self.c.CRED + "   r =red"  
        print self.c.CGREEN  + "   g =green" + self.c.CYELLOW + "   y =yellow" 
        print self.c.CBLUE   + "   b =blue " + self.c.CCYAN + "   c =cyan" + self.c.ENDC 
        print "---------------------------------------------------------------------\n"
        
        guess = [self.c.CBLACK,self.c.CBLACK,self.c.CBLACK,self.c.CBLACK] 
        x = 0
        while x <= 3:
            try:
                ui = raw_input()
            except ValueError:
                print("sorry, I didn't understand that.")
                continue

            if ui == 'w':
                guess[x] = self.c.CWHITE
                print("Location #%s choice was white" % (str(x+1)))
                x += 1
            elif ui == 'r':
                guess[x] = self.c.CRED
                print("Location #%s choice was red" % (str(x+1)))
                x += 1
            elif ui == 'g':
                guess[x] = self.c.CGREEN
                print("Location #%s choice was green" % (str(x+1)))
                x += 1
            elif ui == 'y':
                guess[x] = self.c.CYELLOW
                print("Location #%s choice was yellow" % (str(x+1)))
                x += 1
            elif ui == 'b':
                guess[x] = self.c.CBLUE
                print("Location #%s choice was blue" % (str(x+1)))
                x += 1
            elif ui == 'c':
                guess[x] = self.c.CCYAN
                print("Location #%s choice was cyan" % (str(x+1)))
                x += 1
            else:
                print("you didnt pick a valid color!")
        #self.check_guess(guess)
        return guess
    
    def check_guess(self,guess):
        a = self.answer
        g = guess
        # this lets me know how many white pegs
        color_count = len(list(set(a).intersection(g)))
        # This lets me know ho many green pegs 
        location_count = 0
        for i,j in zip(a,g):
            if i==j:
                location_count += 1
                print("location count")
                print(location_count)
        # set the win flag 
        if location_count == 4:
            self.winFlag = True

        self.update_clueColorList(color_count, location_count)
        print ""
        
    def print_board(self):
        print "---MASTERMIND---"
        print "| X X X X |    |"
        print "|---------|----|"
        for i in range(self.numRows):
            #build the guess string 
            gstr0 = ''.join([self.colorList[i][0], self.guessList[i][0]])
            gstr1 = ''.join([self.colorList[i][1], self.guessList[i][1]])
            gstr2 = ''.join([self.colorList[i][2], self.guessList[i][2]])
            gstr3 = ''.join([self.colorList[i][3], self.guessList[i][3], self.c.ENDC])
            
            #build the clue string
            cstr0 = ''.join([self.clueColorList[i][0], self.clueList[i][0]])
            cstr1 = ''.join([self.clueColorList[i][1], self.clueList[i][1]])
            cstr2 = ''.join([self.clueColorList[i][2], self.clueList[i][2]])
            cstr3 = ''.join([self.clueColorList[i][3], self.clueList[i][3], self.c.ENDC])
            
            guessString = self.c.CBLACKBG + "| %s %s %s %s |" % (gstr0,gstr1,gstr2,gstr3) \
                + self.c.CBLACKBG + "%s%s%s%s|" % (cstr0,cstr1,cstr2,cstr3) 
            print( guessString)
        print "----------------\n"

gb = GameBoard()

print( chr(27) + "[2J" )
gb.build_secret_code()

try:
    gameCounter = 0
    while not gb.winFlag: 
        if gameCounter == 10:
            print(" You lost. Used all %s moves.\n\n" % gameCounter)
            break
        guess = gb.user_guess()
        gb.update_guess(guess)
        gb.check_guess(guess)
        gb.print_board()
        gameCounter += 1

    print(" You won in %s moves!\n\n" % gameCounter)

except KeyboardInterrupt:
    print "Ending the Game\n\n"


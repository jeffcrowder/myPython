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
    
    thisGuess = [c.CBLACK,c.CBLACK,c.CBLACK,c.CBLACK]
    CBLACKBG = c.CBLACKBG
    ENDC = c.ENDC

    numRows = 10
    guessCount = 10

    def latest_guess(self, colors):
        self.thisGuess = colors
        self.guessCount -= 1
        self.update_colorList(colors,self.guessCount)
        #print(self.guessCount)
    
    def update_colorList(self,colors,cnt):
        for i in range(4):
            self.colorList[cnt][i] = colors[i]
            #print(str(self.colorList[cnt][i]))

    def user_guess(self):
        print "---------------------------------------------------------------------"
        print ""
        print ""
        print "Enter your guess for the four colors and position of the secret code."
        print "Please choose four of the six following colors: " 
        print self.c.CWHITE  + "   w =white" 
        print self.c.CRED    + "   r =red " 
        print self.c.CGREEN  + "   g =green " 
        print self.c.CYELLOW + "   y =yellow "
        print self.c.CBLUE   + "   b =blue " 
        print self.c.CCYAN   + "   c =cyan " + self.c.ENDC
        print "---------------------------------------------------------------------"
        
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
        return guess

    def print_board(self):
        for i in range(self.numRows):
            #c = PrintColor()
            #build the guess string 
            gstr0 = ''.join([self.colorList[i][0], self.guessList[i][0]])
            gstr1 = ''.join([self.colorList[i][1], self.guessList[i][1]])
            gstr2 = ''.join([self.colorList[i][2], self.guessList[i][2]])
            gstr3 = ''.join([self.colorList[i][3], self.guessList[i][3], pc.ENDC])
            
            #build the clue string
            #currently this is hard coded it needs to come from server
            clueColor0 = self.c.CWHITE
            clueColor1 = self.c.CGREEN
            clueColor2 = self.c.CBLACK
            clueColor3 = self.c.CBLACK
            
            cstr0 = ''.join([clueColor0, self.clueList[i][0]])
            cstr1 = ''.join([clueColor1, self.clueList[i][1]])
            cstr2 = ''.join([clueColor2, self.clueList[i][2]])
            cstr3 = ''.join([clueColor3, self.clueList[i][3], pc.ENDC])
            
            guessString = self.c.CBLACKBG + "| %s %s %s %s |" % (gstr0,gstr1,gstr2,gstr3) \
                + self.c.CBLACKBG + "%s%s%s%s|" % (cstr0,cstr1,cstr2,cstr3) 
            print( guessString)

gb = GameBoard()

pc = gb.c #PrintColor()

print( chr(27) + "[2J" )
print" test "

gameCounter = 0
while gameCounter < 10:
    guess = gb.user_guess()
    gb.latest_guess(guess)
    gb.print_board()
    gameCounter += 1





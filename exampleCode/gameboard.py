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

print" test "
# Get the guess colors from the command line 
guessColor0 = pc.CVIOLET
guessColor1 = pc.CBLUE
guessColor2 = pc.CRED
guessColor3 = pc.CYELLOW
guess = [guessColor0, guessColor1, guessColor2, guessColor3]
         
gb.latest_guess(guess)

gb.print_board()

print('Next guess: ')

guessColor0 = pc.CRED
guessColor1 = pc.CVIOLET
guessColor2 = pc.CYELLOW
guessColor3 = pc.CWHITE
guess = [guessColor0, guessColor1, guessColor2, guessColor3]

gb.latest_guess(guess)
gb.print_board()

print('Next guess: ')

guessColor0 = pc.CYELLOW
guessColor1 = pc.CVIOLET
guessColor2 = pc.CCYAN
guessColor3 = pc.CRED
guess = [guessColor0, guessColor1, guessColor2, guessColor3]

gb.latest_guess(guess)
gb.print_board()


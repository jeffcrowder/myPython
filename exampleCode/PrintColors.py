import time

class PrintColors:
    ENDC      = '\33[0m'
    CBOLD     = '\33[1m'
    CITALIC   = '\33[3m' # does not work
    CURL      = '\33[4m'
    CBLINK    = '\33[5m' # does not work
    CBLINK2   = '\33[6m' # does not work
    CSELECTED = '\33[7m'

    CBLACK  = '\33[30m'
    CRED    = '\33[31m'
    CGREEN  = '\33[32m'
    CYELLOW = '\33[33m'
    CBLUE   = '\33[34m'
    CVIOLET = '\33[35m'
    CCYAN   = '\33[36m'
    CWHITE  = '\33[37m'

    CBLACKBG  = '\33[40m'
    CREDBG    = '\33[41m'
    CGREENBG  = '\33[42m'
    CYELLOWBG = '\33[43m'
    CBLUEBG   = '\33[44m'
    CVIOLETBG = '\33[45m'
    CCYANBG   = '\33[46m'
    CWHITEBG  = '\33[47m'

    CGREY    = '\33[90m'
    CRED2    = '\33[91m'
    CGREEN2  = '\33[92m'
    CYELLOW2 = '\33[93m'
    CBLUE2   = '\33[94m'
    CVIOLET2 = '\33[95m'
    CCYAN2   = '\33[96m'
    CWHITE2  = '\33[97m'

    CGREYBG    = '\33[100m'
    CREDBG2    = '\33[101m'
    CGREENBG2  = '\33[102m'
    CYELLOWBG2 = '\33[103m'
    CBLUEBG2   = '\33[104m'
    CVIOLETBG2 = '\33[105m'
    CCYANBG2   = '\33[106m'
    CWHITEBG2  = '\33[107m'

    def print_format_table(self):
        """
        prints table of formated text over format option
        """
        workingStyles  = [1,3,7]
        for style in workingStyles:
            for fg in range(30,38):
                s1 = ''
                for bg in range(40,48):
                    format = ';'.join([str(style), str(fg), str(bg)])
                    #s1 += '\x1b[%sm %s \x1b[0m' % (format, format)
                    s1 += '\33[%sm %s \33[0m' % (format, format)
                print(s1)
            print('\n')


    def print_examples(self):
        """
        here are a couple print examples as reminders
        """
        print self.CBOLD + "BOLD: adasdfasd" + self.ENDC
        print self.CURL + "UNDERLINE: adasdfasd" + self.ENDC
        print self.CRED + self.CBEIGEBG2 + self.CURL + "CRED: "  + self.CGREEN + self.CREDBG + "sfassd" + self.ENDC

    def clear_screen(self):
        """
        here is the escape sequence to clear the terminal screen
        """
        print(chr(27) + "[2J")


if __name__ ==  "__main__":
    pc = PrintColors()
    pc.print_examples()
    time.sleep(3)
    pc.clear_screen()
    pc.print_format_table()
    time.sleep(3)


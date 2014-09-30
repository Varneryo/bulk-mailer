import smtplib
import sys
import os.path
from email import message
class Mailer():
    """
    Commandline bulk mailer utility.
    """
    def __init__(self,user_path,csv_path,msg_path,subject):
        self.user_path = user_path
        self.csv_path = csv_path
        self.msg_path = msg_path
        self.subject = subject
        self.name, self.username, self.password, self.SMTP_server = self._parse_user()

    def _parse_user(self):
        user_data = []
        with open(self.user_path,'r') as f_user:
            for line in f_user:
                line = line.rstrip('\n')
                user_data = line.split(',')
        return user_data

    def _parse_csv(self):
        recipients = []
        with open(self.csv_path,'r') as f_csv:
            for line in f_csv:
                line = line.rstrip('\n')
                line = line.split(',')
                recipients.append(line)
        return recipients

    def _parse_msg(self):
        message = []
        with open(self.msg_path,'r') as f_m:
            for line in f_m:
                message.append(line)
        return message

    def _assemble_email(self,recipient_pair,text):
        recipient = "%s <%s>" % (recipient_pair[0],recipient_pair[1])
        sender = "%s <%s>" % (self.name,self.username)

        email_message = message.Message()
        email_message.add_header('From',sender)
        email_message.add_header('To',recipient)
        email_message.add_header('Subject',self.subject)
        email_message.set_payload(recipient_pair[0]+":\n\n"+"".join(text))
        return email_message.as_string()
        
        
    def send(self,retry_count=0):
        server = smtplib.SMTP(self.SMTP_server,587) # use secure
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(self.username,self.password)
        print "SMPT Login Sucessful. Begining transmission."
        
        recipients = self._parse_csv()
        message = self._parse_msg()
        
        for recipient in recipients:
            server.sendmail(self.username,recipient,self._assemble_email(recipient,message))
            print "Message sent to %s via %s" % (recipient[0],recipient[1])
        print "Transmissions complete. Closing SMPT server."
        server.close()
        
if __name__ == "__main__":
    if (len(sys.argv) == 5):
        ,user_path,csv_path,msg_path,subject = sys.argv
    else:
        print "Usage: python mailer.py <user.csv> <recipients.csv> <message.txt> <subject.txt>"
        sys.exit()

    mailer = Mailer(user_path,csv_path,msg_path,subject)
    mailer.send()

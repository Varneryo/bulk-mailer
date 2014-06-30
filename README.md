bulk-mailer
===========

bulk mailer in python

The mailer requires 3 files to run.

user.csv - a user info file containing a single line sender information. Format is as follows:
<Full Name>,<SMTP email username>,<SMTP password>,<SMTP Server>
example user.csv:
Daniel Booth,daniel@exampledomain.com,password,mail,exampledomain.com

emails.csv - a csv file containing all the recipients for your email. Format is as follows:
<Recipient Full Name>,<Recipient email address>

example emails.csv:
John Doe, jdoe@gmail.com
Jane Doe, jdoe2@gmail.com

message.txt - plain text message to be sent out to all recipients. The recipient's full name is automatically appended to the begining of each message.
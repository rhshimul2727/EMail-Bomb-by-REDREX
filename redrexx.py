import smtplib
server = smtplib.SMTP("smtp.gmail.com",587)
server.starttls()
server.login("gabiroy560@gmail.com","701702703")
for i in range(5000):
    server.sendmail("choda@gmail.com","doubleaech3@gmail.com","You have been crash in 10 second")
    print 'massage has been send'
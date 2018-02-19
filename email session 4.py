import smtplib
s = smtplib.SMTP("smtp.gmail.com",587)
s.starttls()
s.login("paramjeetsingh070@gmail.com","paramyuvi")
message = ("how you doin?")
s.sendmail("paramjeetsingh070@gmail.com","manasa17300@gmail.com",message)
s.quit()

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

fro_add="aniketindian8@gmail.com"
to_add="sumanabasu2001@gmail.com"

message=MIMEMultipart()
message['From']=fro_add
message['To']=",".join(to_add)
message['subject']="Testinf mail"

body='Hai this is dilip ,How are you'

message.attach(MIMEText(body,'plain'))

email=" "
password=" "

mail=smtplib.SMTP('smtp.gmail.com',587)
mail.ehlo()
mail.starttls()
mail.login(email,password)
text=message.as_string()
mail.sendmail(fro_add,to_add,text)
mail.quit()
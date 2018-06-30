import smtplib

mail_obj = smtplib.SMTP('smtp.gmail.com',587)

content = 'Hello This is test mail'
mail_obj.ehlo()
mail_obj.starttls()
mail_obj.login('praneethalaghari@gmail.com', 'kelish1234')
mail_obj.sendmail('cool','praneethalaghari@gmail.com',content)

mail_obj.close()
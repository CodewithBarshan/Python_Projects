import smtplib as sl
ob=sl.SMTP('smtp.gmail.com',587) #port no -587
ob.ehlo() #greets the server to connect
ob.starttls()
ob.login("barshanmukherjee033@gmail.com",'Barshan1234@')
subject="Test Python"
body="I love Python"
message="subject:{}\n\n{}".format(subject,body)
listadd=["prajapatgaurav08@gmail.com","aurodutta001@gmail.com"]
ob.sendmail("barshanmukherjee022@gmail.com",listadd,message)
print("mail sent successfully")
ob.quit()  #will quit the server 
import datetime as dt
import random
import smtplib

sender_address = 'yourmail@gmail.com'
password = 'yourpassword'

with open('quotes.txt', 'r') as file:
    data = file.read()
    into_list = data.split("\n")

quote = random.choice(into_list)

now = dt.datetime.now()
day_of_week = now.weekday()

if day_of_week == 1:

    with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
        connection.starttls()
        connection.login(user=sender_address, password=password)
        connection.sendmail(from_addr=sender_address, to_addrs='bhargavdas77@hotmail.com',
                            msg=f"Subject:'Quote of the day'\n\n{quote}")

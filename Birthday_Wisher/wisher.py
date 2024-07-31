from datetime import datetime
import smtplib
import random
import pandas as pd


SENDER_EMAIL = 'yourmail@email.com'
PASSWORD = 'yourpassword'

today = (datetime.now().month, datetime.now().day)

data = pd.read_csv('birthdays.csv')
data_dict = {(data_row['month'], data_row['day']): data_row for (index, data_row) in data.iterrows() }

if today in data_dict:
    birthday_person = data_dict[today]
    file = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"]) ## common mistake to avoid. Save in a variable to actually replace.
    with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
        connection.starttls()
        connection.login(user=SENDER_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=SENDER_EMAIL, to_addrs=birthday_person["email"],msg=f"Subject:Happy Birthday!\n\n{contents}")

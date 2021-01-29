import os
import smtplib

from email.message import EmailMessage

# add into enironmental variables of the respective systems
EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')


msg = EmailMessage()
msg['Subject'] = "csv file working?"
msg['From'] = EMAIL_ADDRESS
msg['To'] = 'facerecognition2021@gmail.com'
msg.set_content('phase-1 working properly or not')

# adding file in al list in order to access the file

Files = ['switch_games.csv']

for file in Files:
    with open(file, 'rb') as f:
        file_data = f.read()
        file_name = f.name

        msg.add_attachment(file_data, maintype='application',
                           subtype='octet-stream', filename=file_name)


with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    smtp.send_message(msg)
    print("succesfull message sent to the respective email")

import os
import smtplib

from email.message import EmailMessage

# add into enironmental variables of the respective systems
EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')


new_msg = EmailMessage()
new_msg['Subject'] = "csv file working?"
new_msg['From'] = EMAIL_ADDRESS
new_msg['To'] = 'facerecognition2021@gmail.com'
new_msg.set_content('phase-1 working properly or not')

# adding file in al list in order to access the file

Files = ['switch_games.csv']

for file in Files:
    with open(file, 'rb') as f:
        file_data = f.read()
        file_name = f.name

        new_msg.add_attachment(file_data, maintype='application',
                               subtype='octet-stream', filename=file_name)


with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    smtp.send_message(new_msg)
    print("succesfull message sent to the respective email")

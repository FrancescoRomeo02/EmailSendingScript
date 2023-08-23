import os
from os import walk
from getpass import getpass
import smtplib
from email.message import EmailMessage

# Search for data file #
pre_decision = 0
for root, dirs, files in os.walk(os.getcwd()):
    for file in files:
        if file.endswith("dati_predefiniti.txt"):
            file_path = (os.path.join(root, file))
            pre_decision = 1

# Start
dato = input('Use predefined data (y/n)? ').strip().lower()  # Clean and convert to lowercase

temp_data = []
data = {
    "mail": "",
    "password": "",
    "to": "",
    "path": ""
}

# Check user's choice
if dato == 'y' and pre_decision != 0:
    decision = 1
elif pre_decision == 0:
    print('The predefined file was deleted.\nEnter data manually and I will create it for you.')
    decision = 0
elif dato == 'n':
    decision = 0
else:
    os.system("python mail.py")

if decision:
    # Use predefined data #
    with open(file_path, "r") as d:
        temp_data = [line.strip() for line in d]

    data['mail'] = temp_data[0]
    data['password'] = temp_data[1]
    data["to"] = temp_data[2]
    data['path'] = temp_data[3]

    address = data['mail']
    password = data['password']
    to = data['to']
    path_file = data['path']

    msg = EmailMessage()
    msg['Subject'] = 'Romeo Francesco'
    msg['From'] = address
    msg['To'] = to
    msg.set_content('')

else:
    # Enter new data #
    print('To use a profile different from the default one, enable access to less secure apps:\nhttps://myaccount.google.com/u/1/lesssecureapps\n\nIf your profile has two-step verification, use the app password:\nhttps://myaccount.google.com/u/0/apppasswords?rapt=AEjHL4OHEKXhuBJJEiQLV-7kiULeXp3dME-JnZOp14JqJzohdhQOOlExWvg0eZ5ju5UjZr6VIZIOSDBloiGQgEVcu4f1WryX2w')

    address = input('Sender email: ')
    temp_data.append(address)

    password = getpass('Sender password: ')
    temp_data.append(password)

    to = input('Recipient email: ')
    temp_data.append(to)

    path_file = input('Folder path for files: ')
    temp_data.append(path_file)

    with open("dati_predefiniti.txt", "w") as txt_file:
        for line in temp_data:
            txt_file.write(line + "\n")

    msg = EmailMessage()
    msg['Subject'] = input('Subject: ')
    msg['From'] = address
    msg['To'] = to
    msg.set_content(input('Message: '))

files = []
for (dirpath, dirnames, filenames) in walk(path_file):
    files.extend(filenames)
    break

for file in files:
    with open(os.path.join(path_file, file), 'rb') as f:
        file_data = f.read()
        file_name = f.name

    msg.add_attachment(file_data, maintype='application',
                       subtype='octet-stream', filename=file_name)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(address, password)
    smtp.send_message(msg)
    input("Email sent successfully. Press Enter to exit.")

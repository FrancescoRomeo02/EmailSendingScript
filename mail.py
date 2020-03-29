import os
from os import walk
from getpass import getpass
import smtplib
from email.message import EmailMessage


# ricerca file dati #
pre_decision = 0
for root, dirs, files in os.walk(os.getcwd()):
    for file in files:
        if file.endswith("dati_predefiniti.txt"):
            file_path = (os.path.join(root, file))
            pre_decision = 1

# start
dato = input('usare i dati predefiniti(s/n)? ')
dato.upper().lower()

temp_date = []
data = {
    "mail": "",
    "password": "",
    "to": "",
    "path": ""
}

# controllo scelta
if(dato == 's'and pre_decision != 0):
    decision = 1
elif(pre_decision == 0):
    print('il file predefinito è stato cancellato.\n inserisci i dati manulamnete e lo creerò per te')
    decision = 0
elif(dato == 'n'):
    decision = 0
else:
    os.system("python mail.py")

if(decision):
    # standard #
    d = open(file_path, "r")

    for date_line in d:
        temp_date.append(date_line)

    data['mail'] = temp_date[0].rstrip("\n")
    data['password'] = temp_date[1].rstrip("\n")
    data["to"] = temp_date[2].rstrip("\n")
    data['path'] = temp_date[3].rstrip("\n")

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
    # modifica dati #
    print('per utilizzare un profilo diverso da quello predefinito abilitare l\'accesso ad app meno sicure:\n https://myaccount.google.com/u/1/lesssecureapps \n\ninoltre se il profilo dispone della verifica in due passaggi usare come password quella per le app: \n https://myaccount.google.com/u/0/apppasswords?rapt = AEjHL4OHEKXhuBJJEiQLV-7kiULeXp3dME-JnZOp14JqJzohdhQOOlExWvg0eZ5ju5UjZr6VIZIOSDBloiGQgEVcu4f1WryX2w ')

    address = input('email mittente: ')
    temp_date.append(address)

    password = getpass('password mittente: ')
    temp_date.append(password)

    to = input('mail destinatario: ')
    temp_date.append(to)

    path_file = input('percorso cartella file: ')
    temp_date.append(path_file)

    with open("dati_predefiniti.txt", "w") as txt_file:
        for line in temp_date:
            txt_file.write(" ".join(line) + "\n")

    msg = EmailMessage()
    msg['Subject'] = input('oggetto: ')
    msg['From'] = address
    msg['To'] = to
    msg.set_content(input('messaggio: '))

files = []
for (dirpath, dirnames, filenames) in walk(path_file):
    files.extend(filenames)
    break

for file in files:
    with open(path_file+"/"+file, 'rb') as f:
        file_data = f.read()
        file_name = f.name

    msg.add_attachment(file_data, maintype='application',
                       subtype='octet-stream', filename=file_name)


with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(address, password)
    smtp.send_message(msg)
    input("email inviata con successo, premi invio per uscire")

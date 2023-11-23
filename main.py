import os

from dotenv import load_dotenv
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Load environment variables from the .env file
load_dotenv()


# const from enviroment files:
SendingEmail = os.environ.get("Email")
Password = os.environ.get("Password")
EmailSubject = os.environ.get("EmailSubject")
EmailBody = os.environ.get("EmailBody")



def get_google_sheet_data(sheet_title,sheet_index=0):
    # setting connection to google sheet
    scope = ['https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive"]

    credentials = ServiceAccountCredentials.from_json_keyfile_name('./auth.json',scope)
    gc = gspread.authorize(credentials=credentials)

    try:
        # openning the google spreadsheet using its title
        spreadsheet = gc.open(sheet_title)
        worksheet = spreadsheet.get_worksheet(sheet_index)

        # getting values from the spreadsheet
        response_data = worksheet.get_all_values()
        print("respionse data=>",response_data)

        # skiping header row if it exists
        if response_data and response_data[0]:
            headers = response_data[0]
            response_data = response_data[1:]

            return response_data ,headers,worksheet
        
    except Exception as err:
        print(f"Error accessing Google Sheets: {err}")
        return None
    


# sending emails

def send_email(name,email,phone,res_email,flag_cell,worksheet):
    sender_email = SendingEmail
    sender_password = Password
    subject = EmailSubject
    body = f"Dear {name},\n\n {EmailBody}"


    # creating the mime object
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = res_email
    msg['Subject'] = subject

    # Email body
    msg.attach(MIMEText(body, 'plain'))

    # connecting the SMTP server and sending the email
    try:
        with smtplib.SMTP('smtp.gmail.com',587) as server:
         server.starttls()
         server.login(sender_email,sender_password)
         server.sendmail(sender_email,res_email,msg.as_string())

        # updating the flag in the google sheet for next time
        worksheet.update_cell(flag_cell[0],flag_cell[1], 'Email Sended')
    except Exception as err:
        print(f"Error sending email to {name}: {err}")





google_Sheet_title = 'Society'
responses, headers,worksheet = get_google_sheet_data(google_Sheet_title)

    # print(headers,"header here//")

if responses:
    flag_index = headers.index('EmailSent') if 'EmailSent' in headers else None
    if flag_index is not None:

        for row in responses:
            name = row[1]
            email = row[2]
            phone = row[3]
            resEmail = row[4]
            flag_cell = (responses.index(row)+2, flag_index+1)

            if row[flag_index] != 'Email Sended':
                send_email(name,email,phone,resEmail,flag_cell,worksheet)


            #    print(f"name{name}, email{email},phone{phone},resEmail{resEmail}")
                print(f"Email sent to {name} at {resEmail}")
            else:
                 print(f"Email already sent to {name} at {resEmail}")
    else:
         print(f"Column 'Email Sent' not found in the google sheet.")
else:
  print("Failed to retrive responses.")
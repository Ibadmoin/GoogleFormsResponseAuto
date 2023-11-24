
# GOOGLE FROMS' AUTO-RESPONSE!
Hi! this is a simple python scripts for sending automate emails from google forms via **google sheet API.**


# REQUIREMENTS:
you will need authentication JSON format file key from Google Could Console for google sheet project. Give editor access to the response sheet from google form to the user. you create while making this project

**App Password ** :
 you also need to set app password for your email address so it can be used to send automate emails. 
 1.  Go to your Google Account.
2.  Select Security.
3.  Under "Signing in to Google," select 2-Step Verification.
4.  At the bottom of the page, select App passwords.
5.  Enter a name that helps you remember where you'll use the app password.
6.  Select Generate.



# Cloning the Repository

To get started with the project, you'll need to clone the repository to your local machine. Follow these steps:

## Step 1: Install Git

Make sure you have Git installed on your machine. If not, download and install it from [https://git-scm.com/](https://git-scm.com/).

## Step 2: Clone the Repository

Open your terminal or command prompt and run the following command to clone the repository:

```bash
git clone
https://github.com/Ibadmoin/GoogleFormsResponseAuto.git

cd GoogleFormsResponseAuto

**Create a virtual Enviroment**

python -m venv venv
.\venv\scripts\activate

note: make sure to change execetuon policy from windows powershell set it to remote-signed or unrestricted 


**Install Dependencies**
pip install -r requirements.txt


```

## Create a ENV File

Owner = "ibad"

SheetTitle = "your google sheet title"

Email = 'your email address'

Password = 'app password generated from google account manager'

  

EmailSubject = "your  email's subject"

EmailBody = "Thanks for joining Our Society. \n We will like to have you as our members.\n thank your\n ~ NEON"

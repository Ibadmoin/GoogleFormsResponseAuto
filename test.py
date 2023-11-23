from dotenv import load_dotenv
import os

load_dotenv()


EmailSubject = os.environ.get("EmailSubject")
EmailBody = os.environ.get("EmailBody")
body = f"Dear User,\n\n {EmailBody}"



print(f"The subject Will be: {EmailSubject}" )
print(body)


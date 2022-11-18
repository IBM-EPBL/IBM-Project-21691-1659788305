# import sendgrid
# import os
# from sendgrid.helpers.mail import *

API_KEY='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'

# sg = sendgrid.SendGridAPIClient(api_key=os.environ.get(API_KEY))
# from_email = Email("test@example.com")
# to_email = To("clashharish@gmail.com")
# subject = "Sending with SendGrid is Fun"
# content = Content("text/plain", "and easy to do anywhere, even with Python")
# mail = Mail(from_email, to_email, subject, content)
# response = sg.client.mail.send.post(request_body=mail.get())
# print(response.status_code)
# print(response.body)
# print(response.headers)

import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

message = Mail(
    from_email='trapremix21@gmail.com',
    to_emails='clashharish@gmail.com',
    subject='Sending with Twilio SendGrid is Fun',
    html_content='<strong>and easy to do anywhere, even with Python</strong>')
try:
    sg = SendGridAPIClient(API_KEY)
    response = sg.send(message)
    print('new',response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e)
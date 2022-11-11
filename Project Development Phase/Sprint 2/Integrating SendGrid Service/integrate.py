import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

message = Mail(
    from_email='safreenasafreen848@gmail.com',
    to_emails='19cse023safreen@gmail.com',
    subject='Sending with Twilio SendGrid is Fun',
    html_content='<strong>and easy to do anywhere, even with Python</strong>')
try:
    sg = SendGridAPIClient(os.environ.get('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'))
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e.message)
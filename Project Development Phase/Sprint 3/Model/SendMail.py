from flask import Flask
from flask_mail import Mail, Message
   
app = Flask(_name_)
mail = Mail(app) # instantiate the mail class
   
# configuration of mail
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'ajithkumarc67@gmail.com'
app.config['MAIL_PASSWORD'] = 'oaijanvwlpaixuby'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)
   
# message object mapped to a particular URL ‘/’
@app.route("/")
def index():
   msg = Message(
                'Alert',
                sender ='kumar@gmail.com',
                recipients = ['ajith@gmail.com']
               )
   msg.body = 'you have crossed your limit.'
   mail.send(msg)
   return 'Sent'
   
if _name_ == '_main_':
   app.run(debug = True)

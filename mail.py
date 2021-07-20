from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)
mail = Mail(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT']=465
app.config['MAIL_USERNAME']='umerm64@gmail.com' #update it with the mail address you want to use
app.config['MAIL_PASSWORD']='Uet_2014ee63'      #update it with the password of the entered mail
app.config['MAIL_USE_TLS']=False
app.config['MAIL_USE_SSL']=True
mail = Mail(app)

@app.route('/')
def index():
    #                sender mail=the one entered above          recipients=addresses wehre you want to send messages
    msg = Message('Hello', sender='umerm64@gmail.com', recipients=['msee20003@itu.edu.pk'])
    msg.body = "Hello Flask! This message is sent from Flask-Mail"
    mail.send(msg)
    return 'Message Sent'

if __name__ == '__main__':
    app.run(debug=True)

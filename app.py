from flask import Flask, render_template, request, redirect, flash, url_for
from flask_mail import Mail, Message
import json

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for flashing messages

# Mail configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'vasthav8656@gmail.com'      
app.config['MAIL_PASSWORD'] = 'rawu xnzu blmt hqcc'      # App password from Google
app.config['MAIL_DEFAULT_SENDER'] = 'vasthav8656@gmail.com'     

mail = Mail(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/projects')
def projects():
    with open('data/projects.json') as f:
        projects = json.load(f)
    return render_template('projects.html', projects=projects)


@app.route('/mycertificates')
def mycertificates():
    return render_template('mycertificates.html')

@app.route('/skills')
def skills():
    return render_template('skills.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route("/sendmessage", methods=["POST"])
def send_message():
    name = request.form.get("name")
    email = request.form.get("email")
    message = request.form.get("message")

    # Compose and send the message
    msg = Message(
        subject="New Contact Form Submission",
        recipients=['vasthav8656@gmail.com'],  
        reply_to=email  
    )
    msg.body = f"""
    You received a new message from your portfolio website:

    Name: {name}
    Email: {email}

    Message:
    {message}
    """

    try:
        mail.send(msg)
        flash("Your message has been sent successfully! 🥳", "success")
    except Exception as e:
        print(f"Error: {e}")
        flash("Something went wrong 😞. Please try again later.", "danger")

    return redirect(url_for("contact"))


if __name__ == '__main__':
    app.run(debug=True)

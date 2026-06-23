from flask import Flask, render_template, request, flash, redirect, url_for, send_from_directory
from flask_mail import Mail, Message
import os
app = Flask(__name__)
# Secret Key
app.secret_key = "your_secret_key_here"

# ==========================
# MAIL CONFIGURATION
# ==========================
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True

# Your Gmail
import os

app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')

mail = Mail(app)

# ==========================
# HOME PAGE
# ==========================
@app.route('/')
def home():
    return render_template('index.html')

# ==========================
# CONTACT FORM
# ==========================
@app.route('/contact', methods=['POST'])
def contact():

    try:
        name = request.form.get('name')
        email = request.form.get('email')
        mobile = request.form.get('mobile')
        reason = request.form.get('reason')
        message_text = request.form.get('message')

        body = f"""
        New Portfolio Contact Request

        Name: {name}
        Email: {email}
        Mobile: {mobile}
        Reason: {reason}

        Message:
        {message_text}
        """

        msg = Message(
            subject=f"Portfolio Contact - {name}",
            sender=app.config['MAIL_USERNAME'],
            recipients=['yourgmail@gmail.com']
        )

        msg.body = body

        mail.send(msg)

        flash("Message sent successfully!", "success")

    except Exception as e:
        print(e)
        flash("Failed to send message.", "danger")

    return redirect(url_for('home'))

# ==========================
# RESUME DOWNLOAD
# ==========================
@app.route('/resume')
def resume():
 return send_from_directory(
        directory='static', 
        path='Vijay_Resume.pdf', 
        as_attachment=True, 
        download_name='Vijay_Resume.pdf'
    )

# ==========================
# ERROR HANDLERS
# ==========================
@app.errorhandler(404)
def page_not_found(error):
    return render_template("index.html"), 404

@app.errorhandler(500)
def internal_server_error(error):
    return render_template("index.html"), 500

# ==========================
# RUN APP
# ==========================
if __name__ == "__main__":
    app.run(debug=True)
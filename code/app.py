# importing libraries needed
import sqlite3
from flask import Flask, render_template, request, url_for, redirect, session, send_from_directory
from flask_uploads import UploadSet, IMAGES, configure_uploads
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, file_allowed, FileAllowed
from wtforms import SubmitField
import random


def register_user_to_db(username, password):
    con = sqlite3.connect('users.db')
    cur = con.cursor()
    cur.execute('INSERT INTO users(username,password) values (?,?)', (username, password))
    con.commit()
    con.close()


def check_user(username, password):
    con = sqlite3.connect('users.db')
    cur = con.cursor()
    cur.execute('Select username,password FROM users WHERE username=? and password=?', (username, password))

    result = cur.fetchone()
    if result:
        return True
    else:
        return False


app = Flask(__name__)
app.secret_key = "r@nd0mSk_1"
app.config['SECRET_KEY'] = 'r@nd0mSk_1'
app.config['UPLOADED_PHOTOS_DEST'] = 'uploads'




@app.route("/")
def index():
    return render_template('login.html')


@app.route('/register', methods=["POST", "GET"])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        register_user_to_db(username, password)
        return redirect(url_for('index'))

    else:
        return render_template('register.html')


@app.route('/login', methods=["POST", "GET"])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        print(check_user(username, password))
        if check_user(username, password):
            session['username'] = username

        return redirect(url_for('home'))
    else:
        return redirect(url_for('index'))


@app.route('/home', methods=['POST', "GET"])
def home():
    if 'username' in session:
        return render_template('home.html', username=session['username'])
    else:
        return "Username or Password is wrong!"


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))


photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)

class UploadForm(FlaskForm):
    photo = FileField(validators=[FileAllowed(photos, 'Only images are allowed'),FileRequired('File field should not be empty')])
    submit = SubmitField('Upload')


@app.route('/code/<filename>')
def get_file(filename):
    return send_from_directory(app.config['UPLOADED_PHOTOS_DEST'], filename)


@app.route("/media", methods=['GET', 'POST'])
def upload_image():
    form = UploadForm()
    if form.validate_on_submit():
        filename = photos.save(form.photo.data)
        file_url = url_for('get_file', filename=filename)
    else:
        file_url = None
    return render_template('media.html', form=form, file_url=file_url)

'''app = Flask(__name__)  # setting a variable for flask to make it easier to use


@app.route('/')  # setting up a route to flask and the function
# making a function that renders the main html
def mainMenu():
    return render_template('home.html')


app.route('/membership')
def membershipPage():
    return render_template('membership.html')





@app.route('/newuser', methods = ['POST', 'GET'])
def newUser():
    if request.method == 'POST':
        try:
            email = request.form['email']
            searchpassword = request.form['password']
            
            #name = request.form['name']
            #membership = True

            with sqlite3.connect("users.db") as conn:
            cur = conn.cursor()
            msg = cur.execute("SELECT email FROM user where email = (?)",[email.data]).fetchone()
            if msg is None:
                raise IndexError('This Email ID is not registered. Please register before login')
'''               
    

if __name__ == "__main__":
    app.run(debug=True)

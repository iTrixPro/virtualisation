from flask import Flask, render_template, url_for, request, session, redirect
from flask_mysqldb import MySQL 

# set our app
app = Flask(__name__)
app.secret_key = 'uo09QQnOgpwTM4Y'

# set database config
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'virtualisation'

db = MySQL(app)

# set route config
@app.route('/', methods=['GET', 'POST'])
def login(): 
    if request.method == 'POST':
        username = request.form.get('username', False)
        pwd = request.form.get('pwd', False)

        cur = db.connection.cursor()
        cur.execute(f"select username, pwd from Users where username = '{username}'")

        user = cur.fetchone()
        cur.close()

        if user and pwd == user[1]:
            session['username'] = user[0]
            return redirect(url_for('home'))
        else:
           return render_template('login.html', error='invalid username or password !')

    else:       
        return render_template('login.html')

@app.route('/home')
def home():
    if 'username' in session:
        return render_template('home.html', username=session['username'])
    else:
        return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username', False)
        pwd = request.form.get('pwd', False)

        cur = db.connection.cursor()
        cur.execute(f"insert into Users(username, pwd) values('{username}', '{pwd}')")

        db.connection.commit()
        cur.close()

        return redirect(url_for('login'))
        
    else:
        return render_template('register.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True, port=5000, host="0.0.0.0")
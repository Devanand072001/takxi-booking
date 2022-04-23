from flask import Flask, render_template, request, redirect, session, flash, url_for
from functools import wraps
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'taxi_booking_app'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)


@app.route("/")
@app.route("/index")
def Homepage():
    return render_template("index.html", feedback="False")

# Login

@app.route('/driverlogin', methods=['POST', 'GET'])
def driverlogin():
    status = True
    if request.method == 'POST':
        email = request.form["email"]
        pwd = request.form["upass"]
        cur = mysql.connection.cursor()
        cur.execute(
            "select * from driver where EMAIL=%s and UPASS=%s", (email, pwd))
        data = cur.fetchone()
        if data:
            session['logged_in'] = True
            session['username'] = data["UNAME"]
            flash('Login Successfully', 'success')
            return redirect('driverhome')
        else:
            flash('Invalid Login. Try Again', 'danger')
    return render_template("driverlogin.html")


@app.route('/userlogin', methods=['POST', 'GET'])
def userlogin():
    status = True
    if request.method == 'POST':
        email = request.form["email"]
        pwd = request.form["upass"]
        cur = mysql.connection.cursor()
        cur.execute(
            "select * from users where EMAIL=%s and UPASS=%s", (email, pwd))
        data = cur.fetchone()
        if data:
            session['logged_in'] = True
            session['username'] = data["UNAME"]
            flash('Login Successfully', 'success')
            return redirect('userhome')
        else:
            flash('Invalid Login. Try Again', 'danger')
    return render_template("userlogin.html")

# check if driver logged in


def is_driverlogged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('Unauthorized, Please Login', 'danger')
            return redirect(url_for('driverlogin'))
    return wrap

# check if user logged in


def is_userlogged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('Unauthorized, Please Login', 'danger')
            return redirect(url_for('userlogin'))
    return wrap


# Registration
@app.route('/driverreg', methods=['POST', 'GET'])
def driverreg():
    status = False
    if request.method == 'POST':
        name = request.form["uname"]
        email = request.form["email"]
        pwd = request.form["upass"]
        contact = request.form["contact"]
        cur = mysql.connection.cursor()
        cur.execute("insert into driver(UNAME,UPASS,EMAIL,CONTACT) values(%s,%s,%s,%s)",
                    (name, pwd, email, contact))
        mysql.connection.commit()
        cur.close()
        flash('Registration Successfully. Login Here...', 'success')
        return redirect('driverlogin')
    return render_template("driverreg.html", status=status)

# Registration


@app.route('/userreg', methods=['POST', 'GET'])
def userreg():
    status = False
    if request.method == 'POST':
        name = request.form["uname"]
        email = request.form["email"]
        pwd = request.form["upass"]
        contact = request.form["contact"]
        cur = mysql.connection.cursor()
        cur.execute("insert into users(UNAME,UPASS,EMAIL,CONTACT) values(%s,%s,%s,%s)",
                    (name, pwd, email, contact))
        mysql.connection.commit()
        cur.close()
        flash('Registration Successfully. Login Here...', 'success')
        return redirect('userlogin')
    return render_template("userreg.html", status=status)

# Home page


@app.route("/driverhome")
@is_driverlogged_in
def driverhome():
    return render_template('driverhome.html')

# Home page


@app.route("/userhome")
@is_userlogged_in
def userhome():
    
    return render_template('userhome.html')

# logout


@app.route("/driverlogout")
def driverlogout():
    session.clear()
    flash('You are now logged out', 'success')
    return redirect(url_for('driverlogin'))

# logout


@app.route("/userlogout")
def userlogout():
    session.clear()
    flash('You are now logged out', 'success')
    return redirect(url_for('userlogin'))


if __name__ == '__main__':
    app.secret_key = 'secret'
    app.run(debug=True)

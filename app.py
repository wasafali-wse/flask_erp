from flask import Flask,render_template,request,redirect,url_for,session
import pymysql
import os


app = Flask(__name__)
secret_key = os.urandom(24)
app.secret_key = secret_key

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'  # Your MySQL username
app.config['MYSQL_PASSWORD'] = ''  # Your MySQL password
app.config['MYSQL_DB'] = 'test'  # Your MySQL database name

mysql = pymysql.connect(host='localhost',
                        port=3308,
                        user='root',
                        password='',
                        db='test',
                        cursorclass=pymysql.cursors.DictCursor)


@app.route("/logout")
def logout():
    # Remove user data from session
    session.pop('user', None)
    # Redirect to the login page
    return redirect(url_for("login"))


@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Get username and password from the form
        username = request.form.get("first")
        password = request.form.get("password")
        
        # Query the database to check if the username and password are correct
        cursor = mysql.cursor()
        sql = "SELECT * FROM `user` WHERE `first_name`=%s AND `password`=%s"
        cursor.execute(sql, (username, password))
        user = cursor.fetchone()

        if user:
            # If user exists and password is correct, set user info in session and redirect to dashboard
            session['user'] = user
            return redirect(url_for("dashboard"))
        else:
            
            # If user doesn't exist or password is incorrect, display error message
            error_message = "Invalid username or password. Please try again."
            return render_template("Login.html", error_message=error_message)
    else:
        # Render the login template
        return render_template("Login.html")

@app.route("/register", methods=["POST", "GET"])
def register():
    if request.method == "POST":
        # Get form data
        first_name = request.form.get("first")
        last_name = request.form.get("last")
        email = request.form.get("email")
        password = request.form.get("password")
        confirm_password = request.form.get("repassword")
        access_type = request.form.get("Access")

        

        # Check if passwords match
        if password != confirm_password:
            return "Passwords do not match"

        # Insert data into user table
        cursor = mysql.cursor()
        sql = "INSERT INTO `user` (first_name, last_name, email, password, confirm_password, access_type) VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(sql, (first_name, last_name, email, password, confirm_password, access_type))
        mysql.commit()

        return redirect(url_for("login"))
    else:
        return render_template("Register.html")

@app.route("/dashboard")
def dashboard():
    # Check if user is logged in
    if 'user' in session:
        user = session['user']
        access_type = user['access_type']
        
        # Determine which dashboard template to render based on the access type
        if access_type == 'admin':
            return render_template("dashboard.html", user=user)
        elif access_type == 'accountant':
            return render_template("dashboard_accountant.html", user=user)
        elif access_type == 'receptionist':
            return render_template("dashboard_receptionist.html", user=user)
        else:
            # If access type is not recognized, redirect to login page
            return  "accessnot matched "# redirect(url_for("login"))
    else:
        # If user is not logged in, redirect to login page
        return redirect(url_for("login"))

@app.route("/new/token")
def new_token():
    # Check if user is logged in and 'user' is in session
    if 'user' in session:
        user = session['user']
        # Render the template and pass the 'user' object to it
        return render_template("new_token.html", user=user)
    else:
        # If user is not logged in, redirect to the login page
        return redirect(url_for("login"))
@app.route("/new/label")
def new_label():
    # Check if user is logged in and 'user' is in session
    if 'user' in session:
        user = session['user']
        # Render the template and pass the 'user' object to it
        return render_template("new_label.html", user=user)
    else:
        # If user is not logged in, redirect to the login page
        return redirect(url_for("login"))
@app.route("/new/l_invoice")
def new_l_invoice():
    # Check if user is logged in and 'user' is in session
    if 'user' in session:
        user = session['user']
        # Render the template and pass the 'user' object to it
        return render_template("new_l_invoice.html", user=user)
    else:
        # If user is not logged in, redirect to the login page
        return redirect(url_for("login"))
@app.route("/new/invoice")
def new_invoice():
    # Check if user is logged in and 'user' is in session
    if 'user' in session:
        user = session['user']
        # Render the template and pass the 'user' object to it
        return render_template("new_invoice.html", user=user)
    else:
        # If user is not logged in, redirect to the login page
        return redirect(url_for("login"))
@app.route("/new/quotation")
def new_quotation():
    # Check if user is logged in and 'user' is in session
    if 'user' in session:
        user = session['user']
        # Render the template and pass the 'user' object to it
        return render_template("new_quotation.html", user=user)
    else:
        # If user is not logged in, redirect to the login page
        return redirect(url_for("login"))
@app.route("/search")
def search():
    # Check if user is logged in and 'user' is in session
    if 'user' in session:
        user = session['user']
        # Render the template and pass the 'user' object to it
        return render_template("search.html", user=user)
    else:
        # If user is not logged in, redirect to the login page
        return redirect(url_for("login"))
@app.route("/check")
def check():
    # Check if user is logged in and 'user' is in session
    if 'user' in session:
        user = session['user']
        # Render the template and pass the 'user' object to it
        return render_template("check.html", user=user)
    else:
        # If user is not logged in, redirect to the login page
        return redirect(url_for("login"))
@app.route("/invetory")
def inventory():
    # Check if user is logged in and 'user' is in session
    if 'user' in session:
        user = session['user']
        # Render the template and pass the 'user' object to it
        return render_template("inventory.html", user=user)
    else:
        # If user is not logged in, redirect to the login page
        return redirect(url_for("login"))
@app.route("/hrm")
def hrm():
    # Check if user is logged in and 'user' is in session
    if 'user' in session:
        user = session['user']
        # Render the template and pass the 'user' object to it
        return render_template("hrm.html", user=user)
    else:
        # If user is not logged in, redirect to the login page
        return redirect(url_for("login"))
@app.route("/report")
def report():
    # Check if user is logged in and 'user' is in session
    if 'user' in session:
        user = session['user']
        # Render the template and pass the 'user' object to it
        return render_template("report.html", user=user)
    else:
        # If user is not logged in, redirect to the login page
        return redirect(url_for("login"))
@app.route("/todo")
def todo():
    # Check if user is logged in and 'user' is in session
    if 'user' in session:
        user = session['user']
        # Render the template and pass the 'user' object to it
        return render_template("todo.html", user=user)
    else:
        # If user is not logged in, redirect to the login page
        return redirect(url_for("login"))









if __name__ == "__main__":
    app.run( debug=True)
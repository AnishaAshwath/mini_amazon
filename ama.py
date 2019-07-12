from flask import Flask,render_template,request,redirect,url_for,session

app=Flask(__name__)

app.secret_key="he"

@app.route('/')

def home():
	return render_template("home1.html",title="home")

@app.route('/about')

def about():
	return render_template("about.html",title="about")

@app.route('/contact')

def contact():
	return render_template("contact.html",title="contact")
@app.route('/login',methods=['GET','POST'])
def login():
	users = {'user1':'111','user2':'222','user3':'333','user4':'444'}
	username=request.form["username"]
	password=request.form["password"]

	if username not in users:
		return "user does'nt exist"
	if users[username]!=password:
		return 'incorrect password'
	session['username']=username
	#return render_template("home1.html",signin=True)
	return redirect(url_for("home"))


@app.route('/logout')
def logout():
	session.clear()
	return redirect(url_for("home"))


app.run(debug=True)


from flask import Flask,render_template,request,redirect,url_for,session
from models.model import user_exists,save_user,product_exists,add_product,product_list,remove_from_db,remove_frm_cart,add_to_cart,cart_info
import os
print(os.getcwd())

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

@app.route('/login',methods=["GET","POST"])
def login():
	if request.method=="POST":
		username=request.form['username']
		password=request.form['password']
		result=user_exists(username)
		if result:
			if result['password1']!=password:
				return "password does'nt match"
			session['username']=username
			session['c_type']=result['c_type']
			return redirect(url_for("home"))
		return "username does'nt exists"
	return redirect(url_for("home"))


'''@app.route('/login',methods=['GET','POST'])
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
	return redirect(url_for("home"))'''

@app.route('/signup',methods=['GET','POST'])
def signup():

	if request.method=='POST':

		user_info={}
		#import pdb;pdb.set_trace()
		user_info['username']=request.form['username']
		user_info['password1']=request.form['password1']
		password2=request.form['password2']
		user_info['c_type']=request.form['type']
		if user_info['c_type']=="buyer":
			user_info['cart']=[]
		if user_exists(user_info['username']):
			return "username already exists"
		if user_info['password1']!=password2:
			return "passwords don't match!!!"
		save_user(user_info)
		#return redirect(url_for("home"))

	return redirect(url_for("home"))


@app.route('/products',methods=['GET','POST'])
def products():
	if request.method=='POST':

		product_info={}
		#import pdb;pdb.set_trace()
		product_info['name']=request.form['name']
		product_info['price']=int(request.form['price'])
		product_info['description']=request.form['description']
		product_info['seller']=session['username']
		
		if product_exists(product_info['name']):
			return "product exists"
		add_product(product_info)
		#return "product added! check your db"
		return redirect(url_for("home"))
	return render_template('ran.html',products=product_list())
	


@app.route('/removeproducts',methods=['GET','POST'])
def removeproducts():
	if request.method=="POST":
		name=request.form['name']
		remove_from_db(name)
		return redirect(url_for("products"))
	return redirect(url_for("products"))

@app.route('/cart',methods=['GET','POST'])
def cart():
	if request.method=="POST":
		name=request.form['name']
		add_to_cart(name)
		return redirect(url_for('products'))
		#product=cart_info()
	return render_template('cart.html',products=cart_info())

@app.route('/remove_from_cart',methods=['GET','POST'])
def remove_cart():
	if request.method=="POST":
		name=request.form['name']
		remove_frm_cart(name)
		return redirect(url_for('cart'))
	return redirect(url_for('cart'))

@app.route('/logout')
def logout():
	session.clear()
	return redirect(url_for("home"))




app.run(debug=True)


from flask import Flask, render_template, url_for, request , session, flash, redirect
from app import app
app.secret_key = "cobaanTuhan"


#from app.models.user import User ## import kelas User dari model

#@app.route('/', methods = ['GET'])
#def index():
	#user =  User() ## membuat objek dari kelas user
	#nama = user.getName() ## memanggil method untuk mengambil nama
	#return render_template('index.html', nama=nama)

@app.route('/')
def index():
	if "user" in session:
		return redirect(url_for('main'))
	else:
		return render_template ("index2.html")
	
	

@app.route('/register')
def register():
	return render_template('register.html')

@app.route('/login', methods = ["POST","GET"])
def login():
	if "user" in session:
		username = session["user"]
		return redirect (url_for('main'))
	elif request.method == "POST":
		username = request.form["nama_user"]
		password = request.form["kata_sandi"]
		if username == password:
			#session.permanent = True
			session["user"] = request.form["nama_user"]
			
			if "memori" in session:
				memori = session["memori"]
				print(session["memori"], "ini dari login")
				session.pop("memori")
				return redirect(memori)
			else:
				return redirect(url_for('main'))  
		else:
			flash("USERNAME PASSWORD TIDAK SAMA")
			return redirect(url_for('login'))
	else:
	 	 return render_template("login.html")

@app.route('/main')
def main():
    if "user" in session:
        return render_template("index3.html", username = session["user"])
    else:
        return redirect(url_for('index'))

@app.route('/profile')
def profile():
	if "user" in session:
		return render_template("profile.html")
	else:
		session["memori"]= url_for('profile')
		print(session["memori"], "ini dari profile")
		return redirect(url_for('login'))

@app.route('/logout')
def logout():
	session.pop('user')
	return redirect(url_for('index'))

if __name__== '__main__':
    app.run()



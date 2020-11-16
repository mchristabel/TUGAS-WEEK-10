#from flask import Flask, render_template, request
#from app import app
#from app.models.user import User ## import kelas User dari model

#@app.route('/register', methods = ['GET'])
#def register_index():
	#return render_template('auth/register.html')

#@app.route('/login', methods = ['GET'])
#def login_index():
	#return render_template('auth/login.html')

#@app.route('/authenticate', methods = ['POST'])
#def auth_check():
	#user =  User() ## membuat objek dari kelas user

	#nama_user = request.form['username']
	#kata_sandi = request.form['password']
	#isAllowed = user.checkAccess(nama_user,kata_sandi) ## memanggil method untuk mengecek akses masuk

	#if isAllowed==1:
		#balasan = "Boleh Masuk Boy! " + user.getUsername()
		#return balasan
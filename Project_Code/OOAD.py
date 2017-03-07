from flask import Flask 
from flask import abort
from flask import make_response
from flask import request
from flask import render_template
from flask import url_for
from flask import redirect
from firebase import firebase

app = Flask(__name__)
Name=""
@app.route('/welcome',methods=['GET'])
def welcome():
	return render_template('welcome.html')

@app.route('/login',methods=['GET','POST'])
def login():
	error=None
	firebase1=firebase.FirebaseApplication('https://hospitalmanagementsystem-edfd9.firebaseio.com/')
	result=firebase1.get('/admin',None)
	user_key_list=[]
	for i in result.keys():
		user_key_list.append(i)
	print(user_key_list)
	if request.method =='POST':
		flag=0
		for i in user_key_list:
			if request.form['username'] == str(result[i]['username']) and request.form['password'] == str(result[i]['password']):
				token=i
				flag=1
				break
		if flag == 1:
			return render_template('welcome.html',name=result[token]['name'])
		else:
			error='Invalid credentials. Please try again.'
	return render_template('login.html',error=error)

@app.route('/register',methods=['GET','POST'])
def register():
	error=None
	if request.method =='POST':
		flag=0
		if request.form['password'] == request.form['againPassword']:
			firebase1=firebase.FirebaseApplication('https://hospitalmanagementsystem-edfd9.firebaseio.com/')
			result=firebase1.post('/admin',{
				"username":request.form['username'],
				"password":request.form['password'],
				"name":request.form['name']
			})
			flag=1
			Name=request.form['name']
		if flag == 1:
			return render_template('welcome.html',name=Name)
		else:
			error='Invalid credentials. Please try again.'
	return render_template('register.html',error=error)

@app.route('/addDoctor',methods=['GET','POST'])
def addDoctor():
	error=None
	return render_template('addDoctor.html',name=Name)










if __name__ == '__main__':
    app.run(debug=True,threaded=True)


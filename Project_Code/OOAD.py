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

		firebase1=firebase.FirebaseApplication('https://hospitalmanagementsystem-edfd9.firebaseio.com/')
		result=firebase1.get('/admin',None)
		user_key_list=[]
		count=0
		for i in result.keys():
			user_key_list.append(i)

		for i in user_key_list:
			if result[i]['username'] == request.form['username']:
				count=count+1


		if request.form['password'] == request.form['againPassword'] and count == 0:
			firebase1=firebase.FirebaseApplication('https://hospitalmanagementsystem-edfd9.firebaseio.com/')
			result=firebase1.post('/admin',{
				"username":request.form['username'],
				"password":request.form['password'],
				"name":request.form['name']
			})
			flag=1
			count=0
		if flag == 1:
			return render_template('welcome.html')
		elif request.form['password'] != request.form['againPassword']:
			error='Error: both the passwords are not matching'
		elif count >=1:
			error='username already exists'
	return render_template('register.html',error=error)

@app.route('/addDoctor',methods=['GET','POST'])
def addDoctor():
	error=None
	if request.method == 'POST':
		firebase1=firebase.FirebaseApplication('https://hospitalmanagementsystem-edfd9.firebaseio.com/')
		result=firebase1.get('/doctor',None)
		user_key_list=[]
		count=0
		for i in result.keys():
			user_key_list.append(i)

		for i in user_key_list:
			if result[i]['name'] == request.form['name'] and result[i]['department'] == request.form['department'] and result[i]['hospital'] == request.form['hospital']:
				count=count+1

		if len(request.form['mobile']) > 10:
			error='Invalid Number'

		elif count == 0:
			firebase1=firebase.FirebaseApplication('https://hospitalmanagementsystem-edfd9.firebaseio.com/')
			result=firebase1.post('/doctor',{
				"aadhar_number":request.form['aadhar'],
				"name":request.form['name'],
				"hospital":request.form['hospital'],
				"department":request.form['department'],
				"mobile_number":request.form['mobile'],
			})
			name=request.form['name']
			firebase1=firebase.FirebaseApplication('https://hospitalmanagementsystem-edfd9.firebaseio.com/')
			result=firebase1.get('/doctor',None)
			user_key_list=[]
			for i in result.keys():
				user_key_list.append(str(i))
			for i in user_key_list:
				if result[i]['name'] == name:
					firebase1=firebase.FirebaseApplication('https://hospitalmanagementsystem-edfd9.firebaseio.com/')
					result=firebase1.patch('/doctor/'+i,{
						"employee_number":i,
						"appointments_count":0
					})
			count=0
			user_key_list=[]
			return render_template('welcome.html')
		elif count >= 1:
			error='Doctor alreay exists'

	return render_template('addDoctor.html',error=error)

@app.route('/searchDoctor',methods=['GET','POST'])
def searchDoctor():
	error=None
	if request.method == 'POST':
		firebase1=firebase.FirebaseApplication('https://hospitalmanagementsystem-edfd9.firebaseio.com/')
		result=firebase1.get('/doctor',None)
		user_key_list=[]
		flag=0
		for i in result.keys():
			user_key_list.append(i)

		for i in user_key_list:
			if result[i]['mobile_number'] == request.form['mobile']:
				name=result[i]['name']
				aadhar=result[i]['aadhar_number']
				appointments=result[i]['appointments_count']
				department=result[i]['department']
				hospital=result[i]['hospital']
				mobile=result[i]['mobile_number']
				employee=result[i]['employee_number']
				flag=1
				user_key_list=[]

		patient_mobile_numbers=[]
		firebase1=firebase.FirebaseApplication('https://hospitalmanagementsystem-edfd9.firebaseio.com/')
		result=firebase1.get('/appointments',None)
		user_key_list=[]
		for i in result.keys():
			user_key_list.append(i)

		for i in user_key_list:
			if result[i]['doctor_name'] == name:
				patient_mobile_numbers.append(result[i]['patient_number'])

		if flag == 1:
			return render_template('displayDoctor.html',name=name,aadhar=aadhar,appointments=appointments,department=department,hospital=hospital,mobile=mobile,employee=employee,number_list=patient_mobile_numbers)

		if flag == 0:
			error="Invalid Doctor"

	return render_template('searchDoctor.html',error=error)

@app.route('/searchPatient',methods=['GET','POST'])
def searchPatient():
	error=None
	if request.method == 'POST':
		firebase1=firebase.FirebaseApplication('https://hospitalmanagementsystem-edfd9.firebaseio.com/')
		result=firebase1.get('/patient',None)
		user_key_list=[]
		flag=0
		for i in result.keys():
			user_key_list.append(i)

		for i in user_key_list:
			if result[i]['mobile_number'] == request.form['mobile']:
				name=result[i]['name']
				file=result[i]['file_number']
				mobile=result[i]['mobile_number']
				address=result[i]['address']
				appointments=result[i]['appointments_count']
				flag=1
				user_key_list=[]
				return render_template('displayPatient.html',name=name,file=file,mobile=mobile,address=address,appointments=appointments)

		if flag == 0:
			error="Invalid Patient"

	return render_template('searchPatient.html',error=error)
@app.route('/displayAppointments/<name>',methods=['GET'])
def displayAppointments(name):
	firebase1=firebase.FirebaseApplication('https://hospitalmanagementsystem-edfd9.firebaseio.com/')
	result=firebase1.get('/appointments',None)
	user_key_list=[]
	patient_mobile_numbers=[]
	count=0
	for i in result.keys():
		user_key_list.append(i)
	for i in user_key_list:
		if result[i]['doctor_name'] == name:
			count=count+1
			patient_mobile_numbers.append(result[i]['patient_number'])

	print(patient_mobile_numbers)

	return render_template('viewAppointments.html',patient_list=patient_mobile_numbers,count=count)
	








if __name__ == '__main__':
    app.run(debug=True,threaded=True)


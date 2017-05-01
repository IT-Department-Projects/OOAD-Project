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


@app.route('/searchDoctor',methods=['GET','POST'])
def searchDoctor():
	error=None
	if request.method == 'POST':
		firebase1=firebase.FirebaseApplication('https://hospitalmanagementsystem-edfd9.firebaseio.com/')
		result=firebase1.get('/doctors_info',None)
		user_key_list=[]
		flag=0
		for i in result.keys():
			user_key_list.append(i)

		for i in user_key_list:
			if result[i]['phone'] == request.form['mobile']:
				name=result[i]['name']
				employee_id=result[i]['employee_id']
				department=result[i]['department']
				hospital=result[i]['hospital']
				phone=result[i]['phone']
				username=result[i]['username']
				flag=1
				user_key_list=[]

		if flag == 1:
			return render_template('displayDoctor.html',name=name,employee_id=employee_id,department=department,hospital=hospital,phone=phone,username=username)


		if flag == 0:
			error="Invalid Doctor"

	return render_template('searchDoctor.html',error=error)

@app.route('/searchPatient',methods=['GET','POST'])
def searchPatient():
	error=None
	if request.method == 'POST':
		firebase1=firebase.FirebaseApplication('https://hospitalmanagementsystem-edfd9.firebaseio.com/')
		result=firebase1.get('/patients_info',None)
		user_key_list=[]
		flag=0
		for i in result.keys():
			user_key_list.append(i)

		for i in user_key_list:
			if result[i]['phone'] == request.form['mobile']:
				name=result[i]['name']
				file_number=result[i]['file_number']
				phone=result[i]['phone']
				address=result[i]['address']
				insurance=result[i]['insurance']
				username=result[i]['username']
				flag=1
				user_key_list=[]

		if flag == 1:
			return render_template('displayPatient.html',name=name,file_number=file_number,phone=phone,address=address,insurance=insurance,username=username)

		if flag == 0:
			error="Invalid Patient"

	return render_template('searchPatient.html',error=error)



@app.route('/appointments',methods=['GET','POST'])
def appointments():
	error=None
	if request.method == 'POST':
		oldstr=request.form['email_id']
		email_id = oldstr.replace(".", "")
		firebase1=firebase.FirebaseApplication('https://hospitalmanagementsystem-edfd9.firebaseio.com/')
		result=firebase1.get('/'+email_id,None)
		user_key_list=[]
		for i in result.keys():
			user_key_list.append(i)
		flag=0
		total_list=[]
		for i in user_key_list:
			individual_list=[]
			doctorName=result[i]['doctorName']
			individual_list.append(doctorName)
			time=result[i]['time']
			individual_list.append(time)
			total_list.append(individual_list)
			flag=1

		if flag == 1:
			return render_template('displayAppointments.html',total_list=total_list)
		else:
			error="No Appointments"
	return render_template('appointments.html',error=error)

@app.route('/schedule',methods=['GET','POST'])
def schedule():
	error=None
	if request.method == 'POST':
		oldstr=request.form['email_id']
		email_id = oldstr.replace(".", "")
		firebase1=firebase.FirebaseApplication('https://hospitalmanagementsystem-edfd9.firebaseio.com/')
		result=firebase1.get('/'+email_id,None)
		user_key_list=[]
		for i in result.keys():
			user_key_list.append(i)
		flag=0
		total_list=[]
		for i in user_key_list:
			individual_list=[]
			patientName=result[i]['patientName']
			individual_list.append(patientName)
			patient_file_number=result[i]['patient_file_number']
			individual_list.append(patient_file_number)
			patient_insurance=result[i]['patient_insurance']
			individual_list.append(patient_insurance)
			time=result[i]['time']
			individual_list.append(time)
			total_list.append(individual_list)
			flag=1

		if flag == 1:
			return render_template('displaySchedule.html',total_list=total_list)
		else:
			error="No Schedule"
	return render_template('schedule.html',error=error)









if __name__ == '__main__':
    app.run(debug=True,threaded=True)


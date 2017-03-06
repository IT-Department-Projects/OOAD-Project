from firebase import firebase

class CreatePatient:
	def __init__(self,patient_username,patient_password,patient_name,patient_phone_number,patient_insurance,patient_address):
		self.user_username=patient_username
		self.user_password=patient_password
		self.user_name=patient_name
		self.user_number=patient_phone_number
		self.user_insurance=patient_insurance
		self.user_address=patient_address

		firebase1=firebase.FirebaseApplication('https://hospitalmanagementsystem-edfd9.firebaseio.com/')
		result=firebase1.get('/patient',None)

		user_key_list=[]
		if not result.keys():
			firebase1=firebase.FirebaseApplication('https://hospitalmanagementsystem-edfd9.firebaseio.com/')
			result=firebase1.post('/patient',{
				"username":self.user_username,
				"password":self.user_password,
				"name":self.user_name,
				"mobile_number":self.user_number,
				"insurance":self.user_insurance,
				"address":self.user_address,
				"appointments_count":0

			})

		
			firebase1=firebase.FirebaseApplication('https://hospitalmanagementsystem-edfd9.firebaseio.com/')
			result=firebase1.get('/patient',None)
			user_key_list=[]
			for i in result.keys():
				user_key_list.append(i)

			for i in user_key_list:
				if result[i]['username'] == self.user_username:
					firebase1=firebase.FirebaseApplication('https://hospitalmanagementsystem-edfd9.firebaseio.com/')
					result=firebase1.patch('/patient/'+i,{
						"file_number":i
					})
			
		else:
			for i in result.keys():
				user_key_list.append(i)
			flag=0
			for i in user_key_list:
				if result[i]['username']== patient_username:
					print("Username exists")
					flag=1
					break
			if flag == 0:
				firebase1=firebase.FirebaseApplication('https://hospitalmanagementsystem-edfd9.firebaseio.com/')
				result=firebase1.post('/patient',{
					"username":self.user_username,
					"password":self.user_password,
					"name":self.user_name,
					"mobile_number":self.user_number,
					"insurance":self.user_insurance,
					"address":self.user_address,
					"appointments_count":0
				})

				firebase1=firebase.FirebaseApplication('https://hospitalmanagementsystem-edfd9.firebaseio.com/')
				result=firebase1.get('/patient',None)

				user_key_list=[]
				for i in result.keys():
					user_key_list.append(i)

				for i in user_key_list:
					if result[i]['username'] == self.user_username:
						firebase1=firebase.FirebaseApplication('https://hospitalmanagementsystem-edfd9.firebaseio.com/')
						result=firebase1.patch('/patient/'+i,{
							"file_number":i
						})

class Patient:
	def searchPatient(self,mobileNumber):
		self.patient_mobile_number=mobileNumber
		
		firebase1=firebase.FirebaseApplication('https://hospitalmanagementsystem-edfd9.firebaseio.com/')
		result=firebase1.get('/patient',None)
		user_key_list=[]

		for i in result.keys():
			user_key_list.append(i)

		for i in user_key_list:
			if result[i]['mobile_number'] == self.patient_mobile_number:
				print("Name: "+result[i]['name'])
				print("Phone Number: "+result[i]['mobile_number'])
				print("File Number: "+i)
				print("Insurance: "+result[i]['insurance'])
				print("Address: "+result[i]['address'])
				print("Appointments: "+str(result[i]['appointments_count']))
				if result[i]['appointments_count'] > 0:
					pass

				break

class AddDoctor:
	def __init__(self,doctor_username,doctor_password,doctor_name,doctor_phone_number,doctor_hospital,doctor_department,doctor_aadhar_number):
		self.user_username=doctor_username
		self.user_password=doctor_password
		self.user_name=doctor_name
		self.user_number=doctor_phone_number
		self.user_hospital=doctor_hospital
		self.user_department=doctor_department
		self.user_aadhar_number=doctor_aadhar_number

		firebase1=firebase.FirebaseApplication('https://hospitalmanagementsystem-edfd9.firebaseio.com/')
		result=firebase1.get('/doctor',None)

		user_key_list=[]
		if not result.keys():
			firebase1=firebase.FirebaseApplication('https://hospitalmanagementsystem-edfd9.firebaseio.com/')
			result=firebase1.post('/doctor',{
				"username":self.user_username,
				"password":self.user_password,
				"name":self.user_name,
				"mobile_number":self.user_number,
				"hospital":self.user_hospital,
				"appointments_count":0,
				"department":self.user_department,
				"aadhar_number":self.user_aadhar_number
			})

		
			firebase1=firebase.FirebaseApplication('https://hospitalmanagementsystem-edfd9.firebaseio.com/')
			result=firebase1.get('/doctor',None)
			user_key_list=[]
			for i in result.keys():
				user_key_list.append(i)

			for i in user_key_list:
				if result[i]['username'] == self.user_username:
					firebase1=firebase.FirebaseApplication('https://hospitalmanagementsystem-edfd9.firebaseio.com/')
					result=firebase1.patch('/doctor/'+i,{
						"employee_number":i
					})
			
		else:
			for i in result.keys():
				user_key_list.append(i)
			flag=0
			for i in user_key_list:
				if result[i]['username']== self.user_username:
					print("Username exists")
					flag=1
					break
			if flag == 0:
				firebase1=firebase.FirebaseApplication('https://hospitalmanagementsystem-edfd9.firebaseio.com/')
				result=firebase1.post('/doctor',{
				"username":self.user_username,
				"password":self.user_password,
				"name":self.user_name,
				"mobile_number":self.user_number,
				"hospital":self.user_hospital,
				"appointments_count":0,
				"department":self.user_department,
				"aadhar_number":self.user_aadhar_number	
				})

				firebase1=firebase.FirebaseApplication('https://hospitalmanagementsystem-edfd9.firebaseio.com/')
				result=firebase1.get('/patient',None)

				user_key_list=[]
				for i in result.keys():
					user_key_list.append(i)

				for i in user_key_list:
					if result[i]['username'] == self.user_username:
						firebase1=firebase.FirebaseApplication('https://hospitalmanagementsystem-edfd9.firebaseio.com/')
						result=firebase1.patch('/doctor/'+i,{
							"employee_number":i
						})


class Doctor:
	def searchDoctor(self,mobileNumber):
		self.doctor_mobile_number=mobileNumber
		firebase1=firebase.FirebaseApplication('https://hospitalmanagementsystem-edfd9.firebaseio.com/')
		result=firebase1.get('/doctor',None)
		user_key_list=[]

		for i in result.keys():
			user_key_list.append(i)

		for i in user_key_list:
			if result[i]['mobile_number'] == self.doctor_mobile_number:
				print("Name: "+result[i]['name'])
				print("Phone Number: "+result[i]['mobile_number'])
				print("Employee Number: "+i)
				print("Hospital: "+result[i]['hospital'])
				print("Department: "+result[i]['department'])
				print("Appointments: "+str(result[i]['appointments_count']))
				print("Aadhar Number: "+result[i]['aadhar_number'])

				if result[i]['appointments_count'] > 0:
					pass

				break




createpatient=CreatePatient("aimananees","aiman","Aiman Abdullah Anees","7760566874","Bupa Life Insurance","Hyderabad")
patient=Patient()
patient.searchPatient('7760566874')
doctor=AddDoctor("draiman","aiman","DrAiman Abdullah Anees","7760566874","Oak Crest Hospital","Cardiology","100000501")
doctor1=Doctor()
doctor1.searchDoctor('7760566874')










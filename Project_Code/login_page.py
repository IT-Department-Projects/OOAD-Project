from firebase import firebase

class CreatePatient:
	def __init__(self,patient_username,patient_password,patient_name,patient_phone_number,patient_insurance,patient_address):
		self.user_username=patient_username
		self.user_password=patient_password
		self.user_name=patient_name
		self.user_number=patient_phone_number
		self.user_insurance=patient_insurance
		self.user_address=patient_address

		#firebase1=firebase.FirebaseApplication('https://hospitalmanagementsystem-edfd9.firebaseio.com/')
		#result=firebase1.get('/patient',None)

		user_key_list=[]
		if 1 == 1:
			firebase1=firebase.FirebaseApplication('https://hospitalmanagementsystem-edfd9.firebaseio.com/')
			result=firebase1.post('/patient',{
				"username":self.user_username,
				"password":self.user_password,
				"name":self.user_name,
				"mobile_number":self.user_number,
				"insurance":self.user_insurance,
				"address":self.user_address,
				"file_number":0
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
					"address":self.user_address
				})

				firebase1=firebase.FirebaseApplication('https://hospitalmanagementsystem-edfd9.firebaseio.com/')
				result=firebase1.get('/patient',None)

				user_key_list=[]
				for i in result.keys():
					user_key_list.append(i)

				for i in user_key_list:
					if result[i]['username'] == self.user_username:
						firebase1=firebase.FirebaseApplication('https://hospitalmanagementsystem-edfd9.firebaseio.com/')
						result=firebase1.post('/patient/'+i,{
							"file_number":i
						})



createpatient=CreatePatient("aimananees","aiman","Aiman Abdullah Anees","7760566874","Bupa Life Insurance","Hyderabad")









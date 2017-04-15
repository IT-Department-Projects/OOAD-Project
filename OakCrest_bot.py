import telepot
from pprint import pprint
import time
import requests
import json
from firebase import firebase


bot = telepot.Bot('368306790:AAHn0VEXIK5c5hNtE7S1bC10okdBEIzEOdE')
def handle(msg):
    #chat_id is an unique identifier for the bot user
    content_type, chat_type, chat_id = telepot.glance(msg)
    if content_type == 'text':
        pprint(msg)

        inp = msg['text']
        inp = inp.split()
        
        if len(inp) == 1:
            request_type=inp[0]
            if request_type == "1":
                doctor_key_list=[]
                doctor_max_appointments_dict={}
                doctor_max_appointments_list=[]
                #FIREBASE GET Request
                firebase1=firebase.FirebaseApplication('https://hospitalmanagementsystem-edfd9.firebaseio.com/')
                result=firebase1.get('/doctors',None)
                for i in result.keys():
                    doctor_key_list.append(i)
                
                for i in doctor_key_list:
                    doctor_max_appointments_dict[result[i]["name"]]=result[i]["appointments"]
                    

                doctor_max_appointments_list=sorted(doctor_max_appointments_dict.items(), key=lambda x: x[1])
                print doctor_max_appointments_list[-1][0]
                print doctor_max_appointments_dict
        
                j=-1
                for i in xrange(0,3):
                    bot.sendMessage(chat_id,"/"+str(doctor_max_appointments_list[j][0]))
                    j=j-1
                #Clearing the lists and dictionaries
                doctor_key_list=[]
                doctor_max_appointments_dict={}
                doctor_max_appointments_list=[]
                

            elif request_type[0:3] == "/Dr":
                request_type=request_type.split('/')
                print request_type[1]
                firebase1=firebase.FirebaseApplication('https://hospitalmanagementsystem-edfd9.firebaseio.com/')
                result=firebase1.get('/doctors',None)
                for i in result.keys():
                    if result[i]['name'] == request_type[1]:
                        bot.sendMessage(chat_id,"Department: "+str(result[i]['department']))
                        bot.sendMessage(chat_id,"Hospital: "+str(result[i]['hospital']))

            elif request_type == "4":
                bot.sendMessage(chat_id,"Please enter Patient's mobile number: ")
            
            elif len(request_type) ==10:
                firebase1=firebase.FirebaseApplication('https://hospitalmanagementsystem-edfd9.firebaseio.com/')
                result=firebase1.get('/patients_info',None)
                flag=0
                flag1=0
                for i in result.keys():
                    if result[i]['phone'] == str(request_type):
                        bot.sendMessage(chat_id,"Name: "+str(result[i]['name']))
                        bot.sendMessage(chat_id,"File Number: "+str(result[i]['file_number']))
                        bot.sendMessage(chat_id,"Insurance: "+str(result[i]['insurance']))
                        bot.sendMessage(chat_id,"Username: "+str(result[i]['username']))
                        bot.sendMessage(chat_id,"Address: "+str(result[i]['address']))
                        flag=1
                result1=firebase1.get('/doctors_info',None)
                for i in result1.keys():
                    if result1[i]['phone'] == str(request_type):
                        bot.sendMessage(chat_id,"Name: "+str(result1[i]['name']))
                        bot.sendMessage(chat_id,"Employee ID: "+str(result1[i]['employee_id']))
                        bot.sendMessage(chat_id,"Hospital: "+str(result1[i]['hospital']))
                        bot.sendMessage(chat_id,"Department: "+str(result1[i]['department']))
                        bot.sendMessage(chat_id,"Username: "+str(result1[i]['username']))
                        flag1=1
            
            
                if flag == 0 and flag1 == 0:
                    bot.sendMessage(chat_id,"File does not exist")

            elif request_type == "2":
                hospital_key_list=[]
                hospital_max_crowd_dict={}
                hospital_max_crowd_list=[]
                #FIREBASE GET Request
                firebase1=firebase.FirebaseApplication('https://hospitalmanagementsystem-edfd9.firebaseio.com/')
                result=firebase1.get('/hospitals',None)
                for i in result.keys():
                    hospital_key_list.append(i)
                
                for i in hospital_key_list:
                    hospital_max_crowd_dict[result[i]["name"]]=result[i]["crowd"]
                    

                hospital_max_crowd_list=sorted(hospital_max_crowd_dict.items(), key=lambda x: x[1])
            
                j=-1
                for i in xrange(0,3):
                    bot.sendMessage(chat_id,str(hospital_max_crowd_list[j][0]))
                    j=j-1
                #Clearing the lists and dictionaries
                hospital_key_list=[]
                hospital_max_crowd_dict={}
                hospital_max_crowd_list=[]

            elif request_type == "3":
                bot.sendMessage(chat_id,"Please enter Doctor's mobile number: ")

            elif request_type.lower() == "hello" or request_type.lower() == "hi" or request_type == "/start start" or request_type == "/start" :
                bot.sendMessage(chat_id,"Hello "+str(msg['from']['first_name'])+"! How can I help you today?\nPlease enter a number from 1-4 for the following options:\n1. Top three doctors of the week\n2. Top three hospitals of the week\n3. Doctor Info\n4. Patient Info")

            elif request_type == "/start":
                pass

            else:
                bot.sendMessage(chat_id,"Oops, I didn't get that.")




        
bot.message_loop(handle)
print ('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)

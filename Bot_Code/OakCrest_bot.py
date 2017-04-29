import telepot
from pprint import pprint
import time
import requests
import json
from firebase import firebase


bot = telepot.Bot('368306790:AAHn0VEXIK5c5hNtE7S1bC10okdBEIzEOdE')
condition_request_type=""

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
                bot.sendMessage(chat_id,"Please enter Patient's Email ID: ")
                global condition_request_type
                condition_request_type=request_type


            elif "@" in request_type:
                email_extractor=request_type
                newstr = email_extractor.replace(".", "")

                if condition_request_type == "1":    
                    appointment_key_list=[]
                    firebase1=firebase.FirebaseApplication('https://hospitalmanagementsystem-edfd9.firebaseio.com/')
                    result=firebase1.get('/'+newstr,None)
                    for i in result.keys():
                        appointment_key_list.append(i)

                    bot.sendMessage(chat_id,"Name: "+str(result[appointment_key_list[0]]["patientName"]))
                    bot.sendMessage(chat_id,"File Number: "+str(result[appointment_key_list[0]]["patient_file_number"]))
                    bot.sendPhoto(chat_id=chat_id, photo=str(result[appointment_key_list[0]]["patientImage"]))

                    for i in appointment_key_list:
                        bot.sendMessage(chat_id,"Doctor Name: "+str(result[i]["doctorName"]))
                        bot.sendPhoto(chat_id=chat_id, photo=str(result[i]["doctorImage"]))
                        bot.sendMessage(chat_id,"Time: "+str(result[i]["time"]))

                elif condition_request_type == "2":
                    schedule_key_list=[]
                    firebase1=firebase.FirebaseApplication('https://hospitalmanagementsystem-edfd9.firebaseio.com/')
                    result=firebase1.get('/'+newstr,None)
                    for i in result.keys():
                        schedule_key_list.append(i)

                    bot.sendMessage(chat_id,"Doctor Name: "+str(result[schedule_key_list[0]]["doctorName"]))
                    bot.sendPhoto(chat_id=chat_id, photo=str(result[schedule_key_list[0]]["doctorImage"]))

                    for i in schedule_key_list:
                        bot.sendMessage(chat_id,"Patient Name: "+str(result[i]["patientName"]))
                        bot.sendPhoto(chat_id=chat_id, photo=str(result[i]["patientImage"]))
                        bot.sendMessage(chat_id,"Time: "+str(result[i]["time"]))

            elif request_type == "4":
                bot.sendMessage(chat_id,"Please enter Patient's mobile number: ")
                global condition_request_type
                condition_request_type=request_type
            
            elif len(request_type) ==10:
                flag=0
                if condition_request_type == "3":
                    firebase1=firebase.FirebaseApplication('https://hospitalmanagementsystem-edfd9.firebaseio.com/')
                    result=firebase1.get('/doctors_info',None)
                    for i in result.keys():
                        if result[i]['phone'] == str(request_type):
                            bot.sendPhoto(chat_id=chat_id, photo=str(result[i]["image_url"]))
                            bot.sendMessage(chat_id,"Name: "+str(result[i]['name']))
                            bot.sendMessage(chat_id,"Employee ID: "+str(result[i]['employee_id']))
                            bot.sendMessage(chat_id,"Hospital: "+str(result[i]['hospital']))
                            bot.sendMessage(chat_id,"Department: "+str(result[i]['department']))
                            bot.sendMessage(chat_id,"Username: "+str(result[i]['username']))
                            flag=1

                elif condition_request_type == "4":
                    firebase1=firebase.FirebaseApplication('https://hospitalmanagementsystem-edfd9.firebaseio.com/')
                    result=firebase1.get('/patients_info',None)
                    for i in result.keys():
                        if result[i]['phone'] == str(request_type):
                            bot.sendPhoto(chat_id=chat_id, photo=str(result[i]["image_url"]))
                            bot.sendMessage(chat_id,"Name: "+str(result[i]['name']))
                            bot.sendMessage(chat_id,"File Number: "+str(result[i]['file_number']))
                            bot.sendMessage(chat_id,"Insurance: "+str(result[i]['insurance']))
                            bot.sendMessage(chat_id,"Username: "+str(result[i]['username']))
                            bot.sendMessage(chat_id,"Address: "+str(result[i]['address']))
                            flag=1

                if flag == 0:
                    bot.sendMessage(chat_id,"File does not exist")

            elif request_type == "2":
                bot.sendMessage(chat_id,"Please enter Doctor's Email ID: ")
                global condition_request_type
                condition_request_type=request_type

            elif request_type == "3":
                bot.sendMessage(chat_id,"Please enter Doctor's mobile number: ")
                global condition_request_type
                condition_request_type=request_type

            elif request_type.lower() == "hello" or request_type.lower() == "hi":
                bot.sendMessage(chat_id,"Hello "+str(msg['from']['first_name'])+"! How can I help you today?\nPlease enter a number from 1-4 for the following options:\n1. Appointments\n2. Doctor's Schedule\n3. Doctor Info\n4. Patient Info")

            elif request_type.lower() == "thanks" or request_type.lower() == "thnx":
                bot.sendMessage(chat_id,"You're welcome.")

            else:
                bot.sendMessage(chat_id,"Oops, I didn't get that.")




        
bot.message_loop(handle)
print ('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)

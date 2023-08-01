#################################################################################################
######################## VOICE ASSISTANT PROJECT BASED LEARNING PROJECT #########################
#################################################################################################

import imp

from platform import uname_result
from matplotlib.animation import MovieWriter
from numpy import take

import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import sys
from pywikihow import search_wikihow
from pywikihow import RandomHowTo
import requests
from bs4 import BeautifulSoup
import json
import time
import random
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak(date)
    speak(month)
    speak(year)
    print(date, month, year)

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning sir!")
        print("Good Morning sir!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon sir!")
        print("Good Afternoon sir!")
    else:
        speak("Good Evening sir!")
        print("Good Evening sir!")
    speak("the current date is")
    date()
    speak("Please tell me how may I help you")
    print("Please tell me how may I help you")

def takeCommand():
    #It takes microphone input from the user and returns string output
    print("GIVE COMMAND")
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.7
        audio = r.listen(source)
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please...")    
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('projectbasedlearning51@gmail.com', 'projectbasedlearninghai')
    server.sendmail('projectbasedlearning51@gmail.com', to, content)
    server.close()

def wikipediaMethod(query):
    speak('Searching Wikipedia...')
    query = query.replace("wikipedia", "")
    results = wikipedia.summary(query, sentences=3)
    speak("According to Wikipedia")
    print(results)
    speak(results)

def openWeb(webName):
    webbrowser.open(webName)
    speak("opening "+webName)
    print("opening "+webName)

def sendMail():
    mail=input()
    speak("What should I say?")
    content = takeCommand()
    sendEmail(mail, content)
    speak("Email has been sent!")
    print("Email has been sent!")

def howToDo():
    speak("how to do mode is activated")
    while True:
        speak("please tell me what you want to know")
        print("Please tell me what you want to know")
        how = takeCommand()
        try:
            if"exit" in how or "close" in how:
                speak("ok sir how to do mode is closed")
                print("Ok sir, How to do mode is closed")
                break
            else:
                max_results = 1
                how_to = search_wikihow(how, max_results)
                assert len(how_to) == 1
                speak("This is your result: ")
                how_to[0].print()
                # speak(how_to[0].summary)
                time.sleep(10)
        except Exception as e:
            speak("sorry sir i am unable to find this")
            

def temperature():
    try:
        search = "my location"
        url1 = f"https://www.google.com/search?query={search}"
        r1 = requests.get(url1)
        data1 = BeautifulSoup(r1.text, "html.parser")
        location = data1.find("div", class_="BNeawe").text
        search_temp = "temperature in " + location
        url2 = f"https://www.google.com/search?query={search_temp}"
        r2 = requests.get(url2)
        data2 = BeautifulSoup(r2.text, "html.parser")
        temp = data2.find("div", class_="BNeawe").text
        speak(f"current temperature of {location} is {temp}")
        print(f"current temperature of {location} is {temp}")
        
    except Exception as e:
        speak("Sorry sir I am unable to find this.")
        print("Sorry sir I am unable to find this.")
        
        
def meaningMode():
    while True:
        speak("Which word do you want meaning of?")
        word_to_search = takeCommand().lower()
        if word_to_search=='exit':
            speak("Exiting meaning mode  ")
            print("Exiting meaning mode :")
            break
        try:
            url1 = f"https://www.google.com/search?query={word_to_search} meaning"
            r1 = requests.get(url1)
            data1 = BeautifulSoup(r1.text, "html.parser")
            word_retreived = data1.find("div", class_="BNeawe" ).text
            meaning = data1.find("div", class_="BNeawe s3v9rd AP7Wnd").text
            word2 = word_retreived[1::]
            if word2 == word_to_search and len(word_to_search) != 0:
                meaning = data1.find("div", class_="BNeawe s3v9rd AP7Wnd").text
                print(word2)
                print(meaning.partition(".")[0].partition(" ")[2])
                speak(meaning.partition(".")[0].partition(" ")[2])
            else:
                print("Invalid word")
        except Exception as e:
            speak("Sorry sir I am unable to find this.")
            print("Sorry sir I am unable to find this.")

#################################################################################################
################################## MAIN FUNCTION OF THE CODE ####################################
#################################################################################################
           
if __name__ =="__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            try:
                wikipediaMethod(query)
            except Exception as e:
                print(e)
                speak("sorry sir i am unable to perform this task")
        elif 'open youtube' in query:
            try:
                openWeb('youtube')
            except Exception as e:
                print(e)
                speak("sorry sir i am unable to perform this task")
        elif 'open google' in query:
            try:
                openWeb('google')
            except Exception as e:
                print(e)
                speak("sorry sir i am unable to perform this task")
        elif 'open stack overflow' in query:
            try:
                openWeb('stackoverflow')
            except Exception as e:
                print(e)
                speak("sorry sir i am unable to perform this task")
        elif 'open facebook' in query:
            try:
                openWeb('facebook')
            except Exception as e:
                print(e)
                speak("sorry sir i am unable to perform this task")
        elif 'open instagram' in query:
            try:
                openWeb('instagram')
            except Exception as e:
                print(e)
                speak("sorry sir i am unable to perform this task")
        elif 'open twitter' in query:
            try:
                openWeb('twitter')
            except Exception as e:
                print(e)
                speak("sorry sir i am unable to perform this task")
        elif "send email" in query:
            
            speak("Enter enter the email id of the acount you want to send message : ")
            try:
                sendMail()
            except Exception as e:
                print(e)
                speak("sorry sir i am unable to send email")
        elif "activate how to do mode" in query:
            howToDo()
        elif "temperature" in query:
            temperature()
        elif "meaning mode" in query:
            meaningMode()
        elif 'who are you' in query:
            speak("I am your voice assistant I can perform various tasks , and I am always there for you")
            print("I am your voice assistant I can perform various tasks , and I am always there for you")
        elif 'what tasks can you perform' in query:
            speak("I can open various applications , send email ,search web and many more ")
            print("I can open various applications , send email ,search web and many more ")
        elif "play music" in query:
            try:
                codePath = "D:\\Music"
                path = "D:\\Music\\"
                folder = os.listdir(codePath)
                song = random.choice(folder)
                speak("playing music")
                print("playing music")
                os.startfile(path + song)
            except Exception as e:
                print(e)
                speak("Error"+e)
        elif "play movie" in query:
            try:
                codePath = "D:\\Movies"
                path = "D:\\Movies\\"
                movie_list = os.listdir(codePath)
                print(movie_list)
                for i in range(len(movie_list)):
                    print(f"{i+1} + {movie_list[i]}")
                movie_index = int(input("Enter the movie number:"))
                movie_name = movie_list[movie_index-1]
                speak("playing movie")
                print("playing movie")
                os.startfile(path + movie_name)
            except Exception as e:
                print(e)
                speak("Error"+e)
        elif "open notepad" in query:
            try:
                codePath = "C:\\Program Files\\Notepad++\\notepad++.exe"
                speak("opening notepad")
                print("opening notepad")
                os.startfile(codePath)
            except Exception as e:
                print(e)
                speak("Error" + e)
        elif "open code" in query:
            try:
                codePath = "C:\\Users\\Hitesh\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                speak("opening vs code")
                print("opening VS code")
                os.startfile(codePath)
            except Exception as e:
                print(e)
                speak("Error"+e)
        elif "ok quit" in query:
            speak("thanks for using me good day sir")
            print("Thanks for using me good day sir!!")
            sys.exit()
#################################################################################################
###################################### END OF THE PROJECT #######################################
#################################################################################################

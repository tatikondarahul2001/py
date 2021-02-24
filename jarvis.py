import pyttsx3 #pip install pyttsx3
import datetime #its already a built in function
import speech_recognition as sr #pip install SpeechRecognition
import wikipedia #pip install wikipedia
import smtplib #its also a built in function
import webbrowser as wb #inbuilt function
import psutil #pip install psutil
import pyjokes #pip install pyjokes
import os #it is a pre defined library
import subprocess as sp #this is a built-in library
import pyautogui as pgui #pip install pyautogui
import json #this is a built in module
import requests #this is also a built in module
from urlib3.request import urlopen #pip install urlopen 'and' pip install urllib3
import wolframalpha as wm #pip install wolframalpha

engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def time_():
    Time = datetime.datetime.now().strftime("%H:%M:%S")#for 12 hour format
    speak("the current time is ")
    speak(Time)
def date_():
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    date = datetime.datetime.now().day
    speak("the current date is ")
    speak(date)
    speak(month)
    speak(year)
def wishme():
    speak("Welcome back Rahul!")
    time_()
    date_()
    #Greetings

    hour = datetime.datetime.now().hour

    if hour>=6 and hour<=12:
        speak("Good Morning sir !")
    elif hour>=12 and hour<18:
        speak("Good Afternoon sir !")
    elif hour>=18 and hour<24:
        speak("good Evening sir !")
    else:
        speak("Good Night !")

    speak("jarvis at your service. Please tell me how can i help you today")

def TakeCommand():

    r = sr.Recognizer() #pip install PyAudio
    with sr.Microphone() as source:
        print("Listening.......")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing........")
        query = r.recognize_google(audio,language = 'en-US')
        print(query)
    except Exception as e:
        print(e)
        print("Say that again please........")
        return "None"
    return query
def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()

    #for this function , you must enable low security in your gmail which you are goint to use as sender
    server.login('20h65a1206@cvsr.ac.in','27451133415882977907706300639490321948001259')
    server.sendmail('tatikondarahul010@gmail.com',to,content)
    server.close()
def cpu():
    usage = str(psutil.cpu_percent())
    speak("CPU is at"+usage)
def joke():
    speak(pyjokes.get_joke())

    battery = psutil.sensors_battery()
    speak('Battery is at'+str(battery.percent)+'percent')
def screenshot():
    img = pgui.screenshot()
    img.save('C:/Users/RAHUL/Desktop/screenshot.png')

if __name__ == "__main__":


    while True:
        query = TakeCommand().lower()

        #All commmands will be stored in lower case in query
        #for easy recogniton
        if 'time' in query: #tell us time when asked
            time_()

        elif 'date' in query: #tell us date when asked
            date_()

        elif 'wikipedia' in query:
            speak("Searching......")
            query == query.replace('wikipedia','')
            result = wikipedia.summary(query,sentences = 3)
            speak('According to wikipedia')
            print(result)
            speak(result)

        elif 'send email' in query: #to use this you should disable less secure apps in gmail to send the mail
            try:
                speak('what should i say?')
                content = TakeCommand()
                #provide receiver email address
                speak('who is the receiver?')
                receiver = input("Enter the Receiver's Email :")
                to = receiver
                sendEmail(to,content)
                speak(content)
                speak('email has not been sent')
            except Exception as e:
                print(e)
                speak("Unable to send Email.")

        elif 'search in edge' in query:
            speak('What should i search?')
            edgepath = "C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe %s"
            #edge path where edge has been installed can be seen using properties of edge
            search = TakeCommand().lower()
            wb.get(edgepath).open_new_tab(search+'.com') #only open websites with '.com' at end.

        elif 'search in chrome' in query:
            speak('What should i search?')
            chromepath = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
            #edge path where edge has been installed can be seen using properties of edge
            search = TakeCommand().lower()
            wb.get(chromepath).open_new_tab(search+'.com') #only open websites with '.com' at end.

        elif 'youtube' in query: #from here i should check
            speak('What should i search?')
            search_Term = TakeCommand().lower()
            speak('Here We go to YOUTUBE')
            wb.open('https://www.youtube.com/results?search_query'+search_Term)

        elif 'google' in query:
            speak('What would you like to search')
            search_Term = TakeCommand().lower()
            speak('Searching.....')
            wb.open('https://www.google.com/search?q='+search_Term)

        elif 'cpu' in query:
            cpu()

        elif 'joke' in query:
            joke()

        elif 'go offline' in query:
            speak('Going offline sir')
            quit()

        elif 'word' in query:
            speak('Opening MS Word.....')
            ms_word = r"C:/Program Files/Microsoft Office/root/Office16/WINWORD.EXE"
            os.startfile(ms_word)

        elif 'notepad' in query: #from here this is an experinmental block of code sometimes it works sometimes not
            speak('Opening Notepad.....')
            sp.call('notepad.exe')

        elif 'cmd' in query:
            speak('Opening CMD.....')
            sp.call('cmd.exe')

        elif 'calculator' in query:
            speak('Opening Calculator')
            sp.call('calc.exe')

        elif 'write a note' in query:
            speak('What should I write, Sir!')
            notes = TakeCommand()
            file = open('notes.txt','w')
            speak('Sir should I Include date and time?')
            ans = TakeCommand()
            if 'yes' in ans or 'sure' in ans:
                strTime = datetime.datetime.now().strftime('%H:%M:%S')
                file.write(strTime)
                file.write(':-')
                file.write(notes)
                speak('Done taking Notes, Sir!')
            else:
                file.write(notes)

        elif 'show notes' in query:
            speak('showing notes')
            file = open('notes.txt','r')
            print(file.read())
            speak(file.read())

        elif 'screenshot' in query:
            screenshot()

        elif 'play music' in query: #i need to test after downloading songs
            songs_dir = 'path where it is stored'
            music = os.listdir(songs_dir)
            speak('What should I Play')
            ans = TakeCommand().lower()
            no =int(ans.replace('number',''))
            os.startfile(os.path.join(songs_dir,music[no]))
        
        #this is the block for music related code


        elif 'remember that' in query:
            speak('What should I remember?')
            memory = TakeCommand()
            speak('You asked me to remember that'+memory)
            remember = open('memory.txt','w')
            remember.write(memory)
            remember.close()
        
        elif 'do you remember anything' in query:
            remember = open('memory.txt','r')
            speak('You asked me to remember that'+remember.read())

        elif 'news' in query:
            try:
                jsonObj = urlopen('http://newsapi.org/v2/everything?q=bitcoin&from=2020-12-23&sortBy=publishedAt&apiKey=8889ada2c4b342e1a4b4d0660ac5c8d5')
                data = json.load(jsonObj)
                i = 1

                speak('Here are some top headline about the bitcoin')
                print('===============TOP HEADLINES======================'+'\n')
                for item in data['articles']:
                    print(str[i]+'. '+item['title']+'\n')
                    print(item['derscription']+'\n')
                    speak(item['title'])
                    i += 1

                except Exception as e:
                    print(str(e))
        
        elif 'where is' in query:
            query = query.replace('Where is','')
            location = query
            speak('Users asked to locate'+location)
            wb.open_new_tab('https://www.google.com/maps/place/'+location)

        

        



        

            





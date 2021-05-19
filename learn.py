import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import pyautogui
import ctypes
import time
import subprocess
import psutil
import random
import requests
import cv2
import pywhatkit as kit
import pyjokes
import json
import wolframalpha
from urllib.request import urlopen
from selenium import webdriver
from time import sleep
from requests import get
from newsapi import NewsApiClient

webdriver = webdriver.Chrome()

chrome_path = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

wolframalpha_app_id = 'K636RG-UYJEH55VAP'

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Maam!!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Maam!!")

    else:
        speak("Good Evening Maam!!")

    speak("Please tell me how may I help you?")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-US')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('xyz@gmail.com', 'xyzPasssword')  # sender-mail and password
    server.sendmail('abc@gmail.com', to, content)  # receiver-mail
    server.close()

def lock():
    ctypes.windll.user32.LockWorkStation()


def Search():
    speak("Which Song?")  # SELECTION OF SONG
    SearchText = takeCommand().lower()
    speak("let's go to youtube")
    webdriver.get("https://www.youtube.com/results?search_query=" + SearchText)
    sleep(2)
    # x = webdriver.find_element_by_class_name("style-scope ytd-video-renderer").click()
    x = webdriver.find_element_by_xpath("/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]/div/div[1]/div/h3/a/yt-formatted-string").click()
    sleep(2)


def City():
    speak("Which city?")
    MyText = takeCommand().lower()
    webdriver.get("https://www.weather-forecast.com/locations/" + MyText + "/forecasts/latest")
    speak(str(webdriver.find_elements_by_class_name("b-forecast__table-description-content")[0].text))
    # SpeakText(MyText)
    # print("Did you say "+MyText)

def GoglSearch():
    speak("What should i search?")  # SELECTION OF Google Search
    SearchText = takeCommand().lower()
    speak("searching")
    webbrowser.open("https://www.google.co.in/search?q="+SearchText)

def security():
    os.mkdir('Personal')
    os.chdir('Personal')
    for i in range(10):  # layer 1
        os.mkdir(str(i))
        os.chdir(str(i))
        for j in range(10):  # layer 2
            os.mkdir(str(j))
            os.chdir(str(j))
            for k in range(10):  # layer 3
                os.mkdir(str(k))
                os.chdir(str(k))
                for l in range(10):  # layer 4
                    os.mkdir(str(l))
                os.chdir('..')
            os.chdir('..')
        os.chdir('..')


def timerlock():
    # =====================================
    speak("For how many seconds?")
    seconds = int(takeCommand().lower())
    speak("timer set..")
    for i in range(seconds):
        print(str(seconds - i) + " remaining")

        time.sleep(1)
    # ==========================================

    subprocess.Popen("rundll32.exe user32.dll,LockWorkStation")
    webdriver.close()
    exit()

def shutdwm():
    # =====================================
    speak("For how many seconds?")
    seconds = int(takeCommand().lower())
    speak("timer set..")
    for i in range(seconds):
        print(str(seconds - i) + " remaining")

        time.sleep(1)
    # ==========================================
    os.system("shutdown /s /t "+str(seconds))

def joke():
    speak(pyjokes.get_joke())



def cpu():
    usage = str(psutil.cpu_percent())
    print("CPU is at:" + usage)
    speak("CPU is at:" + usage)

    battery = psutil.sensors_battery()
    print("Battery is at:" + battery.percent)
    speak("Battery is at:" + battery.percent)

if __name__ == "__main__":
    wishMe()
    while True:
        # if 1:
        query = takeCommand().lower()
        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=10)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'please exit' in query:
            speak("getting exit...")
            webdriver.close()
            exit()

        elif 'open youtube' in query:
            webbrowser.get('chrome').open("youtube.com")

        elif 'exit youtube' in query:
            webdriver.close()

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'according to google' in query:
            speak('opening google..')
            query = query.replace('according to google', '')
            webbrowser.open("http://google.com/#q=" + query, new=2)

        elif 'open facebook' in query:
            speak('opening facebook..')
            webbrowser.open("facebook.com")

        elif 'open github' in query:
            speak('opening github..')
            webbrowser.open("github.com")

        elif 'open instagram' in query:
            webbrowser.open("https://www.instagram.com")
            speak("opening instagram")

        elif 'open yahoo' in query:
            webbrowser.open("https://www.yahoo.com")
            speak("opening yahoo")

        elif 'open gmail' in query:
            webbrowser.open("https://mail.google.com")
            speak("opening google mail")

        elif 'open snapdeal' in query:
            webbrowser.open("https://www.snapdeal.com")
            speak("opening snapdeal")

        elif 'open amazon' in query or 'shop online' in query:
            webbrowser.open("https://www.amazon.com")
            speak("opening amazon")

        elif 'open flipkart' in query:
            webbrowser.open("https://www.flipkart.com")
            speak("opening flipkart")

        elif 'open ebay' in query:
            webbrowser.open("https://www.ebay.com")
            speak("opening ebay")

        elif 'open notepad' in query:
            speak("opening notepad..")
            npath = "C:\\WINDOWS\\system32\\notepad.exe"
            os.startfile(npath)

        elif 'close notepad' in query:
            speak("Closing notepad..")
            os.system("taskkill /f /im notepad.exe")

        elif 'open paint' in query:
            speak("opening paint")
            ppath = "C:\\WINDOWS\\system32\\mspaint.exe"
            os.startfile(ppath)

        elif 'open command prompt' in query or 'open cmd' in query:
            speak("opening command prompt")
            os.system("start cmd")

        elif 'tell me ip address' in query:
            speak("getting ip address..")
            ip = get('https://api.ipify.org').text
            print("Your IP address is: "+ip)
            speak(f"Your IP Address Is {ip}")

        elif 'tell me weather for few days' in query:
            City()

        elif 'play song on youtube' in query:
            Search()

        elif 'tell me a joke' in query:
            joke()

        elif 'headline for today' in query:
            try:
                jsonObj = urlopen("http://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=6df5e5eea2b341109847d1c38fefe75e")
                data = json.load(jsonObj)
                i = 1
                speak("Here are some headlines")
                print("**************************************Top Headlines*******************************************"+"\n")
                for item in data['articles']:
                    print(str(i)+'. '+item['title']+'\n')
                    print(item['description']+'\n')
                    speak(item['title'])
                    i += 1
            except Exception as e:
                print(str(e))

        elif 'news' in query:
            topic_name = query.replace('news','')
            newsapi = NewsApiClient(api_key='6df5e5eea2b341109847d1c38fefe75e')  # Add your api key
            data = newsapi.get_top_headlines(q = topic_name, country = 'in', language='en', page_size=5)

            articles = data['articles']
            # print(articles)
            if (articles == []):
                speak("No news availabe on this topic")
            else:
                for x, y in enumerate(articles):
                    print(f'{x} {y["description"]}')
                    speak(f'{x} {y["description"]}')

                speak("that's it for now i'll updating you next time ")

        elif 'take photo' in query:
            cam = cv2.VideoCapture(0)
            count = 0
            while True:
                ret, img = cam.read()
                cv2.imshow("Robo Capture",img)
                if not ret:
                    break
                k = cv2.waitKey(1)
                if k%256 == 27:
                    print("close")
                    speak("closing camera")
                    break
                elif k%256 == 32:
                    print("Image" + str(count)+"saved")
                    file = 'C:\\Users\\Mosami\\Desktop\\ai\\RoboCap'+str(count)+'.jpg'
                    cv2.imwrite(file, img)
                    count += 1

            cam.release()
            cv2.destroyAllWindows()

        elif 'where is ' in query:
            query = query.replace("where is","")
            location = query
            speak("User asked to locate"+location)
            webbrowser.open_new_tab("http://www.google.com/maps/place/"+location)

        elif 'calculate' in query:
            client = wolframalpha.Client(wolframalpha_app_id)
            indx = query.lower().split().index('calculate')
            query = query.split()[indx + 1:]
            res = client.query(''.join(query))
            answer = next(res.results).text
            print("The Answer is :"+answer)
            speak("The Answer is "+ answer)

        elif 'what is' in query or 'who is' in query:
            client = wolframalpha.Client(wolframalpha_app_id)
            res = client.query(query)

            try:
                print(next(res.results).text)
                speak(next(res.results).text)
            except StopIteration:
                print("No Result Found..")
                speak("No Result Found..")

        elif 'i want to ask' in query:
            speak('I can answer to computational and geographical questions  and what question do you want to ask now')
            question = takeCommand()
            client = wolframalpha.Client(wolframalpha_app_id)
            res = client.query(question)
            answer = next(res.results).text
            print(answer)
            speak(answer)

        elif 'stop listening' in query or 'go to sleep' in query:
            speak("For how many seconds you want me to stop listening to your commands?")
            ans = takeCommand().lower()
            while ('seconds' not in ans):
                speak("I couldn't understand you please try again")
                ans = takeCommand().lower()
            ans1 = ans.replace("seconds","")
            ans = int(ans1)
            print(ans)
            time.sleep(ans)
            speak("How are u maam? I'm back at your service...")

        elif 'shutdown immediately' in query:
            speak("shutting down")
            os.system("shutdown /s /t 0")

        elif 'shutdown after few second' in query:
            shutdwm()

        elif 'shutdown' in query:
            os.system("shutdown /s")

        elif 'log of my pc' in query:
            os.system("shutdown /l")

        elif 'restart my pc' in query:
            os.system("shutdown /r")

        elif 'sleep my pc' in query:
            os.system("rundll32.exe powrproof.dll,SetSuspendState 0,1,0")

        elif 'take screenshot' in query:
            ss = pyautogui.screenshot()
            ss.save(r'C:\\Users\\Mosami\\Desktop\\ai\\screenshot.png')
            speak("screenshot taken.....")

        elif 'open camera' in query or 'open mirror' in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k == 27:
                    break
            cap.release()
            cv2.destroyAllWindows()

        elif 'open vs code' in query:
            os.startfile('C:\\Users\\Mosami\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe')

        elif 'open twitter account' in query:
            from twitter_bot import execute

        elif 'play songs' in query:
            songs_dir = 'C:\\Users\\Mosami\\Desktop\\ai\\music'
            music = os.listdir(songs_dir)
            speak("which song should i play?")
            speak("Please select number.")
            ans = takeCommand().lower()
            while('number' not in ans):
                speak("I couldn't understand you please try again")
                ans = takeCommand().lower()
            no = int(ans.replace('number',''))
            os.startfile(os.path.join(songs_dir,music[no]))

        elif 'play random songs' in query:
            songs_dir = 'C:\\Users\\Mosami\\Desktop\\ai\\music'
            music = os.listdir(songs_dir)
            no = random.randint(1,4)
            speak("Playing song..")
            os.startfile(os.path.join(songs_dir, music[no]))


        elif 'play music' in query:
            music_dir = 'C:\\Users\\Mosami\\Desktop\\ai\\music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'play video' in query:
            speak("ok i am playing videos")
            video_dir = 'C:\\Users\\Mosami\\Desktop\\ai\\video'
            videos = os.listdir(video_dir)
            print(videos)
            os.startfile(os.path.join(video_dir, videos[0]))

        elif 'play particular video' in query:
            video_dir = 'C:\\Users\\Mosami\\Desktop\\ai\\video'
            videos = os.listdir(video_dir)
            speak("which song should i play?")
            speak("Please select number.")
            ans = takeCommand().lower()
            while('number' not in ans):
                speak("I couldn't understand you please try again")
                ans = takeCommand().lower()
            no = int(ans.replace('number',''))
            os.startfile(os.path.join(video_dir,videos[no]))

        elif 'song mode' in query or 'movie mode' in query or 'video mode' in query or 'audio mode' in query:

            video = 'C:\\Users\\Mosami\\Desktop\\ai\\video'

            audio = 'C:\\Users\\Mosami\\Desktop\\ai\\music'

            if 'song mode' in query or 'audio mode' in query:

                songs_dir = audio

                songs = os.listdir(songs_dir)

                print(songs)

            elif 'movie mode' in query or 'video mode' in query:

                songs_dir = video

                songs = os.listdir(songs_dir)

                print(songs)

            speak("select a random number")

            rand = takeCommand().lower()

            while('number' in rand or rand == 'random'):
                if 'number' in rand:

                    rand1 = int(rand.replace('number', ''))

                    os.startfile(os.path.join(songs_dir, songs[rand1]))

                elif 'random' in rand:

                    rand = random.randint(0, 5)

                    os.startfile(os.path.join(songs_dir, songs[rand]))

                    continue

                elif 'please exit' in rand:
                    continue

        elif 'tell me time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"Sir, the time is {strTime}")

        elif 'tell me date' in query:
            year = int(datetime.datetime.now().year)
            month = int(datetime.datetime.now().month)
            date = int(datetime.datetime.now().day)
            speak("the current Date is")
            speak(date)
            speak(month)
            speak(year)

        elif 'set alarm' in query:
            setalm = takeCommand()
            print(setalm)
            tt = ''
            while(tt != setalm):
                hr = datetime.datetime.now().hour
                mn = datetime.datetime.now().minute
                tt = hr + mn
            alarm_dir = 'C:\\Users\\Mosami\\Desktop\\ai\\music'
            songs = os.listdir(alarm_dir)
            os.startfile(os.path.join(alarm_dir, songs[0]))

        elif 'make security folder' in query:
            security()
            speak("security folder is made.")

        elif 'open my secure folder' in query:
            speak("Please enter your pin?")
            pina = input()
            pinb = input()
            pinc = input()
            pind = input()
            os.startfile("C:\\Users\\Mosami\\Desktop\\ai\\personal\\"+pina+"\\"+pinb+"\\"+pinc+"\\"+pind)

        elif 'email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "abc@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend. I am not able to send this email")

        elif 'search in chrome' in query:
            speak('what should i search?')
            search = takeCommand().lower()
            webbrowser.get('chrome').open_new_tab(search+'.com')

        elif 'send message in whatsapp' in query:
            speak('please speak number.')
            num = takeCommand()
            sendernum = "+91" + num
            speak("what is the message")
            msg = takeCommand()
            print("Did u said: "+msg)
            kit.sendwhatmsg(sendernum,msg,2,25)

        elif 'on youtube' in query:
            song_name = query.replace('on youtube','')
            song_name = song_name.replace('play','')
            kit.playonyt(song_name)

        elif 'search in google' in query:
            GoglSearch()

        elif 'lock my pc after few second' in query:
            timerlock()

        elif 'lock right now' in query:
            lock()

        elif 'battery and cpu usage' in query:
            cpu()

        elif 'open word' in query:
            speak("Opening MS Word.....")
            ms_word = r''
            os.startfile()

        elif 'write a note' in query:
            speak(" What Should I Write, Sir?")
            notes = takeCommand()
            file = open('notes.txt','w')
            speak("Sir Should I include Date and Time?")
            ans = takeCommand().lower()
            if 'yes' in ans and 'sure' in ans:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                file.write(strTime)
                file.write(':-')
                file.write(notes)
                speak('Done Taking Notes')
            else:
                file.write(notes)

        elif 'please read notes' in query:
            speak("Reading Notes")
            file = open('notes.txt','r')
            print(file.read())
            speak(file.read())

        elif 'remember that' in query:
            speak("What should I remember?")
            data = takeCommand()
            speak("you said me to remember that" + data)
            remember = open('remember.txt', 'w')
            remember.write(data)
            remember.close()

        elif 'do you know anything' in query:
            remember = open('remember.txt', 'r')
            speak("you said me to remember that" + remember.read())

        elif 'how is the weather' and 'weather' in query:

            url = 'https://api.openweathermap.org/'  # Open api link here

            res = requests.get(url)

            data = res.json()

            weather = data['weather'][0]['main']
            temp = data['main']['temp']
            wind_speed = data['wind']['speed']

            latitude = data['coord']['lat']
            longitude = data['coord']['lon']

            description = data['weather'][0]['description']
            speak('Temperature : {} degree celcius'.format(temp))
            print('Wind Speed : {} m/s'.format(wind_speed))
            print('Latitude : {}'.format(latitude))
            print('Longitude : {}'.format(longitude))
            print('Description : {}'.format(description))
            print('weather is: {} '.format(weather))
            speak('weather is : {} '.format(weather))

        elif 'open' in query:
            os.system('explorer C://{}'.format(query.replace('Open', '')))

        elif "what\'s up" in query or 'how are you' in query:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy','i am okey ! How are you']
            ans_q = random.choice(stMsgs)
            speak(ans_q)
            ans_take_from_user_how_are_you = takeCommand().lower()
            if 'fine' in ans_take_from_user_how_are_you or 'happy' in ans_take_from_user_how_are_you or 'okey' in ans_take_from_user_how_are_you:
                speak('okey..')
            elif 'not' in ans_take_from_user_how_are_you or 'sad' in ans_take_from_user_how_are_you or 'upset' in ans_take_from_user_how_are_you:
                speak('oh sorry..')

        elif 'make you' in query or 'created you' in query or 'develop you' in query:
            ans_m = " For your information Mosami Patel Created me ! I give Lot of Thanks to Her "
            print(ans_m)
            speak(ans_m)

        elif "who are you" in query or "about you" in query or "your details" in query:
            about = "I am Learny an A I based computer program but i can help you lot like a your close friend ! i promise you ! Simple try me to give simple command ! like playing music or video from your directory i also play video and song from web or online ! i can also entain you i so think you Understand me ! ok Lets Start "
            print(about)
            speak(about)

        elif "hello" in query or "hello learny" in query:
            hel = "Hello maam ! How May i Help you.."
            print(hel)
            speak(hel)

        elif "your name" in query or "sweat name" in query:
            na_me = "Thanks for Asking my name my self ! Learny"
            print(na_me)
            speak(na_me)

        elif "you feeling" in query:
            print("feeling Very sweet after meeting with you")
            speak("feeling Very sweet after meeting with you")

        elif "thank you" in query:
            print("Don't mind your always welcome")
            speak("Don't mind your always welcome")

        elif query == 'none':
            continue

        elif 'exit' in query or 'abort' in query or 'stop' in query or 'bye' in query or 'quit' in query:
            ex_exit = 'I feeling very sweet after meeting with you but you are going! i am very sad'
            speak(ex_exit)
            exit()

        else:
            temp = query.replace(' ', '+')
            g_url = "https://www.google.com/search?q="
            res_g = 'sorry! i cant understand but i search from internet to give your answer ! okay'
            print(res_g)
            speak(res_g)
            webbrowser.open(g_url + temp)
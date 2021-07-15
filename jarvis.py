from tkinter import *
import requests
import json
import re
import threading
import time
import cv2
import PIL.Image
import PIL.ImageTk
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import smtplib
import roman
#from Class1 import Student
#import pytesseract
from PIL import Image

#pytesseract.pytesseract.tesseract_cmd = r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Tesseract-OCR\tesseract.exe"


API_KEY = "tbsCZgbVo_uB"
PROJECT_TOKEN = "tyLOv_-3HJ13"
RUN_TOKEN = "t2JEDsRTaz9s"



numbers = {'hundred': 100, 'thousand': 1000, 'lakh': 100000}
a = {'name': 'your email'}
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

window = Tk()
global var
global var1

var = StringVar()
var1 = StringVar()


def speak(audio):
	engine.say(audio)
	engine.runAndWait()


def sendemail(to, content):
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.ehlo()
	server.starttls()
	# email id - use any email id whose security/privacy is off
	server.login('email id', 'password')
	server.sendmail('email id', to, content)
	server.close()


def wishme():
	hour = int(datetime.datetime.now().hour)
	if hour >= 0 and hour <= 12:
		var.set("Good Morning YASH")  # Name - your Name
		window.update()
		speak("Good Morning YASH!")
	elif hour >= 12 and hour <= 18:
		var.set("Good Afternoon YASH!")
		window.update()
		speak("Good Afternoon YASH!")
	else:
		var.set("Good Evening YASH")
		window.update()
		speak("Good Evening YASH!")
	speak("Whatsup ")  # BotName - Give a name to your assistant


def takeCommand():
	r = sr.Recognizer()
	with sr.Microphone() as source:
		var.set("Listening...")
		window.update()
		print("Listening...")
		r.pause_threshold = 1
		r.energy_threshold = 400
		audio = r.listen(source)
	try:
		var.set("Recognizing...")
		window.update()
		print("Recognizing")
		query = r.recognize_google(audio, language='en-in')
	except Exception as e:
		return "None"
	var1.set(query)
	window.update()
	return query

def get_audio():
	r = sr.Recognizer()
	with sr.Microphone() as source:
		audio = r.listen(source)
		said = ""

		try:
			said = r.recognize_google(audio)
		except Exception as e:
			print("Exception:", str(e))

	return said.lower()


def play():
	btn2['state'] = 'disabled'
	btn0['state'] = 'disabled'
	btn1.configure(bg='orange')
	wishme()
	while True:
		btn1.configure(bg='orange')
		query = takeCommand().lower()
		if 'exit' in query:
			var.set("Bye sir")
			btn1.configure(bg='#5C85FB')
			btn2['state'] = 'normal'
			btn0['state'] = 'normal'
			window.update()
			speak("Bye sir")
			break

		elif 'wikipedia' in query:
			if 'open wikipedia' in query:
				webbrowser.open('wikipedia.com')
			else:
				try:
					speak("searching wikipedia")
					query = query.replace("according to wikipedia", "")
					results = wikipedia.summary(query, sentences=2)
					speak("According to wikipedia")
					var.set(results)
					window.update()
					speak(results)
				except Exception as e:
					var.set('sorry sir could not find any results')
					window.update()
					speak('sorry sir could not find any results')

		elif 'open youtube' in query:
			var.set('opening Youtube')
			window.update()
			speak('opening Youtube')
			webbrowser.open("youtube.com")

		elif 'open course error' in query:
			var.set('opening course era')
			window.update()
			speak('opening course era')
			webbrowser.open("coursera.com")

		elif 'open google' in query:
			var.set('opening google')
			window.update()
			speak('opening google')
			webbrowser.open("google.com")

		elif 'hello' in query:
			var.set('Hello Sir')
			window.update()
			speak("Hello Sir")

		elif 'open stackoverflow' in query:
			var.set('opening stackoverflow')
			window.update()
			speak('opening stackoverflow')
			webbrowser.open('stackoverflow.com')

		elif ('play music' in query) or ('change music' in query):
			var.set('Here are your favorites')
			window.update()
			speak('Here are your favorites')
			music_dir = 'D:\My Music\Favourites'  # Enter the Path of Music Library
			songs = os.listdir(music_dir)
			n = random.randint(0, 27)
			os.startfile(os.path.join(music_dir, songs[n]))

		elif 'the time' in query:
			strtime = datetime.datetime.now().strftime("%H:%M:%S")
			var.set("Sir the time is %s" % strtime)
			window.update()
			speak("Sir the time is %s" % strtime)

		elif 'the date' in query:
			strdate = datetime.datetime.today().strftime("%d %m %y")
			var.set("Sir today's date is %s" % strdate)
			window.update()
			speak("Sir today's date is %s" % strdate)

		elif 'thank you' in query:
			var.set("Welcome Sir")
			window.update()
			speak("Welcome Sir")

		elif 'can you do for me' in query:
			var.set(
				'I can do multiple tasks for you sir. tell me whatever you want to perform sir')
			window.update()
			speak(
				'I can do multiple tasks for you sir. tell me whatever you want to perform sir')

		elif 'old are you' in query:
			var.set("I am a little baby sir")
			window.update()
			speak("I am a little baby sir")

		elif 'open media player' in query:
			var.set("opening VLC media Player")
			window.update()
			speak("opening V L C media player")
			# Enter the correct Path according to your system
			path = "C:\\Program Files\\VideoLAN\\VLC\\vlc.exe"
			os.startfile(path)

		elif 'your name' in query:
			var.set("Myself Jarvis Sir")
			window.update()
			speak('myself Jarvis sir')

		elif 'who creates you' in query:
			var.set('My Creator is Mr. Mridul Gupta')
			window.update()
			speak('My Creator is Mr. Mridul Gupta')

		elif 'say hello' in query:
			var.set('Hello Everyone! My self Jarvis')
			window.update()
			speak('Hello Everyone! My self Jarvis')

		elif 'open vscode' in query:
			var.set("Openong vscode")
			window.update()
			speak("Opening vscode")
			# Enter the correct Path according to your system
			path = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2018.3.2\\bin\\pycharm64.exe"
			os.startfile(path)

		elif 'open chrome' in query:
			var.set("Opening Google Chrome")
			window.update()
			speak("Opening Google Chrome")
			# Enter the correct Path according to your system
			path = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
			os.startfile(path)

		elif 'email to me' in query:
			try:
				var.set("What should I say")
				window.update()
				speak('what should I say')
				content = takeCommand()
				to = a['name']
				sendemail(to, content)
				var.set('Email has been sent!')
				window.update()
				speak('Email has been sent!')

			except Exception as e:
				print(e)
				var.set("Sorry Sir! I was not able to send this email")
				window.update()
				speak('Sorry Sir! I was not able to send this email')

		elif "open python" in query:
			var.set("Opening Python Ide")
			window.update()
			speak('opening python Ide')
			# Enter the correct Path according to your system
			os.startfile(
				'C:\\Users\\mridu\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Python 3.7\\IDLE (Python 3.7 64-bit)')

		elif 'open code blocks' in query:
			var.set('Opening Codeblocks')
			window.update()
			speak('opening Codeblocks')
			# Enter the correct Path according to your system
			os.startfile("C:\\Program Files (x86)\\CodeBlocks\\codeblocks.exe")

		elif 'open anaconda' in query:
			var.set('Opening Anaconda')
			window.update()
			speak('opening anaconda')
			# Enter the correct Path according to your system
			os.startfile(
				"C:\\Users\\mridu\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Anaconda3 (64-bit)\\Anaconda Navigator")

		elif 'calculation' in query:
			sum = 0
			var.set('Yes Sir, please tell the numbers')
			window.update()
			speak('Yes Sir, please tell the numbers')
			while True:
				query = takeCommand()
				if 'answer' in query:
					var.set('here is result'+str(sum))
					window.update()
					speak('here is result'+str(sum))
					break
				elif query:
					if query == 'x**':
						digit = 30
					elif query in numbers:
						digit = numbers[query]
					elif 'x' in query:
						query = query.upper()
						digit = roman.fromRoman(query)
					elif query.isdigit():
						digit = int(query)
					else:
						digit = 0
					sum += digit
		'''
		elif 'enter student details' in query:
			s = Student()
			var.set('Name of the student')
			window.update()
			speak('Name of the student')
			name = takeCommand()
			var.set('standard in which he/she study')
			window.update()
			speak('standard in which he/she study')
			standard = takeCommand()
			var.set('Role Number')
			window.update()
			speak('Roll number')
			rollno = takeCommand()
			s.Enterdetalis(name,standard,rollno)
			var.set('Details are saved')
			window.update()
			speak('Details are saved')

		elif 'show me details' in query:
			var.set('Name: '+name+' Standard: '+ standard+' Roll No.: '+ rollno)
			window.update()'''


'''        elif 'click photo' in query:
			stream = cv2.VideoCapture(0)
			grabbed, frame = stream.read()
			if grabbed:
				cv2.imshow('pic', frame)
				cv2.imwrite('pic.jpg',frame)
			stream.release()

		elif 'record video' in query:
			cap = cv2.VideoCapture(0)
			out = cv2.VideoWriter('output.avi', -1, 20.0, (640,480))
			while(cap.isOpened()):
				ret, frame = cap.read()
				if ret:
					
					out.write(frame)

					cv2.imshow('frame',frame)
					if cv2.waitKey(1) & 0xFF == ord('q'):
						break
				else:
					break
			cap.release()
			out.release()
			cv2.destroyAllWindows()'''
'''            
		elif 'read the photo' in query: #If you have Pytesseract installed for Optical Character Recognition
			try:
				im = Image.open('pic.jpg')
				text = pytesseract.image_to_string(im)
				speak(text)
			except Exception as e:
				print("Unable to read the data")
				print(e)
			'''
class Data:
	def __init__(self, api_key, project_token):
		self.api_key = api_key
		self.project_token = project_token
		self.params = {
			"api_key": self.api_key
		}
		self.get_data()

	def get_data(self):
		response = requests.get(
			f'https://www.parsehub.com/api/v2/projects/{self.project_token}/last_ready_run/data', params=self.params)
		self.data = json.loads(response.text)

	def get_total_cases(self):
		data = self.data['total']

		for content in data:
			if content['name'] == "Coronavirus Cases:":
				return content['values']

	def get_total_deaths(self):
		data = self.data['total']

		for content in data:
			if content['name'] == "Deaths:":
				return content['values']

		return "0"

	def get_total_recovered(self):
		data = self.data['total']

		for content in data:
			if content['name'] == "Recovered:":
				return content['values']

		return "0"

	def get_country_data(self, country):
		data = self.data["country"]

		for content in data:
			if content['name'].lower() == country.lower():
				 return content
		return "0"

	def get_list_of_countries(self):
		countries = []
		for country in self.data['country']:
			countries.append(country['name'].lower())
			
		return countries

	def update_data(self):
		response = requests.post(f'https://www.parsehub.com/api/v2/projects/{self.project_token}/run', params=self.params)
		
		def poll():
			time.sleep(0.1)
			old_data = self.data
			while True:
				new_data = self.get_data()
				if new_data != old_data:
					self.data = new_data
					print("Data updated")
					break
				time.sleep(5)

		t = threading.Thread(target=poll)
		t.start()

def main():
	print("Started Program")
	data = Data(API_KEY, PROJECT_TOKEN)
	END_PHRASE = "stop"
	country_list = data.get_list_of_countries()

	TOTAL_PATTERNS = {
					re.compile("[\w\s]+ total [\w\s]+ cases"):data.get_total_cases,
					re.compile("[\w\s]+ total cases"): data.get_total_cases,
					re.compile("[\w\s]+ total [\w\s]+ deaths"): data.get_total_deaths,
					re.compile("[\w\s]+ total deaths"): data.get_total_deaths,
					re.compile("[\w\s]+ total [\w\s]+ recovered"): data.get_total_recovered,
					re.compile("[\w\s]+ total recovered"): data.get_total_recovered
					}

	COUNTRY_PATTERNS = {
					re.compile("[\w\s]+ cases [\w\s]+"): lambda country: data.get_country_data(country)['total_cases'],
					re.compile("[\w\s]+ deaths [\w\s]+"): lambda country: data.get_country_data(country)['total_deaths'],
					re.compile("[\w\s]+ deaths [\w\s]+"): lambda country: data.get_country_data(country)['total_recovered'],
					}

	UPDATE_COMMAND = "update"

	while True:
		print("Listening...")
		text = get_audio()
		print(text)
		result = None

		for pattern, func in COUNTRY_PATTERNS.items():
			if pattern.match(text):
				words = set(text.split(" "))
				for country in country_list:
					if country in words:
						result = func(country)
						break
					
		for pattern, func in TOTAL_PATTERNS.items():
			if pattern.match(text):
				result = func()
				break
			
		if text == UPDATE_COMMAND:
			result = "Data is being updated. This may take a moment!"
			data.update_data()

		if result:
			speak(result)
 
		if text.find(END_PHRASE) != -1:  # stop loop
			print("Exit")
			#break



def update(ind):
	frame = frames[(ind) % 100]
	ind += 1
	label.configure(image=frame)
	window.after(100, update, ind)


label2 = Label(window, textvariable=var1, bg='#FAB60C')
label2.config(font=("Courier", 20))
var1.set('User Said:')
label2.pack()

label1 = Label(window, textvariable=var, bg='#ADD8E6')
label1.config(font=("Courier", 20))
var.set('Welcome')
label1.pack()

frames = [PhotoImage(file='Assistant.gif', format='gif -index %i' % (i))
		  for i in range(100)]
window.title('JARVIS')
label = Label(window, width=500, height=500)
label.pack()
window.after(0, update, 0)

btn0 = Button(text='WISH ME', width=20, command=wishme, bg='#5C85FB')
btn0.config(font=("Courier", 12))
btn0.pack()
btn1 = Button(text='PLAY', width=20, command=play, bg='#5C85FB')
btn1.config(font=("Courier", 12))
btn1.pack()
btn2 = Button(text='EXIT', width=20, command=window.destroy, bg='#5C85FB')
btn2.config(font=("Courier", 12))
btn2.pack()

wishme()
window.mainloop()
main()

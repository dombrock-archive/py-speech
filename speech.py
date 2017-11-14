import speech_recognition as sr  
import pyttsx3

speech_engine = pyttsx3.init('sapi5') # see http://pyttsx.readthedocs.org/en/latest/engine.html#pyttsx.init
speech_engine.setProperty('rate', 150)

r = sr.Recognizer()

def speak(text):
	print("SPEAKING: "+text)
	speech_engine.say(text)
	speech_engine.runAndWait()

def breakdown(u_said):
	u_said_array = u_said.split(" ")
	for word in u_said_array:
		print(word)
	return (u_said_array)

def confirm(u_said):
	confirmation = ask("Did you say '"+u_said+"'?")
	if(confirmation=="yes"):
		return(True)
	else:
		return(False)

def check_confirmation(u_said):
	while (confirm(u_said) == False):
		u_said = ask("I'm sorry then, please say that again.")

def calibrateMic():
	with sr.Microphone() as source:  
		speak("I need silence to calibrate. Please wait 5 seconds...") 
		# listen for 5 seconds and create the ambient noise energy level  
		r.adjust_for_ambient_noise(source, duration=5)  

# obtain audio from the microphone  
  

def ask(question):
	with sr.Microphone() as source:  
		speak(question) 
		audio = r.listen(source)  

		# recognize speech using Sphinx  
		try:    
			print("Sphinx thinks you said '" + r.recognize_sphinx(audio) + "'")  
			u_said = r.recognize_sphinx(audio)
			return(u_said)
		except sr.UnknownValueError:  
			print("Sphinx could not understand audio")  
		except sr.RequestError as e:  
			print("Sphinx error; {0}".format(e))  
		return("null")


def Start():
	calibrateMic()
	u_said = ask("test question?")
	check_confirmation(u_said)
	print("must be correct")
	u_said_array = breakdown(u_said)
	if ("run" in u_said_array and "chrome" in u_said_array):
		print("run chrome")

Start()

import pyaudio,os
import speech_recognition as sr
import time
import pyautogui

def recordAudio():
    # Record Audio
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)

    # Speech recognition using Google Speech Recognition
    data = ""
    try:
        # Uses the default API key
        # To use another API key: `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        data = r.recognize_google(audio)
        print("You said: " + data)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    return data
def player1():
    pyautogui.moveTo(550,251,duration=0.75)
    pyautogui.click()
    pyautogui.write("Vineet")
def player2():
    pyautogui.moveTo(550,416,duration=0.75)
    pyautogui.click()
    pyautogui.write("Vivek")
def submit():
    pyautogui.moveTo(497,492,duration=0.75)
    pyautogui.click()
def first():
    pyautogui.moveTo(220,194,duration=0.75)
    pyautogui.click()
def second():
    pyautogui.moveTo(412,194,duration=0.75)
    pyautogui.click()
def third():
    pyautogui.moveTo(616,194,duration=0.75)
    pyautogui.click()
def forth():
    pyautogui.moveTo(220,340,duration=0.75)
    pyautogui.click()
def fifth():
    pyautogui.moveTo(412,340,duration=0.75)
    pyautogui.click()
def sixth():
    pyautogui.moveTo(616,340,duration=0.75)
    pyautogui.click()
def seventh():
    pyautogui.moveTo(220,500,duration=0.75)
    pyautogui.click()
def eighth():
    pyautogui.moveTo(412,500,duration=0.75)
    pyautogui.click()
def nineth():
    pyautogui.moveTo(616,500,duration=0.75)
    pyautogui.click()
def enter_():
    pyautogui.press("enter")

def internet():
    pyautogui.moveTo(0,0,duration=0.75)
        
    #pyautogui.position(0,0)
    #pyautogui.write(f"Hlo{i}")
    #pyautogui.write(random.choice(l))
    pyautogui.press("enter")

    # os.system("start chrome.exe")

def start():
    os.startfile(r"C:\Users\vinee\AppData\Local\Programs\Python\Python311\Tic Tak Toe game.py")
def mainfunction():
        user = recordAudio()
        print(user)
        if "player 1" in user or"player one" in user:
            player1()
        elif "player 2" in user or "player two" in user or"player to" in user:
            player2()
        elif "submit" in user or"summit" in user:
            submit()
        elif "1st" in user or "first" in user:
            first()
        elif "2nd" in user or "second" in user:
            second()
        elif "3rd" in user or "third" in user:
            third()
        elif "4th" in user or "forth" in user or "fourth" in user:
            forth()
        elif "5th" in user or "fifth" in user:
            fifth()
        elif "6th" in user or "sixth" in user:
            sixth()
        elif "7th" in user or "seventh" in user:
            seventh()
        elif "8th" in user or "eighth" in user:
            eighth()
        elif "9th" in user or "ninth" in user:
            nineth()
        elif "enter" in user:
            enter_()
            
        elif user=="start":
                start()
while 1:
        mainfunction()

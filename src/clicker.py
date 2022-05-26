import keyboard
import mouse
import pyttsx3
import signal
import sys

def good_bye():
    if(mouse.is_pressed(button='right')):
        mouse.release(button='right')
    if(mouse.is_pressed(button='left')):
        mouse.release(button='left')

    speak('good bye')
    sys.exit()

def signal_handling(signum,frame):
    print('exit on signal')
    good_bye()

signal.signal(signal.SIGINT,signal_handling)

def speak(text):
    print(text)
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    engine.stop()

speak('welcome and press esc to exit')

def toggle_button(btn):
    if(mouse.is_pressed(button=btn)):
        mouse.release(button=btn)
        speak(btn+' released')
    else:
        mouse.press(button=btn)
        speak('holding '+btn)

keyboard.add_hotkey('[', lambda:toggle_button('left'))
keyboard.add_hotkey(']', lambda:toggle_button('right'))

keyboard.wait('esc')

good_bye()

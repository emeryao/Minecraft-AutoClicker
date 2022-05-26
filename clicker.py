import keyboard
import mouse
import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    engine.stop()
    print(text)

speak('welcome and press esc to exit')

def toggle_button(btn):
    if(mouse.is_pressed(button=btn)):
        mouse.release(button=btn)
        speak(btn+" released")
    else:
        mouse.press(button=btn)
        speak("holding "+btn)

keyboard.add_hotkey('[', lambda:toggle_button('left'))
keyboard.add_hotkey(']', lambda:toggle_button('right'))

keyboard.wait('esc')

mouse.release(button='right')
mouse.release(button='left')
speak("good bye")

import pyttsx3

print('Initializing System')
# Initialize the speech generation library
engine = pyttsx3.init()

print('Set up text to say')
# Provide some text to 'say'
engine.say('Good afternoon.')

# Runs the engine and waits until the text has been 'said'
engine.runAndWait()

print('Done')

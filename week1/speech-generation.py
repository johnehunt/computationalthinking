import pyttsx3

# Initialize the speech generation library
engine = pyttsx3.init()

# Provide some text to 'say'
engine.say('Good morning.')

# Runs the engine and waits until the text has been 'said'
engine.runAndWait()
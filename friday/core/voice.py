import pyttsx3
import speech_recognition as sr

class VoiceInterface:
    def __init__(self, voice_id=0):
        # Text-to-speech setup
        self.engine = pyttsx3.init('sapi5')
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', voices[voice_id].id)

        # Speech recognition setup
        self.recognizer = sr.Recognizer()

    def speak(self, text):
        print(f"FRIDAY: {text}")
        self.engine.say(text)
        self.engine.runAndWait()

    def listen(self):
        with sr.Microphone() as source:
            print("Listening...")
            self.recognizer.pause_threshold = 1

            # 🔴 Try to listen – but handle timeout nicely
            try:
                audio = self.recognizer.listen(
                    source,
                    timeout=7,          # ⬅ more time to START speaking
                    phrase_time_limit=7 # ⬅ how long you can speak
                )
            except sr.WaitTimeoutError:
                print("Listening timed out, no speech detected.")
                self.speak("I didn't hear anything, please try again.")
                return None

        # 🔴 Now try to recognize the speech
        try:
            print("Recognizing...")
            query = self.recognizer.recognize_google(audio, language='en-in')
            print(f"User: {query}")
            return query
        except sr.UnknownValueError:
            print("Could not understand audio.")
            self.speak("Sorry, I could not understand. Please repeat.")
            return None
        except Exception as e:
            print("Error during recognition:", e)
            self.speak("Something went wrong while listening.")
            return None

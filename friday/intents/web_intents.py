import time
import webbrowser
import wikipedia
from friday.config import WEBSITES

def handle_open_website(query, speak):
    for name, url in WEBSITES.items():
        if f"open {name}" in query:
            speak(f"Opening {name}")
            webbrowser.open(url)
            time.sleep(2)
            return True
    return False

def handle_wikipedia(query, speak):
    if "wikipedia" not in query:
        return False

    speak("Searching Wikipedia, sir.")
    topic = query.replace("wikipedia", "").strip()
    if not topic:
        speak("What should I search on Wikipedia?")
        return True

    try:
        results = wikipedia.summary(topic, sentences=2)
        print(results)
        speak(results)
    except Exception:
        speak("Sorry, I couldn't fetch that from Wikipedia.")
    time.sleep(2)
    return True

import datetime
import time


def handle_time(query, speak):
    """
    Handle questions about the current time.
    Triggered for phrases containing the word 'time'.
    """
    try:
        if "time" in query:
            now = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {now}")
            time.sleep(0.5)
            return True
        return False
    except Exception as e:
        print("Error in handle_time:", e)
        speak("Sorry, I had a problem telling the time.")
        return True  # we handled it, no crash


def handle_exit(query, speak):
    if "thank you" in query or "goodbye" in query or "stop friday" in query:
        speak("You're welcome, sir. Shutting down FRIDAY.")
        return True
    return False


def handle_greeting(query, speak):
    if "hello" in query or "hi friday" in query or "hey friday" in query:
        speak("Hello sir, how can I help you?")
        return True
    return False

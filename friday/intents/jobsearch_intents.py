import os
import time
import webbrowser

from friday.config import JOB_SITES, PROFILES, RESUME_FOLDER

def handle_open_profile(query, speak):
    for name, url in PROFILES.items():
        if f"open {name}" in query or f"open my {name}" in query:
            speak(f"Opening your {name}.")
            webbrowser.open(url)
            time.sleep(2)
            return True
    return False

def handle_open_job_site(query, speak):
    for name, url in JOB_SITES.items():
        if name in query:
            speak(f"Opening {name}.")
            webbrowser.open(url)
            time.sleep(2)
            return True

    if "jobs" in query and "linkedin" in query:
        speak("Opening LinkedIn jobs.")
        webbrowser.open(JOB_SITES["linkedin jobs"])
        time.sleep(2)
        return True

    return False

def handle_open_resume_folder(query, speak):
    if "resume" in query:
        if os.path.exists(RESUME_FOLDER):
            speak("Opening your resume folder.")
            os.startfile(RESUME_FOLDER)
        else:
            speak("I could not find your resume folder. Please update the path in config.py.")
        time.sleep(1)
        return True
    return False

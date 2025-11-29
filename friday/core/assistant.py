from friday.core.voice import VoiceInterface
from friday.intents.web_intents import handle_open_website, handle_wikipedia
from friday.intents.info_intents import handle_time, handle_greeting, handle_exit
from friday.intents.jobsearch_intents import (
    handle_open_profile,
    handle_open_job_site,
    handle_open_resume_folder,
)
import datetime


class FridayAssistant:
    def __init__(self):
        self.voice = VoiceInterface()
        self.greeted = False  # <-- track if we already greeted

    def wish(self):
        """Greet the user based on time of day."""
        hour = datetime.datetime.now().hour

        if 0 <= hour < 12:
            self.voice.speak("Happy morning, sir.")
        elif 12 <= hour < 18:
            self.voice.speak("Happy afternoon, sir.")
        else:
            self.voice.speak("Happy evening, sir.")

        self.voice.speak("This is FRIDAY. How can I help you?")
        self.greeted = True

    def _ensure_greeted(self):
        """Call wish() once per session."""
        if not self.greeted:
            self.wish()

    def run(self):
        """Main loop for CLI mode (infinite listening)."""
        self._ensure_greeted()

        while True:
            query = self.voice.listen()
            if not query:
                continue

            original_query = query
            query = query.lower()

            # Exit command
            if handle_exit(query, self.voice.speak):
                break

            handled = (
                handle_open_website(query, self.voice.speak)
                or handle_wikipedia(query, self.voice.speak)
                or handle_time(query, self.voice.speak)
                or handle_greeting(query, self.voice.speak)
                or handle_open_profile(query, self.voice.speak)
                or handle_open_job_site(query, self.voice.speak)
                or handle_open_resume_folder(query, self.voice.speak)
            )

            if not handled:
                self.voice.speak("I don't know how to do that yet, but I'm learning.")

        def handle_once(self):
            self._ensure_greeted()

        query = self.voice.listen()

        if not query:
            return {
                "user": None,
                "friday": self.voice.last_text or "I didn't hear anything."
            }

        original_query = query
        query = query.lower()

        try:
            # Exit intent
            if handle_exit(query, self.voice.speak):
                return {
                    "user": original_query,
                    "friday": self.voice.last_text
                }

            handled = (
                handle_open_website(query, self.voice.speak)
                or handle_wikipedia(query, self.voice.speak)
                or handle_time(query, self.voice.speak)
                or handle_greeting(query, self.voice.speak)
                or handle_open_profile(query, self.voice.speak)
                or handle_open_job_site(query, self.voice.speak)
                or handle_open_resume_folder(query, self.voice.speak)
            )

            if not handled:
                self.voice.speak("I don't know how to do that yet, but I'm learning.")

        except Exception as e:
            print("Error in handle_once:", e)
            self.voice.speak("Sorry, something went wrong processing that command.")

        return {
            "user": original_query,
            "friday": self.voice.last_text or "..."
        }


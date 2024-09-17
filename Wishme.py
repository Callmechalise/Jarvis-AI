from datetime import datetime
import win32com.client


def wishme():
    # Get the current time
    now = datetime.now()
    # Extract the current hour
    hour = now.hour

    # Determine the appropriate greeting based on the hour
    if 5 <= hour < 12:
        greeting = "Good morning daddy"
    elif 12 <= hour < 18:
        greeting = "Good afternoon daddy"
    elif 18 <= hour < 22:
        greeting = "Good evening daddy"
    else:
        greeting = "Good night daddy"

    # Print the greeting
    speaker = win32com.client.Dispatch('SAPI.SpVoice')
    print(greeting)
    speaker.speak(greeting)
# Call the function to see the result
wishme()

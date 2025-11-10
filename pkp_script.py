import time
import requests
from bs4 import BeautifulSoup
from pushbullet import Pushbullet

chill = "https://tickets.pukkelpop.be/nl/meetup/demand/day2/a/"
relax = "https://tickets.pukkelpop.be/nl/meetup/demand/day2/b/"

def test_chill():
    try:
        response = requests.get(chill)
        response.raise_for_status()  # Check if the request was successful (HTTP 200)
        if "Geen tickets beschikbaar" in response.text:
            print("Chill Page is navigable and 'Geen tickets beschikbaar' text is present.")
        else:
            print("Tickets available")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

def test_relax():
    try:
        response = requests.get(relax)
        response.raise_for_status()  
        if "Geen tickets beschikbaar" in response.text:
            print("Relax Page is navigable and 'Geen tickets beschikbaar' text is present.")

        else:
            print("Tickets available")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

def send_push_notification_chill():
    api_key = "apikey" 
    pb = Pushbullet(api_key)
    push = pb.push_note("Pukkelpop Tickets Notification", "Chill Tickets are available! https://tickets.pukkelpop.be/nl/meetup/demand/day2/a/")
    print("Push notification sent.")

def send_push_notification_relax():
    api_key = "apikey"  
    pb = Pushbullet(api_key)
    push = pb.push_note("Pukkelpop Tickets Notification", "Relax Tickets are available! https://tickets.pukkelpop.be/nl/meetup/demand/day2/b/")
    print("Push notification sent.")

# Function to check the website
def check_website_chill():
    response = requests.get(chill)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Check if the specific text is present
    if "Geen tickets beschikbaar" not in soup.text:
        send_push_notification_chill()
        return True
    return False

def check_website_relax():
    response = requests.get(relax)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Check if the specific text is present
    if "Geen tickets beschikbaar" not in soup.text:
        send_push_notification_relax()
        return True
    return False

while True:
    test_relax()
    check_website_relax()
        
    time.sleep(30)  # Wait for 30 seconds before the next check

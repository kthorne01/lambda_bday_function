import requests
import datetime

TOKEN = "Bv9F1BLoHEqspVsoCJM7Y7zydz72y2tORFzzctOB"
BOT_ID = "f2ed96df753c0b1dbaacce3511"

def send_message(msg):
    url = "https://api.groupme.com/v3/bots/post"
    data = {
        "bot_id": BOT_ID,
        "text": msg
    }
    response = requests.post(url, json=data)
    print(response.content)

def check_birthdays():
    # You can use a dictionary, database, or any other method to store birthdays
    birthdays = {
        "dear Sister Kayla": "09-01",
        # Add more friends like: "Name": "MM-DD",
    }

    today = datetime.datetime.now().strftime("%m-%d")

    for name, bday in birthdays.items():
        if bday == today:
            send_message(f"Saints, please join me in wishing our {name} the Happiest of Birthdays on today!!!")

if __name__ == "__main__":
    check_birthdays()

import requests
import datetime
import json

TOKEN = "Bv9F1BLoHEqspVsoCJM7Y7zydz72y2tORFzzctOB"
# BOT_ID = "f2ed96df753c0b1dbaacce3511" # test group bot ID
BOT_ID = "e426f5452a51fde95288bb16bd" # ALC church group bot ID

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
        "dear Sister Kayla": "09-02",
        "dear Sister Stephanie": "09-02",
        "dear Brother Ted": "09-02",
        # Add more friends like: "Name": "MM-DD",
    }

    today = datetime.datetime.now().strftime("%m-%d")

    birthday_people = [name for name, bday in birthdays.items() if bday == today]

    if len(birthday_people) == 1:
        send_message(f"Saints, please join me in wishing our {birthday_people[0]} the Happiest of Birthdays on today!!!")
    elif len(birthday_people) == 2:
        send_message(f"Saints, please join me in wishing the Happiest of Birthdays to our {birthday_people[0]} and our {birthday_people[1]}!!!")
    elif len(birthday_people) > 2:
        # Handle cases where there are more than 2 people with birthdays
        names_except_last = ", ".join(birthday_people[:-1])
        send_message(f"Saints, please join me in wishing the Happiest of Birthdays to our {names_except_last}, and {birthday_people[-1]}!!!")

    # for name, bday in birthdays.items():
    #     if bday == today:
    #         send_message(f"Saints, please join me in wishing our {name} the Happiest of Birthdays on today!!!")


def lambda_handler(event, context):
    check_birthdays()
    return {
        'statusCode': 200,
        'body': json.dumps('Birthday check complete!')
    }


if __name__ == "__main__":
    check_birthdays()

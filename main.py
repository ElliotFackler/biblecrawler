import requests
import sqlite3
from bs4 import BeautifulSoup
from datetime import date
from liturgy import *

# No more universal variables.
daily_reading = {}
conn = sqlite3.connect('readings.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS readings (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        text TEXT
    )
''')
conn.commit()

def get_readings(today):

    # Future addition that adds liturgy information
    #print(get_liturgy(today))
   
    url = f"https://bible.usccb.org/bible/readings/{today}.cfm"

    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    print(soup.title.string)

    readings = []
    current_section = None

    all_pp = soup.find_all('p')
    

    headings2 = soup.find_all("h3")
    pp = 1
    print(all_pp[pp].text.strip())

    for h in headings2:
        pp+= 1
        
        # Prints section title Ex. "Gospel"
        print(h.text.strip())

        siblings = h.find_next_siblings()

        for sib in siblings:
            
            if sib.name and sib.name.startswith('h'):
              break
            # Prints verse numbers. I really need to get better at naming variables.
            print(sib.get_text(strip=True), '\n')
            # Prints the text of the reading
            print(all_pp[pp].text.strip())
            daily_reading[h.text.strip() + " : " + sib.get_text(strip=True)] = all_pp[pp].text.strip()

        print("-" * 40)  # separator

    return


def send_readings_to_db(readings):
    for title, text in readings.items():
        cursor.execute('''
            INSERT INTO readings (title, text) VALUES (?, ?)
        ''', (title, text))
    conn.commit()
    print("Readings saved to database.")

    return

def get_db_input():
    try:
        return input("Do you want to save the readings to the database? (yes/no): ").strip().lower()
    except EOFError:
        return None
    except KeyboardInterrupt:
        print("\nInput interrupted.")
        return None
    

def get_new_date_input():
    try:
        new_date = input("Do you want to get readings for a different date? (yes/no): ").strip().lower()
        if new_date == 'yes':
            new_date_input = input("Enter the date in MMDDYY format: ").strip()
            get_readings(new_date_input)
            get_new_date_input()
        elif new_date == 'no':
            print("Exiting the program.")
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
            get_new_date_input()
    except EOFError:
        return None
    except KeyboardInterrupt:
        print("\nInput interrupted.")
        return None



if __name__ == "__main__":
    today = date.today()
    print("Today is:", today.strftime("%A, %B %d, %Y"))
    today = today.strftime("%m%d%y")

    get_readings(today)

    db_decision = get_db_input()
    if db_decision == 'yes':
        send_readings_to_db(daily_reading)
    elif db_decision == 'no':
        print("Readings will not be saved to the database.")
    else:
        get_db_input()

    get_new_date_input()

    conn.close()

    
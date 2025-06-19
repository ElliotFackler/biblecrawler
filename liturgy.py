import requests
import json
from datetime import date

def get_liturgy(today):
    # Load calendar JSON from romcal GitHub repo
    url = "https://raw.githubusercontent.com/pejulian/romcal/main/examples/calendar.en.json"
    response = requests.get(url)

    if response.status_code != 200:
        return "Liturgical info not available."

    calendar_data = response.json()
    today_str = today.isoformat()

    for day in calendar_data:
        if day['date'] == today_str:
            color = day.get("liturgicalColor", "unknown").capitalize()
            season = day.get("season", "unknown").replace('_', ' ').title()
            celebration = day.get("celebration", "None")
            rank = day.get("rank", "")

            return {today_str}
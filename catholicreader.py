import requests
from bs4 import BeautifulSoup
from datetime import date


today = date.today()
print("Today is:", today.strftime("%A, %B %d, %Y"))

def get_readings():
    today = date.today().strftime("%m%d%y")
   
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
        
        print(h.text.strip())

        siblings = h.find_next_siblings()

        for sib in siblings:
            
            if sib.name and sib.name.startswith('h'):
              break
            print(sib.get_text(strip=True), '\n')
            print(all_pp[pp].text.strip())

        print("-" * 40)  # separator

    return



if __name__ == "__main__":
    get_readings()

    
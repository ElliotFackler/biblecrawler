Daily Biblical Readings Scraper
This Python script scrapes daily biblical readings from the United States Conference of Catholic Bishops (USCCB) website and saves them to a local SQLite database. It's a simple, command-line tool designed for personal use to easily access and archive daily readings.

Features
Daily Readings: Fetches the readings for the current day by default.

Custom Date Support: Allows you to input a specific date in MMDDYY format to get readings for a different day.

Database Storage: Stores the title and text of each reading in a SQLite database file named readings.db.

Command-Line Interface: Provides a simple prompt to decide whether to save the readings or get readings for another date.

Prerequisites
Before running the script, you'll need to install the necessary Python libraries. You can do this using pip.

pip install requests beautifulsoup4

How to Run the Script
Clone or download the script to your local machine.

Open your terminal or command prompt and navigate to the directory where you saved the file.

Run the script using the following command:

python your_script_name.py

Follow the on-screen prompts to interact with the program. It will ask if you want to save the readings to the database or if you want to enter a new date.

Project Structure
your_script_name.py: The main Python script that handles web scraping and database interactions.

readings.db: The SQLite database file created and used by the script to store the readings.

Planned Improvements
The code includes a commented-out section for future additions that would use the liturgy library. This suggests a potential for future expansion to include more liturgical information alongside the readings.

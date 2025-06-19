import tkinter as tk
import sqlite3

def show_readings():
    conn = sqlite3.connect('readings.db')
    cursor = conn.cursor()
    cursor.execute('SELECT title, text FROM readings')
    readings = cursor.fetchall()
    conn.close()
    text_box.delete('1.0', tk.END)
    for title, text in readings:
        text_box.insert(tk.END, f"{title}\n{text}\n\n")

root = tk.Tk()
root.title("Bible Readings")

show_btn = tk.Button(root, text="Show Readings", command=show_readings)
show_btn.pack()

text_box = tk.Text(root, width=60, height=20)
text_box.pack()

root.mainloop()
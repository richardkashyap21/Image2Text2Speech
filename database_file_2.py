import mysql.connector
import tkinter as tk
from tkinter import messagebox,scrolledtext


def display_database_contents():
    root = tk.Tk()
    text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=70, height=15)
    text_area.pack(pady=10)

    global connection, my_cursor
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='image_db',
            user='root',
            password='1234'
        )

        my_cursor = connection.cursor()
        my_cursor.execute("SELECT * FROM images")
        rows = my_cursor.fetchall()


        text_area.delete(1.0, tk.END)

        for row in rows:
            text_area.insert(tk.END, f"ID: {row[0]}\n")
            text_area.insert(tk.END, f"Name: {row[1]}\n")
            text_area.insert(tk.END, f"Audio file: {row[2]}\n")
            text_area.insert(tk.END, f"Extracted Text: {row[3]}\n\n")

    except mysql.connector.Error as error:
        messagebox.showerror("Error", f"Failed to fetch data from MySQL table: {error}")

    finally:
        if connection.is_connected():
            my_cursor.close()
            connection.close()


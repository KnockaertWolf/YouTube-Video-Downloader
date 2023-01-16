import pytube
import tkinter as tk
from tkinter import ttk
import os

screen = tk.Tk()
screen.title("YT Video Downloader")

default_location_txt = 'Default location: Currentlocation/videos'

current_location = os.getcwd()

def on_entry_click(event):
    """function that gets called whenever entry is clicked"""
    if location_enter_get == default_location_txt:
       location_enter.delete(0, "end") # delete all the text in the entry
       location_enter.insert(0, '') #Insert blank for user input
       location_enter.config(fg = 'black')

def on_focusout(event):
    if location_enter_get == '':
        location_enter.insert(0, default_location_txt)
        location_enter.config(fg = 'grey')

def display_text():
	if location_enter_get == default_location_txt:
		location_enter.delete(0, 'end')
	url = LinkEnter.get()
	location = location_enter_get
	if location == "":
		check_video_folder = os.path.exists(current_location + '/Videos')
		if not check_video_folder:
			location_enter.delete(0, 'end')
			os.mkdir('Videos')
			location = current_location + '/Videos'
			print(current_location)
			print(location)

		else:
			location = current_location + '/Videos'

	file = pytube.YouTube(url).streams.filter(res='1080p').first().download(location)
	base = os.path.splitext(file)[0]
	os.rename(file, base + '.mp4')


link_enter_text = tk.Label(text="Link:")
LinkEnter = tk.Entry(bg="white", width=50)

location_enter_text = tk.Label(text="location:")
location_enter = tk.Entry(bg="white", width=50)
location_enter_get = location_enter.get()

link_enter_text.pack()
LinkEnter.pack()

location_enter.insert(0, default_location_txt)
location_enter.bind('<FocusIn>', on_entry_click)
location_enter.bind('<FocusOut>', on_focusout)
location_enter.config(fg = 'grey')

location_enter_text.pack()
location_enter.pack()





ttk.Button(screen, text= "Download",width= 20, command= display_text).pack(pady=20)



screen.mainloop()


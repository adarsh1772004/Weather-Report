from tkinter import *
import tkinter
import requests


def findWeather():
    city = city_text.get()
    api_link = "http://api.openweathermap.org/data/2.5/weather?q=" + \
        city+"&units=metric&appid=22515dbe8047cf659da74a1cae281c2e"
    responce = requests.get(api_link)
    api_data = responce.json()
    location_lbl["text"] = "{} , {}".format(
        api_data["name"], api_data["sys"]["country"])
    temp_lbl["text"] = "Temperature : {}°C".format(api_data["main"]["temp"])
    temp_min_lbl["text"] = "Minimum Temperature : {}°C".format(
        api_data["main"]["temp_min"])
    temp_max_lbl["text"] = "Maximum Temperature : {}°C".format(
        api_data["main"]["temp_max"])


app = Tk()
app.title("Weather Report")
app.geometry('700x350')


city_text = StringVar()
city_entry = Entry(app, textvariable=city_text)
city_entry.pack()


search_button = Button(app, text='Search', width=12, command=findWeather)
search_button.pack()

location_lbl = Label(app, text="", font=("bold", 20))
location_lbl.pack()

temp_lbl = Label(app, text="", font=("bold", 20))
temp_lbl.pack()

temp_min_lbl = Label(app, text="", font=("bold", 20))
temp_min_lbl.pack()

temp_max_lbl = Label(app, text="", font=("bold", 20))
temp_max_lbl.pack()
app.mainloop()

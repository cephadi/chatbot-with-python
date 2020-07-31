from tkinter import *
from datetime import datetime
import wikipedia
import pyttsx3

gui = Tk()
gui.title("My ChatBot")

engine = pyttsx3.init('sapi5')


now = datetime.now()

simple_greetings = {
    "hai" : "Hello, My name is Sudo, and i am your new virtual assistant",
    "how are you" : "I'am fine. How are you?",
    "i am fine" : "Nice to hear that",
    "what time is it" : "Today is {}".format(now.strftime("%d %B %Y %H:%M:%S"))
}

def send_info():
    you = "You : {}".format(entry.get())
    text.insert(END, "\n{}".format(you))
    bot = "Bot : "
    if entry.get().lower() in simple_greetings:
        text.insert(END, "\n{0}{1}".format(bot, simple_greetings[entry.get().lower()]))
        engine.say(simple_greetings[entry.get().lower()])
        engine.runAndWait()
        engine.stop()
    else:
        try:
            summary = wikipedia.summary(entry.get().lower())
            text.insert(END, "\nBot : Did you mean this? \nBot : {}".format(summary))
            engine.say("Did you mean this?")
            engine.say(summary)
            engine.runAndWait()
            engine.stop()
        except Exception as e:
            text.insert(END, "\nBot : I didn't get it?")
            engine.say("I didn't get it")
            engine.runAndWait()
            engine.stop()

text = Text(gui, bg='white')
text.grid(row=0, column=0, columnspan=2)

entry = Entry(gui, width=80)
entry.grid(row=1, column=0)

button_send = Button(gui, text='Send', bg='white', width=20, command=send_info)
button_send.grid(row=1, column=1)

totalRow = 3
totalCol = 3
for row in range(totalRow + 1):
    gui.grid_rowconfigure(row, weight=1)

for col in range(totalCol + 1):
    gui.grid_columnconfigure(col, weight=1)

gui.mainloop()
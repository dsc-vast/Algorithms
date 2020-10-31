from tkinter import *
import paho.mqtt.client as mqtt
import time


def click():
	message = textEntry.get()
	client.publish("server/server1", str(message),qos=1)

#exit function
def close_window():
	window.destroy()

def on_publish(client, userdata, mid):
	print("mid"+str(mid))

def on_subscribe(client, userdata, mid, granted_qos):
	print("Subscribed: "+str(mid)+" "+str(granted_qos))

def on_message(client, userdata, msg):
	print(msg.topic+" "+str(msg.qos)+" "+str(msg.payload))
	output.insert(END, msg.payload)
	output.insert(END, '\n')

client = mqtt.Client()
client.on_subscribe = on_subscribe
client.on_message = on_message
client.on_publish = on_publish
client.connect("broker.mqttdashboard.com",1883)
client.subscribe("server/server2", qos=1)
client.loop_start()

#main
window = Tk()
window.title("Title here")

#TextEntry
textEntry = Entry(window, width=20)
textEntry.grid(row=0, column=1, sticky=N)

#Button
Button(window, text="Send", width=8, command=click) .grid(row=1, column=1, sticky=E)

#text box
output = Text(window, width=30, height=6, wrap=WORD, background="white")
output.grid(row=0, column=0, sticky=W)

#exit button
Button(window, text="Quit", width=6, command=close_window) .grid(row=1, column=0, sticky=W)

window.mainloop()
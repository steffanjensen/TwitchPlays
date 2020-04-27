import socket
import pyautogui
import time

server = 'irc.chat.twitch.tv'
channel = '#name'
nick = 'name'
password = "oauth:"
port = 6667

def connect():
    # Connecting to your Twitch IRC
    global ircsock
    ircsock = socket.socket()
    ircsock.connect((server, port))

    ircsock.send(bytes("PASS " + password + "\r\n", 'UTF-8'))
    ircsock.send(bytes("NICK " + nick + "\r\n", 'UTF-8'))
    ircsock.send(bytes("JOIN " + channel + "\r\n", 'UTF-8'))

def click_button(key, output):
    # Click in emulator
    pyautogui.click(1094, 466)
    time.sleep(0.2)
    pyautogui.keyDown(key)
    time.sleep(0.4)
    pyautogui.keyUp(key)
    ircsock.send(bytes("PRIVMSG "+ channel +" :"+ output + " was pressed" + "\r\n", "UTF-8"))

connect()
while True:
    data = ircsock.recv(2048)
    print(data)

    if data.find(b"!A") != -1:
        click_button("z", "A")

    if data.find(b"!B") != -1:
        click_button("x", "B")

    if data.find(b"!LEFT") != -1:
        click_button("g", "LEFT")

    if data.find(b"!RIGHT") != -1:
        click_button("j", "RIGHT")

    if data.find(b"!UP") != -1:
        click_button("y", "UP")

    if data.find(b"!DOWN") != -1:
        click_button("h", "DOWN")

    if data.find(b"!START") != -1:
        click_button("enter", "START")
        
    # If no data reconnect    
    if len(data) == 0:
        print("Disconnected!")
        connect()
    time.sleep(0.1)

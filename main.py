import PySimpleGUI as sg
from functions import spammer

# Set the theme
sg.theme('DarkBlue')

# Define the window's contents
layout = [[sg.Text('Name of Contact :')],
          [sg.Input(key='-CONTACT-')],
          [sg.Text('Enter Text Message :')],
          [sg.Input(key='-MESSAGE-')],
          [sg.Text('Enter of number times to Send :')],
          [sg.Input(key='-COUNT-')],
          [sg.Text(size=(40,1), key='-OUTPUT-')],
          [sg.Button('SPAM !!!'), sg.Button('Quit')]]

# Create the window
window = sg.Window('WhatsApp Spammer', layout, alpha_channel=0.90)

# Display and interact with the Window using an Event Loop
while True:
    event, values = window.read()
    # See if user wants to quit or window was closed
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break

    # Setting Variables
    name=values['-CONTACT-']
    message=values['-MESSAGE-']
    count=values['-COUNT-']

    #calling spammer from functions.py
    S=spammer(name,message,count)

    # Output a message to the window
    window['-OUTPUT-'].update(S)

# Finish up by removing from the screen
window.close()
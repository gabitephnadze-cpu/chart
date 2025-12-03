import FreeSimpleGUI as sg

layout = [
    [sg.Text('Enter Your Name:'), sg.InputText()],
    [sg.Text('Select Your Age:'), sg.Slider(range=(1, 100), orientation='h', size=(20, 15))],
    [sg.Checkbox('I Agree To The TOS')],
    [sg.Button('Submit'), sg.Button('Exit')]
]

window = sg.Window('Driving License', layout)

while True:
    event, values = window.read()
    print(event,values)
    if event == sg.WINDOW_CLOSED or event == 'Exit':
        break
    
    if event == 'Submit':
        name = values[0]
        age = values[1]
        agreed = values[2]
        
        if not agreed:
            sg.popup('You Must Agree To Our TOS!')
            continue
        
        if age < 16:
            message = f'{name.capitalize()} You Are Not Elligable To Get A Driving License Yet'
        elif age >= 16:
            message = f'{name.capitalize()} You Are Elligable To Get A Driving License'
        
        sg.popup(message)
window.close() 
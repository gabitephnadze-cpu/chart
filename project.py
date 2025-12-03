import FreeSimpleGUI as sg

sg.theme('DarkTeal16')

button_size = (5, 2)
font_style = ('Helvetica', 19)

layout = [
    [sg.Text('', key='DISPLAY', size=(20, 1), justification='right', font=('Helvetica', 24),
             background_color='#FFFFFF', text_color='#000000', pad=(10, 20))],
    [sg.Button('7', size=button_size, font=font_style), sg.Button('8', size=button_size, font=font_style),
     sg.Button('9', size=button_size, font=font_style), sg.Button('/', size=button_size, font=font_style)],
    [sg.Button('4', size=button_size, font=font_style), sg.Button('5', size=button_size, font=font_style),
     sg.Button('6', size=button_size, font=font_style), sg.Button('*', size=button_size, font=font_style)],
    [sg.Button('1', size=button_size, font=font_style), sg.Button('2', size=button_size, font=font_style),
     sg.Button('3', size=button_size, font=font_style), sg.Button('-', size=button_size, font=font_style)],
    [sg.Button('0', size=button_size, font=font_style), sg.Button('.', size=button_size, font=font_style),
     sg.Button('+', size=button_size, font=font_style), sg.Button('=', size=button_size, font=font_style)],
    [sg.Button('Clear', size=(22, 1), font=font_style, pad=(10, 10))]
]

window = sg.Window('Calculator', layout, resizable=False)
window.size = (420, 550)

display_text = ''
current_number = ''

while True:
    event, values = window.read()
    if event in (sg.WINDOW_CLOSED, 'Exit'):
        break
    
    if event in '0123456789.':
        current_number = current_number + event
        display_text = display_text + event
        window['DISPLAY'].update(display_text)
    elif event in '+-*/':
        #Only allow all operator if a number was just entered
        if current_number:
            display_text += event
            current_number = ''
            window['DISPLAY'].update(display_text)
    elif event == '=':
        try:
            result = str(eval(display_text))
            display_text = result
            window['DISPLAY'].update(result)
        except Exception:
            window['DISPLAY'].update('Error')
            display_text = ''
            current_number = ''
    elif event == 'Clear':
        display_text = ''
        current_number = ''
        window['DISPLAY'].update('')
        
window.close
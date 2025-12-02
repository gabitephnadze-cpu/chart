import streamlit

streamlit.title('კმ ↔ მილი გადამყვანი')

option = streamlit.radio('აირჩიეთ:', ('კმ ↔ მილი', 'მილი ↔ კმ'))

value = streamlit.number_input('შეიყვანეთ რიცხვი')

if option == 'კმ ↔ მილი':
    result =value * 0.62
    streamlit.write(f'{value} კმ = {result:.2f} მილი')
    
if option == 'მილი ↔ კმ':
    result =value / 0.62
    streamlit.write(f'{value} მილი = {result:.2f} კმ')
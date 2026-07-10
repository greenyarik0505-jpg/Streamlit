import streamlit as st

st.title("Проверка знаний на Дибил")

fotball1 = st.radio("Оберіть Футболиста у кого больше всего голов:", ["Месси", "Роналду", "Неймар"])

if fotball1 == "Роналду":
    st.success("Правильно")
else:
    st.error("Неправильно")
food = st.radio("Яка краща їжа:", ["Бургер", "Чипси", "макарони"])

if food == "Чипси":
    st.success("Правильно")
else:
    st.error("Неправильно")

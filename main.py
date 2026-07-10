import streamlit as st

st.title("Проверка знаний на Дибила")

fotball1 = st.radio("Оберіть Футболиста у кого больше всего голов:", ["Месси", "Роналду", "Неймар"])

if fotball1 == "Роналду":
    st.success("Правильно! 🎉")
else:
    st.error("Неправильно ❌")

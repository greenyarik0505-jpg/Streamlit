from turtle import title
import streamlit as st

st.title = ('Тест на Дибила')

football = st.multiselect(
    "Кто Goat с футболистов:",
    ["Мбаппу", "Месси", "Винисиус", "Неймар", "Роналду"],
)
st.write(f"Твій вибір: {', '.join(football)}")

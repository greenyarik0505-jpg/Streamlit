import streamlit as st

football = st.multiselect(
    "Кто Goat с футболистов:",
    ["Мбаппу", "Месси", "Винисиус", "Неймар", "Роналду"],
)
st.write(f"Твій вибір: {', '.join(football)}")

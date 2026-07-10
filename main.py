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

brainroti = st.radio("Який брейнрот акула?", ["Tralalelo Tralala", "Tung Tung Tung Sahur", "Br Br Patapim"])
if brainroti == "Tralalelo Tralala":
    st.success("Правильно")
else:
    st.error("Неправильно")

strana = st.radio("Какая самая могущая страна била раньше:", ["СРСР", "США", "Немецкая Империя"])
if strana == "СРСР":
    st.success("Правильно")
else:
    st.error("Неправильно")

xtoluck=st.radio("Хто лучший фізік", ["Енштейн", "Епштейн", "Кирилл"])
if xtoluck == "Енштейн":
    st.success("Правильно")
else:
    st.error("Неправильно") 

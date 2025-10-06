import streamlit as st

st.title("Solar Sentience Dashboard ☀️🧠")

mood = st.slider("Rate your current mood", 0, 10)
focus = st.slider("Rate your focus level", 0, 10)
stress = st.slider("Rate your stress level", 0, 10)

if st.button("Analyze"):
    score = (mood + focus - stress) / 3
    st.write(f"Your solar-readiness score is: {round(score, 2)}")

    if score > 7:
        st.success("You're in peak condition for field deployment!")
    elif score > 4:
        st.warning("Consider a short break or light tasks.")
    else:
        st.error("High stress detected. Recommend rest or support.")

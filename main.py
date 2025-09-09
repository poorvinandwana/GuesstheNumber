import random
import streamlit as st


st.title("Guess the Number Game")

if "number" not in st.session_state:
    st.session_state.number = random.randint(1,100)
    st.session_state.guesses = 0
    st.session_state.solved = False

if not st.session_state.solved:
        st.text("I have selected a secret number.")
        user = st.number_input("Enter your guess between 1 and 100", min_value=1, max_value=100,step=1)


        if st.button("Submit"):
            st.session_state.guesses += 1
            if user < st.session_state.number:
                st.audio("audio/new-notification.mp3", loop=False, format="audio/mp3", autoplay=True, width=1)
                st.warning("Higher number please!")
            elif user > st.session_state.number:
                st.audio("audio/new-notification.mp3", loop=False, format="audio/mp3", autoplay=True, width=1)
                st.warning("Lower number please!")
            else:
                st.audio("audio/success-trumpets.mp3", loop=False, format="audio/mp3", autoplay=True, width=1)
                st.session_state.solved = True
                st.success(f"Congratulations! You finally guessed my secret number {st.session_state.number} in {st.session_state.guesses} guesses.")
                st.balloons()

else:
    st.button("Play Again", on_click=lambda: [st.session_state.pop(k) for k in list(st.session_state.keys())])


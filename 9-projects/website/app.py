import streamlit as st

# --- Page Configuration ---
st.set_page_config(
    page_title="Python Mini Projects",
    page_icon="🐍",
    layout="wide"
)

# --- Projects Data ---
projects = [
    {
        "title": "📖 Mad Libs Python Project",
        "description": "Create a story by filling in the blanks! A fun way to explore string manipulation and user input."
    },
    {
        "title": "🤖 Guess the Number (Computer vs User)",
        "description": "The computer picks a number and you guess it with hints. Learn loops and random module."
    },
    {
        "title": "🧠 Guess the Number (User vs Computer)",
        "description": "You choose a number, and the computer tries to guess it using logic and binary search techniques."
    },
    {
        "title": "✂️ Rock, Paper, Scissors",
        "description": "Classic game versus the computer. Learn about conditionals and game logic."
    },
    {
        "title": "🪢 Hangman Game",
        "description": "Guess the secret word letter by letter. Practice loops, conditionals, and strings."
    },
    {
        "title": "⏳ Countdown Timer",
        "description": "Set a countdown and watch the time tick away. Great intro to Python's `time` module."
    },
    {
        "title": "🔐 Password Generator",
        "description": "Generate strong passwords with customizable settings. Learn randomness and string functions."
    },
    {
        "title": "🧮 BMI Calculator Web App",
        "description": "Input your height and weight to calculate BMI. Perfect to practice functions and UI development."
    },
]

# --- Main UI ---
def main():
    st.title("🚀 Python Mini Projects")
    st.markdown("""
    Welcome to a collection of fun and interactive Python mini-projects built using Streamlit! 🎉  
    Learn core concepts of Python with hands-on games and tools.
    """)

    st.divider()
    st.subheader("📌 All Projects at a Glance")

    # Display projects in a responsive grid (3 columns per row)
    for i in range(0, len(projects), 3):
        cols = st.columns(3)
        for idx, project in enumerate(projects[i:i+3]):
            with cols[idx]:
                with st.container(border=True):
                    st.markdown(f"### {project['title']}")
                    st.markdown(project['description'])
                    st.markdown("")

# --- Run App ---
if __name__ == "__main__":
    main()

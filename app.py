import streamlit as st

st.set_page_config(
    page_title="FitBuddy",
    page_icon="💪",
    layout="centered"
)

st.title("💪 FitBuddy")
st.subheader("AI Fitness Plan Generator")
st.write("Your personal activity planner!")

st.info("This is a demo version of FitBuddy. It provides general activity suggestions, not medical advice.")

st.header("Your Fitness Preferences")

goal = st.selectbox(
    "Choose Your Goal",
    ["Improve General Fitness",
     "Build an Activity Habit",
     "Improve Flexibility"]
)

level = st.selectbox(
    "Experience Level",
    ["Beginner", "Intermediate"]
)

days = st.selectbox(
    "Days Per Week",
    [2, 3, 4, 5]
)

duration = st.selectbox(
    "Available Time",
    [10, 15, 20, 30]
)

activities = st.multiselect(
    "Choose Your Activities",
    ["Walking", "Yoga", "Cycling",
     "Stretching", "Dance"]
)

if st.button("Generate My Fitness Plan"):
    if not activities:
        st.warning("Please select an activity.")
    else:
        st.success("Your FitBuddy Plan is Ready!")

        st.subheader("🏃 Weekly Activity Plan")

        st.write("**Goal:**", goal)
        st.write("**Level:**", level)
        st.write("**Days:**", days)
        st.write("**Duration:**", str(duration) + " minutes")

        for day in range(1, days + 1):
            activity = activities[(day - 1) % len(activities)]
            st.write(f"Day {day}: {activity}")

        st.subheader("💡 Healthy Reminders")
        st.write("- Start gently and progress gradually.")
        st.write("- Drink water regularly.")
        st.write("- Take rest when needed.")
        st.write("- Stop if you feel pain or unwell.")

        st.caption("FitBuddy Demo Version")
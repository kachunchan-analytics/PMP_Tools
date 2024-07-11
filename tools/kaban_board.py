import streamlit as st

st.title("My Kanban Board")

# Define columns
columns = ["To Do", "In Progress", "Done"]

# Create a Kanban board using Streamlit's `beta_columns`
col1, col2, col3 = st.beta_columns(len(columns))

# Add cards to each column
for i, column in enumerate(columns):
    st.write(f"## {column}")
    with st.beta_container():
        for card_title in ["Task 1", "Task 2", "Task 3"]:
            if i == 0:
                col1.write(f"- {card_title}")
            elif i == 1:
                col2.write(f"- {card_title}")
            else:
                col3.write(f"- {card_title}")

# Add a "Add Card" button
st.button("Add Card")
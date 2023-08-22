import streamlit as st

def main():
    st.title("Chatty Potter ⚡️")
    st.write("A chatbot built with ChatGPT (3.5 Turbo) where you can pick a Harry Potter character and chat with them as if you were talking over text. My absolute FAVOURITE thing is the emojis that the characters respond with. It is utterly delightful when Voldy comes back with snake and death eater emojis 🐍💀")

    # Dropdown menu with Harry Potter character names
    characters = [
        "Harry Potter",
        "Hermione Granger",
        "Ron Weasley",
        "Albus Dumbledore",
        "Severus Snape",
        "Lord Voldemort",
        "Rubeus Hagrid",
        "Draco Malfoy",
        "Luna Lovegood"
    ]
    selected_character = st.selectbox("Select a character:", characters)

    st.write(f"You selected: {selected_character}")

    # Text area for writing a message
    message = st.text_area("Write a message to the selected character:")

    # Create a session state to store conversation history for each character
    if "conversation_history" not in st.session_state:
        st.session_state.conversation_history = {}

    if selected_character not in st.session_state.conversation_history:
        st.session_state.conversation_history[selected_character] = []

    # Submit button
    if st.button("Submit"):
        # Process the message and generate a response (you need to implement this part)
        response = generate_response(selected_character, message)
        add_to_conversation(selected_character, message, response)

    # Display conversation history
    display_conversation(selected_character)

def generate_response(character, message):
    response = "Response"  # This seems to be a placeholder, you should actually generate the response
    return response

def add_to_conversation(character, user_message, response):
    st.session_state.conversation_history[character].append((character, user_message, response))

def display_conversation(character):
    st.subheader("Message History:")
    for _, user_message, response in st.session_state.conversation_history[character]:
        st.write(f"You:", user_message)
        st.write(f"{character}:", response)
        st.write("")

if __name__ == "__main__":
    main()

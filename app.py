import streamlit as st
import openai

openai.api_key =  st.secrets["mykey"]

# Title and Heading
st.title("Choojun's First Streamlit App")
st.header("This is a header")
st.write("This is some text.")

# Input and Output
name = st.text_input("Enter your name:", value="Type here")
if st.button("Submit"):
    st.write(f"Hello, {name}! I love TAR UMT! ")
    
    
# Insert a chat message container.
with st.chat_message("user"):
    st.write("Hello 👋")
    st.line_chart(np.random.randn(30, 3))

# Display a chat input widget at the bottom of the app.
>>> st.chat_input("Say something")

# Display a chat input widget inline.
with st.container():
    st.chat_input("Say something")


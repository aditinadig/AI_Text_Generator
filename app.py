import streamlit as st
from transformers import pipeline
import time

# Sidebar settings
st.sidebar.title("Settings")
model_name = st.sidebar.selectbox("Choose a model:", ["gpt2", "EleutherAI/gpt-neo-125M"])
max_length = st.sidebar.slider("Maximum output length:", 10, 200, 50)
num_return_sequences = st.sidebar.slider("Number of results:", 1, 5, 1)

# Cache the model loading for faster response times
@st.cache(allow_output_mutation=True)
def load_model(model_name):
    return pipeline('text-generation', model=model_name)

generator = load_model(model_name)

# App Title and Description
st.title("AI Text Generator")
st.write("Enter a prompt, and let GPT-2 generate text for you!")

# User Input
prompt = st.text_input("Enter your prompt:", "")
if prompt:
    st.write(f"Character count: {len(prompt)}")

# Initialize results variable to avoid NameError
results = []

# Generate Text
if st.button("Generate"):
    if prompt.strip():
        with st.spinner("Generating text..."):
            time.sleep(1)  # Simulate loading time
            results = generator(prompt, max_length=max_length, num_return_sequences=num_return_sequences)
        st.success("Done!")
        for idx, result in enumerate(results):
            st.markdown(f"### Output {idx + 1}")
            st.code(result['generated_text'])
    else:
        st.warning("Please enter a valid prompt!")

# Save results functionality
if st.button("Save Results"):
    if results:  # Check if results are generated
        with open("generated_results.txt", "w") as f:
            for idx, result in enumerate(results):
                f.write(f"Output {idx + 1}:\n")
                f.write(result['generated_text'] + "\n\n")
        st.success("Results saved to generated_results.txt!")
    else:
        st.warning("Please generate text before saving!")
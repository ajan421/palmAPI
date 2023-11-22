import pprint
import streamlit as st
import streamlit_chat
import google.generativeai as palm
palm.configure(api_key='AIzaSyAO9Whlwig1JZq6p9mc0bI3XzJg0HqoEhg')
models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]
model = models[0].name

prompt = """
how many letters are in "gopiiiii"?
"""

completion = palm.generate_text(
    model=model,
    prompt=prompt,
    temperature=0,
    # The maximum length of the response
    max_output_tokens=800,
)

st.write(completion.result)
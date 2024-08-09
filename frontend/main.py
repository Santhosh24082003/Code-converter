import streamlit as st
import requests

# Define the backend API URL
BACKEND_API_URL = "http://127.0.0.1:3001/convert"  # Use the correct port for your backend

# Streamlit UI
st.set_page_config(page_title="COBOL Code Converter", layout="wide")

# Title
st.title("COBOL Code Converter")

# Layout configuration: two columns
col1, col2 = st.columns([1, 2])

with col1:
    st.header("COBOL Code Input")
    cobol_code = st.text_area("Enter COBOL code here:", height=300)

with col2:
    st.header("Converted Code")
    # Language selector and convert button in the same column
    target_language = st.selectbox("Select target language:", ["Python", ".NET"])
    convert_button = st.button("Convert")

    # Display result or a placeholder
    if convert_button:
        if cobol_code:
            # Prepare the request payload
            payload = {
                "cobol_code": cobol_code,
                "target_language": target_language
            }
            try:
                # Send request to the backend
                response = requests.post(BACKEND_API_URL, json=payload)
                response.raise_for_status()

                # Get the converted code from the response
                response_data = response.json()
                result = response_data.get("converted_code", "")
                
                # Display the converted code
                st.subheader("Converted Code")
                st.code(result, language='text')

            except requests.exceptions.RequestException as e:
                st.error(f"An error occurred: {e}")
        else:
            st.warning("Please enter COBOL code before converting.")
    else:
        st.info("Click 'Convert' to see the result.")

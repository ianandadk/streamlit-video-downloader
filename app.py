import streamlit as st
import requests

# Set up the Streamlit app layout
st.title("Video Downloader")
st.write("Enter the URL of the video you'd like to download.")

# User input for the URL
url = st.text_input("Enter video URL:")

# If the user provides a URL
if url:
    # Button to trigger the download
    if st.button("Download Video"):
        headers = {
            "Referer": "https://xhamster19.com"  # You can adjust the Referer as needed
        }

        try:
            # Sending the GET request
            response = requests.get(url, headers=headers)

            if response.status_code == 200:
                # Writing the content to a file
                with open("video.mp4", "wb") as f:
                    f.write(response.content)
                
                # Notify the user of success
                st.success("Download successful!")
                st.write("The video has been saved as 'video.mp4'.")

            else:
                st.error(f"Failed to download. HTTP Status Code: {response.status_code}")

        except Exception as e:
            st.error(f"An error occurred: {e}")


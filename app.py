import streamlit as st
import requests

# Title of the app
st.title("Video Viewer")

# Get the URL input from the user
video_url = st.text_input("Enter Video URL:")

# Button to process the URL
if st.button('Open Video'):
    # Define headers to simulate the referer
    headers = {
        "Referer": "https://xhamster19.com"
    }

    # Send GET request to the URL
    response = requests.get(video_url, headers=headers)

    if response.status_code == 200:
        # If the video is accessible, create an embedded link to open it in a new tab
        video_stream_url = video_url  # You can directly use the video URL or modify it if needed
        st.video(video_stream_url)  # Use Streamlit's video player to display the video
        st.success("Video is ready to view!")
    else:
        # Display error message if video is not accessible
        st.error(f"Failed to retrieve video. Status code: {response.status_code}")

import streamlit as st
from dotenv import load_dotenv
import os
import google.generativeai as genai
from youtube_transcript_api import YouTubeTranscriptApi

# Load environment variables
load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")

if not API_KEY:
    st.error("API key not found. Please set the GOOGLE_API_KEY in your environment variables.")
else:
    genai.configure(api_key=API_KEY)

# Improved Prompt for Google Gemini Pro
prompt = """
You are a highly efficient summarizer for YouTube videos, tasked with creating concise, insightful summaries.
For each video, provide a summary within 250 words that captures:
- Key points and main topics discussed.
- Important conclusions or recommendations made.
- Any notable facts or insights.
Format the summary in bullet points, and maintain a neutral, informative tone.
Here is the text to summarize:
"""

# Function to get the transcript data from YouTube videos
def extract_transcript_details(youtube_video_url):
    try:
        video_id = youtube_video_url.split("v=")[1].split("&")[0]
        transcript_data = YouTubeTranscriptApi.get_transcript(video_id)
        transcript = " ".join([item["text"] for item in transcript_data])
        return transcript
    except Exception as e:
        st.error("Error fetching transcript. Please check the video URL or try another video.")
        return None

# Function to generate a summary using Google Gemini Pro
def generate_gemini_content(transcript_text, prompt):
    try:
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(prompt + transcript_text)
        return response.text
    except Exception as e:
        st.error("Error generating summary. Please try again.")
        return None

# Streamlit App UI
st.title("YouTube Transcript to Detailed Notes Converter")
youtube_link = st.text_input("Enter YouTube Video Link:")

# Display video thumbnail
if youtube_link:
    try:
        video_id = youtube_link.split("v=")[1].split("&")[0]
        st.image(f"http://img.youtube.com/vi/{video_id}/0.jpg", use_column_width=True)
    except IndexError:
        st.error("Invalid YouTube link format. Please ensure it includes 'v=' parameter.")

# Button to fetch and display the summary
if st.button("Get Detailed Notes"):
    with st.spinner("Extracting transcript and generating summary..."):
        transcript_text = extract_transcript_details(youtube_link)

        if transcript_text:
            summary = generate_gemini_content(transcript_text, prompt)
            if summary:
                st.markdown("## Detailed Notes:")
                st.write(summary)

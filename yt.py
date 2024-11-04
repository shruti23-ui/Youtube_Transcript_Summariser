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

# Default prompt for Google Gemini Pro
base_prompt = """
You are an expert summarizer specifically trained for YouTube videos. Your task is to create comprehensive and clear summaries based on the transcript provided. For each video, ensure to include:

1. **Key Points**: Identify and outline the most important ideas discussed.
2. **Conclusions**: Highlight any significant conclusions or recommendations made by the speaker(s).
3. **Insights**: Note any notable facts, figures, or insights that are shared throughout the video.

The output should be tailored to the requested format. When creating bullet points, ensure that each point is succinct and clear. When creating a paragraph, maintain a coherent flow, linking ideas together logically.

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
        return response.text.strip()  # Strip whitespace from the response
    except Exception as e:
        st.error("Error generating summary. Please try again.")
        return None

# Streamlit App UI
st.title("YouTube Transcript to Detailed Notes Converter")
youtube_link = st.text_input("Enter YouTube Video Link:")

# User options for summary customization
st.sidebar.header("Summary Settings")
summary_length = st.sidebar.slider("Max Words for Summary", min_value=50, max_value=5000, value=250, step=50)
summary_format = st.sidebar.radio("Summary Format", options=["Bullet Points", "Paragraph"])

# Adjust the prompt based on user settings
if summary_format == "Bullet Points":
    prompt = base_prompt + f" Please summarize the following transcript in bullet points, keeping it concise and within {summary_length} words."
    
elif summary_format == "Paragraph":
    prompt = base_prompt + f" Please provide a coherent single paragraph summary, strictly avoiding bullet points, maintaining a formal tone, and staying within {summary_length} words."

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

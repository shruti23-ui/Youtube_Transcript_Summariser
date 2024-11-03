# YouTube Transcript to Detailed Notes Converter

This application uses Google Gemini API and YouTube Transcript API to convert YouTube video transcripts into concise, insightful summaries in note form. Designed to help users quickly understand the key points of a video, this Streamlit-based app generates summarized notes based on a customizable prompt.

## Features

- **Transcript Extraction**: Automatically extracts transcripts from YouTube videos using the video URL.
- **Summarization**: Uses Google Gemini API to generate a structured summary of the video’s content.
- **Customizable Prompt**: Generates summaries based on a predefined prompt to ensure concise, bullet-pointed notes.
- **Downloadable Notes**: Allows users to view and download the summary in an easy-to-read format.

## Requirements

- **Python 3.10+**
- **Streamlit**
- **dotenv**
- **google-generativeai**
- **YouTube Transcript API**
  
## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/yt-transcript-to-notes.git
   cd yt-transcript-to-notes
2. **Set Up a Virtual Environment**:
     ```bash
   python -m venv venv
   source venv/bin/activate      # On MacOS/Linux
   venv\Scripts\activate         # On Windows

3. **Install Required Packages**:
   ```bash
    pip install -r requirements.txt

4. **Set Up Environment Variables**:
   ```bash
   GOOGLE_API_KEY=your_google_api_key
## Usage

1. **Run the Streamlit App**:
   ```bash
   streamlit run app.py
2. **Use the App:** Open your web browser and go to http://localhost:8501. Enter a YouTube video link to extract the transcript, and click Get Detailed Notes to generate a summary based on the transcript.
   
3. **View and download notes:** The app displays a structured summary based on the extracted transcript. You can download the generated notes for easy reference.
   
## Contribution

Feel free to contribute by opening issues or submitting pull requests. 

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---
  

   


     

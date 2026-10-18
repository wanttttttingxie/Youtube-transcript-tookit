# Youtube-transcript

# YouTube Transcript Toolkit

A lightweight Python toolkit to bulk-download YouTube video transcripts, map them to video titles, and rename them for NLP/LLM ingestion.

## Features
- **Download:** Scrapes auto-generated English subtitles from any YouTube channel.
- **Map:** Uses `yt-dlp` to fetch video IDs, upload dates, and titles.
- **Rename:** Converts files from `YYYYMMDD_VIDEOID.txt` to `YYYYMMDD_VIDEOTITLE.txt` for easy reading.

## Setup
1. Clone this repo.
2. Install dependencies (Anaconda recommended):
   ```bash
   conda env create -f environment.yml
   conda activate deepseek_api

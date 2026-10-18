# YouTube Transcript Toolkit

A lightweight, professional Python toolkit to bulk-download YouTube video transcripts and prepare them for NLP (Natural Language Processing) or LLM (Large Language Model) ingestion.

## Features

- **Bulk Download:** Scrapes auto-generated English subtitles from any YouTube channel.
- **Single Video:** Download the transcript for just one specific video.
- **Smart Filtering:** Automatically skips videos that have already been downloaded (resumable).
- **Rate-Limit Protection:** Includes a randomized delay between downloads to prevent YouTube from blocking your IP.
- **Ready for LLMs:** Outputs clean `.txt` files without timestamps, perfect for feeding into AI models.

---

## ⚙️ Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/wanttttttingxie/Youtube-transcript-tookit.git
cd Youtube-transcript-tookit
```
### 2. Set up your Python environment
```bash
conda create -n transcript_env python=3.10
conda activate transcript_env
```
### 3. Install dependencies
```bash
pip install -r requirements.txt
```
## 🚀 How to Use
### Option A: Download an Entire Channel
By default, the script is configured to download the entire channel of @rareliquid.

Open download_rareliquid.py in your code editor.

Find line 8 and change the channel handle:
```python
CHANNEL_HANDLE = "@rareliquid"  # Change this to your target channel (e.g., "@MrBeast")
```
Save the file.

Run the script:
```bash
python download_rareliquid.py
```
The script will create a folder called rareliquid_transcripts and save all .txt files there.
### Option B: Download a Single Specific Video
```bash
python download_rareliquid.py "https://www.youtube.com/watch?v=nyot7FkYoqM"
```
(You can also just pass the video ID: python download_rareliquid.py nyot7FkYoqM)

### Option C: Run inside VS Code (No Terminal Typing)
1. Open the project folder in VS Code.

2. Press Cmd + Shift + P (Mac) and select Python: Select Interpreter.

3. Choose your Conda environment (e.g., Python 3.10 ('transcript_env')).

4. Open download_rareliquid.py.

5. Scroll down to line 45, change if len(sys.argv) > 1: to if True:

6. Change video_id = sys.argv[1] to video_id = "YOUR_VIDEO_ID_HERE".

7. Click the Play button (▶) in the top right corner.

## ⚠️ Troubleshooting
"YouTube is blocking requests from your IP" or "Too Many Requests"
YouTube heavily rate-limits automated scraping. If you start seeing errors, follow these steps:

1. Download a free VPN (like Proton VPN).

2. Connect to a server outside your university or home network.

3. Run the script again. It will automatically skip the videos you already downloaded and continue from where it left off.

"No supported JavaScript runtime could be found"
This is a harmless warning from yt-dlp. It will not stop your transcripts from downloading.





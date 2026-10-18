import yt_dlp
from youtube_transcript_api import YouTubeTranscriptApi
from pathlib import Path
import time
import random
import sys

CHANNEL_HANDLE = "@rareliquid"
OUTPUT_DIR = Path("rareliquid_transcripts")
DELAY_RANGE = (15, 25)

def get_video_ids():
    print(f"Fetching video list for {CHANNEL_HANDLE}...")
    ydl_opts = {'quiet': True, 'extract_flat': True, 'skip_download': True, 'ignoreerrors': True}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(f"https://www.youtube.com/{CHANNEL_HANDLE}/videos", download=False)
        return [entry['id'] for entry in info.get('entries', []) if entry and 'id' in entry]

def download_single_video(video_id):
    """Downloads the transcript for just one specific video."""
    OUTPUT_DIR.mkdir(exist_ok=True)
    
    # Check if it exists first
    if any(OUTPUT_DIR.glob(f"*_{video_id}.txt")):
        print(f"Skipped (already exists): {video_id}")
        return

    try:
        print(f"Downloading single video: {video_id}")
        api = YouTubeTranscriptApi()
        transcript = api.fetch(video_id, languages=["en"])
        text = "\n".join(segment.text.strip() for segment in transcript if segment.text.strip())
        
        # Save file
        with open(OUTPUT_DIR / f"00000000_{video_id}.txt", "w", encoding="utf-8") as f:
            f.write(text)
        print(f"Saved: {video_id}")
        
    except Exception as e:
        print(f"Error ({video_id}): {e}")

def main():
    # Check if you passed a video ID in the terminal
    if len(sys.argv) > 1:
        # If you typed: python download_rareliquid.py nyot7FkYoqM
        video_id = sys.argv[1]
        # Extract ID if a full URL was pasted
        if "v=" in video_id:
            video_id = video_id.split("v=")[1].split("&")[0]
            
        download_single_video(video_id)
        return

    # Otherwise, do the normal whole-channel download
    OUTPUT_DIR.mkdir(exist_ok=True)
    video_ids = get_video_ids()
    print(f"Found {len(video_ids)} videos. Starting download...")
    
    for vid in video_ids:
        if any(OUTPUT_DIR.glob(f"*_{vid}.txt")):
            print(f"Skipped (exists): {vid}")
            continue
            
        try:
            time.sleep(random.uniform(*DELAY_RANGE))
            print(f"Downloading: {vid}")
            api = YouTubeTranscriptApi()
            transcript = api.fetch(vid, languages=["en"])
            text = "\n".join(segment.text.strip() for segment in transcript if segment.text.strip())
            
            with open(OUTPUT_DIR / f"00000000_{vid}.txt", "w", encoding="utf-8") as f:
                f.write(text)
            print(f"Saved: {vid}")
            
        except Exception as e:
            print(f"Error ({vid}): {e}")

if __name__ == "__main__":
    main()
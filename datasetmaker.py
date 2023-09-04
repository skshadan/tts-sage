import os
import glob
import subprocess
from pathlib import Path
import whisper  # Replace with actual import

# Specify the path to the directory containing audio files
upload_dir = r'E:\\MyWorks\\DatasetMaker\\final'  # Use raw string to avoid escaping issues

# Create 'out' and 'splits' directories if they don't exist
output_dir = os.path.join(upload_dir, 'out')
splits_dir = os.path.join(output_dir, 'splits')
concatenated_dir = os.path.join(output_dir, 'concatenated')

os.makedirs(output_dir, exist_ok=True)
os.makedirs(splits_dir, exist_ok=True)
os.makedirs(concatenated_dir, exist_ok=True)

# Convert audio files to WAV format
audio_files = glob.glob(os.path.join(upload_dir, '*.mp3')) + glob.glob(os.path.join(upload_dir, '*.wav'))
for audio_file in audio_files:
    output_filename = os.path.splitext(os.path.basename(audio_file))[0] + '.wav'
    output_path = os.path.join(output_dir, output_filename)
    subprocess.run(['ffmpeg', '-i', audio_file, '-acodec', 'pcm_s16le', '-ar', '48000', '-ac', '1', output_path])

# Split audio files using SoX
start_audio_path = r'E:\\MyWorks\\DatasetMaker\\final\\start_audio.wav'  # Replace with your actual start audio file path
wav_files = glob.glob(os.path.join(output_dir, '*.wav'))
for wav_file in wav_files:
    subprocess.run(['sox', wav_file, os.path.join(splits_dir, os.path.basename(wav_file)), 'silence', '1', '0.5', '0.1%', '1', '0.5', '0.1%', ':', 'newfile', ':', 'restart'])

# Loop through the newly split files and add the 'start' audio at the beginning
split_files = glob.glob(os.path.join(splits_dir, '*.wav'))
for split_file in split_files:
    concat_filename = os.path.join(concatenated_dir, 'concat_' + os.path.basename(split_file))
    subprocess.run(['sox', start_audio_path, split_file, concat_filename])

# Remove small audio files (less than 15KB)
small_files = glob.glob(os.path.join(concatenated_dir, '*.wav'))
for small_file in small_files:
    if os.path.getsize(small_file) < 15000:  # Size in bytes
        os.remove(small_file)

# Load the Whisper model
model = whisper.load_model("medium.en")  # Replace with actual load function

# Initialize lists to store filenames and transcript text
all_filenames = []
transcript_text = []

# Open the metadata.csv file for writing
metadata_path = os.path.join(upload_dir, 'metadata.csv')
with open(metadata_path, 'w', encoding='utf-8') as outfile:
     for filepath in glob.glob(os.path.join(splits_dir, '*.wav')):
        base = os.path.splitext(os.path.basename(filepath))[0]  # Get the base filename without extension
        final_base = "concat_" + base
        all_filenames.append(base)
        result = model.transcribe(filepath)
        output = result["text"].lstrip()
        output = output.replace("\n", "")
        # Add '[ Surprise ]' to the beginning of every transcription
        modified_output = '[Surprise]' + output
        # Write filename (without extension), transcript, and cleaned transcript to the CSV file
        outfile.write(final_base + '|' + modified_output + '|' + modified_output + '\n')
        print(final_base + '|' + modified_output + '|' + modified_output + '\n')


print("Audio splitting and transcription completed.")
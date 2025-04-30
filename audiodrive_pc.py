import os
import json
import subprocess

# Define the path where your audio files are located
audio_dir = r'C:\Users\Lenovo\audio_repo'

# Define the path to the audio_files.json file
json_file_path = os.path.join(audio_dir, 'audio_files.json')

# Define the GitHub repository URL
repo_url = 'https://github.com/Hanumanthuvinitha/audio_repo'

# Step 1: Get the list of audio files (e.g., .mp3, .wav, .flac, .ogg)
audio_extensions = ['.mp3', '.wav', '.flac', '.ogg']
audio_files = []

# Walk through the audio directory and collect audio files
for root, dirs, files in os.walk(audio_dir):
    for file in files:
        if any(file.endswith(ext) for ext in audio_extensions):
            audio_files.append(file)

# Step 2: Update the audio_files.json
if os.path.exists(json_file_path):
    with open(json_file_path, 'r') as json_file:
        try:
            data = json.load(json_file)
            if isinstance(data, list):
                # Convert list to dict format
                data = {"audio_files": data}
        except json.JSONDecodeError:
            data = {"audio_files": []}
else:
    data = {"audio_files": []}

# Update the list with new audio files
data['audio_files'] = audio_files

# Save the updated JSON file
with open(json_file_path, 'w') as json_file:
    json.dump(data, json_file, indent=4)

# Step 3: Stage the new audio files and audio_files.json using Git
subprocess.run(['git', 'add', '.'], cwd=audio_dir)

# Step 4: Commit the changes
subprocess.run(['git', 'commit', '-m', 'Automatically update audio files and json'], cwd=audio_dir)

# Step 5: Push to GitHub
subprocess.run(['git', 'push', 'origin', 'main'], cwd=audio_dir)

print("✅ Audio files and JSON have been successfully pushed to GitHub.")

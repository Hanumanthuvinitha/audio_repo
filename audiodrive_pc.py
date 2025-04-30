import os
import json
from git import Repo

# Local Git repo path (should already be cloned)
repo_path = r'C:\Users\Lenovo\audio_repo'
audio_files_json = os.path.join(repo_path, 'audio_files.json')

# Get list of audio files
audio_extensions = ['.mp3', '.wav']
audio_files = [f for f in os.listdir(repo_path) if os.path.splitext(f)[1] in audio_extensions]

# Update audio_files.json
with open(audio_files_json, 'w') as f:
    json.dump(audio_files, f, indent=4)

# Git automation
repo = Repo(repo_path)
repo.git.add(A=True)
repo.index.commit("Updated audio files and audio_files.json")
origin = repo.remote(name='origin')
origin.push()

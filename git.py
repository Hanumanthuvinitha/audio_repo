import os

ignore_path = r'C:\Users\Lenovo\audio_repo\.gitignore'

if not os.path.exists(ignore_path):
    with open(ignore_path, 'w') as f:
        f.write("client_secrets.json\n")
else:
    with open(ignore_path, 'r+') as f:
        content = f.read()
        if "client_secrets.json" not in content:
            f.write("\nclient_secrets.json\n")

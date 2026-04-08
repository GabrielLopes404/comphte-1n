import zipfile
import os
import sys

# Hardcoded project directory
project_dir = '/vercel/share/v0-project'

# Try multiple paths
possible_paths = [
    f'{project_dir}/escortwp.zip',
    '/vercel/path0/escortwp.zip',
    '/vercel/path1/escortwp.zip'
]

# Also scan /vercel for any zip files
import glob
for g in glob.glob('/vercel/**/escortwp.zip', recursive=True):
    possible_paths.insert(0, g)

zip_path = None
for p in possible_paths:
    if os.path.exists(p):
        zip_path = p
        print(f"Found ZIP at: {p}")
        break

if not zip_path:
    print(f"Project dir: {project_dir}")
    print(f"Files in project: {os.listdir(project_dir) if os.path.exists(project_dir) else 'N/A'}")
    print(f"Searching /vercel...")
    for root, dirs, files in os.walk('/vercel'):
        for f in files:
            if f.endswith('.zip'):
                print(f"Found: {os.path.join(root, f)}")
    sys.exit(1)

extract_to = '/vercel/share/v0-project/extracted'

os.makedirs(extract_to, exist_ok=True)

with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(extract_to)
    print(f"Extracted {len(zip_ref.namelist())} files")
    for name in zip_ref.namelist()[:50]:
        print(name)
    if len(zip_ref.namelist()) > 50:
        print(f"... and {len(zip_ref.namelist()) - 50} more files")

import zipfile
import os

zip_path = '/vercel/share/v0-project/escortwp.zip'
extract_to = '/vercel/share/v0-project/extracted'

os.makedirs(extract_to, exist_ok=True)

with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(extract_to)
    print(f"Extracted {len(zip_ref.namelist())} files")
    for name in zip_ref.namelist()[:50]:
        print(name)
    if len(zip_ref.namelist()) > 50:
        print(f"... and {len(zip_ref.namelist()) - 50} more files")

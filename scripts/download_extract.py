import urllib.request
import zipfile
import io
import os

url = "https://v0chat-agent-data-prod.s3.us-east-1.amazonaws.com/vm-binary/TzV2NFuFMZH/ff97873d97681581dc16d650fa02fff42dfe007cc42aa882db35feca86a71584.zip?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA52KF4VHQDTZ5RDMT%2F20260408%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260408T180653Z&X-Amz-Expires=3600&X-Amz-Signature=c490ef0c1154cc16277b2e91dbf286a0d2df8333d90159246465b73dce031ba6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject"

extract_to = "/tmp/escortwp"

print("Downloading ZIP...")
response = urllib.request.urlopen(url)
zip_data = response.read()
print(f"Downloaded {len(zip_data)} bytes")

print("Extracting...")
os.makedirs(extract_to, exist_ok=True)
with zipfile.ZipFile(io.BytesIO(zip_data), 'r') as zip_ref:
    zip_ref.extractall(extract_to)
    files = zip_ref.namelist()
    print(f"Extracted {len(files)} files")
    for name in files[:100]:
        print(name)
    if len(files) > 100:
        print(f"... and {len(files) - 100} more files")

print(f"\nExtracted to: {extract_to}")
print(f"Contents: {os.listdir(extract_to)}")

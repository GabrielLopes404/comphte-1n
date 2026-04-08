import urllib.request
import zipfile
import io
import os

# URL do ZIP
url = "https://v0chat-agent-data-prod.s3.us-east-1.amazonaws.com/vm-binary/TzV2NFuFMZH/c64210fb1267eea713f4d6901f3c3b60dbfd3ffb2330e54b306512a94f044cd5.zip?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA52KF4VHQDTZ5RDMT%2F20260408%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260408T180855Z&X-Amz-Expires=3600&X-Amz-Signature=5d13b3a1e700cd56e7d73ab81c21e600cfbcdacf6537c37cfc5ad1a7447011ea&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject"

project_dir = "/vercel/share/v0-project"

print("Downloading ZIP from S3...")
try:
    response = urllib.request.urlopen(url)
    zip_data = response.read()
    print(f"Downloaded {len(zip_data)} bytes")
    
    # Extract
    with zipfile.ZipFile(io.BytesIO(zip_data)) as zf:
        files = zf.namelist()
        print(f"Found {len(files)} files in ZIP")
        
        # List some files
        for f in files[:20]:
            print(f"  - {f}")
        if len(files) > 20:
            print(f"  ... and {len(files) - 20} more files")
        
        # Extract to project directory
        zf.extractall(project_dir)
        print(f"\nExtracted all files to {project_dir}")
        
except Exception as e:
    print(f"Error: {e}")

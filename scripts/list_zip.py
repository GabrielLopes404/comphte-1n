import urllib.request
import zipfile
import io
import os

url = "https://blobs.vusercontent.net/blob/document-zj6gcvCpO4Mv1mQdxDkXl8M6JRhHZ8.zip"

print("Downloading ZIP...")
response = urllib.request.urlopen(url)
zip_data = response.read()
print(f"Downloaded {len(zip_data)} bytes")

# List all files
with zipfile.ZipFile(io.BytesIO(zip_data), 'r') as z:
    files = z.namelist()
    print(f"\nTotal files: {len(files)}")
    
    # Group by extension
    extensions = {}
    for f in files:
        if '.' in f:
            ext = f.split('.')[-1].lower()
        else:
            ext = 'no_ext'
        extensions[ext] = extensions.get(ext, 0) + 1
    
    print("\nFiles by extension:")
    for ext, count in sorted(extensions.items(), key=lambda x: -x[1]):
        print(f"  .{ext}: {count}")
    
    # List PHP files
    php_files = [f for f in files if f.endswith('.php')]
    print(f"\nPHP files ({len(php_files)}):")
    for f in sorted(php_files)[:50]:
        print(f"  {f}")
    if len(php_files) > 50:
        print(f"  ... and {len(php_files) - 50} more")
    
    # Extract and save to project directory
    print("\n\nExtracting files...")
    output_dir = "/vercel/share/v0-project/escortwp"
    
    for name in z.namelist():
        # Skip directories and __MACOSX
        if name.endswith('/') or '__MACOSX' in name:
            continue
        
        # Get relative path (remove escortwp/ prefix if present)
        rel_path = name
        if rel_path.startswith('escortwp/'):
            rel_path = rel_path[9:]
        
        target_path = os.path.join(output_dir, rel_path)
        target_dir = os.path.dirname(target_path)
        
        # Create directory
        os.makedirs(target_dir, exist_ok=True)
        
        # Extract file
        with z.open(name) as src:
            with open(target_path, 'wb') as dst:
                dst.write(src.read())
    
    print(f"Extracted to {output_dir}")
    
    # List extracted structure
    extracted_files = []
    for root, dirs, files in os.walk(output_dir):
        for f in files:
            extracted_files.append(os.path.join(root, f))
    
    print(f"\nExtracted {len(extracted_files)} files")

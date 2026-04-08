import shutil
import os

src = '/tmp/escortwp/escortwp'
dst = '/vercel/share/v0-project/escortwp'

if os.path.exists(dst):
    shutil.rmtree(dst)

shutil.copytree(src, dst)
print(f"Copied {src} to {dst}")

# List PHP files
for root, dirs, files in os.walk(dst):
    for f in files:
        if f.endswith('.php'):
            print(os.path.join(root, f))

const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

const zipPath = '/vercel/share/v0-project/escortwp.zip';
const extractPath = '/vercel/share/v0-project';

try {
  // Extract the zip file
  execSync(`unzip -o "${zipPath}" -d "${extractPath}"`, { stdio: 'inherit' });
  console.log('Extraction completed successfully!');
  
  // List extracted files
  const files = execSync(`find "${extractPath}" -type f -name "*.php" -o -name "*.js" -o -name "*.css" -o -name "*.html" | head -100`).toString();
  console.log('Extracted files:\n', files);
} catch (error) {
  console.error('Error extracting:', error.message);
}

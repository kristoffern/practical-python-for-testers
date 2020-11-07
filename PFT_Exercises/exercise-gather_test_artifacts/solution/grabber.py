import os
import shutil
import ftplib
import zipfile
from datetime import datetime

if __name__ == '__main__':
    # Remove the target directory if it exists
    if os.path.isdir('/tmp/testartifacts'):
        shutil.rmtree('/tmp/testartifacts')
    # Create an empty directory
    os.makedirs('/tmp/testartifacts')
    # Copy the files
    shutil.copy('/opt/PFT/firstLarge', '/tmp/testartifacts')
    shutil.copy('/opt/PFT/secondLarge', '/tmp/testartifacts')

    # Generate file name for the zip file
    filename = datetime.now().strftime('testartifacts_%Y%m%d_%H%M%S.zip')
    filepath = os.path.join('/tmp/', filename)

    # Create ZIP file and write contents
    zipf = zipfile.ZipFile(filepath, 'w', zipfile.ZIP_DEFLATED)
    zipf.write('/tmp/testartifacts/firstLarge')
    zipf.write('/tmp/testartifacts/secondLarge')
    zipf.close()

    # Use FTP to upload the files
    session = ftplib.FTP('127.0.0.1', 'tester', 'python')
    session.cwd('upload')
    trfile = open(filepath, 'rb')
    session.storbinary('STOR ' + filename, trfile)

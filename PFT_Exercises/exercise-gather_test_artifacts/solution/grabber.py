import ftplib
import glob
import os
import shutil
import zipfile

from datetime import datetime

testartifacts_folder = '/tmp/testartifacts'

if(os.path.isdir(testartifacts_folder)):
    shutil.rmtree(testartifacts_folder)
os.mkdir(testartifacts_folder)

log_folders = ['/opt/PFT/DataDigger', '/home/pft/output', '/opt/SUT/logs']

for folder in log_folders:
    found_files = glob.glob(os.path.join(folder, '*.log'))
    for log_file in found_files:
        shutil.copy(log_file, testartifacts_folder)

now = datetime.now()
filename = now.strftime('testartifacts_%Y%m%d_%H%M%S.zip')

zipf = zipfile.ZipFile(filename, 'w', zipfile.ZIP_DEFLATED)
for log_file in glob.glob(os.path.join(testartifacts_folder, '*.log')):
    zipf.write(log_file)
zipf.close()

session = ftplib.FTP('127.0.0.1', 'tester', 'python')
session.cwd('upload')
local_file = open(filename, 'rb')
session.storbinary('STOR {}'.format(filename), local_file)

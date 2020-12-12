import ftplib
import glob
import os
import shutil
import zipfile
from datetime import datetime

# Create a folder to copy the artifacts into

# Define the list of folders to look in for log files
# A for loop for every folder in the list
	
	# use glob.glob() to list all .log files in folder

	# A for loop for every file found by glob
		# Copy the file into testartifacts folder

# Create a filename with the timestamp
# And extend the path to include your testartifacts folder

# Open a zipfile for writing
# For every log-file in testartifacts 
# Write the files into the zip archive. 

# Dont forget to close the zip archive
# Open an ftp session and upload the file

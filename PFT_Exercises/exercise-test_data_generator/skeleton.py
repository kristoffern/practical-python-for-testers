import os
import shutil
import random
import requests


def add_data_to_folder(folder, names, states, files):
    pass #remove this line once you fill in the method
    # Retrieve a random first and last name from names, and state from states
    # Write the data into data.txt in folder
    # Find a random picture from files
    # Copy the picture into the data folder


def add_filepaths_into_list(path):
    # Create empty list for filepaths to pictures
    # Use os.walk to travers the folder 'faces' and add files with full path into list
    return pictures


if __name__ == "__main__":
    # Define the base_folder here to reuse

    # Check if base_folder exists if so remove and create new
    
    # Call add_filepaths_into_list() and assign result to variable picture

    # Create folder (/tmp/testdata)
    for first_level in range(0, 5):
        # Create top level folder in /tmp/testdata – use os.makedirs & os.path.join
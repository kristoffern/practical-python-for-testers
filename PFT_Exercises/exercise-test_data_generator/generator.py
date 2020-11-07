import os
import csv
import tarfile
import random
import shutil


def csv_to_list(filename, fields):
    csvfile = open(filename, 'rtU')
    reader = csv.DictReader(csvfile)
    my_list = []
    for line in reader:
        value = ""
        for field in fields:
            value += line[field] + ' '
        my_list.append(value.strip())
    csvfile.close()
    return my_list


def extract_faces(filename, foldername):
    if os.path.isdir(foldername):
        print("tar file seems to be already extracted")
        return
    tfile = tarfile.open(filename, 'r')
    tfile.extractall()
    print("tarfile extracted")


def get_faces(root_folder):
    """
    Get all jpg:s from a folder, recursively
    """
    faces = []
    for folder, folders, files in os.walk(root_folder):
        for filename in files:
            if filename.endswith(".jpg"):
                faces.append(os.path.join(
                    folder, filename
                ))
    return faces


def write_data(faces, states, names):
    if os.path.exists("target"):
        shutil.rmtree("target")
    os.mkdir("target")
    for parent in range(5):
        os.mkdir(os.path.join("target", str(parent)))
        for child in range(5):
            dest = os.path.join("target", str(parent),
                                str(child))
            os.mkdir(dest)
            # copy jpg
            shutil.copy(random.choice(faces),
                        os.path.join(dest, 'face.jpg'))
            # write text file
            data = open(os.path.join(dest, 'data.txt'), 'wt')
            data.write("Name: " + random.choice(names) + '\n')
            data.write("State: " + random.choice(states) + '\n')


def main():
    # Extract faces if not already done
    extract_faces('faces.tgz', 'lfw')
    names = csv_to_list('names.csv', ['FirstName', 'LastName'])
    states = csv_to_list('states.csv', ['State'])
    faces = get_faces('lfw')
    write_data(faces, states, names)


if __name__ == "__main__":
    main()

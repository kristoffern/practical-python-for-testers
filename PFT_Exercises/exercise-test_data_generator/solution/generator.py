import os
import requests
import shutil
import random


def add_testdata(path, pictures):

    response = requests.get('http://www.slumpa.net/api')
    person = response.json()

    with open(os.path.join(path, 'person.txt'), 'wt') as f:

        f.write('Name:\t{}\n \
Gender:\t{}\n \
Address:\t{}\n \
Zip-code:\t{}\n'.format(person['name'], \
                        person['gender'], \
                        person['address']['street'], \
                        person['address']['zipcode']))

    face = random.choice(pictures)
    shutil.copyfile(face, os.path.join(path, 'face.jpg'))


def add_filepaths_into_list(path):
    pictures = []
    for folder, dirs, files in os.walk(path):
        for file in files:
            pictures.append(os.path.join(folder, file))
    return pictures


if __name__ == '__main__':

    base_folder = '/tmp/testdata/'

    if os.path.exists(base_folder):
        shutil.rmtree(base_folder)
    os.makedirs(base_folder)

    pictures = add_filepaths_into_list('./faces')

    for i in range(5):
        new_folder = os.path.join(base_folder, str(i))
        os.makedirs(new_folder)
        add_testdata(new_folder, pictures)
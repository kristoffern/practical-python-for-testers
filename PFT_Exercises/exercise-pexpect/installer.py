import sys
import random
import time

'''
Installation path [/opt/esconfs]:
Full or light installation [Full/Light]:
Deploy web server  [Y/N]:
    On which port [80]:
    Admin user account [admin]:
    Admin acount password []:
Backup previous data [Y/N]:
    Backup path [~/esconfs_backup/]:
Install with these setting [Y/N]:
'''

if __name__ == '__main__':

    installation_options = {}

    installation_options['install_path'] = input(
        " Installation path [/opt/esconfs]: ")
    if installation_options['install_path'] == '':
        installation_options['install_path'] = '/opt/esconfs'

    installation_options['full_light'] = input(
        " Full or light installation [Full/Light]: ")
    while installation_options['full_light'] == '':
        print("  Please answer: Full or Light")
        installation_options['full_light'] = input(
            " Full or light installation [Full/Light]: ")

    if installation_options['full_light'] == 'Full':

        installation_options['deploy'] = input(" Deploy web server  [Y/N]: ")
        while installation_options['deploy'] != 'Y' and installation_options['deploy'] != 'N':
            print("  Please answer: Y or N")
            installation_options['deploy'] = input(
                " Deploy web server  [Y/N]: ")

        if installation_options['deploy'] == 'Y':

            installation_options['port'] = input(" On which port [80]: ")
            if installation_options['port'] == '':
                installation_options['port'] = '80'

    installation_options['admin'] = input(" Admin user account [admin]: ")
    if installation_options['admin'] == '':
        installation_options['admin'] = 'admin'

    installation_options['password'] = input(" Admin acount password []:  ")

    installation_options['backup'] = input(" Backup previous data [Y/N]: ")
    while installation_options['backup'] != 'Y' and installation_options['backup'] != 'N':
        print("  Please answer: Y or N")
        installation_options['backup'] = input(" Backup previous data [Y/N]: ")

    if installation_options['backup'] == 'Y':
        installation_options['backup_path'] = input(
            " Backup path [~/esconfs_backup/]: ")
        if installation_options['backup_path'] == '':
            installation_options['backup_path'] = '~/esconfs_backup/'

    print("\n\n")
    print("\t----------Installation Path--------")
    if 'install_path' in installation_options.keys():
        print("\t[Install Path]: " + installation_options['install_path'])
    if 'full_light' in installation_options.keys():
        print("\t[Full Light]: " + installation_options['full_light'])
    if 'deploy' in installation_options.keys():
        print("\t[Deploy]: " + installation_options['deploy'])
    if 'port' in installation_options.keys():
        print("\t[Port]: " + installation_options['port'])
    if 'admin' in installation_options.keys():
        print("\t[Admin]: " + installation_options['admin'])
    if 'password' in installation_options.keys():
        print("\t[Password]: ****")
    if 'backup' in installation_options.keys():
        print("\t[Backup]: " + installation_options['backup'])
    if 'backup_path' in installation_options.keys():
        print("\t[Backup Path]: " + installation_options['backup_path'])
    print("\t-----------------------------------")
    print("\n")

    installation_options['go_ahead'] = input(
        " Install with these setting [Y/N]:  ")
    while installation_options['go_ahead'] != 'Y' and installation_options['backup'] != 'N':
        print("  Please answer: Y or N")
        installation_options['go_ahead'] = input(
            " Install with these setting [Y/N]:  ")

    if installation_options['go_ahead'] == 'Y':
        print("Starting installation")
    else:
        print("Aborting installation")
        sys.exit(0)

    time.sleep(random.randint(0, 10))

    if 'port' in installation_options.keys() and 'admin' in installation_options.keys():
        if installation_options['port'] == '8080' and installation_options['admin'] == 'admin':
            print("An error occured during installation, please see installation log.")
            sys.exit(2)
    print("Finished installation succesfully")

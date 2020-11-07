import pexpect
import sys

if __name__ == '__main__':
    # spawnu is neccesary to log to stdout
    proc = pexpect.spawnu('python3 installer.py')
    proc.logfile = sys.stdout

    proc.expect('Installation path')
    proc.sendline('/tmp/esconfs')

    proc.expect(r'Full or light installation \[Full/Light\]:')
    proc.sendline('Full')

    proc.expect(r'Deploy web server  \[Y/N\]:')
    proc.sendline('Y')

    proc.expect(r'On which port \[80\]:')
    proc.sendline('80')

    proc.expect(r'Admin user account \[admin\]:')
    proc.sendline('admin')

    proc.expect(r'Admin acount password \[\]:')
    proc.sendline('esconfs')

    proc.expect(r'Backup previous data \[Y/N\]:')
    proc.sendline('Y')

    proc.expect(r'Backup path \[~/esconfs_backup/\]:')
    proc.sendline('\n')

    proc.expect(r'Install with these setting \[Y/N\]:')
    proc.sendline('Y')

    whichOption = proc.expect(
        ['Finished installation succesfully', 'An error occured during installation'])

    print("\n---- Test Runner Done ---- \n")

    if whichOption == 0:
        print("Application claims to have been installed with no problem.")
    elif whichOption == 1:
        print("An error occured during installation, check into it.. like now!")

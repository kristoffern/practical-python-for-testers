import sys
import pexpect

child = pexpect.spawnu('python3 installer.py')
child.logfile = sys.stdout

child.expect('Installation path')
child.sendline('/tmp/what')
child.expect('Full or light installation')
child.sendline('Full')

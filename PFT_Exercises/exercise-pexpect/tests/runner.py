import pexpect
import sys
from test_paths import HappyPath, UnhappyPath


def runTestcase(questions, answers):
    child = pexpect.spawnu('/usr/bin/python3 installer.py')
    child.logfile = sys.stdout

    for i in range(len(questions)):
        child.expect(questions[i])
        child.sendline(answers[i])

    result = child.expect(['.*succesfully.*', '.*error.*'])

    if result == 0:
        print("Yay, probably worked according to installer")
    elif result == 1:
        print("Look into possible bug!")

    return result


runTestcase(HappyPath.questions, HappyPath.answers)
runTestcase(UnhappyPath.questions, UnhappyPath.answers)

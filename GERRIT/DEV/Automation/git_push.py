import time
import subprocess

branch_repo = "Python_R1A"

subprocess.Popen("git add .",shell=True)
subprocess.Popen("git commit -m " + str(time.time()))
subprocess.Popen("git push origin HEAD:" + str(branch_repo))

import os
import subprocess
import sys

if(len(sys.argv) > 2):
    os.system("echo Too many arguments")

repo_name = sys.argv[1]
goto_dir = "cd ../../" + repo_name + " && "
os.mkdir("../../" + repo_name)
os.system(goto_dir + "git init")
os.system(goto_dir + "git branch -M main")
os.system(goto_dir + "copy nul README.md && echo # " + repo_name + "> README.md")
os.system(goto_dir + "git add .")
os.system(goto_dir + 'git commit -m "initial commit"')
with open("../../token.txt", "r") as token:
    subprocess.run(["gh", "auth", "login", "--with-token"],  stdin=token)
    subprocess.run(["gh", "repo", "create", "--public", "--source=../../" + repo_name, "--remote=upstream", "--push"])

os.system(goto_dir + "git remote add origin https://github.com/albindahlberg/" + repo_name + ".git")
os.system(goto_dir + "git push origin main")
os.system(goto_dir + "code .")
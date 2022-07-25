import os
import subprocess
import sys

if(len(sys.argv) > 2):
    os.system("echo Too many arguments")
    exit(0)

repo_name = sys.argv[1]
goto_dir = "cd Documents/Github/" + repo_name + " && "
os.mkdir("Documents/Github/" + repo_name)
os.system("git init Documents/Github/" + repo_name)
os.system(goto_dir + "git branch -M main")
os.system(goto_dir + "copy nul README.md && echo # " + repo_name + "> README.md")
os.system(goto_dir + "git add .")
os.system(goto_dir + 'git commit -m "initial commit"')
with open("Documents/Github/token.txt", "r") as token:
    subprocess.run(["gh", "auth", "login", "--with-token"], stdin=token)
    subprocess.run(["gh", "repo", "create", "--public", "--source=Documents/Github/" + repo_name, "--remote=upstream", "--push"])

os.system(goto_dir + "git remote add origin https://github.com/albindahlberg/" + repo_name + ".git")
os.system(goto_dir + "git push origin main")
os.system(goto_dir + "code .")
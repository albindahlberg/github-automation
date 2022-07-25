import os
import subprocess
import sys

if(len(sys.argv) > 2):
    os.system("echo Too many arguments")
    exit(0)

repo_name = sys.argv[1]

# Delete repo from Github
with open("Documents/Github/token.txt", "r") as token:
    subprocess.run(["gh", "auth", "login", "--with-token"], stdin=token)
    subprocess.run(["gh", "repo", "delete", "--confirm", repo_name])

# Delete directory from computer
os.system("rmdir /s Documents\\Github\\" + repo_name)
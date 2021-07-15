
import subprocess

git_repo = "https://github.com/rodrigo-veloso/hermione.git"
branch = 'master'
	
subprocess.call(["git","init"])
subprocess.call(["git","remote","add","origin",git_repo])
subprocess.call(["git","pull","origin",branch])



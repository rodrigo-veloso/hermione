
import subprocess

branch = 'test'
commit_name = 'test'
remote_name = 'origin'	

subprocess.call(["git","checkout","-b",branch])
subprocess.call(["git","add","."])
subprocess.call(["git","commit","-m",commit_name])
subprocess.call(["git","push","--set-upstream","origin",branch])



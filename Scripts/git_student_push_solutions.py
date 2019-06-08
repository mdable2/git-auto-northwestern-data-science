'''
git_student_push_solutions --> python git_student_push_solutions.py [module_num] [lesson_num]
    * Takes [module_num] [lesson_num], pull from instructor repo master, update student repo [module_num] [lesson_num]
     with activity solutions for student activites.
'''

from subprocess import Popen, PIPE
import shlex
import sys
from git import Repo
import os

repo_path = os.path.join(os.getcwd(), "../")
file_path = os.path.join(os.getcwd(), "test.txt")

repo = Repo(repo_path)
master = repo.heads.master
print(repo.git.add("."))
print(repo.git.commit(m="test message"))
# print(repo.git.status())
# print(repo.git.push())
cmd = ['git', 'push']
p = Popen(cmd)
p.wait()
print("Successfuly pushed from script!")


# print(repo)
# assert not repo.bare
# command_line = sys.argv
# module_num = command_line[1]
# lesson_num = command_line[2]

# p = Popen(["git", "pull"], stdout=PIPE)
# stuff = p.communicate()
# print(stuff)

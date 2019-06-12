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
import shutil

def copy_and_check(src, dst):
    if os.path.isdir(src):
        # Copy over entire directory
        shutil.copytree(src, dst)

repo_path = os.path.join(os.getcwd(), "../")
command_line = sys.argv
module_num = command_line[1]
lesson_num = command_line[2]
commit_message = f"Added solutions for module: {module_num} lesson: {lesson_num}"

# Standard paths for teacher and student modules
modules_path_teacher = os.path.join("..", "..", "DataViz-Lesson-Plans", "01-Lesson-Plans")
#################### FOR TESTING ##############################
modules_path_student = os.path.join("..", "..", "git-auto-northwestern-data-science", "Scripts", "Activities")
# modules_path_student = os.path.join("..", "..", "NUCHI201905DATA2")

# Get directory that corresponds to entered module_num
directories = os.listdir(modules_path_teacher)
directory = [f for f in directories if str(module_num) in f]
directory_path = os.path.join(directory[0], str(lesson_num), "Activities")

# Append directory_path to the correct module_num to the src and dst paths
src_path_teacher = os.path.join(modules_path_teacher, directory_path)
#################### FOR TESTING ##############################
dst_path_student = modules_path_student
# dst_path_student = os.path.join(modules_path_student, directory_path)

# Get all file names from src and dst file paths
src_all_files_teacher = os.listdir(src_path_teacher)
dst_all_files_student = os.listdir(dst_path_student)

for f in src_all_files_teacher:
    # This means it a student directory
    if "Stu" in f:
        # If not created, create the directory in destination
        if f not in dst_all_files_student:
            new_directory = os.path.join(dst_path_student, f)
            print("NEW: " + new_directory)
            os.mkdir(new_directory)
        src_path = os.path.join(src_path_teacher, f, "Solved")
        dst_path = os.path.join(dst_path_student, f, "Solved")
        copy_and_check(src_path, dst_path)
        
repo = Repo(repo_path)
assert not repo.bare
master = repo.heads.master

try:
    repo.git.add(".")
    repo.git.commit(m = commit_message)
    cmd = ['git', 'push']
    p = Popen(cmd)
    p.wait()
    print("Successfuly pushed from script!")
except:
    print("Error occured. Git script ran unsuccessfully!")

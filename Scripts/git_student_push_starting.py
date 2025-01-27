'''
git_student_push_starting --> python git_student_push_starting.py [module_num]
    * Takes [module_num], pull from instructor repo master, check if student repo has [module_num] folder.
        * If student repo [module_num] folder present, check difference and copy over all excluded files.
        * If student repo [module_num] folder not present, create folder and copy over all necessary files.
        * Files to include: README.md, StudentGuide.md, VideoGuide.md, Lesson 1 - 3, and a homework folder.
        * In Lesson 1 - 3, have all activities copied over and exlude answers for student activities.
        * Create homework folder and put in the Instructions folder from teacher repo.

ITERATION #1: * Assume that the [module_num] is not present and that you want to create all the folders WITHOUT solutions for student activities.
              * If it is present, this script does nothing.
              * Does not include homework folder.
'''

from subprocess import Popen, PIPE
import shlex
import sys
from git import Repo
import os
import shutil
from pathlib import Path

#################### FOR TESTING ##############################
#repo_path = os.path.join(os.getcwd(), "../")
repo_path = os.path.join("..", "..", "NUCHI201905DATA2")
command_line = sys.argv
module_num = command_line[1]
commit_message = f"Added folders for module: {module_num} via super cool script!"

# Standard paths for teacher and student modules
modules_path_teacher = os.path.join("..", "..", "DataViz-Lesson-Plans", "01-Lesson-Plans")
#################### FOR TESTING ##############################
#modules_path_student = os.path.join("..", "..", "git-auto-northwestern-data-science", "Scripts", "Activities")
modules_path_student = os.path.join("..", "..", "NUCHI201905DATA2")

# Get directory that corresponds to entered module_num
directories = os.listdir(modules_path_teacher)
directory = [f for f in directories if str(module_num) in f]
directory_path = os.path.join(directory[0])

# Append directory_path to the correct module_num to the src and dst paths
src_path_teacher = os.path.join(modules_path_teacher, directory_path)
#################### FOR TESTING ##############################
#dst_path_student = modules_path_student
dst_path_student = os.path.join(modules_path_student, directory_path)

# Make directories /1 /2 /3
for i in range(1, 4):
    new_directory = os.path.join(dst_path_student, str(i))
    os.mkdir(new_directory)

# Get all file names from dst file path
dst_all_files_student = os.listdir(dst_path_student)

##### BUG: If the newly created folder only has a README.md, it gives:
# FileNotFoundError: [Errno 2] No such file or directory: '..\\..\\NUCHI201905DATA2\\06-Python-APIs\\1\\07-Stu_Explore_OMDb_API\\README.md'
# Not too sure what is going on.

# Collect files from directories /1 /2 /3
for i in range(0, 3):
    # Get all file names from src file paths
    sub_directory = os.path.join(str(i + 1), "Activities")
    files = os.listdir(os.path.join(src_path_teacher, sub_directory))
    for f in files:
        if "Stu" in f:
            # If student, step into directory and add all directories/files if NOT solution
            src_path_sub = os.path.join(src_path_teacher, sub_directory, f)
            sub_files = os.listdir(src_path_sub)
            sub_files.sort(reverse = True)

            for sub_f in sub_files:
                if not sub_f == "Solved":
                    src_path = os.path.join(src_path_sub, sub_f)
                    if os.path.isdir(src_path):
                        dst_path = os.path.join(dst_path_student, str(i + 1), f, sub_f)
                        shutil.copytree(src_path, dst_path)
                    else:
                        dst_path = os.path.join(dst_path_student, str(i + 1), f, sub_f)
                        Path(dst_path).touch()
                        shutil.copy(src_path, dst_path)
        else:
            # Go through those files - if instructor, add it straight away
            src_path = os.path.join(src_path_teacher, sub_directory, f)
            dst_path = os.path.join(dst_path_student, str(i + 1), f)
            shutil.copytree(src_path, dst_path)

repo = Repo(repo_path)
assert not repo.bare
master = repo.heads.master

try:
    repo.git.add(".")
    repo.git.commit(m = commit_message)
    cmd = ['git', 'push']
    # p = Popen(cmd)
    # p.wait()
    # print("Successfuly pushed from script!")
except:
    print("Error occured. Git script ran unsuccessfully!")
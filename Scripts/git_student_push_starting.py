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

#################### FOR TESTING ##############################
repo_path = os.path.join(os.getcwd(), "../")
# repo_path = os.path.join("..", "..", "NUCHI201905DATA2")
command_line = sys.argv
module_num = command_line[1]
commit_message = f"Added folders for module: {module_num}."

# Standard paths for teacher and student modules
modules_path_teacher = os.path.join("..", "..", "DataViz-Lesson-Plans", "01-Lesson-Plans")
#################### FOR TESTING ##############################
modules_path_student = os.path.join("..", "..", "git-auto-northwestern-data-science", "Scripts", "Activities")
# modules_path_student = os.path.join("..", "..", "NUCHI201905DATA2")

# Get directory that corresponds to entered module_num
directories = os.listdir(modules_path_teacher)
directory = [f for f in directories if str(module_num) in f]
directory_path = os.path.join(directory[0])

# Append directory_path to the correct module_num to the src and dst paths
src_path_teacher = os.path.join(modules_path_teacher, directory_path)
#################### FOR TESTING ##############################
dst_path_student = modules_path_student
# dst_path_student = os.path.join(modules_path_student, directory_path)

# Make directories /1 /2 /3
for i in range(1, 4):
    new_directory = os.path.join(dst_path_student, str(i))
    os.mkdir(new_directory)

# Get all file names from dst file path
dst_all_files_student = os.listdir(dst_path_student)

# Collect files from directories /1 /2 /3
for i in range(0, 3):
    # Get all file names from src file paths
    sub_directory = os.path.join(str(i + 1), "Activities")
    files = os.listdir(os.path.join(src_path_teacher, sub_directory))
    for f in files:
        if "Stu" in f:
            # If student, step into directory and add all directories/files if NOT solution
            pass
        else:
            # Go through those files - if instructor, add it straight away
            src_path = os.path.join(src_path_teacher, sub_directory, f)
            dst_path = os.path.join(dst_path_student, str(i + 1), f)
            shutil.copytree(src_path, dst_path)



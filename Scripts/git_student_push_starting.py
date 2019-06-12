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

# Get all file names from src and dst file paths
src_all_files_teacher = os.listdir(src_path_teacher)
dst_all_files_student = os.listdir(dst_path_student)

print("scr: " + str(src_all_files_teacher))
print("dst: " + str(dst_all_files_student))

# Make directories /1 /2 /3
# Collect files from /1
# Go through those files - if instructor, add it straight away
# 
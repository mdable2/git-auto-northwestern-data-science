# Auto git updates for Northwestern Data Science Bootcamp

Python scripts to programatically do the following:

1. git_student_push_starting --> python git_student_push_starting.py [module_num]
    * Takes [module_num], pull from instructor repo master, check if student repo has [module_num] folder.
        * If student repo [module_num] folder present, check difference and copy over all excluded files.
        * If student repo [module_num] folder not present, create folder and copy over all necessary files.
        * Files to include: README.md, StudentGuide.md, VideoGuide.md, Lesson 1 - 3, and a homework folder.
        * In Lesson 1 - 3, have all activities copied over and exlude answers for student activities.
        * Create homework folder and put in the Instructions folder from teacher repo.

2. git_student_push_solutions --> python git_student_push_solutions.py [module_num] [lesson_num]
    * Takes [module_num] [lesson_num], pull from instructor repo master, update student repo [module_num] [lesson_num] with activity solutions for student activites.

[EOF]

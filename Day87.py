# Shutil Module in Python


import shutil
import os

# Copy any file to any folder with this method like: [FileNmae FolderNmae] ~
# shutil.copy("main.py", "mainFolder")

# Copy all the files from the folder to any folder like: ["FolderName WhereToCopyThisFile_FolderName"]
# shutil.copytree("mainFolder", "myMainFolder")

# Change any file name from any folder ~
# shutil.move("myMainFolder/main.py", "ChangeName.py")

# Remove any folder with using thsi method ~
# shutil.rmtree("myMainFolder")

# Remove any file with using os module, cause we cannot remove any file with using shutil module ~
# os.remove("ChangeName.py")
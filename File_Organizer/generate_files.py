#                        ****** FILE GENERATOR SCRIPT *****
# This script utilise os module to create files
# the ----os.path.abspath(__file__)---- gave us the whole path of our directory till end
# the ----os.path.dirname()---- function is used to move one step behind the original directory we in 
# once in the directory where our folder exist the we used ----os.path.join(root_dir,"test")---- 
# it connect the folder with directory.
# After getting the folder where we want to make files we Creates dummy .jpeg files inside the test directory.
# It is used for testing the file organizer project. initialize file names file path where they will be created and
# then create the file by using file write function.

import os
current_dir=os.path.dirname(os.path.abspath(__file__))
root_dir=os.path.dirname(current_dir)
test_dir=os.path.join(root_dir,"test")
os.makedirs(test_dir, exist_ok=True)
for i in range(1,10):
    file_name=f"File_{i}.jpeg"
    file_path=os.path.join(test_dir,file_name)
    with open(file_path,"w") as f:
        f.write(f"the file {i} has been created") # content not gonna appear on jpeg files though
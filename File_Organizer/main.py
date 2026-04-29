import os
import shutil

folders=["images","PDF","txt_files"]

# here we made some path to our directories so that we can create and sort our folders and files from this 
# working directory to the one residing in root folders.

current_dir=os.path.dirname(os.path.abspath(__file__))
root_dir=os.path.dirname(current_dir)
needed_one=os.path.join(root_dir,"test")
sorted_folders=os.path.join(root_dir,"Sorted_folders")

# made some conditions and iterations from our test folder containing mixed files to get the each file types name.
imj=[f for f in os.listdir(needed_one) if f.endswith(".jpeg")]
txt=[f for f in os.listdir(needed_one) if f.endswith(".txt") ]
pdf=[f for f in os.listdir(needed_one) if f.endswith(".pdf") ]

# made a sorted_folder in the root directory by defining the path
os.makedirs(sorted_folders,exist_ok=True)

# made folders where each type of files will be sorted, but this time from the root directory to inside 
# the sorted_folder directory
for folder in folders:
    new=os.path.join(sorted_folders,folder)
    os.makedirs(new,exist_ok=True)

# made destination path to the folders of each type inside the sorted folder directory
destination=os.path.join(sorted_folders,"PDF")
destination2=os.path.join(sorted_folders,"txt_files")
destination3=os.path.join(sorted_folders,"images")

# iterate through each list containing the names of files of each type then locating it in root directory and then
# moving them to our sorted directories sorted folders of each type

for f in pdf:
    source = os.path.join(needed_one, f)
    shutil.move(source,destination)
for f in txt:
    source = os.path.join(needed_one, f)
    shutil.move(source,destination2)
for f in imj:
    source = os.path.join(needed_one, f)
    shutil.move(source,destination3)


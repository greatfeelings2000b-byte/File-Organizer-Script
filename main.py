import os
current_dir=os.path.dirname(os.path.abspath(__file__))
root_dir=os.path.dirname(current_dir)
test_dir=os.path.join(root_dir,"test")
os.makedirs(test_dir, exist_ok=True)
for i in range(1,10):
    file_name=f"File_{i}.jpeg"
    file_path=os.path.join(test_dir,file_name)
    with open(file_path,"w") as f:
        f.write(f"the file{i} has been created")
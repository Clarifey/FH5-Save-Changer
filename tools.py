import os
import shutil
appdata = os.getenv('LOCALAPPDATA')

file_list = []
container_list = []
def get_latest_file(files:list):
    latest_file  = max(files, key=os.path.getmtime)
    return latest_file

def get_latest_save_file():
    path = os.path.join(appdata, "Packages", "Microsoft.624F8B84B80_8wekyb3d8bbwe", "SystemAppData", "wgs")
    if os.path.exists(path):
        files = os.listdir(path)
    
        for file_name in files:
            file_path = os.path.join(path, file_name)
            file_list.append(file_path)

        latest_file = get_latest_file(file_list)
    
        file_list.clear()
    
        latest_files = os.listdir(latest_file)
    
        for file_name in latest_files:
            file_path = os.path.join(latest_file, file_name)
            if file_name == "containers.index":
                continue
            file_list.append(file_path)
    
        latest_file2 = get_latest_file(file_list)
    
        latest_file_dir = os.listdir(latest_file2)
        file_list.clear()
        for file in latest_file_dir:
            file_path = os.path.join(latest_file2, file)
            if str(file).startswith('container.'):
                container_list.append(file_path)
                continue
            file_list.append(file_path)
        
        biggest_file = max(file_list,key=os.path.getsize)
        return biggest_file

def copy_save():
    latest_save = get_latest_save_file()
    name = str(latest_save).split('\\')[11]
    shutil.copy(latest_save,'./backups/'+name)

def replace_latest_save(replace_save):
    latest_save = get_latest_save_file()
    name = str(latest_save).split('\\')[11]
    shutil.copy2(replace_save,replace_save+'_backup')
    os.rename(replace_save+'_backup',name)
    shutil.move(name, latest_save)
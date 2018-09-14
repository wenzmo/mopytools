def GetFilesWithEnding(folder,ending):
    import os
    path_list = []
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith(ending):
                path_list.append(os.path.join(root, file))
    return(path_list)
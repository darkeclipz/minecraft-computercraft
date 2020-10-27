import os
import shutil

root_dir = 'D:\\Minecraft\\technic\\technic\\modpacks\\tekkitmain\\saves\\Arborean\\computer\\'
directories = os.listdir(root_dir)
directories = [d for d in directories if os.path.isdir(root_dir + d)]

for d in directories[1:]:
    for f in os.listdir(root_dir + '0'):
        shutil.copy(root_dir + '0\\' + f, root_dir + d)

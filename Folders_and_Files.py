# Create folders and files with static name
# and automatically generated number attached to it
import os

def createFolder(directory):
    if not os.path.exists(directory):
        os.mkdir(directory)

n = 1
while n <= 100: #<- Change this value if you want less or more folders
    # Change on your directory and name of files you want
    createFolder('C:/Users/sebci/Desktop/Python exercise/cfs/ex' + str(n) + '/')
    f = open('C:/Users/sebci/Desktop/Python exercise/cfs/ex' + str(n) + '/ex' + str(n) + '.py', 'w+')
    int(n)
    n = n + 1
print('All done')

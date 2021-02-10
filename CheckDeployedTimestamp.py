import os.path, time
print("Last modified: %s" % time.ctime(os.path.getmtime("")))
print("Created: %s" % time.ctime(os.path.getctime("")))
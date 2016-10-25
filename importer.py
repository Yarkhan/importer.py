#! /usr/bin/env python
import os
import datetime
import errno
import shutil
import sys


def create_dir(path):
    try:
    	os.makedirs(path)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise


dst_path = "/media/yarkhan/CCEAA3FAEAA3DF48/fotos"
items = os.listdir(os.getcwd())
total = 1

for filename in items:
	print "\r Copying "+str(total)+" of "+str(len(items))+" items",
	sys.stdout.flush();
	total +=1
	info = os.stat(filename)
	date = datetime.date.fromtimestamp(info.st_mtime)

	year_dir 	 = os.path.join(dst_path,str(date.year))
	album_dir 	 = os.path.join(year_dir,str(date))
	old_filename = os.path.join(os.getcwd(),filename)
	new_filename = os.path.join(album_dir,filename)

	create_dir(year_dir)
	create_dir(album_dir)
	shutil.copy2(old_filename,new_filename)

print "\n Done!"

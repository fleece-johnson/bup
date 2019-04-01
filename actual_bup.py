import os
import shutil
import time

__author__ = 'Fleece Johnson a.k.a Booty Warrior'

src_path = 'C:\\Users\\Stan' #- sour path for bup
dst_path = 'D:\\Bup\\Stan' #- dest path for bup



def bup_start():
 d_files = for (root,dirs,files) in os.walk('src_path', topdown=True):
    d_files:
     if not os.path.lexists(os.path.join(dst_path, file)):
             shutil.copytree(os.path.join(src_path),
             dst_path)

#asking user whether or not to start the bup program
while  True:
  question = input('Do you back your shit up or what? y/n (or q to quit):')
  if question == 'y':
     print ('Tight butthole. Starting Delta-Backup now!')
     bup_start()
     break
  if question == 'n':
     print ('Zeroizing drive in..')
     num = 4 #countdown starting number
     def countdown(num):
                time.sleep(1)
                if num == 0:
                  return
                print(num)
                countdown(num-1)
     countdown(num)
     print ('Just kidding')
     quit()
  if question == 'q':
     quit()
  else:
     print ('Please input y/n or q')

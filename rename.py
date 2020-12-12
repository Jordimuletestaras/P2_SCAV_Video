import subprocess as sp
import os

if __name__ == '__main__':

    #get the file name
    print(""" Select the file:
    1. 720_10sec_bbb.mp4
    2. 480_10sec_bbb.mp4
    3. 360x240_10sec_bbb.mp4
    4. 160x120_10sec_bbb.mp4
    """)
    selected = int(input())

    if selected == 1:
        actual_name = '720_10sec_bbb.mp4'
    if selected == 2:
        actual_name = '480_10sec_bbb.mp4'
    if selected == 3:
        actual_name = '360x240_10sec_bbb.mp4'
    if selected == 4:
        actual_name = '160x120_10sec_bbb.mp4'

    print("Write the new filename, remember to add the extension")
    new_name = input()

    os.rename(actual_name,new_name)


import subprocess as sp
import os

if __name__ == '__main__':

    # get  filename
    print("Select the file: (remember to add the extension)")
    sp.run('ls', shell=True)
    file_name = input()
    line = 'ffprobe -v error -select_streams v:0 -show_entries stream=width,height -of csv=s=x:p=0 ' + file_name + ''
    print("Actual Resolution:")
    sp.run(line, shell=True)
    print("do you want to change resolution?  [y/N]")
    while (True):
        decision = input()
        if decision == 'y':
            print("New width:")
            w = input()
            print("New heigth:")
            h = input()
            print("New name: (remember to add the extension)")
            new_name = input()
            line = 'ffmpeg -i ' + file_name + ' -vf "scale=(iw*sar)*max(' + w + '/(iw*sar)\,' + h + '/ih):ih*max(' + w + '/(iw*sar)\,' + h + '/ih),crop=' + w + ':' + h + '" ' + new_name + ''
            sp.run(line, shell=True)

            break
        elif decision == 'N':

            break
        else:
            print("chosse a valid option")

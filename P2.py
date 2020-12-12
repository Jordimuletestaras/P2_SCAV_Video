import subprocess as sp
import os


def videoinformation(file_name):
    line = 'ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 ' + file_name + ''  # duration in seconds
    print("Duration:")
    sp.run(line, shell=True)
    line = 'ffprobe -v 0 -of csv=p=0 -select_streams v:0 -show_entries stream=r_frame_rate ' + file_name + ''  # frame rate
    print("Frame rate:")
    sp.run(line, shell=True)
    line = 'ffprobe -v error -select_streams v:0 -show_entries stream=width,height -of csv=s=x:p=0 ' + file_name + ''  # resolution
    print("Resolution:")
    sp.run(line, shell=True)


def resize(file_name):
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
            print("ERROR: Unknown option, please try again.")


def changecodec(file_name):
    print("Select the new Video codec")
    print("""options:
                1 - h.264 (.mp4)
                2 - h.265 (.mp4)
                3 - vp8 (.webm)
                4 - vp9 (.webm)
                5 - av1 (.mkv)
                6 - mpeg-2 (.mpg)""")
    option = int(input())
    print("New name:")
    new_name = input()
    if option == 1:
        codec = 'libx264', '.mp4'
    elif option == 2:
        codec = 'libx265', '.mp4'
    elif option == 3:
        codec = 'vp8', '.webm'
    elif option == 4:
        codec = 'vp9', '.webm'
    elif option == 5:
        codec = 'av1', '.mkv'
    elif option == 6:
        codec = 'mpeg2video', '.mpg'
    else:
        print("chosse a valid option")

    line = 'ffmpeg -i ' + file_name + ' -strict -2 -c:v ' + codec[0] + ' ' + new_name + '' + codec[1] + ''
    sp.run(line, shell=True)


if __name__ == '__main__':
    print("Select the file: (remember to add the extension)")
    sp.run('ls', shell=True)
    file_name = input()
    print("""Options:
    1. See relevant video data
    2. Resize
    3. Change Codec""")
    decision = int(input())
    if decision == 1:
        videoinformation(file_name)
    elif decision == 2:
        resize(file_name)
    elif decision == 3:
        changecodec(file_name)
    else:
        print("chosse a valid option")

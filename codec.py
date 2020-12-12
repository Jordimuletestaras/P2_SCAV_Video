import subprocess as sp
import os

if __name__ == '__main__':

    # ilname
    print("Select the file: (remember to add the extension)")
    sp.run('ls', shell=True)
    file_name = input()
    print("Select the new Video codec")
    print("""options:
            1 - h.264 (.mp4)
            2 - h.265 (.mp4)
            3 - vp8 (.webm)
            4 - vp9 (.webm)
            5 - av1 (.mkv)
            6 - mpeg-2 (.mpg)""")
    n=0
    while(n==0):
        option = int(input())
        if option == 1:
            codec = 'libx264', '.mp4'
            n=1
            break
        elif option == 2:
            codec = 'libx265', '.mp4'
            n = 1
            break
        elif option == 3:
            codec = 'vp8', '.webm'
            n = 1
            break
        elif option == 4:
            codec = 'vp9', '.webm'
            n = 1
            break
        elif option == 5:
            codec = 'av1', '.mkv'
            n=1
            break
        elif option == 6:
            codec = 'mpeg2video', '.mpg'
            n=1
            break
        else:
            print("chose a valid option")
    print("New name:")
    new_name = input()
    line = 'ffmpeg -i ' + file_name + ' -strict -2 -c:v ' + codec[0] + ' ' + new_name + '' + codec[1] + ''
    sp.run(line, shell=True)

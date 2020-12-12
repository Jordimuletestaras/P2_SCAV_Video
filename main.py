import subprocess as sp

if __name__ == '__main__':
    line = 'ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 bbb.mp4' #duration in seconds
    print("Duration:")
    sp.run(line, shell=True)
    line = 'ffprobe -v 0 -of csv=p=0 -select_streams v:0 -show_entries stream=r_frame_rate 720_10sec_bbb.mp4' #frame rate
    print("Frame rate:")
    sp.run(line, shell=True)
    line = 'ffprobe -v error -select_streams v:0 -show_entries stream=width,height -of csv=s=x:p=0 720_10sec_bbb.mp4' #resolution
    print("Resolution:")
    sp.run(line, shell=True)




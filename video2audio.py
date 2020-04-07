from moviepy.editor import VideoFileClip
from os.path import splitext

print("Input the path of the video", end=':')
video_path = input()
audio_path = splitext(video_path)[0]+".mp3"
VideoFileClip(video_path).audio.write_audiofile(audio_path)

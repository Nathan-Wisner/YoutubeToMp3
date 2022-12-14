import moviepy.editor as mp
import os

src = r"C:\Users\Nathan\Documents\youtube-dl-downloads\music\good"
dest = r"C:\Users\Nathan\Documents\youtube-dl-downloads\music\good"

for filename in os.listdir(src):
    if filename.endswith(".mp4") and not os.path.exists(src + "\\" + filename[:-4] + ".wav"):
        clip = mp.VideoFileClip(src + "\\" + filename)
        clip.audio.write_audiofile(dest + "\\" + filename[:-4] + '.wav')
        clip.close()

    if filename.endswith(".mp4") and os.path.exists(src + "\\" + filename[:-4] + ".wav"):
        os.remove(src + "\\" + filename)
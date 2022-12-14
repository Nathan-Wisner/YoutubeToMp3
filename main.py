import moviepy.editor as mp
import os

src = r"C:\Users\%USERPROFILE%\Documents\YTDownloader\Videos"
dest = r"C:\Users\%USERPROFILE%\Documents\YTDownloader\MP3"

for filename in os.listdir(src):
    if filename.endswith(".mp4") and not os.path.exists(src + "\\" + filename[:-4] + ".wav"):
        clip = mp.VideoFileClip(src + "\\" + filename)
        clip.audio.write_audiofile(dest + "\\" + filename[:-4] + '.wav')
        clip.close()

    if filename.endswith(".mp4") and os.path.exists(src + "\\" + filename[:-4] + ".wav"):
        os.remove(src + "\\" + filename)

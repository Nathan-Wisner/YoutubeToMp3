set /p url="Paste input url or id: "
youtube-dl -o "C:\{HOMEPATH}\Documents\YTDownloader\Videos\%%(title)s.%%(ext)s" %url%
python "C:\Users\{USER}\Documents\YTDownloader\Scripts\main.py"

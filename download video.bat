set /p url="Paste input url or id: "
youtube-dl -o "C:\Users\{USER}\Documents\YTDownloader\Videos\%%(title)s.%%(ext)s" %url%
pause

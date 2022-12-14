set /p url="Paste input url or id: "
youtube-dl -o "C:\%HOMEPATH%\Documents\youtube-dl-downloads\videos\%%(title)s.%%(ext)s" %url%
pause
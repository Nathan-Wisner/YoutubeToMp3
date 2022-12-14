set /p url="Paste input url or id: "
youtube-dl -o "C:\%HOMEPATH%\Documents\youtube-dl-downloads\music\good\%%(title)s.%%(ext)s" %url%
python "C:\Users\Nathan\PycharmProjects\MP4 Converter\main.py"
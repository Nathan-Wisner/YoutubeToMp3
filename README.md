# YoutubeToMp3
Youtube to MP3 and general MP4 to MP3 Converter

## General Instructions

### Download
Python: https://www.python.org/downloads/ 

#### Instructions

You'll want to install python, which should let you do most of the commands you need to get the libraries to run the script.

Run `pip.bat` after downloading + installing python and adjusting the files so the folder paths are exactly like yours.
They should look like this `"C:\Users\Bob\Documents...."`

Keep the extention of %%(title).... in the Youtube DL files, they help with the naming of the file.

Now you can run any of the files for thier needs

### What Each File Does

* Main.py - Converts a MP4 file in the location on line 4 into the destination on line 5
* Download.bat - Allows you to paste a youtube video URL and then converts into an MP3 
* Convert.bat - Simply calls the Main.py file using Python
* Download-Video.bat - Allows you to paste a youtube video URL and KEEPS it as an MP4
* pip.bat - Installs the libarary needed to run Main.py

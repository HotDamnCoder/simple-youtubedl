from __future__ import unicode_literals
import youtube_dl
import os, sys
FILE_DIRECTORY = os.path.dirname(os.path.realpath(__file__)) + "/"
OUTPUT_FOLDER = FILE_DIRECTORY + 'output/'
print(FILE_DIRECTORY, OUTPUT_FOLDER)
URL = sys.argv[1]
print(URL)
ydl_opts = {
    'format': 'bestaudio/best',
    'writethumbnail': True,
    'postprocessors': [
        {'key': 'FFmpegExtractAudio', 'preferredcodec': 'mp3', 'preferredquality': '320'},
        {'key': 'EmbedThumbnail'},
        {'key': 'FFmpegMetadata'}
    ],
    'ignoreerrors': True,
    'outtmpl': OUTPUT_FOLDER + '%(playlist)s/%(title)s.%(ext)s'
}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([URL])


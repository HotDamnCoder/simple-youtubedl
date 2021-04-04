from __future__ import unicode_literals
import youtube_dl
import sys
FILE_DIRECTORY = '\\'.join(__file__.split('/')[:-1]) + '\\'
OUTPUT_FOLDER = FILE_DIRECTORY + 'output\\'
FFMPEG_LOCATION = FILE_DIRECTORY
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
    'ffmpeg_location': FFMPEG_LOCATION + 'ffmpeg.exe',
    'outtmpl': OUTPUT_FOLDER + '%(playlist)s/%(title)s.%(ext)s'
}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([URL])


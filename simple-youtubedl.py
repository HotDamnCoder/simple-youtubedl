from __future__ import unicode_literals
import youtube_dl


OUTPUT_FOLDER = 'C:\\Users\\marcus\\Desktop\\Projects\\simple-youtubedl\\output\\'
FFMPEG_LOCATION = 'C:\\Users\\marcus\\Desktop\\Projects\\simple-youtubedl\\'
URL = 'https://www.youtube.com/playlist?list=PLjc__tvX8FXL7nzbY3eMxL_VbuCZWHAVU'
ydl_opts = {
    'format': 'bestaudio/best',
    'writethumbnail': True,
    'postprocessors': [
        {'key': 'FFmpegExtractAudio', 'preferredcodec': 'mp3', 'preferredquality': '320'},
        {'key': 'EmbedThumbnail'},
        {'key': 'FFmpegMetadata'}
    ],
    'ffmpeg_location': FFMPEG_LOCATION + 'ffmpeg.exe',
    'outtmpl': OUTPUT_FOLDER + '%(title)s.%(ext)s'
}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([URL])


from __future__ import unicode_literals
import youtube_dl

ydl_opts = {
    'format': 'bestaudio/best',
    'writethumbnail': True,
    'postprocessors': [
        {'key': 'FFmpegExtractAudio', 'preferredcodec': 'mp3', 'preferredquality': '320'},
        {'key': 'EmbedThumbnail'},
        {'key': 'FFmpegMetadata'}
    ],
    'ffmpeg_location': 'C:\\Users\\marcus\\Desktop\\Projects\\simple-youtubedl\\ffmpeg.exe',
    'outtmpl': 'C:\\Users\\marcus\\Desktop\\Projects\\simple-youtubedl\\output\\%(title)s.%(ext)s'
}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['https://www.youtube.com/playlist?list=PLjc__tvX8FXL7nzbY3eMxL_VbuCZWHAVU'])


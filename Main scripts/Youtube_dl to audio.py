"""

    Download the videos from the youtube and produce an audio file with .wav extension

"""

from __future__ import unicode_literals
import youtube_dl


ydl_opts = {
 #   'verbose': True,
    'format': 'bestaudio/best',
    'channel': 'mono',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'wav',
        'preferredquality': '320',
    }],
    'postprocessor_args': [
        '-ar', '16000',
        '-ac', '1',
	    # '-t', '7:00',
        # '-acodec', 'pcm_s16le'
    ],
    'prefer_ffmpeg': True,
    'outtmpl': 'Videos/FDPICT IW Inaugural Session/%(title)s.%(ext)s',
    # 'keepvideo': True,
    'extractaudio' : True,      # only keep the audio
}


with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['https://www.youtube.com/watch?v=HV5fQkvumrA&list=PL_uaeekrhGzJ1chVqaJFE2HIeoukcrfXv'])















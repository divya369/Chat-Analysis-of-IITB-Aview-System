"""

	code to convert audio.wav file to another .wav file with specific configuration like channel (mono), Hz (16000), encoding (signed 16 bit little 
		endian). Once the conversion is done, the audio file is splited into number of chunks and export to specific folder

"""


import pydub
import os

i = 0
vedio_dir = '/Users/divyapatel/Documents/IITB project/Chat Analysis of Aview System/Youtube video to transcript/Videos'
audio_dir = '/Users/divyapatel/Documents/IITB project/Chat Analysis of Aview System/Youtube video to transcript/ChunkFolder'

for root, subdir, files in os.walk(vedio_dir):
	for file in files:
		filename = os.fsdecode(file)
		if filename.endswith('.wav'): 
			sound = pydub.AudioSegment.from_wav('{0}/{1}'.format(root, file))
			sound = sound.set_channels(1)
			sound = sound.set_sample_width(2)
			sound = sound.set_frame_rate(16000)
			len_of_sound = len(sound)

				# 240000 millisec ~ 4 min segments of audio

			folder_name = os.path.basename(root)
			filename_without_ext = os.path.splitext(file)[0]

			new_path = os.path.join(audio_dir, folder_name, filename_without_ext)

			if not os.path.isdir(os.path.join(audio_dir, folder_name)):
				os.mkdir(os.path.join(audio_dir, folder_name))
			if not os.path.isdir(os.path.join(audio_dir, folder_name, filename_without_ext)):
					os.mkdir(os.path.join(audio_dir, folder_name, filename_without_ext))
					os.mkdir(os.path.join(audio_dir, folder_name, filename_without_ext, "text"))

			for i in range(240000, len_of_sound, 120000):
				slice = sound[i-240000:i]
				slice.export("{0}/{1}_version{2}.wav".format(new_path, filename_without_ext, i//240000), format="wav")

			slice = sound[i: len_of_sound]
			slice.export("{0}/{1}_version{2}.wav".format(new_path, filename_without_ext, i//240000), format="wav")




































# i = 0
# vedio_dir = '/Users/divyapatel/Documents/IITB project/pydub/Videos'
# audio_dir = '/Users/divyapatel/Documents/IITB project/pydub/ChunkFolder'

# for file in os.listdir(vedio_dir):
# 	filename = os.fsdecode(file)
# 	if filename.endswith('.wav'): 
# 		sound = pydub.AudioSegment.from_wav('{0}/{1}'.format(vedio_dir, filename))
# 		sound = sound.set_channels(1)
# 		sound = sound.set_sample_width(2)
# 		sound = sound.set_frame_rate(16000)
# 		len_of_sound = len(sound)

# 			# 420000 millisec ~ 7 min segments of audio

# 		filename_without_ext = os.path.splitext(file)[0]

# 		new_path = str("{0}/{1}".format(audio_dir, filename_without_ext))

# 		if os.path.isdir(new_path):
# 			pass
# 		else:
# 			os.mkdir(new_path)
# 			for subdir, dir, files in os.walk(new_path):
# 				new_path_text = os.path.join(new_path, subdir, "text")
# 				os.mkdir(new_path_text)

# 		for i in range(240000, len_of_sound, 120000):
# 			slice = sound[i-240000:i]
# 			slice.export("{0}/{1}_version{2}.wav".format(new_path, filename_without_ext, i//240000), format="wav")

# 		slice = sound[i: len_of_sound]
# 		slice.export("{0}/{1}_version{2}.wav".format(new_path, filename_without_ext, i//240000), format="wav")




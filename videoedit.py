from moviepy.editor import *

# clip is the video from 00:56 to 01:06
clip = VideoFileClip("sample-mp4-file.mp4").subclip(56, 66)
clip2 = VideoFileClip("sample-mp4-file.mp4").subclip(70, 76)
clip3 = VideoFileClip("sample-mp4-file.mp4").subclip(50, 52)
clip4 = VideoFileClip("sample-mp4-file.mp4").subclip(30, 35)

final_clip = concatenate_videoclips([clip, clip2, clip3, clip4])

final_clip.write_videofile("output_1.mp4")

# Menambahkan Efek

clip = (VideoFileClip("sample-mp4-file.mp4").subclip(56, 66)
        .fx(vfx.colorx, 1.2)  # 20% brighter
        .fx(vfx.lum_contrast, 0, 40, 127))  # and increase the contrast
clip2 = (VideoFileClip("sample-mp4-file.mp4").subclip(70, 76)
        .fx(vfx.invert_colors))
clip3 = VideoFileClip("sample-mp4-file.mp4").subclip(50, 52)
clip4 = VideoFileClip("sample-mp4-file.mp4").subclip(30, 35)

final_clip = concatenate_videoclips([clip, clip2, clip3, clip4])

final_clip.write_videofile("output_2.mp4")

# Efek Audio

musicclip = AudioFileClip("Study and Relax.mp3").subclip(0, 6)
audioclip = (clip.audio).fx(afx.volumex, 1.2).fx(afx.audio_fadein, 1.0)
# Make the sound 20% louder, and fade it in over 1 second
clip_v2 = clip.set_audio(audioclip)  # new first clip

final_clip = concatenate_videoclips([clip_v2, clip2, clip3, clip4])

final_clip.write_videofile("output_3.mp4")

# Menyatukan Semuanya

musicclip = AudioFileClip("Study and Relax.mp3").subclip(0, 6)
audioclip = (clip.audio).fx(afx.volumex, 1.2).fx(afx.audio_fadein, 1.0)
# Make the sound 20% louder, and fade it in over 1 second
clip_v2 = clip.set_audio(audioclip)  # new first clip

composite_start_of_video = CompositeVideoClip([clip_v2,
                                               clip4.fx(vfx.resize, 0.6).fx(afx.volumex, 0.0)])
# clip4 is smaller (60% original size), and on top of clip_v2

clip2_audio = (clip2.audio).fx(afx.volumex, 1.5)  # 50% louder, so we can hear over our music
composite_second_clip_audio = CompositeAudioClip([clip2_audio,
                                                  (musicclip).fx(afx.volumex, 0.3)])  # 70% quieter
clip2_v2 = clip2.set_audio(composite_second_clip_audio)

final_clip = concatenate_videoclips([composite_start_of_video, clip2_v2, clip3, clip4])

final_clip.write_videofile("output_4.mp4")

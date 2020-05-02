# Extract meta data from video file
Metadata is text inside the video file that references the video. The Meta information of a video shows that what is included in the video and what type of content is available in the video.

Before getting into extraction, first you need to install ffmpeg.
## - Ubuntu
*sudo apt-get install ffmpeg*
## - Windows
Download ffmpeg software from [FFMPEG official website](https://www.ffmpeg.org/download.html#build-windows).
Unzip the file and add the bin folder to **environment path**.

### Using MediaInfo class
```
	media_obj = Mediainfo()
	or
	media_obj = Mediainfo(VIDEO_PATH) # VIDEO_PATH must be string
```
> Set video path if not passed
```
	media_obj.video_path = 'video_path'
```

> Get video path
```
	VIDEO_PATH = media_obj.video_path
```

> Extract metadata
```
	metadata = media_obj.getVideoDetail()
```

## Sample of Metadata of video
```
{'DISPOSITION': {'default': '1', 'dub': '0', 'original': '0', 'comment': '0', 'lyrics': '0', 'karaoke': '0', 'forced': '0', 'hearing_impaired': '0', 'visual_impaired': '0', 'clean_effects': '0', 'attached_pic': '0', 'timed_thumbnails': '0'}, 'TAG': {'rotate': '90', 'creation_time': '2020-01-15T10:35:59.000000Z', 'language': 'eng', 'handler_name': 'VideoHandle'}, 'index': '0', 'codec_name': 'h264', 'codec_long_name': 'H.264 / AVC / MPEG-4 AVC / MPEG-4 part 10', 'profile': 'High', 'codec_type': 'video', 'codec_time_base': '133393/3870000', 'codec_tag_string': 'avc1', 'codec_tag': '0x31637661', 'width': '1440', 'height': '1080', 'coded_width': '1440', 'coded_height': '1088', 'has_b_frames': '0', 'sample_aspect_ratio': '1:1', 'display_aspect_ratio': '4:3', 'pix_fmt': 'yuv420p', 'level': '40', 'color_range': 'tv', 'color_space': 'bt709', 'color_transfer': 'bt709', 'color_primaries': 'bt709', 'chroma_location': 'left', 'field_order': 'unknown', 'timecode': 'N/A', 'refs': '1', 'is_avc': 'true', 'nal_length_size': '4', 'id': 'N/A', 'r_frame_rate': '30/1', 'avg_frame_rate': '1935000/133393', 'time_base': '1/90000', 'start_pts': '0', 'start_time': '0.000000', 'duration_ts': '266786', 'duration': '2.964289', 'bit_rate': '11845320', 'max_bit_rate': 'N/A', 'bits_per_raw_sample': '8', 'nb_frames': '43', 'nb_read_frames': 'N/A', 'nb_read_packets': 'N/A', 'side_data_type': 'Display Matrix', 'displaymatrix': '', 'rotation': '-90'}
```

## Extract frame from video
```
	frame = Extractframes(VIDEO_PATH)
	frame.extract_frames() # frame_path='', index=0 as optional arguments.
```

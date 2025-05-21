from dataclasses import dataclass


"""
This is an example of the facade structural pattern implemented in Python.

Scenario:
We're building a media player that plays both audio and video files.
We have subsystems that handle loading, decoding and rendering audio
and video files.  We will implement a facade class that provides
a simple interface to handle playing, pausing and stopping media files
regardless of type.
"""


@dataclass
class File:
    path: str

    def load(self):
        raise NotImplementedError


@dataclass
class AudioFile(File):
    def load(self):
        print(f"Loading audio file: {self.path}")


@dataclass
class VideoFile(File):
    def load(self):
        print(f"Loading video file: {self.path}")


class AudioDecoder:
    def decode(self, file: AudioFile):
        print(f"Decoding audio file: {file.path}")


class VideoDecoder:
    def decode(self, file: VideoFile):
        print(f"Decoding video file: {file.path}")


class AudioRenderer:
    def render(self, file: AudioFile):
        print(f"Rendering audio: {file.path}")


class VideoRenderer:
    def render(self, file: VideoFile):
        print(f"Rendering video: {file.path}")


class MediaPlayer:
    def __init__(self):
        self.audio_decoder = AudioDecoder()
        self.video_decoder = VideoDecoder()
        self.audio_renderer = AudioRenderer()
        self.video_renderer = VideoRenderer()
        self.current_file = None

    def play(self, file: File):
        self.current_file = file
        self.current_file.load()
        if isinstance(file, AudioFile):
            self.audio_decoder.decode(file)
            self.audio_renderer.render(file)
        elif isinstance(file, VideoFile):
            self.video_decoder.decode(file)
            self.video_renderer.render(file)
        else:
            raise ValueError("Unsupported file type")

        print("Playing:", file.path)

    def pause(self):
        if self.current_file:
            print(f"Pause: {self.current_file.path}")
        else:
            print("Nothing to pause")

    def stop(self):
        if self.current_file:
            print(f"Stop: {self.current_file.path}")
            self.current_file = None
        else:
            print("Nothing to stop")


audio_file = AudioFile("~/music/song.mp3")
video_file = VideoFile("~/videos/video.mp4")

media_player = MediaPlayer()

media_player.play(audio_file)
media_player.pause()
media_player.stop()

media_player.play(video_file)
media_player.pause()
media_player.stop()

# Video Subtitler with Whisper

This repository contains a Python application that extracts audio from a video file, transcribes it using OpenAI's Whisper model, and then generates subtitles in SRT format.

## Features

- **Audio Extraction**: Extracts audio from a video file.
- **Speech Recognition**: Transcribes audio to text using OpenAI's Whisper model.
- **Subtitle Generation**: Converts transcribed text into SRT format.

## Requirements

- Python 3.x
- FFmpeg
- Various Python libraries listed in `requirements.txt`

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/video-subtitler.git
   cd video-subtitler
   ```

2. Install the required Python libraries:
   ```bash
   pip install -r requirements.txt
   ```

3. Make sure FFmpeg is installed on your system. Visit the [FFmpeg download page](https://ffmpeg.org/download.html) for installation instructions.

## Usage

1. To use the application, you need to pass the path to the video file as an argument. Optionally, you can specify the paths for the extracted audio and output subtitle file.

   ```bash
   python vsub.py path_to_video.mp4 --audio_file path_to_audio.mp3 --subtitle_file path_to_subtitle.srt
   ```

   For example:

   ```bash
   python vsub.py video.mp4
   ```

   This command will extract audio, transcribe it, and generate subtitles in the same directory as the video file.

## Files Description

- `vsub.py`: The main Python script that orchestrates the extraction, transcription, and subtitle generation.
- `utils/`: Contains helper classes for audio extraction, transcription, text merging, and more.
- `requirements.txt`: A list of Python libraries required to run the application.

## Troubleshooting

If you encounter any issues with the transcription or subtitle generation:
- Ensure that your FFmpeg installation is up to date.
- Check that the paths and filenames in the scripts are correct.
- Verify that the audio and video files are not corrupted and are in a format supported by FFmpeg.

## Contributing

Contributions to this project are welcome. Please fork the repository, make your changes, and submit a pull request.

## License

This project is open-sourced under the MIT License. See the LICENSE file for more details.

## Special thanks!
Thanks [@arturtur](https://github.com/aturtur) for script that imports srt file into Adobe After Effects project.
Link to the script: [Messing with After Effects and Subtitles](https://aturtur.com/messing-with-after-effects-and-subtitles/)
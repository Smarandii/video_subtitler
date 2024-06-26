import os
import argparse
from utils.audio_extractor import AudioExtractor
from utils.file_utility import FileUtility
from utils.segment_detector import SegmentDetector
from utils.text_merger import TextMerger
from utils.transcription_processor import TranscriptionProcessor
from utils.whisper_transcriber import WhisperTranscriber


def setup_argument_parser():
    parser = argparse.ArgumentParser(description="Process video files for audio extraction and subtitle generation.")
    parser.add_argument("video_file", help="The path to the video file to process.")
    parser.add_argument("-a", "--audio_file", help="The path to save the extracted audio file.", required=False)
    parser.add_argument("-s", "--subtitle_file", help="The path to save the subtitle file.", required=False)
    return parser


def process_video(video_file, audio_file, subtitle_file=None):
    if audio_file is None:
        audio_file = f"{os.path.splitext(video_file)[0]}.mp3"
    if subtitle_file is None:
        subtitle_file = f"{os.path.splitext(video_file)[0]}.srt"
    merged_json_file = f"merged_chunks_{os.path.splitext(video_file)[0]}.json"
    unmerged_json_chunks_file = f"unmerged_chunks_{os.path.splitext(video_file)[0]}"
    print(f"We got {video_file} - starting video processing...")

    ae = AudioExtractor()
    fu = FileUtility()
    sg = SegmentDetector(audio_file=audio_file)
    tm = TextMerger()

    segments = sg.detect_audio_segments()
    print(f"Found segments: {segments}")
    json_transcriptions = sg.detect_json_transcriptions()
    print(f"Found json transcriptions: {json_transcriptions}")
    if not segments:
        pauses, total_duration_ms = ae.extract_audio_and_find_pauses(video_file, audio_file)
        segments = ae.split_audio_based_on_silence(audio_file, pauses, total_duration_ms)

    if not json_transcriptions:
        wt = WhisperTranscriber()
        tp = TranscriptionProcessor(wt.get_whisper_pipe())
        transcriptions = tp.transcribe_segments(segments)
    elif json_transcriptions and not os.path.exists(merged_json_file):
        transcriptions = []
        for transcription in json_transcriptions:
            t = fu.load_chunks_from_json(transcription)
            transcriptions.extend(t)
        fu.save_chunks_to_json(transcriptions, unmerged_json_chunks_file)

    if not os.path.exists(merged_json_file):
        merged_chunks = tm.merge_chunks(transcriptions)
        fu.save_chunks_to_json(merged_chunks, merged_json_file)
    else:
        merged_chunks = fu.load_chunks_from_json(merged_json_file)

    fu.generate_srt_file(merged_chunks, subtitle_file)
    print(f"Generated subtitles file: {subtitle_file}")


def main():
    parser = setup_argument_parser()
    args = parser.parse_args()

    process_video(args.video_file, args.audio_file, args.subtitle_file)


if __name__ == "__main__":
    main()

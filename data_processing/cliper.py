import os
import pandas as pd
import subprocess
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor, as_completed


def ffmpeg_extract_subclip(input_file, start_time, end_time, targetname):
    try:
        cmd = [
            'ffmpeg', '-y', '-ss', str(start_time), '-i', input_file,
            '-to', str(end_time - start_time),
            '-c:v', 'libx264', '-c:a', 'aac', '-strict', 'experimental',
            '-avoid_negative_ts', '1', targetname
        ]
        result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if result.returncode != 0:
            raise RuntimeError(f"FFmpeg error during re-encoding: {result.stderr.decode()}")
    except Exception as e:
        raise RuntimeError(f"Error during processing {targetname}: {str(e)}")


def process_video(video_id, video_df, video_base_path, output_base_path):
    video_path = os.path.join(video_base_path, f"{video_id}.mp4")
    segment_count = 0

    if not os.path.exists(video_path):
        print(f"Video {video_path} not found, skipping.")
        return []

    segment_paths = []
    for index, row in video_df.iterrows():
        start_time = row['start']
        end_time = row['end']

        output_dir = os.path.join(output_base_path, video_id)
        os.makedirs(output_dir, exist_ok=True)

        segment_path = os.path.join(output_dir, f"{video_id}_{segment_count}.mp4")

        try:
            ffmpeg_extract_subclip(video_path, start_time, end_time, targetname=segment_path)
            segment_paths.append((index, os.path.abspath(segment_path)))
            segment_count += 1
        except Exception as e:
            print(f"Error processing {segment_path}: {e}")

    return segment_paths


def main():
    excel_path = '/PATH/TO/OphNet2024_loca_challenge.csv'
    output_excel_path = '/PATH/TO/SAVE/OphNet2024_loca_challenge_trimmed.csv' ##path to save new csv file with trimmed video name
    video_base_path = '/PATH/TO//OphNet_all_videos'
    output_base_path = '/PATH/TO/SAVE//OphNet_trimmed_videos' #path to save trimmed videos

    os.makedirs(output_base_path, exist_ok=True)

    df = pd.read_csv(excel_path)

    df['segment_path'] = ''

    unique_video_ids = df['video_id'].unique()
    max_workers = 16

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = []
        for video_id in unique_video_ids:
            video_df = df[df['video_id'] == video_id]
            futures.append(executor.submit(process_video, video_id, video_df, video_base_path, output_base_path))

        for future in tqdm(as_completed(futures), total=len(futures), desc="Processing videos"):
            segment_paths = future.result()
            for index, segment_path in segment_paths:
                df.at[index, 'segment_path'] = segment_path

    df.to_csv(output_excel_path, index=False)
    print(f"Segments saved and new CSV file created at {output_excel_path}")


if __name__ == "__main__":
    main()

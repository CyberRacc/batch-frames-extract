import subprocess
import pkg_resources
import tkinter as tk
from tkinter import filedialog

REQUIRED_PACKAGES = [
    'opencv-python',
    'tqdm'
]

for package in REQUIRED_PACKAGES:
    try:
        dist = pkg_resources.get_distribution(package)
        print('{} ({}) is installed'.format(dist.key, dist.version))
    except pkg_resources.DistributionNotFound:
        print('{} is NOT installed'.format(package))
        subprocess.call(['pip', 'install', package])

import cv2
import os
import glob
from tqdm import tqdm

def extract_frames(video_path, dir_path):
    video_name = os.path.basename(video_path)
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print(f"Could not open video file {video_path}. Please check the file format.")
        return
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    i = 0
    with tqdm(total=total_frames, desc=video_name, ncols=80) as pbar:
        while (cap.isOpened()):
            ret, frame = cap.read()
            if ret == False:
                break
            cv2.imwrite(os.path.join(dir_path, f'{os.path.splitext(video_name)[0]}_frame{i}.png'), frame)
            i += 1
            pbar.update(1)
    cap.release()
    cv2.destroyAllWindows()

def main(input_dir, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    video_extensions = ["*.mp4", "*.avi", "*.mkv", "*.mov", "*.flv", "*.wmv"]
    video_paths = [glob.glob(os.path.join(input_dir, ext)) for ext in video_extensions]
    video_paths = [item for sublist in video_paths for item in sublist]
    if not video_paths:
        print("No video files found in the input directory.")
        return
    for video_path in video_paths:
        extract_frames(video_path, output_dir)

def browse_directory(entry):
    dirname = filedialog.askdirectory()
    entry.delete(0, tk.END)
    entry.insert(0, dirname)

root = tk.Tk()
root.title("Frames Extractor")
root.geometry('500x250')

tk.Label(root, text="Input Directory").pack(pady=5)
input_entry = tk.Entry(root)
input_entry.pack()
input_button = tk.Button(root, text="Select Input Directory", command=lambda: browse_directory(input_entry))
input_button.pack(pady=5)

tk.Label(root, text="Output Directory").pack(pady=5)
output_entry = tk.Entry(root)
output_entry.pack()
output_button = tk.Button(root, text="Select Output Directory", command=lambda: browse_directory(output_entry))
output_button.pack(pady=5)

start_button = tk.Button(root, text="Start", command=lambda: main(input_entry.get(), output_entry.get()))
start_button.pack(pady=10)

root.mainloop()

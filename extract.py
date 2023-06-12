import subprocess
import pkg_resources

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

# Now that we have made sure that all required packages are installed, we can import them.
import cv2
import os
import glob
from tqdm import tqdm

def extract_frames(video_path, dir_path):
    # The video filename with extension
    video_name = os.path.basename(video_path)

    # Start capturing the feed
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print(f"Could not open video file {video_path}. Please check the file format.")
        return

    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    i = 0

    with tqdm(total=total_frames, desc=video_name, ncols=80) as pbar:
        while (cap.isOpened()):
            # Get the frame
            ret, frame = cap.read()
            if ret == False:
                break

            # Save the results in the directory path
            # Include the video filename and frame number in the image filename
            # Strip the video extension for the output image filename
            cv2.imwrite(os.path.join(dir_path, f'{os.path.splitext(video_name)[0]}_frame{i}.png'), frame)
            i += 1
            pbar.update(1)

    cap.release()
    cv2.destroyAllWindows()

# Directory containing the videos
input_dir = "./input"

# Directory where you want to store the frames
output_dir = "./output"

# Check if output directory exists
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Get a list of all video files in the input directory
video_extensions = ["*.mp4", "*.avi", "*.mkv", "*.mov", "*.flv", "*.wmv"]
video_paths = [glob.glob(os.path.join(input_dir, ext)) for ext in video_extensions]
video_paths = [item for sublist in video_paths for item in sublist]

if not video_paths:
    print("No video files found in the input directory.")
    exit(1)

for video_path in video_paths:
    extract_frames(video_path, output_dir)


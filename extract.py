import subprocess
import pkg_resources

REQUIRED_PACKAGES = [
    'opencv-python'
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

def extract_frames(video_path, dir_path):
    # The video filename without extension
    video_name = os.path.splitext(os.path.basename(video_path))[0]

    # Start capturing the feed
    cap = cv2.VideoCapture(video_path)
    i = 0

    while (cap.isOpened()):
        # Get the frame
        ret, frame = cap.read()
        if ret == False:
            break

        # Save the results in the directory path
        # Include the video filename and frame number in the image filename
        cv2.imwrite(os.path.join(dir_path, f'{video_name}_frame{i}.png'), frame)
        i += 1

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

for video_path in video_paths:
    extract_frames(video_path, output_dir)

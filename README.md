# Bulk Video Frames Extractor in Python #

This is a simple script that extract all frames from all videos in the input folder.
Then outputs the frames as .png files into the output folder.

I made this for use with DeepFaceLab, to quickly create a single folder of training images from a bunch of videos in one go.

## Warning ##

This script will extract every single frame from ALL videos in the input folder at original resolution into .png files, if you have a bunch of 20 minute 1080p videos, it can take up A LOT of space! Please be careful!

## How to use ##

1. Make sure you have python installed.

2. Clone this repo or download as .zip and extract.

3. Place video files into the input folder.

4. In terminal, run the following command:

```
python extract.py
```

Or:

```
python3 extract.py
```

It will check for opencv-python and attempt to install it. You can install it manually by using:

```
pip install opencv-python
```

Or:

```
pip3 install opencv-python
```

5. Find your .png files in the output directory.

## Notes ##

Please be aware that this script was created by GPT-4, with minimal edits from myself, but I can verify that it works for my purposes.
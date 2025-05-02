# OpenCV Image Resizer (Enhance or Reduce)

This Python script allows you to enhance a low-resolution image or reduce a large image using OpenCV's interpolation methods.

## Features
- Resize using `cv.INTER_CUBIC` for enhancement.
- Resize using `cv.INTER_AREA` for reduction.
- CLI-based option selection.

## How to Use
1. Place `cat_low.jpg` and `cat_large.jpg` inside the `images/` folder.
2. Run the script:
   ```bash
   python resize_cat.py

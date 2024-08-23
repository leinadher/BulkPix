# 📸 BulkPix - Bulk Image Processing

**Author:** Daniel Herrera

**Date:** 16/08/2024

<img src="assets/screenshot.jpg" alt="Screenshot" width="300"/>

---

## 1. Project Overview

**BulkPix** is a personal tool developed for processing large collections of images captured with my DSLR camera. Designed with flexibility in mind, it provides a range of functionalities, including:

- 🖼️ **Thumbnail Creation**: Automatically generate thumbnails for large batches of images.
- 📏 **Image Resizing**: Resize images to various dimensions for different use cases.
- 🏷️ **Image Metadata**: Extract the metadata from photos stored in a directory and save into a CSV file.
- 🎨 **ASCII Art Generation**: Convert images into ASCII art for creative applications.

This project is an ongoing effort, with plans to expand its capabilities over time. Future enhancements will include additional processing features and a user interface to make it more user-friendly.

## 2. Repository Structure

- 📁 **'apps'**: Contains the sub-apps that are launched by `main.py` for each functionality.
- 📁 **'assets'**: Contains additional assets, icons, etc.
- 📁 **'scripts'**: Contains the classes and functions for each feature.

## 3. Files in the Main Directory

I intend to expand this section as I refine the project and add more functionalities, such as incorporating more scripts into the `main.py`.
- 🗝️ **`main.py`**: Main program, launches a menu that leads to the sub-apps.
- 📄 **`README.md`**: This file, providing an overview of the project.

## 4. Data Sources

BulkPix does not require external data sources, but relies on the images you import into the 'Images' directory for processing. The processed results are saved back into the 'Outputs' directory. It is built using the PIL (Pillow) image processing library as well as Tinkr for the UI.

Feel free to expand the project by adding more features or improving the interface as your needs evolve! 🚀

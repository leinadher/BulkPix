---
Daniel Herrera  
16/08/2024
---

# 📸 BulkPix - Image Bulk Processing

---

## 1. Project Overview

**BulkPix** is a personal tool developed for managing and processing large collections of images captured with my DSLR camera. Designed with flexibility in mind, it provides a range of functionalities, including:

- 🖼️ **Thumbnail Creation**: Automatically generate thumbnails for large batches of images.
- 📏 **Image Resizing**: Resize images to various dimensions for different use cases.
- 🎨 **ASCII Art Generation**: Convert images into ASCII art for creative applications.

This project is an ongoing effort, with plans to expand its capabilities over time. Future enhancements will include additional processing features and a user interface to make it more user-friendly.

---

## 2. Repository Structure

- 📁 **'apps'**: contains the sub-apps that are launched by `main.py` for each functionality.
- 📁 **'scripts'**: contains the main functions and methods for each functionality.

Input / output folders to use as example:
- 📁 **'ASCII'**: Contains ASCII art outputs.
- 📂 **'images'**: The directory where you import the images for processing.
- 📁 **'images_resized'**: Contains the processed images, including resized versions and thumbnails.


---

## 3. Files in the Main Directory

I intend to expand this section as I refine the project and add more functionalities, such as incorporating more scripts into the `main.py`.
- 🗝️ **'main.py'**: main program, launches a menu that leads to the sub-apps.
- 📄 **'README.md'**: This file, providing an overview of the project.

---

## 4. Data Sources

BulkPix does not require external data sources, but relies on the images you import into the 'Images' directory for processing. The processed results are saved back into the 'Outputs' directory. It is built using the PIL (Pillow) image processing library as well as Tinkr for the UI.

---

Feel free to expand the project by adding more features or improving the interface as your needs evolve! 🚀

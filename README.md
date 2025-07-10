# file_move_tool

# 🗂️ File Move Tool (Python)

A simple Python tool that **recursively moves all files** from a root directory and its subdirectories into a **single destination folder**. If duplicate filenames are found, it automatically renames them to avoid overwriting.

---

## ✨ Why I Created This

While transferring data from my phone to my PC, I faced a real challenge. One folder had hundreds of nested folders and files — and manually opening each one and dragging out files was *extremely* tedious.

So, I decided to automate it with Python.

---

## 📦 Features

- Recursively finds files in all subfolders.
- Moves them into a single destination folder.
- Renames files if a duplicate filename is detected (e.g., `image.jpg` → `image_1.jpg`, `image_2.jpg`, etc.)
- Simple command-line interface.

---

## 🚀 How to Use

1. **Clone the repository** or download the `file_move_tool.py` script.
2. Run the script:

```bash
python file_move_tool.py

📌 Example
If you have:

📁 Phone_Backup
├── 📁 WhatsApp
│   └── 📁 Images
│       └── img1.jpg
├── 📁 Camera
│   └── pic1.jpg
└── note.txt

All files (img1.jpg, pic1.jpg, note.txt) will be moved to the destination folder like this:

📁 Destination
├── img1.jpg
├── pic1.jpg
└── note.txt

Duplicate names will be renamed automatically.

🛠️ Requirements
Python 3.x

No external libraries needed (uses os and shutil)

📃 License
This project is open-source and free to use!

🙋‍♂️ Author
Anurag Mishra

Made with ❤️ to save time and effort.

yaml
Copy
Edit

---

Let me know if you'd like a thumbnail/banner for GitHub or LinkedIn too!

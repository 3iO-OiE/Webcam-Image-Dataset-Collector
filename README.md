# Webcam Image Dataset Collector

This script allows you to collect a custom image dataset using your webcam, organizing images into class-labeled directories for easy use in machine learning or computer vision projects.

## 📷 What It Does

* Captures images from a webcam.
* Organizes them into folders based on class labels (e.g., gestures, objects, digits).
* Saves a defined number of images per class.
* Allows manual control to start image collection for each class.

## 🧱 Project Structure

```
project/
├── data/                # Dataset folder (auto-generated)
│   ├── 0/               # Images for class 0
│   ├── 1/               # Images for class 1
│   └── ...
├── collect_images.py    # Main script
└── README.md
```

## 🛠️ Requirements

* Python 3.x
* OpenCV

Install the required package:

```bash
pip install opencv-python
```

## 🚀 How to Use

1. **Adjust Parameters**
   Open `collect_images.py` and set:

   * `number_of_classes`: Total classes you want to collect (e.g., 5 for 0–4).
   * `dataset_size`: Number of images per class.

2. **Run the Script**

   ```bash
   python collect_images.py
   ```

3. **Follow Instructions**
   For each class:

   * You’ll see a live webcam preview.
   * Press **`Q`** to start collecting images.
   * The script captures images and saves them automatically.

4. **Check Output**
   Collected images are stored under `./data/<class_id>/`.

## ✅ Tips

* Make sure lighting conditions are consistent.
* Vary backgrounds and angles slightly for better generalization.
* You can change `cap = cv2.VideoCapture(1)` to `cv2.VideoCapture(0)` if your default webcam is not on index 1.

## 📁 Example Use Cases

* Collecting hand gesture datasets.
* Capturing object images for classification.
* Gathering facial expression samples.

## 📄 License

This project is licensed under the MIT License — feel free to use, modify, and share.

---


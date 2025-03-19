# 🏗️ Building Crack Detection System

This is a web-based Crack Detection system built using **Django**, **TensorFlow**, and **HTML/CSS**. Users can upload images of buildings, and the model predicts whether there is a crack present or not.

---

## 🚀 Features

✅ Upload image functionality  
✅ Deep Learning Model for crack detection (Keras `.h5` model)  
✅ Displays prediction dynamically with styled output  
✅ Dark mode user interface  
✅ Stores uploaded images (if needed for record-keeping)

---

## 🛠 Technology Stack

- Python 3.8
- Django 4.2
- TensorFlow / Keras
- HTML, CSS (dark theme)
- SQLite (default Django DB)

---

## 📂 Project Structure

```
Building_Crack_Detection/
│
├── crack_detection/           # Django App
│   ├── models.py              # UploadedImage model (optional)
│   ├── views.py               # Main view handling uploads and prediction
│   ├── detection.py           # Model loading and prediction logic
│   ├── templates/
│   │   └── index.html         # Styled frontend for upload & prediction
│   ├── models/                # Contains crack_detector.h5 (Not pushed to Git)
│
├── media/                     # Uploaded images (Ignored in Git)
├── db.sqlite3                 # Database
├── manage.py                  # Django management script
└── README.md                  # Project documentation
```

---

## 🖼 Model Placement

Place your trained model `crack_detector.h5` here:

```
crack_detection/models/crack_detector.h5
```

---

## ⚙️ Installation & Setup

1. **Clone the repo**

```bash
git clone <your-repo-url>
cd Building_Crack_Detection
```

2. **Create a virtual environment**

```bash
python -m venv crack_detection_env
source crack_detection_env/Scripts/activate  # For Windows
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Run migrations**

```bash
python manage.py makemigrations
python manage.py migrate
```

5. **Start the Django server**

```bash
python manage.py runserver
```

6. **Visit:** `http://127.0.0.1:8000/`

---

## 📤 Usage

- Upload an image of a building structure.
- The model predicts if the image has a crack or not.
- Result appears dynamically as a popup.

---

## 📑 Example .gitignore

```
media/
crack_detection/models/
__pycache__/
*.pyc
*.sqlite3
env/
crack_detection_env/
```

---

## ✅ TODO / Improvements

- Add history of uploaded images
- Improve model accuracy with more training
- Add frontend enhancements or loader while predicting
- Deploy the app on a cloud platform

---

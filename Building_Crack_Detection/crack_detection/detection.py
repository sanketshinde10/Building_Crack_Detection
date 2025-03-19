import os
from django.conf import settings
import tensorflow as tf
from .preprocessing import preprocess_image

def predict_crack(image_path):
    model_path = os.path.join(settings.BASE_DIR, 'crack_detection', 'models', 'crack_detector.h5')
    model = tf.keras.models.load_model(model_path)
    img = preprocess_image(image_path)
    prediction = model.predict(img)
    return "Crack Detected" if prediction > 0.5 else "No Crack Detected"
from tensorflow.keras.applications.vgg16 import VGG16, preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image
import numpy as np
import cv2

# Load VGG16 model with pre-trained weights
model = VGG16(weights='imagenet')

# Function to verify image integrity
def verify_image_integrity(image_path):
    # Load and resize image to 224x224
    img = image.load_img(image_path)
    img = img.resize((224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)

    preds = model.predict(x)
    return decode_predictions(preds, top=3)[0]

# Example usage
result = verify_image_integrity('output_image.jpg')
print("Image integrity check:", result)

from flask import Flask, request, jsonify,render_template
import tensorflow as tf
from tensorflow.keras.models import load_model
import numpy as np
import base64
from io import BytesIO
from PIL import Image

app = Flask(__name__)

model = load_model(r'C:\Users\dell\OneDrive\Documents\fruit_classifier\Image_classify.keras')
data_cat = ['apple', 'banana', 'Orange']
img_height = 180
img_width = 180

app= Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/classify', methods=['POST'])
def classify():
    data = request.get_json()
    image_data = data['image'].split(',')[1]
    image = Image.open(BytesIO(base64.b64decode(image_data)))
    image = image.resize((img_height, img_width))
    img_array = tf.keras.utils.img_to_array(image)
    img_bat = tf.expand_dims(img_array, 0)
    
    predict = model.predict(img_bat)
    score = tf.nn.softmax(predict[0])
    
    result = {
        'label': data_cat[np.argmax(score)],
        'accuracy': str(np.max(score) * 100)
    }
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)

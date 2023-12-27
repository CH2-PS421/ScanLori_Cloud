from fastapi import FastAPI, UploadFile, File, HTTPException
from tensorflow.keras.models import load_model
from tensorflow.keras.utils import get_file
from tensorflow.keras.utils import load_img
from tensorflow.keras.utils import img_to_array
from tensorflow import expand_dims
from tensorflow.nn import softmax
import tensorflow as tf
import numpy as np
from PIL import Image
import os
import io
import mysql.connector

class_names = ['air', 'apel', 'bakso', 'ikan', 'gudeg', 'cumi', 'Nasi', 'donat', 'bubur', 'anggur', 'mie', 'ayam', 'kentang', 'fu yung hai', 'Roti', 'kebab', 'cakwe', 'pempek', 'jeruk', 'serabi', 'soto', 'Tempe', 'es krim', 'ayam betutu', 'kacang', 'crepes', 'rawon', 'kopi', 'bakwan', 'batagor', 'sate', 'Tahu', 'burger', 'durian', 'nasi kuning', 'capcay', 'kerupuk']

model_dir = "models/image_classificationV2.h5"
model = load_model(model_dir)

def preprocess_image(image):
    image = image.resize((224, 224))  
    image_array = np.array(image)
    image_array = tf.keras.applications.xception.preprocess_input(image_array)
    image_array = np.expand_dims(image, axis=0)
    return image_array

def predict(image):
    try:
        prediction = model.predict(image)
        predicted_class = np.argmax(prediction)

        class_name = class_names[predicted_class]
        probability = np.max(prediction) * 100
    except Exception as e:
        return {"error" : str(e)}
    
    return {"class" : str(class_name), "probability" : probability}

def get_all():
    return Querying_filter("SELECT * FROM scanlori")

def filter_data(nama_makanan):
    return Querying_filter(f"SELECT * FROM scanlori WHERE nama_makanan LIKE \"%{str(nama_makanan)}%\"")

def filter_data_one_output(nama_makanan):
    return Querying_filter(f"SELECT * FROM scanlori WHERE nama_makanan LIKE \"{str(nama_makanan)}\"")

def send_query(qry):
    try:
        cnx = mysql.connector.connect(
            host='34.128.94.175',
            user='caps_CZLRVgMZ',
            password='6F737F3CB8C6F9E1E94B157EADFC81A5F0229865',
            database='caps-food-db'
        )
        cursor = cnx.cursor()
        query = qry
        cursor.execute(query)
        rows = cursor.fetchall()

        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="Item not found")
        
    except Exception as e:
        return str(e)
    finally:
        cursor.close()
        cnx.close()

    return rows

def Querying_filter(qry):
    rows = send_query(qry)
    json_data = []

    for row in rows:
        data = {
            'id': str(row[0]),
            'nama_makanan': str(row[1]),
            'kalori_kcal': str(row[2]),
            'kolesterol_mg': str(row[3]),
            'lemak_g': str(row[4]),
            'karbohidrat_g': str(row[5]),
            'protein_g': str(row[6]),
            'kalium_mg': str(row[7]),
            'nutrisi': str(row[8]),
            'ingredient': str(row[9]),
        }
        json_data.append(data)
    
    return {"data": json_data}

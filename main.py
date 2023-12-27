import os
import io
import apis_config as config
import function as func
from PIL import Image
from starlette.responses import FileResponse 
from fastapi import UploadFile, File

app = config.app

# Defining path operation for root endpoint
@app.get('/')
def main():
    return {'message': 'Welcome to Scanlori Model test API!'}

# Defining path operation for /documentation endpoint
@app.get("/documentation")
async def read_index():
    return FileResponse('doc/index.html')

# Defining path operation for /predict endpoint
@app.post('/predict')
async def predict_image(file: UploadFile = File(...)):
    # Read and preprocess the image
    content = await file.read()
    try:
        image = Image.open(io.BytesIO(content))
    except Exception as e:
        return func.response(status="error", e=e)
    
    image = func.preprocess_image(image)

    prediction = func.predict(image)

    # Return the predicted class
    return prediction

@app.get('/food')
async def get_data():
    # Get data from the database
    data = func.get_all()

    # Return the data as JSON response
    return data

@app.get('/food/{nama_makanan}')
async def get_specific_data(nama_makanan: str):
    data={}
    # Get data from the database
    data = func.filter_data(nama_makanan)

    # Return the data as JSON response
    if data: 
        return data
    else:
        return {"message": "No data found"}

@app.get('/food-specific/{nama_makanan}')
async def get_one_data(nama_makanan: str):
    data = {}

    if nama_makanan.lower() == "air":
        nama_makanan = "Air"
    elif nama_makanan.lower() == "anggur":
        nama_makanan = "Anggur"
    elif nama_makanan.lower() == "apel":
        nama_makanan = "Apel"
    elif nama_makanan.lower() == "ayam":
        nama_makanan = "Ayam"
    elif nama_makanan.lower() == "ayam betutu":
        nama_makanan = "Ayam Betutu"
    elif nama_makanan.lower() == "bakso":
        nama_makanan = "Bakso daging sapi"
    elif nama_makanan.lower() == "bakwan":
        nama_makanan = "Bakwan"
    elif nama_makanan.lower() == "batagor":
        nama_makanan = "Batagor"
    elif nama_makanan.lower() == "bubur":
        nama_makanan = "Bubur"
    elif nama_makanan.lower() == "burger":
        nama_makanan = "Burger"
    elif nama_makanan.lower() == "cakwe":
        nama_makanan = "Cakwe"
    elif nama_makanan.lower() == "capcay":
        nama_makanan = "Capcay"
    elif nama_makanan.lower() == "crepes":
        nama_makanan = "Crepes"
    elif nama_makanan.lower() == "cumi":
        nama_makanan = "Cumi"
    elif nama_makanan.lower() == "donat":
        nama_makanan = "Donat"
    elif nama_makanan.lower() == "durian":
        nama_makanan = "Durian"
    elif nama_makanan.lower() == "es krim":
        nama_makanan = "Es Krim"
    elif nama_makanan.lower() == "fu yung hai":
        nama_makanan = "Fu Yung Hai"
    elif nama_makanan.lower() == "gudeg":
        nama_makanan = "Gudeg"
    elif nama_makanan.lower() == "ikan":
        nama_makanan = "Ikan"
    elif nama_makanan.lower() == "jeruk":
        nama_makanan = "Jeruk"
    elif nama_makanan.lower() == "kacang":
        nama_makanan = "Kacang"
    elif nama_makanan.lower() == "kebab":
        nama_makanan = "Kebab"
    elif nama_makanan.lower() == "kentang":
        nama_makanan = "Kentang"
    elif nama_makanan.lower() == "kerupuk":
        nama_makanan = "Kerupuk"
    elif nama_makanan.lower() == "kopi":
        nama_makanan = "Kopi"
    elif nama_makanan.lower() == "mie":
        nama_makanan = "Mie"
    elif nama_makanan.lower() == "nasi kuning":
        nama_makanan = "Nasi Kuning"
    elif nama_makanan.lower() == "pempek":
        nama_makanan = "Pempek"
    elif nama_makanan.lower() == "rawon":
        nama_makanan = "Rawon"
    elif nama_makanan.lower() == "nasi":
        nama_makanan = "Nasi"
    elif nama_makanan.lower() == "sate":
        nama_makanan = "Sate ayam"
    elif nama_makanan.lower() == "serabi":
        nama_makanan = "Serabi"
    elif nama_makanan.lower() == "soto":
        nama_makanan = "Soto"
    elif nama_makanan.lower() == "tahu":
        nama_makanan = "Tahu"
    elif nama_makanan.lower() == "roti":
        nama_makanan = "Roti"
    elif nama_makanan.lower() == "tempe":
        nama_makanan = "Tempe"
    else:
        # Handle the case when the food is not in the list
        pass

    # Get data from the database
    data = func.filter_data_one_output(nama_makanan)
    # Return the data as JSON response
    if data: 
        return data
    else:
        return {"message": "No data found"}

if __name__ == "__main__":
	port = int(os.environ.get('PORT', 8080))
	run(app, host="0.0.0.0", port=port, timeout_keep_alive=1200)
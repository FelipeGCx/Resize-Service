import base64
from io import BytesIO
from PIL import Image
from flask import Flask, make_response, request

app = Flask(__name__)

@app.route('/ping', methods=['GET'])
def ping():
    return "pong"

@app.route('/resize', methods=['POST'])
def resize_image():
    try: 
        data = {
            "name":  request.json['name'],
            "size_x": request.json['size_x'],
            "size_y": request.json['size_y'],
            "type_format": request.json['type_format'],
            "base64": request.json['base64']
        }
    
        size = (data['size_x'],data['size_y'])
        new_format = data["type_format"]
        image_decode = base64.b64decode(data.get('base64'))
        image_buffer = BytesIO(image_decode)
        image = Image.open(image_buffer)
        image_resized = image.resize(size, Image.LANCZOS)
        output_buffer = BytesIO()
        image_resized.save(output_buffer, format=new_format)
        image_data = output_buffer.getvalue()
        image_base64 = base64.b64encode(image_data).decode()
        return image_base64
    except Exception as e:
        return make_response(f'Could not process the request, error: {e}', 400)        


if __name__ == '__main__':
    app.run(port=5000)

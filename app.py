import base64
import os
from PIL import Image
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/resize')
def Resize_Image():
    #     # begin here, pass the image in base 64
    #     # size = (467, 700)
    data = {
        "name":  request.json['name'],
        "size_x": request.json['size_x'],
        "size_y": request.json['size_y'],
        "type_format": request.json['type_format'],
        "base64": request.json['base64']
    }
    size = (data.get('size_x'),data.get('size_y'))
    name_final = data.get('name')+ data.get('type_format')
    name = data.get('name')+'.png'
    # decode the image and create one for manipulate
    image_64_decode = base64.b64decode(data.get('base64'))
    image_to_manipulate = open(name, 'wb')
    image_to_manipulate.write(image_64_decode)
    image_to_manipulate.close()
    # resize the image
    img = Image.open(name)
    img_final = img.resize(size, Image.ANTIALIAS)
    img_final.save(name_final)
    img_final.close()
    # encode image
    new = open(name_final, 'rb')
    image_read = new.read()
    image_64_encode = base64.b64encode(image_read)
    new.close()
    os.remove(name)
    os.remove(name_final)
    # stament return
    return jsonify({"base64":str(image_64_encode)})

if __name__ == '__main__':
    app.run(debug=True, port=5000)

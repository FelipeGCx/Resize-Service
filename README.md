# Images Resize Service

### this project is created to resize and parse the format of a image passed in base64.

---

# 🚀 Getting started to try or develop

### Install virtual enviroment if you don't have one

```bash
pip install virtualenv
```

### Create your virtual enviroment

```bash
virtualenv venv -p python3
```

### Init your virtual enviroment

```bash
source venv/bin/activate
```

### Install the requirement.txt

```bash
pip install -r requirements.txt
```

### Run the app helper

```bash
python3 app.py OR flask run
```

# 📑 Docs

### How use it

is very important know that to use this service you need to pass to the server path the endpoint `/resize` with the method `POST` and in the request body pass the next values as json format:

```json
{
  "name": "check",
  "size_x": 250,
  "size_y": 180,
  "type_format": ".webp",
  "base64": "your code"
}
```
- remember pass the format with the preffix dot `.` 
- the base64's code usually has this format (data:image/png;base64,iVBORw0KGgoAAAANSUhEUgA...) but for this service, you need to pass just the code after the `,`, don't pass this part (data:image/png;base64,)


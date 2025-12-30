import ollama
import base64
import os

def ai(image):
    def encode_image(image_path):
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')
    base64_image = encode_image(image)
    response = ollama.chat(
        model='llava',
        messages=[
            {
                'role': 'user',
                'content': 'Describe People in this image',
                'images': [base64_image]
            }
        ]
    )
    return response['message']['content']

def pic():
    image = 'picture.jpg'
    command = f'rpicam-jpeg -o {image}'
    os.system(command)
    return image

image = pic()
response = ai(image)
print(response)
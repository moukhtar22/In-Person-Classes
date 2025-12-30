from openai import OpenAI
import base64
import os
from gpiozero import MotionSensor

pir = MotionSensor(21)

def ai(image):
    key = 'YOUR API KEY'
    client = OpenAI(api_key=key)

    def encode_image(image_path):
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode("utf-8")

    base64_image = encode_image(image)

    response = client.responses.create(
        model="gpt-4.1",
        input=[
            {
                "role": "user",
                "content": [
                    { "type": "input_text", "text": 'Describe People in this image' },
                    {
                        "type": "input_image",
                        "image_url": f"data:image/jpeg;base64,{base64_image}",
                    },
                ],
            }
        ],
    )

    return response.output_text

def pic():
    image = 'picture.jpg'
    command = f'rpicam-jpeg -o {image}'
    os.system(command)
    return image

def process():
    image = pic()
    response = ai(image)
    print(response)

while True:
    pir.when_motion = process

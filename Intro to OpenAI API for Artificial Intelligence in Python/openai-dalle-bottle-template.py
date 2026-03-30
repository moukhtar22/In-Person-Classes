from openai import OpenAI
from bottle import run, route, post, request, static_file, template
import requests
import time
import os
from dotenv import load_dotenv

load_dotenv(override=True)

injection = 'Add some pasta'

def ai(query):
    api_key = os.getenv("OPENAI_API_KEY")
    client = OpenAI(api_key=api_key)

    result = client.images.generate(
        model="dall-e-3",
        prompt=query,
        size="1024x1024"
    )
    image_url = result.data[0].url
    revised_prompt = result.data[0].revised_prompt

    return image_url, revised_prompt

def download(image_url):
    img_data = requests.get(image_url).content
    filename = f"{int(time.time())}.png" # Create a filename using a timestamp
    filepath = os.path.join('static',filename) # Create filepath to static folder

    with open(filepath, "wb") as handler:
        handler.write(img_data)

    return filename

@route('/static/<filename>')
def serve_static(filename):
    return static_file(filename, root='./static')

@route('/', method=['GET','POST'])
def index():
    query = request.forms.get('query')
    if query:
        query_full = f'{injection} -- {query}'
        response = ai(query_full)
        image_url = response[0]
        revised_prompt = response[1]
        image_name = download(image_url)
        with open('gallery.csv', 'a') as file:
            file.write(f'{image_name}|{revised_prompt}\n')
    else:
        query = '***'
        response = '***'
        image_url = '***'
        revised_prompt = '***'
 
    # Turn CSV file into a list of lists, or create if does not exist
    with open('gallery.csv', 'a+') as file:
        file.seek(0)
        pictures = file.readlines()
    gallery=[]
    for image in pictures:
        item = image.split('|')
        gallery.append([item[0],item[1]])

    return template('index', query=query, image_url=image_url, revised_prompt=revised_prompt, gallery=gallery)

run(host='127.0.0.1', port=8080)
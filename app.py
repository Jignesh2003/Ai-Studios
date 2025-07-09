from flask import Flask, render_template, request
from groq import Groq
import requests
import io
from PIL import Image

GROQ_API_KEY = "<your-groq-api-key>"
# Hugging Face API
API_URL = "https://api-inference.huggingface.co/models/black-forest-labs/FLUX.1-dev"
headers = {"Authorization": "Bearer <your-hugging-face-api-key>"}

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/StoryGenerator',methods=['GET', 'POST'])
def StoryGenerator():
    generated_story = ''

    if request.method == 'POST':
        user_prompt = request.form.get('story_prompt')

        if user_prompt == "":
            generated_story = "Please enter a prompt to generate a story."
        
        else:

            if "generate a story on" or "Generate a Story on" in user_prompt:
                print("Prompt before trim: ", user_prompt)
                user_prompt = user_prompt.replace("Generate a Story on", "").replace("generate a story on", "").strip()
            
            client = Groq(
                api_key=GROQ_API_KEY,
            )

            chat_completion = client.chat.completions.create(
                messages=[
                    {
                        "role": "user",
                        "content": f"Generate a story on Topic '{user_prompt}'",
                    }
                ],
                model="llama3-8b-8192",
            )
            generated_story = chat_completion.choices[0].message.content

    return render_template('storyGenerator.html',generated_story=generated_story)

@app.route('/PoemGenerator',methods=['GET', 'POST'])
def PoemGenerator():
    generated_poem = ''

    if request.method == 'POST':
        user_prompt = request.form.get('poem_prompt')

        if user_prompt == "":
            generated_poem = "Please enter a prompt to generate a poem."

        else:

            if "generate a Poem on" or "Generate a Poem on" in user_prompt:
                print("Prompt before trim: ", user_prompt)
                user_prompt = user_prompt.replace("Generate a Poem on", "").replace("generate a poem on", "").strip()

            client = Groq(
                api_key=GROQ_API_KEY,
            )

            chat_completion = client.chat.completions.create(
                messages=[
                    {
                        "role": "user",
                        "content": f"Generate a poem on Topic '{user_prompt}'",
                    }
                ],
                model="llama3-8b-8192",
            )
            generated_poem = chat_completion.choices[0].message.content

    return render_template('poemGenerator.html',generated_poem=generated_poem)

@app.route('/ImageGenerator',methods=['GET', 'POST'])
def ImageGenerator():
    image_data = None

    if request.method == 'POST':
        image_prompt = request.form.get('image_prompt')

        if image_prompt == "":
            return render_template('imageGenerator.html', error="Please enter a prompt to generate an image.")

        # Call the Hugging Face API with the prompt
        def query(payload):
            response = requests.post(API_URL, headers=headers, json=payload)
            return response.content

        image_bytes = query({
            "inputs": image_prompt,
        })

        # Convert the response to an image using PIL
        image = Image.open(io.BytesIO(image_bytes))
        image.save("static/generated_image.png")  # Save the image to serve it

        # Set the image path for rendering in the template
        image_data = "static/generated_image.png"

    return render_template('imageGenerator.html', image_data=image_data)

if __name__ == '__main__':
    app.run(debug=True)
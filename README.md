# 🧠 Ai-Studios

**Ai-Studios** is a web-based platform that democratizes AI-powered content creation. It enables users to generate fictional stories, poems, and high-quality images from simple text prompts using large language models (LLMs), text-to-image diffusion models, and text-to-speech technology.

Developed as a final-year engineering project at Atharva College of Engineering, the platform addresses the issues of **accessibility**, **affordability**, and **efficiency** in creative content production, particularly for independent creators.

---
## 🔍 Overview
Ai-Studios provides a user-friendly platform to:
- ✍️ Generate creative **stories** from textual prompts
- 📝 Compose structured **poems** in real-time
- 🖼 Convert text to realistic **images** using generative AI

The platform reduces barriers for small-scale or non-technical creators, helping them produce high-quality multimedia content with ease.

---
## ✨ Key Features
- **Prompt-to-Story Generator**: Transforms input text into fully fleshed-out narratives.
- **Prompt-to-Poem Generator**: Creates poems from themes or emotions given by users.
- **Text-to-Image Generator**: Visualizes descriptive text into vivid images using diffusion models.
- **Simple UI/UX**: Clean and accessible design for all user levels.

---
## 🎯 Goals:
- Make AI tools accessible and affordable
- Enable creators to produce professional content without technical expertise
- Empower innovation in storytelling, poetry, and visual design

---
## 🧩 System Architecture

![image](https://github.com/user-attachments/assets/bb9e3753-af64-420c-95a0-d0782c3f3e1e)
![image](https://github.com/user-attachments/assets/75d78cce-98be-42cd-b58e-0a242bb54135)
![image](https://github.com/user-attachments/assets/d04ee0dd-d969-48f4-9e2a-7f81eb66f037)

---
## ⚙️ Tech Stack

- **Frontend**: HTML, CSS, Bootstrap
- **Backend**: Python, Flask
- **AI APIs**: Groq (for LLM), HuggingFace (for image generation)
- **Tools**: VS Code
- **Models Used using this apis**: llama3-8b-8192 (For Story & Poem Generation), FLUX.1-dev (For Image Generation)

---
## How to Use
- You just have to create your account on:
  - https://groq.com/
  - https://huggingface.co/
- Once the account is created then you have to generate your own API keys in both of this account then have to replace them with the below line of code.

```bash
GROQ_API_KEY = "<your-groq-api-key>"
# Hugging Face API
API_URL = "https://api-inference.huggingface.co/models/black-forest-labs/FLUX.1-dev"
headers = {"Authorization": "Bearer <your-hugging-face-api-key>"}
```
---
## How to Run
-Before typing all this commands make sure that inside the terminal you are in the project directory (eg D:\Ai-Studios>)
- Inside terminal just type the following command
```bash
pip install -r requirements.txt
```
The above command will install all the packages required for project to run

- Now inside terminal type the below command for you code to execute
```bash
python app.py
```
---
## 🖼 Screenshots

![image](https://github.com/user-attachments/assets/67e2165a-11f5-4119-b613-a84e00a3ea16)
![image](https://github.com/user-attachments/assets/6e436863-1a1b-4102-b95b-d3158cf003b0)
![image](https://github.com/user-attachments/assets/1d40ffd3-519e-44c3-ad64-dd8e658f7321)
![image](https://github.com/user-attachments/assets/e841a263-8666-4b4e-a974-033e12f6b30c)

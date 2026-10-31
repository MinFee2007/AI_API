# Lab 2: Application Programming Interface (API) - Computational Thinking

This project builds a Web API service based on **FastAPI** and an AI model from **Hugging Face** for the Lab 2 practical assignment in the Computational Thinking course.

---

## Student Information
* **Name:** Trần Minh Phi
* **Student ID:** *25127116*
* **Class:** *25C09*

---

## AI Model Information
* **Chosen model:** `j-hartmann/emotion-english-distilroberta-base`
* **Task:** Sentiment Analysis / Text Classification
* **Link Hugging Face:** [j-hartmann/emotion-english-distilroberta-base](https://huggingface.co/j-hartmann/emotion-english-distilroberta-base)

---

## System Description
The system functions as a Web API service that analyzes the sentiment of English sentences.
* It accepts text (a `string`) as input.
* Use the `j-hartmann` model to predict a sentiment label (`anger`, `disgust`, `fear`, `joy`, `sadness`, `surprise`, `neutral`) along with a confidence score from 0 to 1 using Top-k retrieval.
* Exception handling and automated input validation using `Pydantic`.

---

## Video link
* **Google Drive link:** [Google Drive video](https://drive.google.com/file/d/1WQF3dcOflowtcTkPJLCHvrNr1nmBfnho/view?usp=sharing)
* **Youtube link:** [Youtube video](https://youtu.be/_-4V7zKssIE?si=fhb-dhBqmUjcB5lS)
* **Complaint:** If you cannot access the video, please send a complaint via email `2512711614@student.hcmus.edu.vn`

---

## Install Instruction

1. **Clone repository to local desktop:**

Open git bash at the working folder then enter those commands:

   ```bash
   git clone https://github.com/tmphi2506-del/Project_AI_API.git
   cd Project_AI_API
   ```

2. **Create and activate a virtual environment:**

Open PowerShell/Terminal at the project folder (`Project_AI_API`) and enter those commands:

   ```PowerShell
   python -m venv .venv
   .venv\Scripts\Activate
   ```
If you prefer using Git Bash instead then here's the commands:

   ```bash
   source .venv/Scripts/activate
   ```

3. **Install the required tools:**

Make sure the virtual environment is activated, then enter this command in Git Bash:

   ```bash
   pip install -r requirements.txt
   ```

## Run Instruction

1. **Run the FastAPI server:**

Run this command on a terminal to start the API server:

   ```bash
   uvicorn main:app --reload
   ```

2. **Create a public URL for outer access (Optional):**

Open a new terminal and run this command:

   ```bash
   python tunnel.py
   ```

3. **Run the test file (Optional):**

Open a new terminal and run this command:

   ```bash
   python test_api.py
   ```

## How To Use The API

1. **Get API Introduction**

- Endpoint: `GET /`
- Description: Get the system general information
- Response:

   ```JSON
   {
  "message": "Welcome to the text sentiment analysis API!",
  "model": "j-hartmann/emotion-english-distilroberta-base",
  "emotions_supported": ["anger", "disgust", "fear", "joy", "sadness", "surprise", "neutral"],
  "usage": "Send POST request to /predict with body: {'text': 'content'}"
   }
   ```

2. **Health Check**

- Endpoint: `GET /health`
- Description: Get the system and model working state
- Response:

   ```JSON
   {
  "status": "healthy",
  "model_loaded": true
   }
   ```

3. **Text Sentiment Analysis**

- Endpoint: `POST \predict`
- Description: Receive input text and return analysis results
- Example request:

   ```JSON
   {
  "text": "I am so thrilled and happy that we completed this project successfully!"
   }
   ```

- Example response (success 200):

   ```JSON
   {
   "input_text": "I am so thrilled and happy that we completed this project successfully!",
   "emotions": [
      {
         "label": "joy",
         "score": 0.9542
      },
      {
         "label": "surprise",
         "score": 0.0231
      },
      {
         "label": "neutral",
         "score": 0.0120
      },
      {
         "label": "sadness",
         "score": 0.0045
      },
      {
         "label": "disgust",
         "score": 0.0021
      },
      {
         "label": "fear",
         "score": 0.0021
      },
      {
         "label": "anger",
         "score": 0.0020
      }
   ]
   }
   ```

- Example response (Error/Invalid input 422):
    ```JSON
    {
    "detail": [
        {
        "type": "string_too_short",
        "loc": ["body", "text"],
        "msg": "String should have at least 1 character",
        "input": ""
        }
    ]
    }
    ```
4. **Automatic Run Test**

To test all endpoints using a Python script, open a new terminal and run:

   ```bash
   python test_api.py
   ```

5. **Run manually using cURL on Command Prompt/Terminal:**

If you do not want to open a browser, you can type `curl` commands directly into another terminal window:

- Test GET / (Root):

   ```bash
   curl -X GET "http://127.0.0.1:8000/"
   ```

- Test GET /health (check state):

   ```bash
   curl -X GET "http://127.0.0.1:8000/health"
   ```

- Test POST /predict (analyze text):

   Command for Git Bash/MacOS/Linux:

   ```bash
   curl -X POST "http://127.0.0.1:8000/predict" \
   -H "Content-Type: application/json" \
   -d '{"text": "INPUT HERE"}'
   ```

   Command for Windows Command Prompt:

   ```bash
   curl -X POST "http://127.0.0.1:8000/predict" -H "Content-Type: application/json" -d "{\"text\": \"INPUT HERE\"}"
   ```

- If tunnel.py is running, you can replace the url `http://127.0.0.1:8000` with the public url(s) provided from the terminal of it.

- NOTE: On your first http request, the system will have to download the AI model cache into your hard disk so the command won't work on the first time. Keep waiting until the terminal of main.py notifies that the AI model is downloaded then you can use the API freely.
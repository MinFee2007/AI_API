from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from transformers import pipeline

# Start API
app = FastAPI(title="AI Model API", version="0.0")

# Model name in Hugging Face
MODEL = "j-hartmann/emotion-english-distilroberta-base"

# Load model from Hugging Face
try:
    model = pipeline("text-classification", model=MODEL, top_k=None)
except Exception as e:
    print(str(e))
    model = None

# Input format definition
class TextRequest(BaseModel):
    text:str = Field(..., min_length=1, description="The string to be analyzed must not be empty")

# Request for getting root, used for introduction
@app.get("/")
def read_root():
    """Get an introduction about the API"""
    return {
        "message": "Welcome to the text sentiment analysis API",
        "model": MODEL,
        "emotions_supported": ["anger", "disgust", "fear", "joy", "sadness", "surprise", "neutral"],
        "usage": "Send POST request to /predict with body: {'text': 'content'}"
    }

# Request for checking system and AI model state
@app.get("/health")
def health_check():
    """Check system and model state"""
    if model is None:
        raise HTTPException(status_code=500, detail="Model is not loaded")
    return {"status": "healthy", "model_loaded": True}

# Request for text sentiment analysis from AI model
@app.post("/predict")
def predict(payload:TextRequest):
    """Get input, call AI model and get result in format JSON"""
    if model is None:
        raise HTTPException(status_code=500, detail="Model service unavailable")
    
    try:
        results = model(payload.text)
        return {
            "input_text": payload.text,
            "emotion": results[0]
        }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error in analysis process: {str(e)}")
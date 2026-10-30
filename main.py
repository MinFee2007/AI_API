from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from transformers import pipeline

app = FastAPI(title="AI Model API", version="0.0")
MODEL = "j-hartmann/emotion-english-distilroberta-base"

try:
    model = pipeline("text-classification", model=MODEL, top_k=2)
except Exception as e:
    print(str(e))
    model = None

class TextRequest(BaseModel):
    text:str = Field(..., min_length=1, description="The string to be analyzed must not be empty")

@app.get("/")
def read_root():
    """Get an introduction about the API"""
    return {
        "message": "Welcome to the text sentiment analysis API",
        "model": MODEL,
        "emotions_supported": ["anger", "disgust", "fear", "joy", "sadness", "surprise", "neutral"],
        "usage": "Send POST request to /predict with body: {'text': 'content'}"
    }

@app.get("/health")
def health_check():
    """Check system and model state"""
    if model is None:
        raise HTTPException(status_code=500, detail="Model is not loaded")
    return {"status": "healthy", "model_loaded": True}

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
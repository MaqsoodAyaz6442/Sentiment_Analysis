from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import pipeline, RobertaForSequenceClassification, RobertaTokenizer
import nest_asyncio
import uvicorn

# Initialize FastAPI
app = FastAPI()

# Define a Pydantic model for the request body
class TextInput(BaseModel):
    text: str

# Define a function to load the model asynchronously during startup
async def load_model():
    global tokenizer, model
    tokenizer = RobertaTokenizer.from_pretrained("cardiffnlp/twitter-roberta-base-sentiment")
    model = RobertaForSequenceClassification.from_pretrained("cardiffnlp/twitter-roberta-base-sentiment")

# Use FastAPI's startup event to load the model
@app.on_event("startup")
async def startup_event():
    await load_model()

# Define the endpoint for text analysis
@app.post("/analyze")
async def analyze_text(input_data: TextInput):
    try:
        # Get the text from the request body
        text = input_data.text

        # Tokenize the text
        inputs = tokenizer(text, return_tensors="pt")

        # Perform sentiment analysis on the text using the loaded model
        outputs = model(**inputs)
        predictions = outputs.logits.argmax(-1)
        sentiment = "positive" if predictions == 2 else "neutral" if predictions == 1 else "negative"

        # Return the sentiment
        return {"sentiment": sentiment}
    except Exception as e:
        # If any error occurs, return an HTTP 500 error
        raise HTTPException(status_code=500, detail=str(e))

# Add a simple endpoint for testing
@app.get("/")
async def read_root():
    return {"message": "Welcome to the sentiment analysis API!"}

# Start the FastAPI application
if __name__ == "__main__":
    nest_asyncio.apply()
    uvicorn.run(app, host="0.0.0.0", port=8000)

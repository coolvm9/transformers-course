import logging
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import pipeline
from typing import List

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()
classifier = pipeline("sentiment-analysis")



class Sentences(BaseModel):
    texts: List[str]

@app.post("/sentiment/")
async def get_sentiment(sentences: Sentences):
    try:
        results = [classifier(text) for text in sentences.texts]
        logger.info("Sentiment analysis performed on multiple sentences")
        return results
    except Exception as e:
        logger.error(f"Error during sentiment analysis: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))
@app.get("/")
@app.get("/heartbeat")
def heartbeat():
    logger.info("Heartbeat checked")
    return {"status": "alive"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5010)
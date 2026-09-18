from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, Dict, Any, List
from knowledge_base import retrieve_knowledge

app = FastAPI(title="Darukaa AI Biodiversity Chatbot API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    message: str
    language: str = "en"  # "en", "hi", "kn"
    context: Optional[Dict[str, Any]] = None

class ChatResponse(BaseModel):
    response: str
    recommendation: Optional[str] = None
    scientific_reasoning: Optional[str] = None
    impacted_metrics: Optional[List[str]] = None
    time_horizon: Optional[str] = None
    confidence: Optional[str] = None
    reference: Optional[str] = None

# Fallback UI strings for backend
STRINGS = {
    "en": {
        "clarify": "Could you provide more details about your land? For example, what is the current soil organic carbon %, rainfall pattern, and land use type?",
        "found": "Based on my environmental analysis, here is what I found."
    },
    "hi": {
        "clarify": "क्या आप अपनी भूमि के बारे में अधिक जानकारी दे सकते हैं? उदाहरण के लिए, वर्तमान मिट्टी जैविक कार्बन %, वर्षा पैटर्न, और भूमि उपयोग का प्रकार क्या है?",
        "found": "मेरे पर्यावरणीय विश्लेषण के आधार पर, मुझे यह मिला है।"
    },
    "kn": {
        "clarify": "ನಿಮ್ಮ ಭೂಮಿಯ ಬಗ್ಗೆ ಹೆಚ್ಚಿನ ವಿವರಗಳನ್ನು ನೀಡುವಿರಾ? ಉದಾಹರಣೆಗೆ, ಪ್ರಸ್ತುತ ಮಣ್ಣಿನ ಸಾವಯವ ಇಂಗಾಲದ %, ಮಳೆಯ ಮಾದರಿ, ಮತ್ತು ಭೂ ಬಳಕೆಯ ಪ್ರಕಾರ ಯಾವುದು?",
        "found": "ನನ್ನ ಪರಿಸರ ವಿಶ್ಲೇಷಣೆಯ ಆಧಾರದ ಮೇಲೆ, ನಾನು ಕಂಡುಕೊಂಡದ್ದು ಇಲ್ಲಿದೆ."
    }
}

@app.post("/chat", response_model=ChatResponse)
async def chat_endpoint(req: ChatRequest):
    target_lang = req.language
    if target_lang not in ["en", "hi", "kn"]:
        target_lang = "en"
        
    # We will pass the original text to retrieve_knowledge. 
    # Since conditions are English words, a real system would translate to EN first.
    # For this mock, we just check if it finds a match, else it falls back nicely.
    # A user typing in Hindi might not trigger the English keyword match, but we have a random fallback.
    # Let's add a quick keyword map so it actually matches if they use specific words.
    
    user_input = req.message.lower()
    
    # Conversational Intelligence: Ask clarifying questions if inputs are incomplete
    if len(user_input.split()) < 3 and not req.context:
        return ChatResponse(response=STRINGS[target_lang]["clarify"])
        
    # Retrieve knowledge (Mock RAG)
    knowledge = retrieve_knowledge(user_input, req.context)
    
    response_text = STRINGS[target_lang]["found"]
    
    return ChatResponse(
        response=response_text,
        recommendation=knowledge.get("recommendation", {}).get(target_lang, ""),
        scientific_reasoning=knowledge.get("scientific_reasoning", {}).get(target_lang, ""),
        impacted_metrics=knowledge.get("impacted_metrics", {}).get(target_lang, []),
        time_horizon=knowledge.get("time_horizon", {}).get(target_lang, ""),
        confidence=knowledge.get("confidence", {}).get(target_lang, ""),
        reference=knowledge.get("reference", {}).get(target_lang, "")
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

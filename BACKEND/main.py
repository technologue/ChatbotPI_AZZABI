from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
app = FastAPI()



app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class AnalyseTexteInput(BaseModel):
    texte: str
@app.post("/analyse")
def analyse_endpoint(analyse_input: AnalyseTexteInput):
    print(analyse_input)
    return {"msg": analyse_input}
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)

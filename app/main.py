from fastapi import FastAPI
import uvicorn
from app.utils import get_player_projections
from fastapi.responses import JSONResponse, FileResponse
import pandas as pd

app = FastAPI()

@app.get("/rankings")
def get_rankings():
    df = get_player_projections()
    df_sorted = df.sort_values(by="projected_points", ascending=False)
    df_sorted.to_csv("ranked_players.csv", index=False)
    return JSONResponse(content=df_sorted.to_dict(orient="records"))

@app.get("/download")
def download_csv():
    return FileResponse("ranked_players.csv", media_type="text/csv", filename="ranked_players.csv")

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

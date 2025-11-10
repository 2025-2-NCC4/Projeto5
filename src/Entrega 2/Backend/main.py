from fastapi import FastAPI, HTTPException
from services.loader import list_data_files, load_table
from typing import List

app = FastAPI(title="CupomGO Backend API", version="1.0.0")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/data/files", response_model=List[str])
def get_files():
    return list_data_files()

@app.get("/data/preview")
def preview(filename: str, n: int = 10):
    try:
        df = load_table(filename)
        return {"filename": filename, "columns": list(df.columns), "head": df.head(n).to_dict(orient="records")}
    except FileNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

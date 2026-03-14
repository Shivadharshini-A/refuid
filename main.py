from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import uuid
from datetime import datetime, timedelta
import hashlib
import random

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

database = []

@app.post("/register")
async def register_face(file: UploadFile = File(...)):

    contents = await file.read()

    if not contents:
        return {"message": "No image received"}

    face_hash = hashlib.md5(contents).hexdigest()

    for person in database:
        if person["hash"] == face_hash:
            return person

    short_id = str(uuid.uuid4())[:8]
    refugee_id = f"REF-{short_id}"

    registered = datetime.now()
    expiry = registered + timedelta(days=90)

    risk = random.choice(["Low", "Medium", "High"])

    record = {
        "id": refugee_id,
        "hash": face_hash,
        "registered": registered.strftime("%Y-%m-%d"),
        "expiry": expiry.strftime("%Y-%m-%d"),
        "risk": risk,
        "location": "Border Checkpoint"
    }

    database.append(record)

    return record


@app.get("/verify/{refugee_id}")
def verify_refugee(refugee_id: str):

    for person in database:
        if person["id"] == refugee_id:

            return f"""
            <html>
            <head>
            <title>Refugee Identity Verification</title>
            <style>
            body {{
                font-family: Arial;
                background:#0b1e2d;
                display:flex;
                justify-content:center;
                align-items:center;
                height:100vh;
                color:white;
            }}

            .card {{
                background: linear-gradient(135deg,#1e3c72,#2a5298);
                padding:30px;
                border-radius:15px;
                width:350px;
                box-shadow:0 10px 25px rgba(0,0,0,0.4);
            }}

            h2 {{
                text-align:center;
                margin-bottom:20px;
            }}

            p {{
                font-size:18px;
                margin:8px 0;
            }}

            </style>
            </head>

            <body>

            <div class="card">

            <h2>Digital Border ID</h2>

            <p><b>ID:</b> {person["id"]}</p>
            <p><b>Status:</b> Registered</p>
            <p><b>Registered:</b> {person["registered"]}</p>
            <p><b>Expiry:</b> {person["expiry"]}</p>
            <p><b>Risk Level:</b> {person["risk"]}</p>
            <p><b>Location:</b> {person["location"]}</p>

            </div>

            </body>
            </html>
            """

    return {"message": "Identity not found"}
def verify_refugee(refugee_id: str):

    for person in database:
        if person["id"] == refugee_id:

            return f"""
            <h1>Refugee Identity Verification</h1>
            <p><b>ID:</b> {person["id"]}</p>
            <p><b>Status:</b> Registered</p>
            <p><b>Registered:</b> {person["registered"]}</p>
            <p><b>Expiry:</b> {person["expiry"]}</p>
            <p><b>Risk Level:</b> {person["risk"]}</p>
            <p><b>Location:</b> {person["location"]}</p>
            """

    return {"message": "Identity not found"}
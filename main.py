from fastapi import FastAPI
from env import load_dotenv
import uuid
from search import search_discovery_engine
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from google.cloud.dialogflowcx_v3beta1.services.sessions import SessionsClient
from google.cloud.dialogflowcx_v3beta1.types import session
from google.api_core.client_options import ClientOptions
import os
from chat import multiturn_generate_content
# from wrapper import proto_to_dict

load_dotenv('.env')

LOCATION = os.getenv("LOCATION")
PROJECT_ID = os.getenv("PROJECT_ID")
LOCATION_DFCX = "us-central1"
DFCX_AGENT_ID = "aa622db9-6d4a-49a5-a6a7-af0dc7f90116"

# Initialize Dialogflow CX client with correct endpoint
client_options = ClientOptions(
    api_endpoint=f"{LOCATION_DFCX}-dialogflow.googleapis.com")
client = SessionsClient(client_options=client_options)

# Define Pydantic models for request data


class QueryModel(BaseModel):
    query: str


class DatastoreImportModel(BaseModel):
    pdf_gcs_filename: str
    category: str
    tenant: str
    description: str
    year: str


# Create FastAPI app
app = FastAPI()


# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    # Allow all origins (for development, be more specific in production)
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
)


# Define API endpoints


@app.get("/api/ping")
async def ping():
    return {"status": "pong"}


@app.post("/api/search")
async def search(query_model: QueryModel):
    search_results = search_discovery_engine(
        location=LOCATION, search_query=query_model.query)
    return search_results

# Create a model for chat


class ChatModel(BaseModel):
    query: str


@app.post("/api/chat")
async def chat(chat_request: ChatModel):
    result = multiturn_generate_content(message=chat_request.query)
    return {"response": str(result).replace(" \n", "")}

import os
from dotenv import load_dotenv

load_dotenv('.env')

PROJECT_ID = os.getenv("PROJECT_ID")
LOCATION = os.getenv("LOCATION")
DATASTORE_ID = os.getenv("DATASTORE_ID")
AGENT_APPLICATION_ID = os.getenv("AGENT_APPLICATION_ID")


def show_all_env():
    response = f"""PROJECT_ID: {PROJECT_ID}\nLOCATION: {LOCATION}\nDATASTORE_ID: {DATASTORE_ID}\nAGENT_APPLICATION_ID: {AGENT_APPLICATION_ID}"""
    print(response)
    return response


show_all_env()

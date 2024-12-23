from typing import List
from google.api_core.client_options import ClientOptions
from google.cloud import discoveryengine_v1 as discoveryengine
from wrapper import proto_to_dict
import os
# from google.oauth2 import service_account

# key_file = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")

# credentials = service_account.Credentials.from_service_account_file(
#     key_file)

PROJECT_ID = os.getenv("PROJECT_ID")
LOCATION = os.getenv("LOCATION")
AGENT_APPLICATION_ID = os.getenv("AGENT_APPLICATION_ID")


def search_discovery_engine(
    search_query: str,
    location: str = "global",
    page_size: int = 1,
) -> List[discoveryengine.SearchResponse]:
    #  For more information, refer to:
    # https://cloud.google.com/generative-ai-app-builder/docs/locations#specify_a_multi-region_for_your_data_store
    client_options = (
        ClientOptions(
            api_endpoint=f"{LOCATION}-discoveryengine.googleapis.com")
        if location != "global"
        else None
    )

    # Create a client
    client = discoveryengine.SearchServiceClient(
        client_options=client_options)

    # The full resource name of the search app serving config
    product_serving_config = f"projects/{PROJECT_ID}/locations/{LOCATION}/collections/default_collection/engines/{AGENT_APPLICATION_ID}/servingConfigs/default_config"

    # Refer to the `SearchRequest` reference for all supported fields:
    # https://cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.SearchRequest
    search_request = discoveryengine.SearchRequest(
        serving_config=product_serving_config,
        query=search_query,
        page_size=page_size
    )

    search_response = search(client, search_request)
    return search_response


@proto_to_dict
def search(client, search_request):
    return client.search(search_request)

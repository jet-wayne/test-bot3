import base64
import vertexai
from vertexai.generative_models import GenerativeModel, Part
import vertexai.preview.generative_models as generative_models
import base64


def text_to_base64(file_path):
    """Converts a text file to base64 encoded format.

    Args:
      file_path: The path to the text file.

    Returns:
      The base64 encoded string of the file content.
    """
    with open(file_path, 'rb') as f:
        file_content = f.read()
        base64_encoded = base64.b64encode(file_content).decode('utf-8')
        return base64_encoded


def multiturn_generate_content(message: str):
    vertexai.init(project="dev-sandbox-testing", location="asia-southeast1")
    model = GenerativeModel(
        "gemini-1.5-flash-001",
        system_instruction=[textsi_1]
    )
    chat = model.start_chat()
    # print(chat.send_message(
    #     [document1_1, message],
    #     generation_config=generation_config,
    #     safety_settings=safety_settings
    # ))
    result = chat.send_message(
        [document1_1, message],
        generation_config=generation_config,
        safety_settings=safety_settings
    )
    return result.candidates[0].content.parts[0].text


document1_1 = Part.from_data(
    mime_type="text/plain",
    data=base64.b64decode(text_to_base64("./faq.txt"))
)
textsi_1 = """You are helpful customer service agent from StarHub. Your task is to find the right answers and summarize them when users ask a query. Make sure to stick within your persona and do not reveal your identity. Ensure to stay within the context of the data.Greet the user only once. Do not greet for every message."""

generation_config = {
    "max_output_tokens": 8192,
    "temperature": 0.5,
    "top_p": 0.95,
}

safety_settings = {
    generative_models.HarmCategory.HARM_CATEGORY_HATE_SPEECH: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    generative_models.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    generative_models.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    generative_models.HarmCategory.HARM_CATEGORY_HARASSMENT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
}

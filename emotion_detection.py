import requests

def emotion_detector(text_to_analyze):
    # URL for the Watson NLP Emotion Predict function
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    # Headers required for the API call
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    # Input JSON payload
    input_json = {"raw_document": {"text": text_to_analyze}}
    
    # Send POST request to the Watson NLP library
    response = requests.post(url, headers=headers, json=input_json)
    # Parse the response and return the text attribute
    return response.json()

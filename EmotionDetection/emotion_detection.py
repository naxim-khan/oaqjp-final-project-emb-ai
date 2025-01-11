import requests
import json

def emotion_detector(text_to_analyze):
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = {"raw_document": {"text": text_to_analyze}}

    try:
        # Send POST request
        response = requests.post(url, headers=headers, json=input_json)
        response.raise_for_status()

        # Convert response to dictionary
        response_dict = json.loads(response.text)

        # Extracting emotions from the response
        emotion_predictions = response_dict.get("emotionPredictions", [])
        if emotion_predictions:
            emotions = emotion_predictions[0].get("emotion", {})
        else:
            emotions = {}

        if not emotions:  # Handle case where emotions are missing
            return {
                'anger': 0,
                'disgust': 0,
                'fear': 0,
                'joy': 0,
                'sadness': 0,
                'dominant_emotion': None
            }

        # Extract scores
        anger = emotions.get("anger", 0)
        disgust = emotions.get("disgust", 0)
        fear = emotions.get("fear", 0)
        joy = emotions.get("joy", 0)
        sadness = emotions.get("sadness", 0)

        # Find the dominant emotion
        dominant_emotion = max(emotions, key=emotions.get)

        # Return output in required format
        return {
            'anger': anger,
            'disgust': disgust,
            'fear': fear,
            'joy': joy,
            'sadness': sadness,
            'dominant_emotion': dominant_emotion
        }

    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}
    except Exception as e:
        return {"error": f"An unexpected error occurred: {str(e)}"}

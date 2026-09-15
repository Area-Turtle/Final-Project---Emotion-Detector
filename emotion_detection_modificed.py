import requests
import json

url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict" 

headers = { "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock" } 

def emotion_detector(text_to_analyse):

    input_json = {"raw_document": {"text": text_to_analyse}}

    response = requests.post(
        url,
        headers=headers,
        json=input_json,
        timeout=30
    )

    response_dict = json.loads(response.text)

    emotions = response_dict["emotionPredictions"][0]["emotion"]

    anger_score = emotions["anger"]
    disgust_score = emotions["disgust"]
    fear_score = emotions["fear"]
    joy_score = emotions["joy"]
    sadness_score = emotions["sadness"]

    emotion_scores = {
        "anger": anger_score,
        "disgust": disgust_score,
        "fear": fear_score,
        "joy": joy_score,
        "sadness": sadness_score
    }

    dominant_emotion = max(emotion_scores, key=emotion_scores.get)

    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }

# >>> from emotion_detection import emotion_detector
# >>> emotion_detector("I am so happy I am doing this.")
# {'anger': 0.0043339236, 'disgust': 0.00037549555, 'fear': 0.0034732423, 'joy': 0.9947189, 'sadness': 0.012704818, 'dominant_emotion': 'joy'}
# >>> 

#mv ./emotion_detection.py ./EmotionDetection


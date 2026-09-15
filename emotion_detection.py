import requests

url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict" 

headers = { "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock" } 

def emotion_detector(text_to_analyse): 
   
    input_json = { "raw_document": { "text": text_to_analyse } } 

    response = requests.post(url, headers=headers, json=input_json,timeout=30) 

    return response.text

# from emotion_detection import emotion_detector

# emotion_detector("I love this new technology.")

# theia@theiadocker-zachary007:/home/project$ python3
# >>> from emotion_detection import emotion_detector
# >>> emotion_detector("I love this new technology.")
# '{"emotionPredictions":[{"emotion":{"anger":0.01364663, "disgust":0.0017160787, "fear":0.008986978, "joy":0.9719017, "sadness":0.055187024}, "target":"", "emotionMentions":[{"span":{"begin":0, "end":27, "text":"I love this new technology."}, "emotion":{"anger":0.01364663, "disgust":0.0017160787, "fear":0.008986978, "joy":0.9719017, "sadness":0.055187024}}]}], "producerId":{"name":"Ensemble Aggregated Emotion Workflow", "version":"0.0.1"}}'

# from EmotionDetection.emotion_detection import emotion_detector
# emotion_detector("I hate working long hours.")
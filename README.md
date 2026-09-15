# Repository for final project
Final project

# Dependencies
Download python3 dependencies (python3 -m pip install <name of library>)
- python3 (or greater)
- requests
- flask
- pylint

# Emotion Prediction Function (Watson NLP Library)
URL: 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
Headers: {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
Input json: { "raw_document": { "text": text_to_analyze } }

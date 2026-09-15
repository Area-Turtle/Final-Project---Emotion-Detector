url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"

headers = {
    "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
}

def emotion_detector(text_to_analyze):
    input_json = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    return input_json

# from emotion_detection import emotion_detector

# emotion_detector("I love this new technology.")

# theia@theiadocker-zachary007:/home/project$ python3
# Python 3.10.12 (main, Aug 15 2025, 14:32:43) [GCC 11.4.0] on linux
# Type "help", "copyright", "credits" or "license" for more information.
# >>> from emotion_detection import emotion_detector
# >>> emotion_detector("I love this new technology.")
# {'raw_document': {'text': 'I love this new technology.'}}
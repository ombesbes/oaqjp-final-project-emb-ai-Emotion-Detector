import json
import requests

def emotion_detector(text_to_analyze):
    
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = myobj, headers=header)
    
    # If the response status code is 200, extract the scores of the emotions from the response
    if response.status_code == 200:
        formatted_response = json.loads(response.text)
        # predicted emotions dictionary
        emotions= formatted_response['emotionPredictions'][0]['emotion']
        # dominant emotion
        d = max(emotions, key=emotions.get)
        emotions['dominant_emotion'] = d
    
    # If the response status code is 400, set the scores of the emotions to None
    elif response.status_code == 400:
        emotions = {
            "anger": None, 
            "disgust": None, 
            "fear": None, 
            "joy": None, 
            "sadness": None, 
            "dominant_emotion": None
            }
    return emotions

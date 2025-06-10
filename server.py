# Import Flask, render_template, request from the flask framework package : 
from flask import Flask, render_template, request

# Import the emotion_detector function from the package created: 
from EmotionDetection.emotion_detection import emotion_detector
#Initiate the flask app : 
app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def emo_detector():

    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the sentiment_analyzer function and store the response
    response = emotion_detector(text_to_analyze)
    
    # Extract the dominant emotion from the response
    dominant_emotion = response['dominant_emotion']

    # Check if the dominant_emotion is not None, extract the scores of the emotions from the response
    if dominant_emotion is not None:
        pairs = [f"{k}: {v}" for k, v in response.items()]
        str1 = "For the given statement, the system response is "
        str2 = " and ".join([", ".join(pairs[:-2]), pairs[-2]])
        str3 = f". The dominant emotion is {dominant_emotion}."
        st = str1 + str2 + str3
        # Return a formatted string with the scores for the different emotions
        return st
    else:
        #if the dominant_emotion is None, indicating an error or invalid input
        return "Invalid text! Please try again!"

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    ''' This functions executes the flask app and deploys it on localhost:5000
    '''
    app.run(host='0.0.0.0', port=5000)

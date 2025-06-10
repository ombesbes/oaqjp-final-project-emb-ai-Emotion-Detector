''' Executing this function initiates the application of Emotion Detection 
    to be executed over the Flask channel and deployed on
    localhost:5000.
'''
# Import Flask, render_template, request from the flask framework package
from flask import Flask, render_template, request

# Import the emotion_detector function from the package created
from EmotionDetection.emotion_detection import emotion_detector
#Initiate the flask app
app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def emo_detector():
    ''' This code receives the text from the HTML interface and 
        runs Emotion Detection over it using emotion_detector()
        function. The output returned shows the scores for the different emotions
    '''
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyze)
    # Extract the dominant emotion from the response
    dominant_emotion = response['dominant_emotion']

    # Check if the dominant_emotion is not None
    if dominant_emotion is not None:
        pairs = [f"{k}: {v}" for k, v in response.items()]
        str1 = "For the given statement, the system response is "
        str2 = " and ".join([", ".join(pairs[:-2]), pairs[-2]])
        str3 = f". The dominant emotion is {dominant_emotion}."
        # formatted string with the scores for the different emotions
        st = str1 + str2 + str3
    else:
        #if the dominant_emotion is None, indicating an error or invalid input
        st = "Invalid text! Please try again!"
    return st

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

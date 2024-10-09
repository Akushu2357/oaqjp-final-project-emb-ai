from EmotionDetection.emotion_detection import emotion_detector

test = ["I am glad this happened", 
        "I am really mad about this",
        "I feel disgusted just hearing about this",
        "I am so sad about this",
        "I am really afraid that this will happen"]

for i in test:
    print(i + ': ' + emotion_detector(i)['dominant_emotion'])
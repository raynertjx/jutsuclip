from flask import Flask, request, jsonify
import cv2
import numpy as np
import HandTrackingModule as htm
import base64
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/test', methods=['GET', 'POST', 'OPTIONS'])
def test_route():
    return jsonify({'message': 'Test successful'})

@app.route('/process_image', methods=['POST'])
def process_image():
    print("request receiced")
    # Get the image from the request
    data = request.json['image']
    # Convert the base64 string to a numpy array
    decoded_data = base64.b64decode(data)
    np_data = np.frombuffer(decoded_data, np.uint8)
    img = cv2.imdecode(np_data, cv2.IMREAD_COLOR)
    detector = htm.handDetector(detectionCon=0.75)
    tipIds = [4, 8, 12, 16, 20]
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)
    #print(lmList)

    handType = detector.findHandType(img)

    if len(lmList) != 0 and handType is not None:
        fingers = []
        # Thumb
        print(handType)
        if handType == 'Right':
            if lmList[tipIds[0]][1] < lmList[tipIds[0] - 1][1]:
                fingers.append(1)
            else:
                fingers.append(0)
        
        elif handType == 'Left':
            if lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1]:
                fingers.append(1)
            else:
                fingers.append(0)

        # 4 Fingers
        for id in range(1, 5):
            if lmList[tipIds[id]][2] < lmList[tipIds[id] - 2][2]:
                fingers.append(1)
            else:
                fingers.append(0)

        #print(fingers)
        totalFingers = fingers.count(1)
        print(totalFingers)

        # Return the results
        return jsonify({'totalFingers': totalFingers, 'handType': handType})

if __name__ == '__main__':
    app.run(debug=True)

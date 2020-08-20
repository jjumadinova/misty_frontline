from mistyPy import Robot

misty = Robot("192.168.0.11")
misty.subscribe("FaceRecognition")
misty.learnFace("Me")
data = misty.faceRec()
print(data)                     # {'personName' : 'Samanta', 'distance' : '95', 'elevation' : '6'}
# name      = data["personName"]  # You could extract specific values of your interest like this
# distance  = data["distance"]    # units in mm
# elevation = data["elevation"]
misty.unsubscribe("FaceRecognition")

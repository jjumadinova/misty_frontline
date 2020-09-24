from mistyPy import Robot
import time

misty = Robot("192.168.0.8")
# misty.subscribe("FaceRecognition")
# misty.clearLearnedFaces()
# misty.save_face_per_sec()
print("start")
misty.startRecordingAudio("audio/pytest.wav")
time.sleep(5)
misty.stopRecordingAudio()
print("end")
misty.populateAudio()
misty.printAudioList()

# misty.learnFace("Me")
# data = misty.faceRec()
# print(data)                     # {'personName' : 'Samanta', 'distance' : '95', 'elevation' : '6'}
# name      = data["personName"]  # You could extract specific values of your interest like this
# distance  = data["distance"]    # units in mm
# elevation = data["elevation"]
# misty.unsubscribe("FaceRecognition")

# print(misty.populateLearnedFaces())

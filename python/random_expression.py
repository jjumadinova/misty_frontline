from mistyPy import Robot
import time
import random


def random_positive():
    positive_pairs = [["e_EcstacyHilarious.jpg", "s_Ecstacy2.wav"], ["e_Joy.jpg", "s_Joy3.wav"], ["e_Love.jpg", "s_Love.wav"], ["e_Surprise.jpg", "s_Awe2.wav"], ["e_Joy2.jpg", "s_Ecstacy.wav"]]
    index = random.randint(1,5)
    misty.changeImage(positive_pairs[index][0])
    time.sleep(1)
    misty.playAudio(positive_pairs[index][1])
    time.sleep(4)
    misty.changeImage("e_DefaultContent.jpg")

misty = Robot("192.168.0.7")
# misty.printImageList()
# time.sleep(5)
# misty.changeImage("e_Joy.jpg")
# time.sleep(5)
# misty.changeImage("e_DefaultContent.jpg")

# random_positive()

# recording
# Positive
# "e_EcstacyHilarious.jpg", "s_Ecstacy2.wav"
# "e_Joy.jpg", "s_Joy3.wav"
# "e_Love.jpg", "s_Love.wav"
# "e_Surprise.jpg", "s_Awe2.wav"
# "e_Joy2.jpg", "s_Ecstacy.wav"
# Negative
# "e_TerrorLeft.jpg", "e_TerrorRight.jpg", "e_Terror.jpg", "e_Disoriented.jpg", "s_DisorientedConfused.wav", "s_DisorientedConfused3.wav", "s_Fear.wav"
# "e_Terror.jpg", "s_Fear.wav"
# "e_Rage.jpg", "e_Rage2.jpg", "s_Anger.wav", "s_Rage.wav"
# "e_Rage.jpg", "s_Rage.wav"
# "e_Anger.jpg", "s_Anger2.wav"
# "e_Disgust.jpg", "s_Disgust2.wav"
# "e_ApprehensionConcerned.jpg", "s_Annoyance.wav" or "s_Annoyance3.wav"

time.sleep(7)
misty.changeImage("e_Joy.jpg")
time.sleep(1)
misty.playAudio("s_Joy.wav")
time.sleep(6)
misty.changeImage("e_DefaultContent.jpg")

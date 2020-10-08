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

random_positive()



# time.sleep(5)
# misty.changeImage("e_Joy.jpg")
# time.sleep(1)
# misty.playAudio("s_Joy.wav")
# time.sleep(4)
# misty.changeImage("e_DefaultContent.jpg")

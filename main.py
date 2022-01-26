import random


ALPHA = list("abcdefghijklmnopqrstuvwxyz")


def makekey():
    int_list = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
    random.shuffle(int_list)

    return int_list


def encrypt(text):
    wheelsfile = open("wheels/wheels.txt", 'r')
    wheelscontent = wheelsfile.readlines()

    tmptext = list(text)

    key_history = []
    text_history = []
    for i in wheelscontent:
        wheel = i
        wheel.strip()
        key = makekey()
        key_history.append(key)
        currentkey = []
        etext = ""
        wheel = list(wheel)

        for j in range(len(tmptext)):
            key_choice = random.choice(key)
            currentkey.append(key_choice)

            if tmptext[j] not in ALPHA:

                etext += tmptext[j]
                continue

            etext += wheel[key_choice]

        tmptext = etext
        key_history.append(currentkey)
        text_history.append(etext)

    return key_history, text_history


keys, history = encrypt("the pigeon was very fast")

print(history[4])

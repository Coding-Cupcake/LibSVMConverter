import os

SEPARATOR = ','
DIRECTORY = os.curdir + "/data/"
DIRECTORY_OUT = os.curdir + "/output_lib_svm/original/"


def pre_processing():
    label_nr = open("config.cfg", 'r')
    lines = label_nr.readlines()
    return int(lines[1])


for currentFile in os.listdir(DIRECTORY):
        if currentFile.endswith('.csv'):
            output = open(DIRECTORY_OUT + os.path.splitext(currentFile)[0] + "_Out", 'w')
            source = open(DIRECTORY + currentFile, 'r')
            class_label = pre_processing()
            for line in source:
                index = 1
                features = line.split(SEPARATOR)
                features[0], features[class_label] = features[class_label], features[0]
                label = float(features[0])
                features[0] = int(round(label))
                for feature in features[1:]:
                    features[index] = repr(index) + ":" + features[index]
                    index += 1
                print features

                size = len(features)
                i = 0

                for feat in features:
                    if i < size - 1:
                        output.write(str(feat) + " ")
                        i += 1
                    else:
                        output.write(str(feat))
source.close()
output.close()

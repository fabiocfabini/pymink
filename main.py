from pymink.preprocess.cleaner import Cleaner

cleaner = Cleaner(process="Process 1")

text = cleaner.clean("1- Abcdefg")

print(text)
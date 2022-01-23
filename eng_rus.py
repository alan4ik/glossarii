import csv
import random

dict_eng_rus = {}
dict_eng_rus_tmp = {}
dict_eng_trans_tmp = {}
iter = 0
with open("D:/untitled1/test_fin_2.csv", encoding='utf-8') as f_obj:
    reader = csv.DictReader(f_obj, delimiter=",")
    for line in reader:
        dict_eng_rus[iter] = {line["English"]: line["Russian"]}
        dict_eng_rus_tmp[line["English"]] = line["Russian"]
        dict_eng_trans_tmp[iter] = {line["English"]: line["Trans"]}
        # dict_eng_rus = {iter: {line["English"]: line["Russian"]}}
        iter += 1

len_dict_eng_rus = len(dict_eng_rus)
# print(dict_eng_rus)
# print(dict_eng_rus_tmp)

while True:
    number = random.randrange(0, len_dict_eng_rus)
    print(dict_eng_rus[number].values())
    tmp = input("enter: ")
    print(dict_eng_trans_tmp[number])

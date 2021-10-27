#!/usr/bin/env python
from typing import Iterable, List, Optional, Tuple
from jiwer import wer 


target_list = []
hypothesis_list = []
correct = 0
incorrect = 0


with open("predictions.txt", "r") as source:
    for line in source:
        lines= line.rstrip()
        if lines.startswith("T-"):
            target_str = lines.split("\t")
            target_list.append(target_str[-1]) 
        if lines.startswith("H-"):
            hypothesis_str = lines.split("\t")
            hypothesis_list.append(hypothesis_str[-1])

    for t, h in zip(target_list, hypothesis_list):
        error = wer(t, h) 
        if error == 0.0:    
            correct += 1
        else:
            incorrect += 1
    
   
    my_WER = incorrect / (correct + incorrect)
    print(f"WER:\t{my_WER * 100:.2f}")
    #print(correct)
    #print(incorrect)
    #print(target_list)
    #print(hypothesis_list)
 
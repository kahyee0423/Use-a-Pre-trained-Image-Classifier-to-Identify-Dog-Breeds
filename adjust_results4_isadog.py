#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/adjust_results4_isadog.py
#
# PROGRAMMER: Hor Kah Yee
# DATE CREATED: 22/11/2024                                
# REVISED DATE: 
# PURPOSE: Create a function adjust_results4_isadog that adjusts the results 
#          dictionary to indicate whether or not the pet image label is of-a-dog, 
#          and to indicate whether or not the classifier image label is of-a-dog.
#          All dog labels from both the pet images and the classifier function
#          will be found in the dognames.txt file.

import argparse

def adjust_results4_isadog(results_dic, dogfile):
    # Create a dictionary of dog names from the dogfile
    dognames_dic = {}
    with open(dogfile, "r") as file:
        for line in file:
            dog_name = line.strip().lower()
            if dog_name not in dognames_dic:
                dognames_dic[dog_name] = 1
            else:
                print(f"Warning: Duplicate dog name {dog_name} found in {dogfile}")
                
    for key, value in results_dic.items():
        pet_label_is_dog = 1 if value[0] in dognames_dic else 0
        classifier_label_is_dog = 1 if any(name.strip() in dognames_dic for name in value[1].split(", ")) else 0
        value.extend([pet_label_is_dog, classifier_label_is_dog])

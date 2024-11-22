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
    """
    Adjusts the results dictionary to determine if the pet image label and the
    classifier label are of-a-dog by comparing them to the dog names in the dogfile.
    Parameters:
        results_dic - Dictionary with key as image filename and value as a List:
                      index 0 = pet image label (string)
                      index 1 = classifier label (string)
                      index 2 = 1/0 (int) 1 = match between pet and classifier labels, 0 = no match
        dogfile - A text file containing names of all dogs (one dog name per line).
    Returns:
        None - results_dic is a mutable data type, so changes are made in place.
    """
    # Create a dictionary of dog names from the dogfile
    dognames_dic = {}
    with open(dogfile, "r") as file:
        for line in file:
            dog_name = line.strip().lower()
            if dog_name not in dognames_dic:
                dognames_dic[dog_name] = 1
            else:
                print(f"Warning: Duplicate dog name {dog_name} found in {dogfile}")
    
    # Iterate through results_dic and determine if labels are of-a-dog
    for key, value in results_dic.items():
        pet_label_is_dog = 1 if value[0] in dognames_dic else 0
        classifier_label_is_dog = 1 if any(name.strip() in dognames_dic for name in value[1].split(", ")) else 0
        value.extend([pet_label_is_dog, classifier_label_is_dog])
     

def get_input_args():
    """
    Retrieves and parses the three command line arguments provided by the user 
    when they run the program from a terminal window. This function uses Python's 
    argparse module to create and define these command line arguments. If the user 
    fails to provide some or all of the arguments, then the default values are 
    used for the missing arguments. Command line arguments:
      1. --dir: path to the folder of pet images (default: 'pet_images/')
      2. --arch: CNN model architecture to use (default: 'vgg')
      3. --dogfile: text file with dognames (default: 'dognames.txt')
    Returns:
      parse_args() - data structure that stores the command line arguments object
    """
    # Create Argument Parser object
    parser = argparse.ArgumentParser()

    # Add arguments with default values and help descriptions
    parser.add_argument('--dir', type=str, default='pet_images/',
                        help='Path to the folder of pet images')
    parser.add_argument('--arch', type=str, default='vgg',
                        help='CNN model architecture to use (e.g., resnet, alexnet, vgg)')
    parser.add_argument('--dogfile', type=str, default='dognames.txt',
                        help='Text file with dognames')

    # Return parsed arguments
    return parser.parse_args()

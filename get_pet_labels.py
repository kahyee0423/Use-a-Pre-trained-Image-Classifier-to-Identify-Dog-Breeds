#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: Hor Kah Yee
# DATE CREATED: 22/11/2024                          
# REVISED DATE: 
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir

def get_pet_labels(image_dir):
    filename_list = listdir(image_dir)
    
    # Initialize the dictionary
    results_dic = {}
    
    # Process filenames to create pet labels
    for filename in filename_list:
        if filename[0] != ".":  # Ignore hidden files
            # Convert to lowercase and split by "_"
            words = filename.lower().split("_")
            # Filter out non-alphabetic parts and create label
            pet_label = " ".join([word for word in words if word.isalpha()]).strip()
            
            # Add to dictionary if not already present
            if filename not in results_dic:
                results_dic[filename] = [pet_label]
            else:
                print(f"** Warning: Duplicate file found: {filename}")
    return results_dic

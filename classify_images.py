#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/classify_images.py
#                                                                             
# PROGRAMMER: Hor Kah Yee
# DATE CREATED:  22/11/2024                               
# REVISED DATE: 
# PURPOSE: Create a function classify_images that uses the classifier function 
#          to create the classifier labels and then compares the classifier 
#          labels to the pet image labels. This function inputs:
#            -The Image Folder as image_dir within classify_images and function 
#             and as in_arg.dir for function call within main. 
#            -The results dictionary as results_dic within classify_images 
#             function and results for the functin call within main.
#            -The CNN model architecture as model wihtin classify_images function
#             and in_arg.arch for the function call within main. 
#           This function uses the extend function to add items to the list 
#           that's the 'value' of the results dictionary.
# Imports classifier function for using CNN to classify images 
from classifier import classifier 

def classify_images(images_dir, results_dic, model):
    for filename in results_dic:
        # Build full file path for the image
        image_path = f"{images_dir}/{filename}"
        
        # Get the classifier label
        classifier_label = classifier(image_path, model)
        
        # Format classifier label: lowercase and strip whitespace
        classifier_label = classifier_label.lower().strip()
        
        # Compare pet label (results_dic[filename][0]) with classifier label
        pet_label = results_dic[filename][0]
        match = 1 if pet_label in classifier_label else 0
        
        # Append classifier label and match result to the results dictionary
        results_dic[filename].extend([classifier_label, match])

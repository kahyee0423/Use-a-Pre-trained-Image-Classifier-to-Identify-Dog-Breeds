#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/print_results.py
#                                                                             
# PROGRAMMER: Hor Kah Yee
# DATE CREATED: 22/11/2024
# REVISED DATE: 
# PURPOSE: Create a function print_results that prints the results statistics
#          from the results statistics dictionary (results_stats_dic). It 
#          should also allow the user to be able to print out cases of misclassified
#          dogs and cases of misclassified breeds of dog using the Results 
#          dictionary (results_dic).  
#         This function inputs:
#            -The results dictionary as results_dic within print_results 
#             function and results for the function call within main.
#            -The results statistics dictionary as results_stats_dic within 
#             print_results function and results_stats for the function call within main.
#            -The CNN model architecture as model wihtin print_results function
#             and in_arg.arch for the function call within main. 
#            -Prints Incorrectly Classified Dogs as print_incorrect_dogs within
#             print_results function and set as either boolean value True or 
#             False in the function call within main (defaults to False)
#            -Prints Incorrectly Classified Breeds as print_incorrect_breed within
#             print_results function and set as either boolean value True or 
#             False in the function call within main (defaults to False)
#         This function does not output anything other than printing a summary
#         of the final results.
# 
def print_results(results_dic, results_stats_dic, model, 
                  print_incorrect_dogs = False, print_incorrect_breed = False):
                    
    # Print summary header
    print(f"\n*** Results Summary for CNN Model Architecture: {model.upper()} ***\n")
    print(f"Number of Images: {results_stats_dic['n_images']}")
    print(f"Number of Dog Images: {results_stats_dic['n_dogs_img']}")
    print(f"Number of 'Not-a' Dog Images: {results_stats_dic['n_notdogs_img']}\n")

    # Print percentages from results_stats_dic
    print("Percentages Summary:")
    for key, value in results_stats_dic.items():
        if key.startswith('pct_'):
            print(f"{key.replace('pct_', '% '):<25}: {value:.2f}%")

    # Print misclassified dogs if requested
    if print_incorrect_dogs:
        # Check if misclassifications occurred
        if (results_stats_dic['n_correct_dogs'] + results_stats_dic['n_correct_notdogs']
                != results_stats_dic['n_images']):
            print("\nIncorrectly Classified Dogs:")
            for key, value in results_dic.items():
                # Sum of dog labels is 1 => one is dog, one is not
                if sum(value[3:]) == 1:
                    print(f"Image: {key} | Pet Label: {value[0]} | Classifier Label: {value[1]}")
        else:
            print("\nNo incorrectly classified dogs.")

    # Print misclassified breeds if requested
    if print_incorrect_breed:
        # Check if breed misclassifications occurred
        if results_stats_dic['n_correct_dogs'] != results_stats_dic['n_correct_breed']:
            print("\nIncorrectly Classified Dog Breeds:")
            for key, value in results_dic.items():
                # Both are dogs, but labels don't match
                if sum(value[3:]) == 2 and value[2] == 0:
                    print(f"Image: {key} | Pet Label: {value[0]} | Classifier Label: {value[1]}")
        else:
            print("\nNo incorrectly classified dog breeds.")
                

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/calculates_results_stats.py
#                                                                             
# PROGRAMMER: Paul Onaolapo
# DATE CREATED: 2026-08-28                           
# REVISED DATE: 
# PURPOSE: Create a function calculates_results_stats that calculates the 
#          statistics of the results of the programrun using the classifier's model 
#          architecture to classify the images. This function will use the 
#          results in the results dictionary to calculate these statistics. 
#          This function will then put the results statistics in a dictionary
#          (results_stats_dic) that's created and returned by this function.
#          This will allow the user of the program to determine the 'best' 
#          model for classifying the images. The statistics that are calculated
#          will be counts and percentages. Please see "Instruction Summary" 
#          for details on how to calculate the counts and percentages.
#         This function inputs:
#            -The results dictionary as results_dic within calculates_results_stats 
#             function and defined for the function call within main.
#         This function creates and returns the Results Statistics Dictionary -
#          results_stats_dic. This dictionary contains the results statistics 
#          (either a percentage or a count) where the key is the statistic's 
#           name (starting with 'pct' for percentage or 'n' for count) and value 
#          is the statistic's value.  This dictionary should contain the 
#          following keys:
#            n_images - number of images
#            n_dogs_img - number of dog images
#            n_notdogs_img - number of NON-dog images
#            n_match - number of matches between pet & classifier labels
#            n_correct_dogs - number of correctly classified dog images
#            n_correct_notdogs - number of correctly classified NON-dog images
#            n_correct_breed - number of correctly classified dog breeds
#            pct_match - percentage of correct matches
#            pct_correct_dogs - percentage of correctly classified dogs
#            pct_correct_breed - percentage of correctly classified dog breeds
#            pct_correct_notdogs - percentage of correctly classified NON-dogs
#
##
# TODO 5: Define calculates_results_stats function below, please be certain to replace None
#       in the return statement with the results_stats_dic dictionary that you create 
#       with this function

def calculates_results_stats(results_dic):
    """
    Calculates statistics of the results of the program run using classifier's model 
    architecture to classifying pet images. Then puts the results statistics in a 
    dictionary (results_stats_dic) so that it's returned for printing aims.
    Parameters:
      results_dic - Dictionary that contains DB of images where:
         key = pet image filename (string)
         value = list where:
           index 0 = pet image label (string)
           index 1 = classifier label (string)
           index 2 = 1/0 where 1 = match between pet image and classifier labels 
                     and 0 = no match
           index 3 = 1/0 where 1 = pet image 'is-a' dog and 0 = pet Image 'is-NOT-a' dog. 
           index 4 = 1/0 where 1 = Classifier classify image 'as-a' dog and 0 = Classifier
                     classify image 'as-NOT-a' dog.
    Returns:
     results_stats_dic - Dictionary that contains the results statistics (count
                         and percentage) where:
                         key = statistic's name (e.g. n_images, pct_correct_dogs,
                                                 pct_correct_breed, pct_correct_none)
                         value = statistic's value (uint or float)
    """
    results_stats_dic = dict()
    
    # Sets all counters to zero
    results_stats_dic['n_images'] = len(results_dic)
    results_stats_dic['n_dogs_img'] = 0
    results_stats_dic['n_notdogs_img'] = 0
    results_stats_dic['n_match'] = 0
    results_stats_dic['n_correct_dogs'] = 0
    results_stats_dic['n_correct_notdogs'] = 0
    results_stats_dic['n_correct_breed'] = 0

    # Iterates through the results dictionary
    for key in results_dic:
        
        # Labels Match Exactly
        if results_dic[key][2] == 1:
            results_stats_dic['n_match'] += 1

        # Pet Image Label is a Dog
        if results_dic[key][3] == 1:
            results_stats_dic['n_dogs_img'] += 1
            
            # Classifier label is also a Dog
            if results_dic[key][4] == 1:
                results_stats_dic['n_correct_dogs'] += 1
                
            # Pet Image Label and Classifier Label Match (Correct Breed)
            if results_dic[key][2] == 1:
                results_stats_dic['n_correct_breed'] += 1
                
        # Pet Image Label is NOT a Dog
        else:
            results_stats_dic['n_notdogs_img'] += 1
            
            # Classifier label is also NOT a Dog
            if results_dic[key][4] == 0:
                results_stats_dic['n_correct_notdogs'] += 1

    # Calculates % Correct Label Matches
    results_stats_dic['pct_match'] = (results_stats_dic['n_match'] / results_stats_dic['n_images']) * 100.0

    # Calculates % Correct Dogs
    if results_stats_dic['n_dogs_img'] > 0:
        results_stats_dic['pct_correct_dogs'] = (results_stats_dic['n_correct_dogs'] / results_stats_dic['n_dogs_img']) * 100.0
        # Calculates % Correct Breed of Dog
        results_stats_dic['pct_correct_breed'] = (results_stats_dic['n_correct_breed'] / results_stats_dic['n_dogs_img']) * 100.0
    else:
        results_stats_dic['pct_correct_dogs'] = 0.0
        results_stats_dic['pct_correct_breed'] = 0.0

    # Calculates % Correct Not-Dog Images
    if results_stats_dic['n_notdogs_img'] > 0:
        results_stats_dic['pct_correct_notdogs'] = (results_stats_dic['n_correct_notdogs'] / results_stats_dic['n_notdogs_img']) * 100.0
    else:
        results_stats_dic['pct_correct_notdogs'] = 0.0

    return results_stats_dic
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: Paul Onaolapo
# DATE CREATED: 2026-08-28                           
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
# Import python modules
from os import listdir

# TODO 2: Define get_pet_labels function below please be certain to replace None
#          in the return statement with results_dic dictionary that you create
#          with this function
#
def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Parameters:
     image_dir - The (full or relative) path to the folder that contains the
                 images to be classified that are being ingested (string)
    Returns:
      results_dic - Dictionary that contains DB of images where:
         key = pet image filename (string)
         value = length 1 list where index 0 = pet image label (string)
    """
    # Retrieve the filenames from folder specified with image_dir
    in_files = listdir(image_dir)
    
    # Creates empty dictionary named results_dic
    results_dic = dict()
    
    # Processes through each file in the folder, extracting only words
    # to create the pet label
    for idx in range(0, len(in_files), 1):
        
        # Skips file if starts with . (like .DS_Store of Hidden files)
        if in_files[idx][0] != ".":
            
            # Converts filename to lower case and splits by _ to get words
            pet_image = in_files[idx].lower()
            word_list_pet_image = pet_image.split("_")
            
            # Creates temporary label variable
            pet_label = ""
            
            # Processes each word in word_list_pet_image to extract label
            for word in word_list_pet_image:
                if word.isalpha():
                    pet_label += word + " "
                    
            # Strips off leading/trailing whitespace
            pet_label = pet_label.strip()
            
            # Adds filename and pet_label to results_dic if not already present
            if in_files[idx] not in results_dic:
                results_dic[in_files[idx]] = [pet_label]
            else:
                print("** Warning: Duplicate files exist in directory:", in_files[idx])
                
    # Returns dictionary of pet labels
    return results_dic
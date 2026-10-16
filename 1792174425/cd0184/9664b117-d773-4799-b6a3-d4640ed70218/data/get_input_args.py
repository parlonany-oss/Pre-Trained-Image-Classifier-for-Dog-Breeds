#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_input_args.py
#                                                                             
# PROGRAMMER: Paul Onaolapo
# DATE CREATED: 2026-08-28                           
# REVISED DATE: 
# PURPOSE: Create a function that retrieves 3 command line arguments inputs from
#          the user using the Argparse Python module. If the user fails to provide
#          some or all 3 arguments, then the default values are used for the missing
#          arguments. Command Line Arguments:
#     1. Image Folder as --dir with default value 'pet_images/'
#     2. CNN Model Architecture as --arch with default value 'vgg'
#     3. Text File with Dog Names as --dogfile with default value 'dognames.txt'
#
import argparse

def get_input_args():
    """
    Retrieves and parses the 3 command line arguments provided by the user when
    they run the program from a terminal window. This function uses Python's 
    argparse module to create and define these 3 command line arguments. If the 
    user fails to provide some or all 3 arguments, then the default values are
    used for the missing arguments.
    Command Line Arguments:
      1. Image Folder as --dir with default value 'pet_images/'
      2. CNN Model Architecture as --arch with default value 'vgg'
      3. Text File with Dog Names as --dogfile with default value 'dognames.txt'
    Parameters:
     None -  using argparse module to store command line arguments object
    Returns:
     parse_args() -data structure that stores the command line arguments object  
    """
    # Create Parse using ArgumentParser
    parser = argparse.ArgumentParser()
    
    # Create 3 command line arguments using add_argument() from Argparse
    parser.add_argument('--dir', type=str, default='pet_images/', 
                        help='path to the folder of pet images')
    parser.add_argument('--arch', type=str, default='vgg', 
                        help='chosen model architecture: resnet, alexnet, or vgg')
    parser.add_argument('--dogfile', type=str, default='dognames.txt', 
                        help='text file that has dog names')
    
    # Replace None with parser.parse_args() parsed argument collection that 
    # you created with this function 
    return parser.parse_args()
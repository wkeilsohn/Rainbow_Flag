#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 11 19:43:30 2021

@author: william
"""

# Import Packages:
import numpy as np 
import PIL as pw
import random

'''
An image is just an array of values, thus we could hypothetically construct one with Numpy.
PIL allows for RGB images, which is a 3x array.
'''

#  Write Classes:

class Color:
    
    red_ls = [255, 0, 0]
    orange_ls = [255, 101, 0]
    yellow_ls = [241, 255, 0]
    green_ls = [19, 255, 0]
    blue_ls = [0, 7, 255]
#    indigo_ls = [90, 0, 255]
    purple_ls = [155, 0, 255]
    
    rainbow_ls = [red_ls, orange_ls, yellow_ls, green_ls, blue_ls, purple_ls]
    
    def rand_color(self): # Create a list of RGB values
        rgb_vals = []
        for i in range(0, 3):
            rgb_vals.append(random.randint(0, 255))
        return rgb_vals

    def simple_color_array(self, rgb_ls, height): # Duplicate a list of RGB values into a Numpy array
        color_array = np.array(rgb_ls)
        for i in range(0, height - 1):
            color_array = np.concatenate((color_array, np.array(rgb_ls)), axis = 0)
        return color_array.reshape((height, len(rgb_ls)))
    
class Image:
    
    def array_to_image(self, array): # turn a numpy array into an image
        return pw.Image.fromarray(np.uint8(array)).convert('RGB')

    def ls_to_image(self, ls, width, height): # Turn a list of RGB values into a image
        return pw.Image.new(mode = 'RGB', size = (width, height), color = tuple(ls))

    def change_image_size(self, image, width, height): # Change the size of an image
        return image.resize((width, height))
    
    def image_combine(self, image_ls, layer_width, layer_height, image_height = 0): # Combine multiple images
        new_img = pw.Image.new('RGB', (layer_width, image_height))
        for i in range(0, len(image_ls)):
            temp_img = image_ls[i]
            new_img.paste(temp_img, (0, (i * layer_height)))
            del temp_img
        return new_img

### The following functions are redefined for flags in the child class:     
    def multi_color_image_maker(self, image_ls, layer_width, layer_height):
        image_height = layer_height * len(image_ls)
        cols_array = np.array(image_ls)
        cols_img_ls = [pw.Image.new(mode = 'RGB', size = (layer_width, layer_height), color = tuple(i)) for i in cols_array]
        return self.image_combine(cols_img_ls, layer_width, layer_height, image_height)

    def random_image_generator(self, number_of_colors = 100, layer_width = 100, layer_height = 10): # Make a random image
        image_height = layer_height * number_of_colors
        cols_array = (np.random.rand(number_of_colors, 3) * 255).astype(int)
        cols_img_ls = [pw.Image.new(mode = 'RGB', size = (layer_width, layer_height), color = tuple(i)) for i in cols_array]
        return self.image_combine(cols_img_ls, layer_width, layer_height, image_height)
    
class Flag(Image):
    
    ratio = (1 + 5 ** 0.5) / 2 # Golden Ratio
    
    def find_flag_height(self, layer_width): # Determine the height of the flag
        return int(layer_width / self.ratio)
        
    def find_layer_height(self, layer_width, color_ls): # Find the height of one layer
        return int(self.find_flag_height(layer_width) / len(color_ls))
    
    def multi_color_flag_maker(self, image_ls, layer_width = 100): # Create a flag out of multiple colors
        cols_img_ls = [pw.Image.new(mode = 'RGB', size = (layer_width, self.find_layer_height(layer_width, image_ls)), color = tuple(i)) for i in np.array(image_ls)]
        return self.image_combine(cols_img_ls, layer_width, self.find_layer_height(layer_width, image_ls), self.find_flag_height(layer_width))
    
    
    
    
        



# Author: Ankush Gupta
# Date: 2015

"""
Visualize the generated localization synthetic
data stored in h5 data-bases
"""
from __future__ import division
import os
import os.path as osp
import numpy as np
import matplotlib.pyplot as plt 
import h5py 
from PIL import Image
import operator
from common import *

def break_up_sentence(sentencesList):
  wordsList = []
  for sentence in sentencesList:
    # split by white space
    wordsList.append(sentence.split())
  return sum(wordsList, [])

def get_positions(texts, wordBB):
  text_pos_dicts = []
  for i in range(len(texts)):
    text_pos_dicts.append({
      'text': texts[i],
      'top_left': { 'x': wordBB[0][0][i], 'y': wordBB[1][0][i] },
      'top_right': { 'x': wordBB[0][1][i], 'y': wordBB[1][1][i] },
      'bottom_right': { 'x': wordBB[0][2][i], 'y': wordBB[1][2][i] },
      'bottom_left': { 'x': wordBB[0][3][i], 'y': wordBB[1][3][i] }
    })
  return text_pos_dicts

def main(db_fname, out_dir):
    images_dir = "images/"
    position_dir = "positions/"
    db = h5py.File(db_fname, 'r')
    dsets = sorted(db['data'].keys())
    for k in dsets:
        # get useful infomation
        rgb = db['data'][k][...]
        # charBB = db['data'][k].attrs['charBB']
        wordBB = db['data'][k].attrs['wordBB']
        txt = db['data'][k].attrs['txt']
        # save the images to a folder
        image = Image.fromarray(rgb)
        image.save(out_dir + images_dir + k + ".jpg")
        # flatten the txt and get it positions
        flatten_txt = break_up_sentence(txt)
        text_pos_dicts = get_positions(flatten_txt, wordBB)

        with open(out_dir + position_dir + k + ".txt", 'w') as oFile:
          for text in text_pos_dicts:
            print(
              str(text["top_left"]["x"]) + ", " +
              str(text["top_left"]["y"]) + ", " +
              str(text["top_right"]["x"]) + ", " +
              str(text["top_right"]["y"]) + ", " +
              str(text["bottom_right"]["x"]) + ", " +
              str(text["bottom_right"]["y"]) + ", " +
              str(text["bottom_left"]["x"]) + ", " +
              str(text["bottom_left"]["y"]) + ", " +
              str(text["text"])
            , file=oFile)


    db.close()

if __name__=='__main__':
    main('results/SynthText.h5', "sync_images/")


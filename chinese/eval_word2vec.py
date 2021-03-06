#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Tenghu Wu
# Date: 2017-Jan-15

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from gensim.models import word2vec
from wikipedia import search, page

import logging
import numpy as np
import os
import tensorflow as tf
import time

# set the global parameters here:
timestamp = str(int(time.time()))
flags = tf.app.flags
flags.DEFINE_string('data_path', './data/ciities_corpus', 'path for training data')
flags.DEFINE_string('save_path', 'runs/1484496451/checkpoints', 'path for saving data')
flags.DEFINE_integer('min_count', 2, 'term occurs less than this is ignored')
flags.DEFINE_integer('size', 50, 'embedding dimensions')
flags.DEFINE_integer('window', 4, 'terms occur within a window-neighborhood of a term')
flags.DEFINE_integer('sg', 1, 'sg=1:skip-gram model; sg=other:CBoW model')
# flags.DEFINE_float()
# flags.DEFINE_boolean()
FLAGS = flags.FLAGS

# the major part
if __name__ == '__main__':
    # load-in trained model
    file_path = os.path.join(FLAGS.save_path,'text.model.bin')
    model = word2vec.Word2Vec.load_word2vec_format(file_path, binary=True)

    # test example 1:
    print('The term most similar to %s is:' %u'刘嘉琪')
    for item in model.most_similar(u'刘嘉琪'):
        print(item[0],item[1])

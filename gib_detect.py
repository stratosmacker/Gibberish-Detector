#!/usr/bin/python2.7

import pickle
import gib_detect_train

model_data = pickle.load(open('gib_model.pki'))

while True:
    l = raw_input()
    model_mat = model_data['mat']
    threshold = model_data['thresh']
    print gib_detect_train.avg_transition_prob(l, model_mat) > threshold

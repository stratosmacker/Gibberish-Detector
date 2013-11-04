#!/usr/bin/python2.7

import pickle
import gib_detect_train


model_data = pickle.load(open('gib_model.pki'))

def detect(l=''):
    model_mat = model_data['mat']
    threshold = model_data['thresh']
    return gib_detect_train.avg_transition_prob(l, model_mat) > threshold # True is good, False is Gibberish

def cmdline_detect():
    while True:
        d = detect(raw_input())
        print d

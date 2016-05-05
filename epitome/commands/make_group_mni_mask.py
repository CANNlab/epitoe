#!/usr/bin/env python

import epitome as epi
import copy
def run(input_name):
    output = copy.copy(input_name)
    print('Makes an MNI-space group mask')
    line = '. ${DIR_PIPE}/modules/pre/make_group_mni_mask'
    return line, output


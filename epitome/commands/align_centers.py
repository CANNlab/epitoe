#!/usr/bin/env python

import epitome as epi

def run(input_name):
    output = 'ac'
    print('Aligns center-of-mass between EPI and T1 images.')
    line = '. ${{DIR_PIPE}}/modules/pre/align_centers {}'.format(input_name)
    return line, output


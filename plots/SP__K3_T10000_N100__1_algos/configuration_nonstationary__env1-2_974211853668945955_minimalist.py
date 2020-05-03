# -*- coding: utf-8 -*-
"""Minimalist file to reproduce experiments with hash = env1-2_974211853668945955."""
from __future__ import division, print_function  # Python 2 compatibility
__author__ = "Lilian Besson"
try:
    from Arms import *
    from Policies import *
    from Policies.kullback import *
    from PoliciesMultiPlayers import *
    from Arms.Bernoulli import Bernoulli
    from Policies.UCB import UCB
except ImportError:
    from SMPyBandits.Arms import *
    from SMPyBandits.Policies import *
    from SMPyBandits.Policies.kullback import *
    from SMPyBandits.PoliciesMultiPlayers import *
    from SMPyBandits.Arms.Bernoulli import Bernoulli
    from SMPyBandits.Policies.UCB import UCB

configuration = {'append_labels': {},
 'change_labels': {},
 'environment': [{'arm_type': Bernoulli,
                  'params': {'changePoints': [0, 1000, 3000, 5000, 7000],
                             'listOfMeans': [[0.3, 0.4, 0.5],
                                             [0.9, 0.4, 0.5],
                                             [0.3, 0.4, 0.5],
                                             [0.9, 0.4, 0.5],
                                             [0.3, 0.4, 0.5]]}},
                 {'arm_type': Bernoulli,
                  'params': {'changePoints': [0, 2000, 4000, 6000, 8000],
                             'listOfMeans': [[0.4, 0.5, 0.9],
                                             [0.5, 0.4, 0.7],
                                             [0.6, 0.3, 0.5],
                                             [0.7, 0.2, 0.3],
                                             [0.8, 0.1, 0.1]]}}],
 'horizon': 10000,
 'n_jobs': 8,
 'nb_break_points': 4,
 'plot_lowerbound': False,
 'policies': [{'archtype': UCB, 'params': {}}],
 'repetitions': 100,
 'showplot': False,
 'verbosity': 6}

# use it with:
# $ python main.py plots/SP__K3_T10000_N100__1_algos/configuration_nonstationary__env1-2_974211853668945955_minimalist.py

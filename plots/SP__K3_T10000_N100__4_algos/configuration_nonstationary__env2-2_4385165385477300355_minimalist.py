# -*- coding: utf-8 -*-
"""Minimalist file to reproduce experiments with hash = env2-2_4385165385477300355."""
from __future__ import division, print_function  # Python 2 compatibility
__author__ = "Lilian Besson"
try:
    from Arms import *
    from Policies import *
    from Policies.kullback import *
    from PoliciesMultiPlayers import *
    from Arms.Bernoulli import Bernoulli
    from Policies.DiscountedUCB import DiscountedUCB
    from Policies.Exp3S import Exp3S
    from Policies.SlidingWindowUCB import SWUCB
    from Policies.UCB import UCB
except ImportError:
    from SMPyBandits.Arms import *
    from SMPyBandits.Policies import *
    from SMPyBandits.Policies.kullback import *
    from SMPyBandits.PoliciesMultiPlayers import *
    from SMPyBandits.Arms.Bernoulli import Bernoulli
    from SMPyBandits.Policies.DiscountedUCB import DiscountedUCB
    from SMPyBandits.Policies.Exp3S import Exp3S
    from SMPyBandits.Policies.SlidingWindowUCB import SWUCB
    from SMPyBandits.Policies.UCB import UCB

configuration = {'append_labels': {},
 'change_labels': {},
 'environment': [{'arm_type': Bernoulli,
                  'params': {'changePoints': [0, 3000, 5000],
                             'listOfMeans': [[0.3, 0.4, 0.5],
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
 'policies': [{'archtype': UCB, 'params': {}},
              {'archtype': SWUCB,
               'params': {}},
              {'archtype': Exp3S,
               'params': {'horizon': 10000, 'max_nb_random_events': 4}},
              {'archtype': DiscountedUCB,
               'params': {'gamma': 0.99}}],
 'repetitions': 100,
 'showplot': False,
 'verbosity': 6}

# use it with:
# $ python main.py plots/SP__K3_T10000_N100__4_algos/configuration_nonstationary__env2-2_4385165385477300355_minimalist.py

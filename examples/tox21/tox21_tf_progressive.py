"""
Script that trains progressive multitask models on Tox21 dataset.
"""
from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals

import tensorflow as tf
tf.random.set_seed(124)

import os
import shutil
import numpy as np
import deepchem as dc
from deepchem.molnet import load_tox21

# Only for debug!
np.random.seed(123)

# Load Tox21 dataset
n_features = 1024
tox21_tasks, tox21_datasets, transformers = load_tox21()
train_dataset, valid_dataset, test_dataset = tox21_datasets

# Fit models
metric = dc.metrics.Metric(dc.metrics.roc_auc_score, np.mean)

model = dc.models.ProgressiveMultitaskClassifier(
    len(tox21_tasks),
    n_features,
    layer_sizes=[1000],
    dropouts=[.25],
    learning_rate=0.001,
    batch_size=50,
    use_openvino=True)

# Fit trained model
# model.fit(train_dataset, nb_epoch=10)

print("Evaluating model")
# train_scores = model.evaluate(train_dataset, [metric], transformers)
import time
for i in range(3):
    start = time.time()
    valid_scores = model.evaluate(valid_dataset, [metric], transformers)
    print(time.time() - start, valid_scores)

# print("Train scores")
# print(train_scores)

# print("Validation scores")
# {'mean-roc_auc_score': 0.5315314298546935}

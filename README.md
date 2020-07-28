# LFM1b-analyses

This repository provides Python scripts for processing and analyzing the LFM-1b dataset: http://www.cp.jku.at/datasets/LFM-1b/

## LFM_fairness.ipynb
This i-python notebook reproduces the "Unfairness in recommender systems" analyzes of https://arxiv.org/pdf/1907.13286v1.pdf in the context of music recommender systems using a subset of the LFM-1b dataset. This reproducibility work was accepted at ECIR'2020 and is available via https://arxiv.org/pdf/1912.04696.pdf.

For executing it, simply download the dataset from https://zenodo.org/record/3475975#.XZ7i1mbgpPY and copy the files into the "data" folder. All other instructions are given in the notebook itself.

### Requirements
* Python 3
* Jupyter
* Pandas
* Matplotlib
* Surprise
* Numpy
* Scipy
* Sklearn

All these packages can be easily installed using https://www.anaconda.com/

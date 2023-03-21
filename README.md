# FairRecSys

This repository provides Python scripts for studying fairness and popularity bias in (multimedia) recommender systems.

## LFM_fairness.ipynb
This i-python notebook analyzes popularity bias and fairness in the context of music recommender systems using a subset of the LFM-1b dataset. This work was accepted at ECIR'2020 and is available via https://arxiv.org/pdf/1912.04696.pdf.

For executing the script, simply download the dataset from https://zenodo.org/record/3475975#.XZ7i1mbgpPY and copy the files into the "data" folder. All other instructions are given in the notebook itself.

## MMRS_fairness.ipynb
This i-python notebook enables to evalute the fairness in multimedia recommender systems (MMRS). This work was accepted at ECIR'2022 and is available via https://arxiv.org/pdf/2203.00376.pdf.

Datasets are available at: https://zenodo.org/record/6123879#.Yg-FRpYxmUk 
For executing the script, please copy the files into the "data" folder and follow the instructions in the notebook itself.

## RecSys_inconsistency.ipynb
This I-python notebook enables to analyze inconsistency in recommender systems by evaluating accuracy, miscalibration and popularity lift. This work was accepted at ECIR'2023 and is available via https://arxiv.org/pdf/2303.00400.pdf.

For executing it, please download the datasets from https://doi.org/10.5281/zenodo.7428435 and copy the "lfm", "ml" and "anime" folders directly in the root folder of the notebook.

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

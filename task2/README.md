# Task 2

## Problem statement

Implementation of neural network from scratch

You are allowed to use any language to accomplish the same if you don't prefer Python, but don't use any library that literally accomplishes the said task. (e.g. TensorFlow or Pytorch). You are allowed to use any dataset of your choice. Make sure you understand the theory.

## Contents

1. **[model.py](https://github.com/majimearun/crux-round3-tasks/blob/main/task2/model.py)**: module with all required classes and methods to build and train the binary classifier

2. **[utils.py](https://github.com/majimearun/crux-round3-tasks/blob/main/task2/utils.py)**: module with the utility functions, namely the cost function (binary cross entropy) and parameters (bias and weight matrices) initialization

3. **[trial.ipynb](https://github.com/majimearun/crux-round3-tasks/blob/main/task2/trial.ipynb)**: jupyter notebook with a trial/test run of the custom neural network on a real life dataset (bank fraud detection)

4. **[fraud_detection_bank_dataset.csv](https://github.com/majimearun/crux-round3-tasks/blob/main/task2/data/fraud_detection_bank_dataset.csv)**

## Run options

1. **Local: (Reccomended)**

**a. Jupyter Server:**

- Follow intructions in main [README.md](https://github.com/majimearun/crux-round3-tasks/blob/main/README.md) file to install the virtual environment

```
venv\Scripts\activate
jupyter notebook
```

- Choose *trial.ipynb* in the task2 folder and run it.


**b. Editor (VSCode)**

- Open the cloned/downloaded repo in VSCode as a folder

- Choose the *venv python 3.10.2* kernel before running the *trial.ipynb*

**NOTE:** some extensions might need to be installed (vscode will prompt you to install them) 

2. **Cloud:**

**a. Google Colab**

- Open the following colab file
- From this repository download and add [model.py]() and [utils.py]() to the notebooks runtime as utility scripts
- Run the notebook

[![Open In Collab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1Uup3MoAT_38IomV6SgktCUT0YsbRHCRi?usp=sharing)

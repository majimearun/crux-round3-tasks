# Task 1

## Problem statement
Time Series forecasting using ARIMA

You're allowed to use standard libraries or frameworks, but are expected to know the theory behind the computation. Use the [same dataset](https://github.com/majimearun/covid-analysis/blob/main/data/country_confirmed.csv) as you did in the first round.

## Contents

1. **[arima.ipynb](https://github.com/majimearun/crux-round3-tasks/blob/main/task1/arima.ipynb)**: notebook with the my study and implementation of the ARIMA model (with the theory I understood/in my own words on how the model is identified, built and works) on the COVID dataset

2. **[extra/arima.pdf](https://github.com/majimearun/crux-round3-tasks/blob/main/task1/extra/arima.pdf)**: notebook exported to pdf for easy access in case one just needs to read the notebook's code and output without the need to run it

3. **[data/country_confirmed.csv](https://github.com/majimearun/crux-round3-tasks/blob/main/task1/data/country_confirmed.csv)**: daily updated (at UTC 0000) time series of total confirmed cases of COVID in each country 

## Run options

1. **Local: (Reccomended)**

**a. Jupyter Server:**

- Follow intructions in main [README.md](https://github.com/majimearun/crux-round3-tasks/blob/main/README.md) file to install the virtual environment

```
venv\Scripts\activate
jupyter notebook
```

- Choose *arima.ipynb* in the task1 folder and run it.


**b. Editor (VSCode)**

- Open the cloned/downloaded repo in VSCode as a folder

- Choose the *venv python 3.10.2* kernel before running the *arima.ipynb*

**NOTE:** some extensions might need to be installed (vscode will prompt you to install them) 

2. **Cloud:**

**a. Google Colab**

[![Open In Collab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1-OjCT2N8rI3jE4DfZi1hI-PSTJD6OVnt?usp=sharing)

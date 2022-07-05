# Quest

How to create new environments in python using NU Quest

## Create new virtual env
**python3 flag will automatically install 3.10.4**

```conda create --name covid-dtm python=3```

## Activate new environment
```conda activate covid-dtm```

## Install packages
```pip install <package-name>```

## Add virtual env to jupyter
```pip install --user ipykernel```

## Add kernal to jupyter
```python -m ipykernel install --user --name=covid-dtm```


### pip install 
```
pip install twarc==2.11.0
pip install tweepy==4.10.0
pip install Argparse
pip install Xtract==0.1a3
pip install wget==3.2
```
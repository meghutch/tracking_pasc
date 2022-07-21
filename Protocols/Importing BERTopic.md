# Steps to load BERTopic into Quest Env

I was having issues loading `BERTopic` and specifically, the supplemental package, `Flair` in Python10

The following steps were performed on Quest to load both libraries into a new virtual env

##

1. `conda create --name bert-topic python=3.8.8`

2. `pip install bertopic`

3. `pip install flair`

4. `pip install pandas`

5. `pip install --user ipykernel`

6. `python -m ipykernel install --user --name=bert-topic`



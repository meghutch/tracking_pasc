# Steps to load BERTopic into Quest Env

I was having issues loading `BERTopic` and specifically, the supplemental package, `Flair` in Python10

The following steps were performed on Quest to load both libraries into a new virtual env

##

1. `conda create --name bert python=3.8`

2. `conda activate bert-topic`

3. `pip install bertopic`

4. `pip install flair`

5. `pip install pandas`

6. `pip install --user ipykernel`

7. `python -m ipykernel install --user --name=bert`



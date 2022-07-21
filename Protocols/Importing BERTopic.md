# Steps to load BERTopic into Quest Env

I was having issues loading `BERTopic` and specifically, the supplemental package, `Flair` in Python10

The following steps were performed on Quest to load both libraries into a new virtual env

##

1. module load python/anaconda3.6

2. `conda create --name bert-topic python=3.9`

3. `pip install bertopic`

4. `pip install flair`

5. `pip install pandas`

6. `pip install --user ipykernel`

7. `python -m ipykernel install --user --name=bert`



# Creating Quest env to fit BERTopic Model with GPU

A tailored virtual environment was needed to fit the BERTopic model using GPUs on Quest. 
This protocol details the instructions to create the environment. 
However, since the environment was made on the project allocation folder, these steps should not need to be repeated by each user.

## Create a [shared virtual environment](https://kb.northwestern.edu/page.php?id=78623) in the project alloctation folder

`cd /projects/p31499`

`mkdir pythonenvs`

## Create a virtual environment to run [pytorch with GPU/CUDA on Quest](https://kb.northwestern.edu/gpus-on-quest)

### purge any active modules

`module purge all`

### make the virtual environment 

`conda create --prefix /projects/p31499/pythonenvs/pytorch-1.11-py38 python=3.8`

### activate environment

`conda activate /projects/p31499/pythonenvs/pytorch-1.11-py38`

### install bertopic and flair

These packakes overide the pytorch/cuda modules, thus, we want to load those last so that we'll have the correct versions

`pip install bertopic`

`pip install flair`

### install pytorch/cuda with conda-forge

`conda install -c conda-forge pytorch=1.11[build=cuda112*] #cudatoolkit=11.2 --yes`

### install numpy

`pip install numpy==1.22`

### check pytorch version

`python`

`import torch`

`torch.__version__`

`print(torch.version.cuda)`

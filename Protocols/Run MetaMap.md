# Run MetaMap on Quest

1. Navigate to the MetaMap directory in the project allocation folder

> `cd /projects/p31499/public_mm`

**Notes:** 
* Meghan copied the MetaMap installation from Dr. Luo's class allocation `/projects/e30766/public_metamap/`
* It looks like the files in this directory are based in this directory (e.g: many of the associated files explictely indicate the `/projects/e37066/` directory
* This is important to keep in mind in case that directory ever expires. Ideally, quest team can help us set this directory up on our project allocation

2. Launch a jupyter notebook on the port that is connected to MetaMap (port=1795)

> `jupyter notebook --no-browser --port=1795`

*Note: An error will raise and the port will autmatically connect to port=1796. This is okay*

3. On your local terminal, SSH onto the quest server to use the jupyter notebook in the browser. Here we will specify `localhost:1795`

> `ssh -N -f -L localhost:1795:localhost:1796 mrh1996@quest.it.northwestern.edu`

4. Navigate to the notebook: `MetaMap.ipynb`

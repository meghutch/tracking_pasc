Importing the Genism DTM function is a bit tricky. 

First, it's important to note that Gensim > 4.0.0 does not support LdaMallet and wrappers needed to run the DTM modules. 

See: 
* https://stackoverflow.com/questions/66884353/modulenotfounderror-no-module-named-gensim-models-wrappers 
* https://github.com/RaRe-Technologies/gensim/wiki/Migrating-from-Gensim-3.x-to-4#15-removed-third-party-wrappers

Thus, we can try to install 3.8.3 or earlier (Meghan has succesfully imported ```from gensim.models.wrappers import DtmModel``` using Gensim 3.8.1.

Next, we have to install the binaries:  https://radimrehurek.com/gensim_3.8.3/models/wrappers/dtmmodel.html

Either from: 

(I think the first option is probably easiest since you should only have to direct to the path where the .exe are located)
1. precompiling from: /magsilva/dtm/

OR 

2. Compile binaries manually from /blei-lab/dtm (original instruction available in https://github.com/blei-lab/dtm/blob/master/README.md), or use this command:

(linux)
```
git clone https://github.com/blei-lab/dtm.git
sudo apt-get install libgsl0-dev
cd dtm/dtm
make
```

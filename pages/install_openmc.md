# Installing OpenMC on Beocat


In the the terminal, do

```
conda create --name openmc-env -y
conda activate openmc-env
conda install -c conda-forge mamba -y
mamba install -c conda-forge openmc -y
mamba install jupyter -y
pip install nbclassic
```

These will take several minutes!

In all OpenMC notebooks, add

```
openmc.config["cross_sections"] = "/homes/jaroberts/data/cross_sections.xml"
```
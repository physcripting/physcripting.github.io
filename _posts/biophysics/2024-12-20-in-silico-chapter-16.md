---
title: "Chapter 16: BioExcel Building Blocks"
author: [PSK, SHM]
date: 2024-12-20 14:10:00 +0800
categories: [eDocuments, Introduction to Biophysics of Biomolecules]
math: true
render_with_liquid: false
---

This chapter provides a brief overview of using the BioExcel Building Block (biobb) to prepare biomolecular systems for molecular dynamics simulations with GROMACS, starting from PDB file manipulation.  For detailed instructions and the latest features, please consult the official  <a href="https://mmb.irbbarcelona.org/biobb-wfs/" target="_blank"> biobb website </a>.

## 1.1 Introduction

## 1.2 Installation

### 1.2.1 Installing Conda Environment
We will install the package through the miniconda environment to minimize the complication. 

**Step 1: Download and Installation**
* Download Miniconda from Miniconda official page.

**Step 2: Add Miniconda to Environment Variables**
Make sure to add Miniconda to the system PATH.

* Go to System Environment Variables.
* Under System variables, scroll down and select Path, then click Edit.
* Click New and add the following paths (adjust if installed elsewhere):
    * C:\Users\YourUsername\miniconda3
    * C:\Users\YourUsername\miniconda3\Scripts
    * C:\Users\YourUsername\miniconda3\Library\bin
* Click OK to save and exit.

**Step 3: Activating conda Environment**

Open Command Prompt and run:

* `conda create --name myenv python=3.10` - Create the python 3.10 version Environment. Omit it to use the latest version available.
* `conda activate name_env` - If you created an environment (e.g., name_env)
* `conda init` -  If conda is still not recognized, initialize it manually
* `conda --version` - varify the conda version
* `conda info --envs` or `conda env list` - list existing envirnments 
* `conda deactivate`- Deactivate a conda environment 
* `conda create --name new_env_name --clone old_env_name` - Create a old envirnment with the New Name
* `conda remove --name env_name --all` -  Remove conda envirnment

**Step 3: Installing Necessry Packages**

* `conda install -c conda-forge jupyterlab`- Installing latest version of Jupyter lab 
* `conda install matplotlib` - Installing packages.

We will run the python envirnment in windows. The biobb can be installed using pip. Below providing the installation of useful function to run biobb. 
* `pip install biobb-common` - base package required to use the biobb packers. 
* `pip install nglview` - A Python widget to interactively view molecular structures and trajectories, which utilizes the embeddable NGL viewer.
* `pin install utils` - A  common helper module. It stores resuaable functions (file handling, logging, math operations, etc.).

## 1.2 PDB Reader and Manipulator
The following module are required to visualize and edit pdb file
* `import nglview as nv`
* `import ipywidgets`
* `from utils import *`

* `view = nv.show_structure_file("1aki.pdb")`
* `view.add_representation(repr_type='ball+stick', selection='all')`
* `view._remote_call('setSize', target='Widget', args=['','300px'])`
* `view`
* `help(view.add_representation)`- Help on method add_reprentation in module nglview.widget. 

We will use  ChimeraX to clean the water molecules and adding hydrogens and missing atoms.
---
title: "Chapter 16: BioExcel Building Blocks"
author: PSK
date: 2024-12-20 14:10:00 +0800
categories: [eDocuments, Introduction to Biophysics of Biomolecules]
math: true
render_with_liquid: false
---

This chapter provides a brief overview of using the BioExcel Building Block (biobb) to prepare biomolecular systems for molecular dynamics simulations with GROMACS, starting from PDB file manipulation.  For detailed instructions and the latest features, please consult the official  <a href="https://mmb.irbbarcelona.org/biobb-wfs/" target="_blank"> biobb website </a>.

## 1.1 Introduction

## 1.2 Installation
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
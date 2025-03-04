---
title: "Chapter 15: Molecular Dynamics with GROMACS"
author: PSK
date: 2024-12-20 14:10:00 +0800
categories: [eDocuments, Introduction to Biophysics of Biomolecules]
math: true
render_with_liquid: false
---

This chapter provides a brief overview of using the molecular dynamics simulations with GROMACS, starting from PDB file manipulation.  For detailed instructions and the latest features, please consult the official :  <a href="https://ftp.gromacs.org/pub/manual/3.0/manual-a4-3.0.pdf" target="_blank">GROMACS USER MANUAL  </a>.

## 1.1 Introduction
The CHARMM-GUI (Chemistry at HARvard Macromolecular Mechanics Graphical User Interface) is a web-based platform designed for building complex molecular systems and preparing input files for various molecular dynamics software packages, including CHARMM, NAMD, GROMACS, AMBER, OpenMM, GENESIS, and LAMMPS.  It simplifies the setup of molecular dynamics simulations, allowing users to quickly configure simulations, including tasks such as introducing point mutations, creating deletions, and setting up steering experiments.

CHARMM-GUI offers an intuitive interface that streamlines the interaction with molecular dynamics software.  It is designed to be accessible to both new and experienced users, enabling the execution of both basic and advanced simulations.  The platform supports a wide range of simulation techniques, from membrane protein modeling and solvation to free energy calculations and coarse-grained modeling.  CHARMM-GUI is a valuable tool for researchers, particularly those without extensive programming experience, facilitating various aspects of molecular dynamics simulations. There are many key features and functionalities are avilable in CHARMM-GUI, however, we will focus on features that are relevant for computational studies of biomolecules include:


i.	Input File Generation: CHARMM-GUI generates input files compatible with various molecular dynamics software packages, including CHARMM, NAMD, GROMACS, AMBER, and LAMMPS. It ensures consistency and compatibility between the system setup and the chosen simulation software.
ii. System Setup: CHARMM-GUI facilitates the setup of molecular systems by providing tools to build and solvate biomolecular system, including proteins, nucleic acids, lipids, and small molecules. Users can define force fields and customize system parameters such as size, shape, and composition. in preparing input files for molecular dynamics simulations.
iii.	Force Field Assignment: CHARMM-GUI allows users to assign appropriate force fields and parameters to biomolecular systems, ensuring accurate representation of molecular interactions during simulations. It supports a wide range of force fields compatible with popular molecular dynamics software packages.
iv.	Solvation and Ionization: The platform assists users in solvating biomolecular systems in explicit solvent environments, with options for adding ions to neutralize system charges and achieve desired ionic strength. It supports various solvent models and provides control over solvation parameters.
v.	Membrane Builder: It includes specialized tools for constructing lipid bilayers and other membrane systems, essential for simulating biomolecules in realistic cellular environments. Users can specify lipid types, membrane dimensions, and membrane-protein interactions.
vi.	Ligand Reader and Modeler: CHARMM-GUI can handle the preparation of ligand structures and their integration into the simulation system.
vi.	Simulation Protocols: CHARMM-GUI offers pre-defined simulation protocols for equilibration and production runs, covering a range of simulation techniques such as molecular dynamics, Monte Carlo simulations, and replica exchange methods. Users can customize simulation parameters and protocols to suit their specific research needs.
vii. Advanced Simulation Options: Advanced features include support for enhanced sampling techniques like umbrella sampling, steered molecular dynamics, and free energy calculations. Users can set up complex simulation setups, including multiple replicas, restraints, and analysis options.
ix.	Analysis Tools: After completing simulations, CHARMM-GUI provides tools for analyzing simulation trajectories, extracting key observables, and visualizing molecular structures and dynamics. It supports a range of analysis techniques, including RMSD analysis, energy calculations, and trajectory visualization.

Overall, CHARMM-GUI serves as a valuable resource for researchers in the field of molecular dynamics, allowing them to set up and analyze simulations efficiently without requiring an in-depth knowledge of the underlying computational methods and protocols. The following sections describe each section in details.

## 1.2 Loading GROMACS
After installing the GROMACS successfully, typically gmx can be check using following the command
* `source /usr/local/gromacs/bin/GMXRC` - To load the gmx to your bash shell
* `source /home/siu85xxx/gromacs-2022.1/bin/GMXRC` - To load the gmx to your bash shell from HPC after installing using miniconda.
* ` gmx help` or `gmx -h`- provide the current installed version of GROMACS in your system. 


## 1.3 MD Analysis of Protein
In this section, we will investigate the hen egg white lysozyme (PDB code 1AKI), which can be download from  <a href="https://www.rcsb.org/" target="_blank"> RCSB </a> Protein Data Bank. It is recommended check the strcuture using visulization like ChimeraX
### 1.3.1 Clearning the pbd file
* `grep -v HOH 1aki.pdb > 1AKI_clean.pdb` - to remove crystal water

After removing the water, we need to varify that all the necessary atoms are presents in the PDB. Next, we will use the GROMACS module, pdb2gmx to generate files:
* The topology for the molecule: contains all the information including  nonbonded parameters (atom types and charges) as well as bonded parameters (bonds, angles, and dihedrals) necessary to define the molecule within a simulation. 
* A position restraint file.
* A post-processed structure file. 

First, we will create a gro file using the following commands:
* `gmx pdb2gmx -f 1AKI_clean.pdb -o 1AKI_processed.gro -water spce`

It will prompt to choose a force field and we will select `15: OPLS-AA/L all-atom force field (2001 aminoacid dihedrals)`

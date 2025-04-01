---
title: "Chapter 15: Molecular Dynamics with GROMACS"
author: PSK
date: 2025-03-24 14:10:00 +0800
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

> gmx can be activate through `source /home/siu85xxx/gromacs-2022.1/bin/GMXRC` when we are running in the command prompt. However, if we are using the bash script to use `source /home/siu85xxx/gromacs-2022.1/bin/gmx` to gromacs simulation
{: .prompt-tip}

## 1.3 MD Analysis of Protein
In this section, we will investigate the hen egg white lysozyme (PDB code 1AKI), which can be download from  <a href="https://www.rcsb.org/" target="_blank"> RCSB </a> Protein Data Bank. It is recommended check the strcuture using visulization like ChimeraX
### 1.3.1 Prepare the Molecule for MD
The following are the typical steps for preparing a molecule for MD simulation using GROMACS:

1. **Removing Crystal Water**:Before proceeding with the simulation, crystal water molecules (HOH) must be removed to avoid unwanted interactions. You can use command-line tools, text editors, or software like ChimeraX.. *Avoid using word processing software, as it may alter the file format*.
* `grep -v HOH 1aki.pdb > 1AKI_clean.pdb` - To remove water molecules using the command line.
2. **Generate Molecular Topology Using pdb2gmx**:  The topology file serves as a blueprint for the simulation, defining atomic interactions, bonding parameters, and force field information.

> Missing or incorrect information in the PDB file can cause errors during topology generation using `pdb2gmx` and may compromise the simulation.
* **Common Issues That May Cause `pdb2gmx` to Fail**:
    - Missing atoms: Missing atoms within residues will lead to errors.
    - Missing residues: Look for lines with "MISSING" in the PDB file, indicating incomplete structures.
    - Terminal regions: Ensure "TER" entries are included to mark chain terminations correctly.
    - Incomplete sequences: Some residues may lack atoms, requiring manual correction.
* **Limitation of `pdb2gmx`**: 
    - Not fully automated: It cannot generate topologies for arbitrary molecules (e.g., ligands or complex cofactors).
    - Restricted residue support: Works primarily with standard biomolecules (proteins, nucleic acids, some cofactors like NAD(H), ATP).
    - Missing atoms/residues must be fixed before running pdb2gmx.
{: .prompt-warning}

After removing water, verify that all necessary atoms are present in the PDB file before proceeding. Next, generate the molecular topology and structure file using the GROMACS `pdb2gmx` module: 

* `gmx pdb2gmx -f 1AKI_clean.pdb -o 1AKI_processed.gro -water spce`- 
Upon execution, GROMACS will prompt you to choose a force field. Select: `15: OPLS-AA/L all-atom force field (2001 aminoacid dihedrals)`. 

> Running `pdb2gmx` creates three key file: 
1. Topology file (`.top`): Contains nonbonded (atom types, charges) and bonded parameters (bonds, angles, dihedrals). Defines molecular interactions according to the chosen force field.
2. Position restraint file (`posre.itp`): Used for restraining atoms (typically heavy atoms) during equilibration to prevent large movements.
3. Processed structure file (`.gro`): A GROMACS coordinate file containing atomic positions and velocities. The `.gro` files is not mandatory, GROMACS supports multiple formats, including PDB (`.pdb`). If you prefer using the PDB format, simply specify the output filename with a `pdb`extension. 
{: .prompt-info}


### 1.3.2 Common Water Models in GROMACS
Depending on your installed force fields, the following water models are typically available in GROMACS:

* `ls /usr/local/gromacs/share/gromacs/top/` - list available water models in the force field directory. Inside this directory, the `.itp` files (e.g., `spce.itp`, `tip3p.itp`) correspond to available water models.
---
title: "Chapter 11: GROMACS on BigDwag Supercomputer"
author: PSK
date: 2024-12-20 14:10:00 +0800
categories: [eDocuments, Introduction to Biophysics of Biomolecules]
math: true
render_with_liquid: false
---

This chapter provides a brief overview of how to access the SIUC BigDog supercomputer and install and configure GROMACS for molecular dynamics simulations. For more detailed information, we encourage you to visit the SIUC supercomputer webpage and refer to the official user instructions.

## 1.1 Request an SIU BigDwag Account
BigDog is available to faculty, researchers, and students at no cost. Student access requires faculty/researcher supervision. All research projects are eligible for use, with no time restrictions.

To obtain a BigDwag supercomputer account, follow the instructions at this link: https://oit.siu.edu/rcc/bigdawg-request-access.php.  For further inquiries, contact research computing at 618-536-2438 or research-computing@siu.edu.

## 1.2 Protein Data Bank
The PDB file, a standard file format from the RCSB PDB (Protein Data Bank), stores three-dimensional structural data of biological macromolecules, primarily proteins and nucleic acids. The RCSB PDB serves as a global repository, https://www.rcsb.org/, collecting and disseminating experimentally determined atomic coordinates and related information of these biomolecules.

PDB files are fundamental in structural biology, offering crucial insights into the molecular architecture and function of biological macromolecules. They provide detailed information about the spatial arrangement of atoms within a molecule, enabling researchers to understand protein folding, ligand binding, and other vital biological processes.

**Key features of PDB files include**:

a. Atomic Coordinates: PDB files provide the precise X, Y, and Z coordinates of each atom in the macromolecule, expressed in Ångströms (Å). This information is essential for visualizing the three-dimensional structure and performing structural analyses.
b. Metadata:
PDB files contain extensive metadata, including the title of the structure,
the names of the authors,
the date of deposition,
details about the experimental methods used to determine the structure (e.g., X-ray crystallography, NMR spectroscopy, cryo-electron microscopy),
experimental conditions,
and literature citations.
c. Connectivity Information: PDB files define the chemical bonds between atoms, specifying the sequence of amino acids or nucleotides and the types of bonds (e.g., peptide bonds, phosphodiester bonds). This information is crucial for understanding the molecular architecture and interactions.
d. Crystallographic Information: For structures determined by X-ray crystallography, the PDB file includes details about the unit cell dimensions (a, b, c), space group, and cell angles (alpha, beta, gamma). This information is essential for understanding the crystallographic symmetry and interpreting the electron density maps.
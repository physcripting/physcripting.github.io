---
title: "Chapter 12: Protein Data Bank"
author: PSK
date: 2025-01-27 14:10:00 +0800
categories: [eDocuments, Introduction to Biophysics of Biomolecules]
math: true
render_with_liquid: false
---

This chapter provides a brief overview of Protein Data Bank (PDB) files, which are a standard format for storing information about the three-dimensional structures of biological molecules, such as proteins and nucleic acids. PDB files contain atomic coordinates, along with other information such as residues, secondary structures, and bonds. For more detailed information about PDB files and the Protein Data Bank, we encourage you to visit the Protein Data Bank website at https://www.wwpdb.org/.

## 1.1 Introduction
The Protein Data Bank (PDB) serves as the global repository for experimentally determined 3D structures of biological macromolecules, including proteins, nucleic acids, and their complexes. It plays a crucial role in advancing research across biology, biochemistry, biophysics, medicine, and computational sciences. With its open-access policy and seamless integration with bioinformatics tools, the repository continues to empower scientists worldwide by providing high-quality, experimentally determined structural data essential for understanding the molecular basis of life.

PDB files, the standard format for storing 3D structural data, are fundamental to structural biology. These files contain detailed atomic coordinates, bond lengths, and angles, providing critical insights into molecular architecture. This structural information enables researchers to explore protein folding, ligand binding, enzymatic activity, and other essential biological processes, driving advancements in drug design and biomolecular engineering

The repository was established in 1971  at Brookhaven National Laboratory (BNL) in New York to serve as a repository for 3D structures of biological molecules. Here are some key historical highlights::

 i. **1971 - Founding**: The PDB began with just seven protein structures, including myoglobin and lysozyme, primarily determined using X-ray crystallography.

 ii. **1980s - Growth**: Significant advancements in computational power and structure determination techniques, such as NMR spectroscopy, led to a rapid increase in the number of deposited structures.

 iii. **1990s - Modernization**: In 1998, management transitioned from BNL to the Research Collaboratory for Structural Bioinformatics (RCSB).

 iv. **2003-wwPDB**: The formation of the Worldwide Protein Data Bank (wwPDB) in 2003 established a global partnership to ensure the consistent curation and dissemination of structural data. Partner organizations include the RCSB PDB (USA), PDBe (Europe), PDBj (Japan), and the BMRB (focused on NMR data).

 v. **2000s - Expansion and Accessibility**: The inclusion of structures determined by cryo-electron microscopy (cryo-EM) significantly expanded the scope of the archive. Furthermore, the development of user-friendly online tools and visualization software greatly enhanced data accessibility for researchers worldwide.

The RSCB PDB (<a href="https://www.rcsb.org/" target="_blank">  rcsb.org </a>)serves as the primary access point for the Protein Data Bank archive.  This freely accessible resource not only provides unrestricted access to the wealth of structural data but also offers a treasure trove of educational resources. Notably, PDB-101 caters to students and the general public, introducing them to the fundamentals of biomolecular structures.

## 1.2 Key Featrues of PDB files
A PDB (Protein Data Bank) file is a structured text file that stores experimentally determined 3D structural data of biological macromolecules. Each line in the file represents a record, which follows a standardized format to describe the molecular structure in detail. The primary sections of a PDB file include:

* **Header Section**: Contains metadata about the structure, including Title, deposition date, literature citations, and experimental methods (techniques used to determine the structure such as X-ray, NMR, cryo-EM) and authors and citations.

* **Coordinate Section (ATOM, HETATM)**: Provides the atomic coordinates of each atom in the structure. This section includes information about the atom type, atom name, residue name, chain identifier, residue sequence number, and the X, Y, Z coordinates, expressed in Ångströms (Å). This information is essential for visualizing the three-dimensional structure and performing structural analyses.
    * **ATOM**:	Atoms in standard residues (amino acids and nucleic acids).
    * **HETATM**: Atoms in nonstandard residues. Nonstandard residues include inhibitors, cofactors, ions, and solvent. The only functional difference from ATOM records is that HETATM residues are by default not connected to other residues. Note that water residues should be in HETATM records.
    * **TER**:	indicates the end of a chain of residues. For example, a hemoglobin molecule consists of four subunit chains that are not connected. TER indicates the end of a chain and prevents the display of a connection to the next chain.
    * **HELIX**:	indicates the location and type (right-handed alpha, etc.) of helices. One record per helix. Helic types: 1. Right-handed alpha (default), 2. Right-handed omega, 3. Right-handed pi, 4. Right-handed gamma, 5. Right-handed, 6. Left-handed alpha, 7. Left-handed omega, 8. Left-handed gamma, 9. 2/7 ribbon/helix, 10. polyproline.
    * **SHEET**:	indicates the location, sense (anti-parallel, etc.) and registration with respect to the previous strand in the sheet (if any) of each strand in the model. One record per strand.
    * **SSBOND**:	defines disulfide bond linkages between cysteine residues.
* **Connectivity Section (CONECT)**: Specifies the bonds between atoms, especially relevant for proteins with multiple chains, specifying the sequence of amino acids or nucleotides and the types of bonds (e.g., peptide bonds, phosphodiester bonds). This information is crucial for understanding the molecular architecture and interactions.
* **Crystallographic Information**: For structures determined by X-ray crystallography, the PDB file includes details about the unit cell dimensions (a, b, c), space group, and cell angles ($$\alpha$$, $$\beta$$, $$\gamma$$). This information is essential for understanding the crystallographic symmetry and interpreting the electron density maps.

## 1.3 Examples of PDB Format
Glucagon is a peptide hormone composed of a single chain of 29 amino acids. It plays a crucial role in glucose metabolism by stimulating the liver to release glucose into the bloodstream. The first residue is the amino-terminal amino acid, histidine (His), which is followed by a serine (Ser) residue and then a glutamine (Gln). The 3D structural information of glucagon is available in the Protein Data Bank (PDB) under entry 1GCN, shown in table below, which provides atomic coordinates for each atom in the molecule.

|ATOM|      1|  N   |HIS| A|   1|      49.668|  24.248|  10.436|  1.00| 25.00| N|
|ATOM|      2|  CA  |HIS| A|   1|      50.197|  25.578|  10.784|  1.00| 16.00| C|
|ATOM|      3|  C   |HIS| A|   1|      49.169|  26.701|  10.917|  1.00| 16.00| C|
|ATOM|      4|  O   |HIS| A|   1|      48.241|  26.524|  11.749|  1.00| 16.00| O|
|ATOM|      5|  CB  |HIS| A|   1|      51.312|  26.048|   9.843|  1.00| 16.00| C|
|ATOM|      6|  CG  |HIS| A|   1|      50.958|  26.068|   8.340|  1.00| 16.00| C|
|ATOM|      7|  ND1 |HIS| A|   1|      49.636|  26.144|   7.860|  1.00| 16.00| N|
|ATOM|      8|  CD2 |HIS| A|   1|      51.797|  26.043|   7.286|  1.00| 16.00| C|
|ATOM|      9|  CE1 |HIS| A|   1|      49.691|  26.152|   6.454|  1.00| 17.00| C|
|ATOM|     10|  NE2 |HIS| A|   1|      51.046|  26.090|   6.098|  1.00| 17.00| N|
|ATOM|     11|  N   |SER| A|   2|      49.788|  27.850|  10.784|  1.00| 16.00| N|
|ATOM|     12|  CA  |SER| A|   2|      49.138|  29.147|  10.620|  1.00| 15.00| C|
|ATOM|     13|  C   |SER| A|   2|      47.713|  29.006|  10.110|  1.00| 15.00| C|
|ATOM|     14|  O   |SER| A|   2|      46.740|  29.251|  10.864|  1.00| 15.00| O|

In PDB coordinate files, atomic names follow a specific nomenclature: atoms names beginning with C represent carbon atoms; N indicates a nitrogen and O indicates oxygen. For amino acid side chains, the next character in the atom name designates the remoteness indicator code, which follows this convention:

|$$\alpha  - $$ A| $$\beta -$$	B| $$\gamma -$$ G| $$\delta -$$	D| $$\varepsilon-$$	E| $$\zeta - $$	Z|$$\eta -$$	H|


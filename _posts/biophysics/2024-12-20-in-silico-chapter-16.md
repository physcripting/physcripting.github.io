---
title: "Chapter 16: CP2K"
author: PSK
date: 2026-03-7 14:10:00 +0800
categories: [eDocuments, Introduction to Biophysics of Biomolecules]
math: true
render_with_liquid: false
---

This chapter provides a brief overview of using the QM/MM with CP2K.  For detailed instructions and the latest features, please consult the official :  <a href="https://www.cp2k.org/about" target="_blank">CP2K  </a>.

## 15.1 Introduction
CP2K is an open-source computational chemistry and solid-state physics software package that enables atomistic simulations of molecular, condensed-phase, and biological systems. It supports a wide range of computational methods, including Density Functional Theory (DFT), Hartree–Fock, semi-empirical quantum methods, molecular mechanics (MM), and hybrid Quantum Mechanics/Molecular Mechanics (QM/MM) approaches.

CP2K is particularly well suited for studying materials, crystals, liquids, interfaces, catalysts, biomolecules, and metal-containing proteins. Its efficient implementation of the Gaussian and Plane Waves (GPW) method allows large-scale electronic structure calculations on high-performance computing systems.

The name CP2K originated from the original CP (Car–Parrinello) code developed for the new millennium. It has evolved into a comprehensive simulation package with capabilities extending far beyond Car–Parrinello molecular dynamics.

Unlike many commercial molecular modeling packages, CP2K does not have a graphical user interface (GUI). Instead, simulations are controlled through text-based input files, typically with the extensions `.in` or `.inp` for input files. These input files define the computational method, molecular structure, simulation parameters, and output options.

Before running CP2K, verify that the software module is available on your computing system:
* `module avail cp2k` or `module spider cp2k` - To check Available Modules 
* `module load CP2K`- To load CP2K 

The examples and instructions in this tutorial are primarily written for the Stampede3 supercomputer at the Texas Advanced Computing Center (TACC), although they can be adapted to other high-performance computing (HPC) systems with minor modifications..

## 15.2 Connecting Cluster
* `ssh username@stampede3.tacc.utexas.edu` -To connect to stempede3 a Linux/macOS shell or Windows terminal.

## 15.3 CP2K modules
Before running CP2K, verify which versions are available on the system.
* `module spider cp2k` or `module avail cp2k` - These commands display the available CP2K versions and their associated compiler and MPI builds.
* `module load cp2k/2025.2.1` - To load specific version

**Running CP2K on Stampede3** CP2K is a parallel MPI application and should not be run directly on the login node. On Stampede3 at the Texas Advanced Computing Center (TACC), CP2K jobs must be executed within an allocated compute environment, either:

* `idev` for through an interactive session
* `sbatch` for through a batch job submition using `slurm`

MPI applications are typically launched using `ibrun`, TACC's recommended launcher.

### 15.3.1 Running CP2K in an Interactive Session
1. Start Interactive Session:  
* `idev`: Wait until compute resources are allocated and a compute-node shell becomes available.
2. Load the CP2K Module
* `module reset`
* `module load cp2k/2025.2.1`
3. Verify the Installation
`ibrun cp2k.psmp --version`
or 
`ibrun -n 1 cp2k.psmp --version`
4. Run a CP2K Calculation 
`ibrun cp2k.psmp -i test.inp -o test.out`
where: 
  * `test.inp` is the CP2K input file
  * `test.out` is the output file generated during the calculation
### 15.3.2 Running CP2K Using a Slurm Batch Job
1. Create a file named `cp2k_test.sh` containing the following script: 

```bash
#!/bin/bash
#SBATCH -J cp2k
#SBATCH -N 2
#SBATCH -n 96
#SBATCH -t 04:00:00
#SBATCH -A YOUR_ALLOCATION

module reset
module load cp2k/2025.2.1
export OMP_NUM_THREADS=2
ibrun cp2k.psmp -i input.inp -o output.out
```
2. Submit the Job 
`sbatch cp2k_test.sh`
3. Monitor Job Status
`squeue -u $USER` or `showq -u $USER`

## 15.4 Example: Water Molecule
Coordiante file  (`.xyz`) and input file (`.inp`) are required for the water molecule. Here we will do the gemeotrical optimization  (`GEO_OPT`) over energy. 
* Create Coordinate file of water molecule `water.xyz` using text file editor or similar

```
O    0.000000    0.000000    0.000000
H    0.758602    0.000000    0.504284
H   -0.758602    0.000000    0.504284
```

* Similarly, create CP2K input file `water.inp`, which optimize using geometry of the molecules

```
&GLOBAL
  PROJECT water
  RUN_TYPE GEO_OPT
  PRINT_LEVEL MEDIUM
&END GLOBAL

&FORCE_EVAL
  METHOD QS

  &DFT
    BASIS_SET_FILE_NAME BASIS_MOLOPT
    POTENTIAL_FILE_NAME GTH_POTENTIALS

    &MGRID
      CUTOFF 400
    &END MGRID

    &QS
      EPS_DEFAULT 1.0E-10
    &END QS

    &SCF
      SCF_GUESS ATOMIC
      EPS_SCF 1.0E-6
      MAX_SCF 50

      &OT
        PRECONDITIONER FULL_SINGLE_INVERSE
        MINIMIZER DIIS
      &END OT
    &END SCF

    &XC
      &XC_FUNCTIONAL PBE
      &END XC_FUNCTIONAL
    &END XC
  &END DFT

  &SUBSYS
    &CELL
      ABC 10.0 10.0 10.0
    &END CELL

    &COORD
      @include water.xyz
    &END COORD

    &KIND O
      BASIS_SET DZVP-MOLOPT-SR-GTH
      POTENTIAL GTH-PBE
    &END KIND

    &KIND H
      BASIS_SET DZVP-MOLOPT-SR-GTH
      POTENTIAL GTH-PBE
    &END KIND

  &END SUBSYS
&END FORCE_EVAL
```

Before submitting the job, let's try the interactive test 
* `module purge`
* `module load CP2K`
* `module list`
* `module load CP2K/2023.2-gcc10.2.0-openmpi4.0.5`
* `cp2k.ssmp --version`
* `cp2k.ssmp water.inp` - If this works CP2K installation is fine

* Create SLURM Script `run_cp2k.sh`

We will run using batch job instead of interactive `srun`. It appears CP2K is giving error with `srun` and `mpirun`on the bridges-2

```bash
#!/bin/bash
#SBATCH --job-name=water
#SBATCH --partition=RM
#SBATCH --nodes=1
#SBATCH --ntasks=2
#SBATCH --time=00:05:00

module purge
module load CP2K/2023.2-gcc10.2.0-openmpi4.0.5

echo "Running on $(hostname)"

cp2k.psmp water.inp > water.log
```
* `sbatch run_cp2k.sh` -To submit the job. You will get something like:  `Submitted batch job 1234567`
* `squeue -u $USER` -To monitor job status
Example: Job waiting in queue

```
JOBID PARTITION NAME        USER   ST TIME  NODES NODELIST(REASON) \\
12345 RM        cp2k_water  abc123 PD 0:00      1 (Priority)
```

* `scontrol show job JOBID` for detailed job information
* `sacct -j JOBID`  - To check job history
* `sacct -u $USER --format=JobID,JobName,State,Elapsed` - To chekc queue history, very useful for debugging.
* You should see output files `water.log`, `cp2k_water.out`, and `cp2k_water.err`
* `grep ENERGY water.out` -To Extract Energy
* `cat cp2k_water.err` to inspect error file

**Check Output of Optimization**
* grep -i "SCF run converged" water_opt.out
* grep -i "MAX_SCF" water_opt.out
* grep -i "GEOMETRY OPTIMIZATION COMPLETED" water_opt.out
* grep "ENERGY| Total FORCE_EVAL" water_opt.out
* grep -A5 "MAXIMUM FORCE" water_opt.out
* `open Water-pos-1.xyz` using ChimeraX to see the optimization animation

## 15.5 Example: Metal-binding Protein 2DSX
This protein is particularly attractive because it is small (52 amino acids) and contains a single Fe atom coordinated by four cysteine sulfur atoms in a nearly tetrahedral geometry.

 1. **Inspect The Structrue**: Open in ChimeraX
  * Check (i) Fe atom exists, (ii) Four coordinating cysteines exist, and (iii) No missing residues
  * Remove crystallographic waters unless they participate directly in Fe coordination.: `delete solvent` and `save 2dsx_clean.pdb` 
  * Keep the Fe(III) ion.
  * Verify protonation states (especially cysteines). There are four cysteines should remain deprotonated (thiolate, S−) because they coordinate the iron center.
  * No missing residues. 
  2. **Classical Minimization** 
The goal of the classical minimization is not to obtain the final electronic structure, but to relax bad contacts, add solvent, equilibrate the protein, and produce a realistic starting structure for the subsequent CP2K QM/MM calculation.
  * **Generate topology, position restraint, & post-processed structure files**:
    * `gmx pdb2gmx -f 2dsx_clean.pdb -o 2dsx_processed.gro -water tip3p` 
We will use the CHARMM36 forice field, which can be obtained from the **MacKerell lab Website** and copy this into the directory. 


  > **Important consideration for the Fe center**: `pdb2gmx` does not automatically parameterize metal coordination. The Fe–S bonds in rubredoxin require special treatment. There are three common strategies:
  1. Distance restraints between Fe and the coordinating sulfur atoms (simplest).
  2. Bonded metal model using custom topology parameters.
  3. Exclude the Fe coordination from classical optimization and rely on the later QM/MM optimization to refine the active site.  This approach is commonly used because the active site geometry will be optimized quantum mechanically. 
  {: .prompt-info}
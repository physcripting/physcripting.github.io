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
CP2K (under active development) is a quantum chemistry and solid state physics software package that can perform atomistic simulations of solid state, liquid, molecular, periodic, material, crystal, and biological systems.
The original meaning was the CP (Car-Parrinello) code for the new Millenium.

CP2K does not have a graphical user interface, instead we use input files to tell CP2K what to do. Our input files have the file extension `.in` or `.inp`.

First, we need to check CP2K module is available
* `module avail cp2k` or `module spider cp2k` - To check Available Modules 
* `module load CP2K`- To load CP2K 

Most of the instructure are written for stempeded3 at Texas Advanced Computing Center (TACO).

## 15.2 Connecting Cluster
* `ssh username@stampede3.tacc.utexas.edu` -To connect to stempede3 a Linux/macOS shell or Windows terminal.

> If you see a message similar as this: <\br> 
The authenticity of host 'stampede3.tacc.utexas.edu (129.114.63.133)' can't be established. ED25519 key fingerprint is SHA256:Pf24LgTG9D0TTBOnYCy0RbKZHTjVo+fw4quHsuGJ+2w. <\br> This key is not known by any other names. <\br> Are you sure you want to continue connecting <\br> (yes/no/[fingerprint])? <br>
* Type  `Yes`
* If te connetion produces `Corrupted MAC on input`
* Try `ssh -o IPQoS=none -o MACs=hmac-sha2-512 -o Ciphers=aes256-ctr username@stampede3.tacc.utexas.edu`
{: .prompt-info}

## 15.3 CP2K modules
* `module spider cp2k` or `module avail cp2k` - This shows available versions and compiler/MPI builds.
* `module load cp2k/2025.2.1` - To load specific version

**To run cp2k.psmp directly** on the login node without an allocated compute environment. On Texas Advanced Computing Center Stampede3, MPI applications must be launched either:

* inside an interactive allocation (`idev`)
* or through a Slurm batch job (`sbatch`)
* typically using `ibrun`

**To run on terminal**
1. Start Interactive Session:

```bash
idev
``
2. Load CP2K

```bash
module reset
module load cp2k/2025.2.1
```

3. Check version correctly
`ibrun cp2k.psmp --version`
or 
`ibrun -n 1 cp2k.psmp --version`
4. Running on shell 
`ibrun cp2k.psmp -i test.inp -o test.out`
5. For jobs using Slurm
Create a cp2k_test.sh file and paste the following 

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

submit with

`sbatch cp2k_test.sh`

## 15.4 Example: Water Molecule
Coordiante file  (`.xyz`) and input file (`.inp`) are required for the water molecule. Here we will do the gemeotrical optimization  (`GEO_OPT`) over energy. 
* Create Coordinate file of water molecule `water.xyz` using text file editor or similar

```
O    0.000000    0.000000    0.000000
H    0.758602    0.000000    0.504284
H   -0.758602    0.000000    0.504284
```

* Similarly, create CP2K input file `water.inp`

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

* `squeue -u $USER -o "%.8A %.10T %.20j %.10M %.6D %R"` better queue format display
* `scontrol show job JOBID` for detailed job information
* You should see output files `water.log`, `cp2k_water.out`, and `cp2k_water.err`
* `grep ENERGY water.out` -To Extract Energy
* `sacct -j JOBID`  - To check job history
* `sacct -u $USER --format=JobID,JobName,State,Elapsed` - To chekc queue history, very useful for debugging.
* `cat cp2k_water.err` to inspect error file
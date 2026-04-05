---
title: "Appendix"
author: PSK
date: 2026-3-7 14:10:00 +0800
categories: [eDocuments, Introduction to Biophysics of Biomolecules]
math: true
render_with_liquid: false
---

This chapter provides a brief overview of using the BioExcel Building Block (biobb) to prepare biomolecular systems for molecular dynamics simulations with GROMACS, starting from PDB file manipulation.  

## 13 Introduction
**Basic Linux Commands Useful for HPC:** These commands are essential for navigating directories, managing files, and monitoring jobs on an HPC system.

**File and Directory Management**
* `pwd` — show current directory
* `ls` — list files
* `ls -l` — detailed file listing
* `cd directory_name` — change directory
* `cd ..` — move up one directory
* `mkdir folder_name` — create a directory
* `rm file` — delete a file
* `rm -r folder` — delete a directory (use carefully)

**Viewing and Editing Files**
* `cat filename` — display file contents
* `less filename` — view large files safely
* `head filename` — show first 10 lines
* `tail filename` — show last 10 lines
* `nano filename` — edit file (beginner-friendly)
* `vi filename` or `vim filename` — advanced editor commonly used on HPC

**System and Job Monitoring**
* `whoami` — show your username
* `hostname` — show compute/login node name
* `top` or `htop` — monitor running processes
* `df -h` — check disk usage
* `du -sh folder_name` — size of a directory

**Job Scheduler (examples — cluster dependent)**
Actual commands depend on the scheduler used on BigDawg, such as SLURM
* `sbatch job.sh` — submit a job
* `squeue -u username` — check job status
* `scancel jobID` — cancel a job

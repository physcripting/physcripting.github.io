---
title: "Chapter 14: Setting Up Local and HPC Environments for MD Simulations"
author: PSK
date: 2025-02-26 14:10:00 +0800
categories: [eDocuments, Introduction to Biophysics of Biomolecules]
math: true
render_with_liquid: false
---

This chapter provides step-by-step instructions for installing Linux (Ubuntu) on Windows using WSL2, accessing the SIUC BigDog supercomputer, installing and configuring GROMACS for molecular dynamics simulations, and running simulations with the installed software. For detailed information, visit the  <a href="https://oit.siu.edu/rcc/" target="_blank"> SIUC Research Computing and Cyberingrastructure </a>  and read the official user documentation.

## 13.1 Introduction
Molecular dynamics (MD) simulations are frequently performed on Linux-based operating systems due to the rich ecosystem of open-source software, powerful command-line tools, and robust computational resources readily available. This chapter provides a comprehensive guide for setting up a suitable environment for MD simulations, covering both local and high-performance computing (HPC) options.

First, we will discuss  the installation procedure of the Ubuntu Linux distribution on a local Windows computer using Windows Subsystem for Linux 2 (WSL2). WSL2 offers a lightweight virtual machine environment optimized for Linux, enabling seamless integration with the Windows operating system.  This allows users to leverage the familiar Windows environment while gaining access to the powerful tools and flexibility of Linux.

Following the Linux installation, we will guide you through setting up the necessary software packages for MD simulations.  A primary focus will be the installation of GROMACS (GROningen MAchine for Chemical Simulations), a versatile package to perform for molecular dynamics simulations of biomolecular systems.  On local machines, GROMACS will be compiled and installed directly within the Linux environment, allowing for efficient use of system resources. We will cover necessary dependencies and best practices for a successful installation.

Computational investigations of macromolecules, such as protein-ligand interaction, polymers, and nucleic acids, often demand significant computational resources. To address the needs of large-scale MD simulations, we will leverage the SIUC BigDawg supercomputer. BigDawg is a high-performance computing (HPC) cluster at SIUC designed for computationally intensive research. For the BigDawg HPC cluster, we will utilize Miniconda, a free and open-source cross-platform package manager, to streamline the installation of GROMACS and other essential software. Miniconda simplifies dependency management and ensures compatibility within the HPC environment.  We will provide instructions on accessing BigDawg and utilizing its resources effectively.


For further information and detailed instructions, please refer to the official  <a href="https://docs.microsoft.com/en-us/windows/wsl/" target="_blank"> Microsoft Windows Subsystem </a> for Linux Documentation and  the SIUC Research Computing Center's <a href="https://oit.siu.edu/rcc/bigdawg-request-access.php" target="_blank"> BigDog access page  </a>. The following sections provide a step-by-step guide to the installation and configuration processes for both local and HPC environments.

## 13.2 Request an SIU BigDawg Account
BigDog is available to faculty, researchers, and students at no cost. Student access requires faculty/researcher supervision. All research projects are eligible for use, with no time restrictions.

To obtain a BigDawg supercomputer account, follow the instructions at this link: https://oit.siu.edu/rcc/bigdawg-request-access.php.  For further inquiries, contact research computing at 618-536-2438 or research-computing@siu.edu.

## 13.3 Installing GROMACS in Local Computer 
In this section, we will discuss the installation of GROMACS on the Windows operating system using the Windows Subsystem for Linux (WSL). GROMACS can be installed through two methods: (1) using the package manager with the command apt-get install gromacs, or (2) performing a manual installation by downloading and configuring GROMACS from the official source.

> Using Anaconda or Miniconda can cause issues when installing GROMACS, particularly related to AVX2 compatibility. If you see a login prompt with "`(base)-bash-$`", it indicates that the Conda environment is active, which may interfere with the installation. 
To avoid potential conflicts, it is recommended to disable Anaconda/Miniconda, restart the system, and then proceed with the GROMACS installation (unless installing via Miniconda).
To disable Conda’s base environment before installing GROMACS, run
* `conda config --set auto_activate_base False`   
{: .prompt-warning}

## 13.4 Installing GROMACS on Linux Server
### 13.4.1 Connecting to the SIU BigDawg Cluster
To connect to the BigDawg cluster and perform remote computing from a Windows system, we will use **MobaXterm** or **WinSCP**.

**Step 1: Connect Cisco Secure Client**
* open **Cisco Secure Client (VPN)**
* Connect to: `private.siu.edu/bigdawg`
* Use your SIU credentials:
    * Username: `siu85xxxxx or xxx@siu.edu`
    * Password : `xxxx`

**Step 2: SSH into BigDwag**

Once connected to the VPN, use SSH to access the cluster
* `ssh siu853xxx@bigdawg.research.siu.edu` 

**Recommended Working Directory**: It is recommended to work in the /scratch/siu85xxxxx directory, as it provides more storage compared to /home/siu85xxxxx. 
* `cd /scratch/siu85xxxxx`
     
**Transferring Files Between Local Computer and BigDawg**
    
Copying a File from Local Computer to BigDawg
* `scp filename siu85xxxxx@bigdawg.research.siu.edu:/scratch/siu85xxxxx/1AKI/`
Copying a File from BigDawg to Local Computer
* `scp siu85xxxxx@bigdawg.research.siu.edu:/scratch/siu85xxxxx/3HTB ./local_directory/` 


### 13.4.2 Installing and Setup Miniconda
As we do not have the root password in the BigDwag, we are limited to installing new software. We can request BigDwag  admistration to install software however, it may take sometime and it may need to frequent optimization to run the modeling properly.  Because of these limitation, we will create a miniconda enviroment and install the software in the minicond invironment without root password in our local directory. 

Installing miniconda and Setup:  Install the software using miniconda or anaconda in the Bigdwag. We don't need to root to install with anaconda or minconda.

**Step 1: Download Miniconda**
Use wget to download the latest Miniconda installer
* `wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh`

**Step 2: Install Minoconda**

Run the downloaded script:
* `bash Miniconda3-latest-Linux-x86_64.sh`

Follow the on-screen instructions and accept the license agreement when prompted.

**Step 3: Initialize Conda**

After installation, initialize Conda:
* `source ~/.bashrc`
* `conda init`

To apply the changes, restart your terminal or run:
* `source ~/.bashrc`

**Step 4: Verify Installation**

Check if Conda is installed correctly
* `conda --version`
you should see output like `conda 23.x.x`

* `modlconda install -c anaconda cmake` - to the latest version of cmake can be installed using 

* `conda update -n base conda` -  to update the conda
* `conda install anaconda::cmake`-   to install update cmake in conda 
* `conda-forge::cmake` - update cmake

**Step 5: Deactivate and active conda environment**
* `conda deativate`  to deativate conda environment
* `conda activate` or  `source ~/.bashrc` to reactive the conda environment manually 

    
   
       

**Working in conda envirnment**



* conda list
* printenv |grep gcc
* conda create -n env-name  (create a new environment such as myenv)
* conda create -n myenv python numpy pandas ( adding package while creating environments)
* conda install --name myenv conda-forge::gcc (install gcc to myenv environment)
* conda install --name myenv conda-forge::cmake (install cmake to myenv environment)
* conda activate myenv (activate specific environment)
* conda activate (change back to default)
*  conda remove cmake (removing cmake)
* conda install cmake=3.19.4 (install old version of cmake)

    creating a conda env with gcc
           - $conda create -n gcc gcc
* conda search gccconda 
* conda activating gcc


**(Optional)Disable Auto Activation of Base Environment**
If you don’t want Conda to activate the (base) environment every time, run:
* `conda config --set auto_activate_base False`


**Removing miniconda**
* rm -rf ~/minconda3
* remove path from .bashrc or .bash_profile . Remove this line:
    * added by Miniconda3 installer
    * export PATH="/home/username/miniconda3/bin:$PATH"
    * run `source ~/.bashrc` to reload the bash profile


### 13.4.3 Installing GROMACS
Gromacs may already in your system which can be check through, 
* `module avail` : to display available modules.
* `load module package_name` such as gromacs-2018-gcc...,
* `which gmx_gmi` 

Download approapriate version of GROMACS for your system. You need check the gcc version in your server and download appropriate GROMACS that can support for that version. Conda has gcc however, GROMACS require system gcc although the GROMACS is installing conda envirnments.  - Before starting to install, get the latest version of C and C++ compilers.  The gcc version can be found through:
* `gcc --version`
* `which gccwhich`

Before installing GROMACS, ensure that CMake is installed and check its version using:
* `cmake --version`
If the latest version is required, it can be installed using Miniconda:
* `conda install -c conda-forge cmake`
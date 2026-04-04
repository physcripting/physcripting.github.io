---
title: "Chapter 13: System Configuration for In-Silico Analysis"
author: [PSK, SHM]
date: 2026-01-28 14:10:00 +0800
categories: [eDocuments, Introduction to Biophysics of Biomolecules]
math: true
render_with_liquid: false
---

This chapter provides step-by-step instructions for installing Linux (Ubuntu) on Windows using WSL2, accessing the SIUC BigDawg supercomputer, installing and configuring GROMACS for molecular dynamics simulations, and running simulations with the installed software. For detailed information, visit the  <a href="https://oit.siu.edu/rcc/" target="_blank"> SIUC Research Computing and Cyberinfrastructure </a>  and read the official user documentation.

## 13.1 Introduction
In-silico molecular modeling, particularly **molecular dynamics (MD)** simulations, requires significant computational resources. These simulations are most commonly performed in **Linux-based environments**, which provide a strong ecosystem of open-source scientific software, powerful command-line tools, and well-established high-performance computing (HPC) infrastructure. 

Many widely used MD software packages, including  <a href="https://www.gromacs.org/" target="_blank">  GROMACS</a> (GROningen MAchine for Chemical Simulations), are primarily developed and maintained primarily for Linux. This chapter provides intruction to setting up an MD simulation environment on both local computers and HPC systems.

We begin by installing the Ubuntu Linux distribution on a Windows computer using **Windows Subsystem for Linux 2 (WSL2)**. WSL2 allows users to run a full Linux environment directly inside Windows. This approach provides:

* High compatibility with Linux applications
* Compatibility with most Linux-based MD applications
* Easy integration with the Windows operating system

With WSL2, users can keep their Windows workflow while using the Linux tools commonly required for molecular simulations.

After setting up WSL2, we will install GROMACS, a widely used molecular dynamics package for simulating biomolecular systems. The software will be compiled and installed within the Linux environment, along with the required dependencies.

While local computers are suitable for small to medium simulations, larger molecular systems require more computational power. For these cases, researchers typically use high-performance computing (HPC) clusters.

In this chapter, we will setup account at <a href="https://oit.siu.edu/rcc/bigdawg-specifications.php" target="_blank"> SIU’s BigDawg HPC cluster </a> and installing GROMACS and necessary packages at user level. To manage software installations at the user level on the cluster, we will use <a href="https://www.anaconda.com/docs/getting-started/miniconda/main" target="_blank"> Miniconda </a>, a lightweight package and environment manager that enables reproducible and isolated software environments without requiring administrative privileges. This chapter includes step-by-step instructions for:
* Setting up Linux using WSL2 on a personal computer
* Accessing and configuring the SIUC  BigDawg HPC cluster
* Installing and configuring GROMACS on both a personal computer and the BigDawg HPC cluster
* Running MD simulations using SLURM, a common workload manager for HPC systems

By the end of this chapter, you will have a working MD simulation environment on both **local systems (Windows + WSL2)** and the **BigDawg HPC cluster**.

## 13.2. WSL2
This section provides a detailed guide on installing Ubuntu (A popular Linux distribution) on Windows using **Windows Subsystem for Linux 2 (WSL2)**. WSL2 is a full Linux kernel implementation that runs within a lightweight, virtualized environment on Windows, offering near-native performance for Linux applications. For official documentation, system requirements, and troubleshooting, refer to the  <a href="https://docs.microsoft.com/en-us/windows/wsl/" target="_blank"> Microsoft Windows Subsystem for Linux Documentation </a> .

In many cases you will find yourself needing to a linux command line to manuever around your files and utilize important software. As such, you can install Windows Terminal, an official application designed to handle WSL and all the other command lines you may interact with on your windows machine. You can get all these tools directly from the **Microsoft Store**:

<figure class="half-width">
	<img src="/assets/img/Biophysics/Chapter-13/C13_2.png" alt="Description of the image" style= "width: 90%;"> 
	<figcaption>Terminal after install WSL2 & setting up</figcaption>
</figure>

[**Windows Terminal**](https://apps.microsoft.com/detail/9n0dx20hk701?hl=en-US&gl=US){:target="_blank"} (link, press view in store, if you get a prompt, click `Open Microsoft Store`, and then click the blue `Get` button to install) 

[**Ubuntu**](https://apps.microsoft.com/detail/9pdxgncfsczv?hl=en-US&gl=US){:target="_blank"} (same as instructions as Windows Terminal)

Once these are both installed, open up the newly installed Ubuntu app. You should now see some messages appear to set up your user info.


> If you aren't too familiar with how to use a linux command line, read [any of these beginner resources here](https://researchcomputing.princeton.edu/education/external-online-resources/linux) to learn the essential commands.
{: .prompt-tip}

* We can access your Windows files from within WSL2 using the following command: `cd /mnt/c`
* You can also use Windows applications from the terminal to open files to edit: `notepad.exe {{text file in PWD}}`
* You can also view and edit Linux files directly in **Windows File Explorer** by navigating to:  `\\wsl.localhost\` (*This provides native access to WSL2 files without requiring SSH or third-party tools*)

> Tip: Store large datasets inside the WSL filesystem (/home/user/) instead of Windows (/mnt/c/) to avoid performance issues.
{: .prompt-tip}

## 13.3 Miniconda
Miniconda is an open-source software distribution that provides a minimal installation of Anaconda, including Conda, Python, and essential packages they depend on. It is lightweight and allows users to manage environments efficiently. More information can be found on the official <a href="https://www.anaconda.com/docs/getting-started/miniconda/main" target="_blank"> Miniconda documentaion</a>.

Using Conda simplifies package installation and dependency management. Because Miniconda can be installed without root privileges, it is especially useful for personal computers and HPC systems. The following steps describe how to install Miniconda on Linux systems, including WSL2. A similar approach can be used when installing software on the SIU BigDawg HPC cluster.

### 13.3.1 Download & Install Miniconda
* The SIU BigDawg HPC cluster uses an older system library (glibc version 2.17), which is incompatible with the latest Miniconda installer. To avoid this compatibility issue, download a stable older version using curl : <br> 
`curl -O https://repo.anaconda.com/miniconda/Miniconda3-py39_4.9.2-Linux-x86_64.sh` 

* Run the installer with bash: <br> 
`bash Miniconda3-py39_4.9.2-Linux-x86_64.sh`
* Follow the on-screen prompts and accept the license agreement. Press Enter to review the license and type yes to accept.

### 13.3.2 Initialize Conda
After installation, initialize Conda:
* `conda init`
Restart your terminal or reload the shell configuration through 
* `source ~/.bashrc`
Check if Conda is installed correctly
* `conda --version` - Display a version number like `conda 23.x.x` or newer
* `conda info` - Shows information about the Conda installation, including the active environment, Conda version, and installation paths.

### 13.3.3 Conda Envirnment
Conda allows you to create isolated environments for different projects. This prevents conflicts between software packages and dependencies. Create a new environment (recommended for molecular dynamic tools). For Example: 
* `conda create -n gromacs_env python=3.10` - to create the environment with python 3.10. 
* `conda env list` - List all the conda environments.
* `conda activate gromacs_env` - Activate specific envirnment
* `conda install --name <environment-name> <package-name>`- General syntax for installing a package

### 13.3.5 Additional Conda Commands 
The following commands are useful when working with Miniconda environments. These are not required for most users but can help with environment management and troubleshooting.

* `conda list` - List all installed packages in the current environment
* `conda install pack_name`- Install a package into the active environment
* `conda activate` - Switch back to the base (default) environment.
* `conda deactivate`: Exit the current Conda environment
* `conda remove --name <env_name> --all` - Remove a specific Conda environment
* `python --version`- To find the python version
* **Removing the Base conda**:  The base environment cannot be removed like other environments because it is part of the core installation of Miniconda or Anaconda. To remove it, you must uninstall Conda entirely.

	- **Step 1**: `conda deactivate`- Deactivate Conda
	- **Step 2:  `rm -rf ~/miniconda3` - Remove the Conda installation directory
	- **Step 3: Clean shell configuration**
		- `nano ~/.bashrc` - open 
		- Remove lines like:

		 \>\>\> conda initialize \>\>\> <br> 			
			... <br> 
		 \<\<\< conda initialize \<\<\<
		 - `source ~/.bashrc`: Apply Changes


## 13.4 GROMACS Local Installation
For the local machine  which is WSL2. We utilize the package manager. 
* `sudo apt-get update && sudo apt-get install gromacs`

This method ensures that dependencies are handled automatically and provides a stable version of GROMACS available in the Ubuntu package repository.

## 13.5 High Performance Computing Setup

### 13.5.1 Requesting Account in SIU BigDawg
BigDawg, SIUC's HPC cluster, is available at no cost to faculty, researchers, and students. However, student access requires faculty or researcher supervision. To gain access to SIU's HPC resources, follow the official instructions at:
<a href="https://oit.siu.edu/rcc/access.php" target="_blank"> Request access to SIU's BigDawg </a>.  For further inquiries, contact research computing:

* Phone: 618-536-2438
* Email: research-computing@siu.edu

After successfully gaining access to the HPC system, we will learn how to install and configure essesntial packages for *in-silico*using Miniconda on the cluster. This includes installing GROMACS and its required dependencies, such as FFTW and MPI, to enable efficient parallel processing. 

### 13.5.2 Connecting to the SIU BigDawg
To connect to the BigDawg cluster and perform remote computing from a Windows system, we will use **MobaXterm** or **Command Prompt**.

<figure class="half-width">
	<img src="/assets/img/Biophysics/Chapter-13/C13_1.png" alt="Description of the image" style= "width: 100%;"> 
	<figcaption>Overview of Cisco Secure Client connection</figcaption>
</figure>

1. **Connect Cisco Secure Client**
* open **Cisco Secure Client (VPN)**
* Connect to (see Figure 2): `private.siu.edu/bigdawg`
* Use your SIU credentials:
    * Username: `siu85xxxxx or email@siu.edu`
    * Password : `xxxx`

**Connecting BigDawg via SSH**: Once connected to the VPN, use **MobaXterm** or **SSH** to access the cluster
* `ssh siu853xxx@bigdawg.research.siu.edu` 

**Recommended Working Directory**: It is recommended to work in the /scratch/siu85xxxxx directory, as it provides more storage compared to /home/siu85xxxxx. 
* `cd /scratch/siu85xxxxx`
     
3. **Useful Commands for Working Bash Shell**

**File Transfer to and from the Cluster:** If you are using **MobaXterm**, you can easily transfer files between your local computer and the cluster using drag and drop via the built-in SFTP panel.

If you are using **Command Prompt**, PowerShell, or a Linux/macOS terminal, file transfers are done using the `scp` (secure copy) command.

* `scp <filename> siu85xxxxx@bigdawg.research.siu.edu:/scratch/siu85xxxxx/1AKI/`-
Copy a File from Local Computer to BigDawg
* `scp siu85xxxxx@bigdawg.research.siu.edu:/scratch/siu85xxxxx/3HTB ./local_directory/` - Copy a File from BigDawg to Local Computer

> **Notes:** 
* Replace siu85xxxxx with your actual SIU user ID.
* /scratch is typically used for large, temporary simulation data.
* ./local_directory/ refers to a folder on your local machine.
{: .prompt-info}

To learn more about SLURM, please visit:  <a href="https://soc.siu.edu/_common/documents/cs/user_guide.pdf" target="_blank"> User Guide for SLURM Scheduler </a>.

To learn more about Linux usage in HPC environments, please visit:
<a href="https://hpc-wiki.info/hpc/Introduction_to_Linux_in_HPC" target="_blank"> Introduction to Linux in HPC </a>.

### 13.5.3 Installing GROMACS on SIU BigDawg
Many clusters already provide GROMACS via environment modules: 
* `module avail` : to display available modules.
* `load module package_name` such as gromacs-2018-gcc...,
* `which gmx_gmi` 

If gromacs is not available, Miniconda is the safest user-level method to  **Install GROMACS** using miniconda.

To install Gromacs 2026 using the **Miniconda**, we need to have conda environment with python 3.10. If you don't have an conda environment with python 3.10, you need  create the conda environment `gromacs_env` using the instructions describe in section **13.3.3 Conda Environment**. After that, activate conda environment that have python 3.10, 

* `conda activate gromacs_env` - Activate envirnment that we create with python 3.10


Many scientific packages are available through the **conda-forge** repository.
Add the `conda-forge` channel. To install Gromacs 2026, we use the **conda-forge** repository:
* `conda config --add channels conda-forge`
* `conda config --set channel_priority strict`

**Option A** — Serial / OpenMP version (most stable)
* `conda install gromacs` -This installs GROMACS and all required dependencies automatically.

This installs:
- GROMACS
- FFTW
- OpenMP support
- CPU-only binaries

Recommended for beginners and teaching.

**Option B** — MPI-enabled GROMACS (for parallel jobs)
* `conda install gromacs mpi4py openmpi`

This enables:
* gmx_mpi
* domain decomposition across nodes
Verify:
* `which gmx`
* `which gmx_mpi`
* `gmx --version` - To verify installation

If you gromacs is install properly,  you need get the out of Gromacs 2026.

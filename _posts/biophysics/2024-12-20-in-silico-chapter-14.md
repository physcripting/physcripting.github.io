---
title: "Chapter 14: System Configuration for In-Silico"
author: [PSK, SHM]
date: 2025-03-11 14:10:00 +0800
categories: [eDocuments, Introduction to Biophysics of Biomolecules]
math: true
render_with_liquid: false
---

This chapter provides step-by-step instructions for installing Linux (Ubuntu) on Windows using WSL2, accessing the SIUC BigDawg supercomputer, installing and configuring GROMACS for molecular dynamics simulations, and running simulations with the installed software. For detailed information, visit the  <a href="https://oit.siu.edu/rcc/" target="_blank"> SIUC Research Computing and Cyberinfrastructure </a>  and read the official user documentation.

## 14.1 Introduction
In-silico studies, particularly molecular dynamics (MD) simulations, are computationally intensive and are predominantly performed on Linux-based operating systems. Linux offers a robust ecosystem of **open-source scientific software**, **powerful command-line tools**, and optimized **high-performance computing (HPC) environments**, making it the preferred choice for large-scale MD simulations.

Many widely used MD software packages, including GROMACS (GROningen MAchine for Chemical Simulations), are primarily developed and maintained primarily for Linux. This chapter provides a comprehensive guide for setting up a suitable environment for MD simulations, covering both **local (Windows + WSL2)** and **HPC-based (BigDawg)**  approaches.

We begin the chapter by discussing the installation of the Ubuntu Linux distribution on a Windows system using **Windows Subsystem for Linux 2 (WSL2)**. **WSL2** is a lightweight virtualization layer that runs a full Linux kernel within Windows, offering:
* Improved system compatibility for Linux applications.
* Seamless execution of Linux-based MD tools alongside Windows applications.

With WSL2, users leverage the familiar Windows environment while gaining access to the powerful tools and flexibility of Linux.

Once WSL2 is configured, we will guide you through installing essential *in-silico* packges, including: 
* <a href="https://www.gromacs.org/" target="_blank">  GROMACS</a>, a leading molecular dynamics package used for simulating biomolecular interactions.
* <a href="https://mmb.irbbarcelona.org/biobb/" target="_blank">  <b> BioExcel Building Blocks (biobb)</b> </a>, a workflow tool that simplifies the setup and execution of MD simulations in GROMACS. 

On local machines, GROMACS will be compiled and installed directly within the Linux environment, allowing easy installation and configuration. We will cover necessary dependencies and outline best practices for a successful installation.

While local installations are sufficient for small to medium-scale MD simulations, large-scale molecular simulations require significant computational power. To support such high-demand simulations, we will utilize <a href="https://oit.siu.edu/rcc/bigdawg-specifications.php" target="_blank"> SIU’s BigDawg HPC cluster </a>. BigDawg is an HPC cluster at Southern Illinois University Carbondale (SIUC), designed for computationally intensive research across multiple scientific disciplines. It provides High-speed parallel processing for accelerating simulations, optimized resoure allocation for efficient computing performace, and scalability for running extensive biomolecular studies.

To simplify software installation on BigDawg, we will use <a href="https://www.anaconda.com/docs/getting-started/miniconda/main" target="_blank"> Miniconda </a>, a lightweight package and environment manager. **Miniconda** helps manage software dependencies efficiently and ensures compatibility across different computing environments. This chapter will provide instructions for accessing and configuring BigDawg for molecular simulations, step-by-step guidance on installing GROMACS and dependencies, and best practices for job script setup, resource allocation, and parallel execution using SLURM, and the workload manager for HPC environments. 

By the end of this chapter, you will have a fully configured MD simulation environment, both on **local Windows/Linux systems via WSL2** and on **SIU’s BigDawg HPC cluster**. The upcoming sections provide detailed step-by-step instructions for:
* Installing, configurating, and executing of *in-silico* simulation packages. 
* Transitioning seamlessly between local and HPC environments.
* Optimizing simulation performance for high-efficiency molecular modeling.

This guide ensures that researchers and students can efficiently run MD simulations for cutting-edge biomolecular research, from small-scale exploratory studies to large-scale computational investigations.

Before you begin, request access to the BigDawg HPC [(as described in the first section of HPC Setup)](#146-hpc-setup) since it will take time for you to get accepted. After that, contine to setup your local environment with WSL2.

## 14.2. WSL2
This section provides a detailed guide on installing Ubuntu (A popular Linux distribution) on Windows using **Windows Subsystem for Linux 2 (WSL2)**. WSL2 is a full Linux kernel implementation that runs within a lightweight, virtualized environment on Windows, offering near-native performance for Linux applications. For official documentation, system requirements, and troubleshooting, refer to the  <a href="https://docs.microsoft.com/en-us/windows/wsl/" target="_blank"> Microsoft Windows Subsystem for Linux Documentation </a> .

In many cases you will find yourself needing to a linux command line to manuever around your files and utilize important software. As such, you can install Windows Terminal, an official application designed to handle WSL and all the other command lines you may interact with on your windows machine. You can get all these tools directly from the **Microsoft Store**:

[**Windows Terminal**](https://apps.microsoft.com/detail/9n0dx20hk701?hl=en-US&gl=US){:target="_blank"} (link, press view in store, if you get a prompt, click `Open Microsoft Store`, and then click the blue `Get` button to install) 

[**Ubuntu**](https://apps.microsoft.com/detail/9pdxgncfsczv?hl=en-US&gl=US){:target="_blank"} (same as instructions as Windows Terminal)

Once these are both installed, open up the newly installed Ubuntu app. You should now see some messages appear to set up your user info.

![Terminal after install WSL2 & setting up](/assets/img/Biophysics/Chapter-14/wslnew.png)

> If you aren't too familiar with how to use a linux command line, consult [any of the beginner resources here](https://researchcomputing.princeton.edu/education/external-online-resources/linux) to learn the essential commands.
{: .prompt-tip}


We can access your Windows files from within WSL2 using the following command:

```bash
cd /mnt/c
```

You can also use Windows applications from the terminal to open files to edit:

```bash
notepad.exe {{text file in PWD}}
```


You can also view and edit Linux files directly in Windows File Explorer by navigating to:
* `\\wsl.localhost\` - This provides native access to WSL2 files without requiring SSH or third-party tools

> Tip: Store large datasets inside the WSL filesystem (/home/user/) instead of Windows (/mnt/c/) to avoid performance issues.
{: .prompt-tip}

## 14.3 Miniconda
Miniconda is an open-source software distribution that provides a minimal installation of Anaconda, including Conda, Python, and essential packages they depend on. It is lightweight and allows users to manage environments efficiently. More information can be found on the official <a href="https://www.anaconda.com/docs/getting-started/miniconda/main" target="_blank"> Miniconda documentaion</a>.

### 14.3.1 Installation and Setup
Using Conda simplifies package management, especially for software like Biobb, which has multiple dependencies. Miniconda can be installed without root privileges, making it accessible for personal and HPC environments. Below are the steps for installing Miniconda on Linux, including WSL2. A similar approach can be followed for installing software on SIU BigDawg HPC.

> To save yourself from having to manually run all of these commands, you can run the following command:
```bash
bash <(curl -sSL https://raw.githubusercontent.com/safan41/gromacs-setup/refs/heads/main/setup.sh)
```
If you do this, you can disregard the next 3 sections and skip to [Verifying Environment](#145-verifying-environment).
{: .prompt-tip}

1. **Download & Install Miniconda**
Use curl to download the latest Miniconda installer, run it in bash, follow the prompts, and accept the license agreement.
```bash
bash <(curl -sSL conda.sh)
```
2. **Initialize Conda**
After installation, initialize Conda:
* `conda init`
Restart your terminal or manually reload the shell configuration:
* `source ~/.bashrc`
3. **Verify Installation**
Check if Conda is installed correctly
* `conda --version`
Expected output like `conda 23.x.x`

### 14.3.2 **Working in Conda Envirnment**
Conda allows you to create isolated environments for different projects, making package and dependency management more efficient and conflict-free.
1. **Checking Installed Packages**
* `conda list` - to list all installed packages in the current environment
2. **Creating and Managing Environments**
The following describe how to create Conda enviorment with different configurations. 
* `conda create -n biobb_env python=3.10` - This creates a new environment named biobb_env with Python 3.10 installed. Note: `conda create -n biobb_env` creates the environment using the latest available version of Python. We can create an envionment and install additional packages during creation such as `conda create -n biobb_env python=3.10 numpy pandas`,this sets up biobb_env with Python 3.10 and installs both numpy and pandas.

3. **Activate An Environment**
* `conda env list` - List all the conda environments.
* `conda activate biobb_env` - Activate specific envirnment: **biobb**.
* `conda activate` - Switch back to the baes (default) environment.

**Installing Specific Packages in an Existing Environment**
* `conda install --name biobb_env -c conda-forge gcc`
* `conda install --name biobb_env -c conda-forge cmake` - To install latest version of cmake. 
* `conda install cmake=3.19.4` - To install old version of cmake in current conda environment.




## 14.3 GROMACS Local Install 
In this section, we will guide you through the installation of GROMACS on the Windows operating system using the Windows Subsystem for Linux (WSL). We are going to install it using 
the package manager. This is the easiest method, where GROMACS can be installed with the command
```bash
sudo apt-get update && sudo apt-get install gromacs
```
This method ensures that dependencies are handled automatically and provides a stable version of GROMACS available in the Ubuntu package repository.

Now gromacs is ready for MD siumlation. 


## 14.4 Biobb Installation
This section provides the guidences to install **biobb** in a WSL2 environment using Conda and set it up to run in JupyterLab, which makes it easier to document and visualize results. If you haven’t set up WSL2 yet, follow the instructions in **Section 13.3.1: Windows Subsystem for Linux 2 (WSL2)**.

Because some of the necessary packages doesn't support after python 3.10, we will use conda environment run the biobb in python 3.10. 

* `conda create -n biobb_env python=3.10` - create a new environment for biobb.
* `conda activate biobb_env` - activate the enviroment to install **biobb**.

First, we will install jupyter lab in `biobb_env` and configure it for easy launch. 
* `conda install -c conda-forge jupyterlab` - With the environment activated, install Jupyter Lab.
* `jupyter lab --no-browser --ip=0.0.0.0` - Start the jupyter lab after installing.

The open  your browser in **Windows** and type:
* `http://localhost:8888` - start the jupyter lab notebook at port 8888.

> * If port 8888 is in use, start Jupyter on a different port:: `jupyter lab --no-browser --ip=0.0.0.0 --port=9999`
* Typically, Jupyter lab will ask for a password or token, you can retrieve the correct token by running:
	* `jupyter server list` - This  outputs something like:  `Currently running servers: http://127.0.0.1:8888/?token=xxxxxx123456 :: /home/user`. Copy the token from the URL (token=xxxxxx123456) and use it to log in
{: .prompt-info}

We can simplify the jupyter lab launch through:
* `vi ~/.bashrc` - Open using vi editor
* `Esc` then `:i` - To switch vi editor to insert mode
* Enter `alias jlab="jupyter lab --no-browser --ip=0.0.0.0"` at the end of the file.
* `Esc` then `:wq` - To save and exist vi editor.

**Reintialize the `.bashrc`** through one of the following step: 
1. Close the terminal and restart OR
2. `source ~/.bashrc`: Run this in the command prompt. After that , reactivate the `'biobb_env` through run `conda activate biobb_env` in the command prompt.


* `jlab` - This starts Jupyter Lab.

If Jupyter Lab is asking for a password or token, you can retrieve the correct token by running:
* `jupyter server list` - This  outputs something like:  `Currently running servers: http://127.0.0.1:8888/?token=xxxxxx123456 :: /home/user`. Copy the token from the URL (token=xxxxxx123456) and use it to log in

If you don’t want to enter a token every time, disable token authentication by running:
* `jupyter lab --NotebookApp.token='' --NotebookApp.password=''`

Or configure it permanently by running:
* `jupyter lab --generate-config`
* `echo "c.NotebookApp.token = ''" >> ~/.jupyter/jupyter_lab_config.py`
* `echo "c.NotebookApp.password = ''" >> ~/.jupyter/jupyter_lab_config.py`
* `jlab` - To access the jupyter in windows browser. 

To install **biobb** in conda environment, All the dependencies must be installed separately. Follow these steps to install required dependencies:

* `conda activate biobb_env`
* `conda install -c bioconda "biobb_io==5.0.1"` 
* `conda install -c conda-forge biopython=1.79 -y` - biopython is required to install before installing biobb_model.
* `conda install -c bioconda biobb_model>=5.0.0 -y` 
* `conda install -c conda-forge gromacs=2022.2` - To install gromacs 2022.2
* `conda install -c bioconda biobb_gromacs>=5.0.0 -y` - To install biobb_gromacs
* `conda install -c conda-forge ambertools=22.5 -y` - Need to install AmberTools from conda-forge before installing biobb_analysis. Ambertools is required for MMPBSA
* `conda install -c bioconda biobb_analysis>=5.0.1 -y`
* `conda install -c bioconda "biobb_amber>=5.0.4"` - biobb_amber allows setup and simulation of atomistic MD simulations using AMBER MD package and its associated AMBER tools.

We also install additional tools for visualization:

* `conda install -c conda-forge simpletraj -y` - To install simpletraj,  Lightweight coordinate-only trajectory reader based on code from GROMACS, MDAnalysis and VMD.
* `conda install -c conda-forge nglview -y`- To install nglview, Jupyter/IPython widget to interactively view molecular structures and trajectories in notebooks.

* `conda list` - to check installed packages.


## 14.5 Verifying Environment

Now, Biobb and all necessary dependencies should be installed.

To verify, run `jlab` in a terminal. In a few seconds, your terminal should look something like this:

![Output of `jlab`](/assets/img/Biophysics/Chapter-14/jlab1.png)

Ctrl+Click the link where it says "Jupyter Server (version number) is running at:" to open it in your browser. This should open a jupyterlab instance with all the modules needed installed.

![Output of `jlab` scrolled down, with link highlighted wih red arrow](/assets/img/Biophysics/Chapter-14/jlab2.png)

Download [this python notebook file]() and upload it into JupyterLab using the file menu at the top left corner.

Run the first cell in the notebook by pressing the play button. Your output should look like this:

> If your output does not look like this, reread each step of this page to ensure you didn't miss any commands. If you're still having trouble consult [the FAQ](/about)
{: .prompt-danger}

Congratulations, you've completed the local environment setup!


## 14.6 HPC Setup

### 14.6.1 Requesting Account in SIU BigDawg
BigDawg, Southern Illinois University’s (SIU) High-Performance Computing (HPC) cluster, is available at no cost to faculty, researchers, and students. However, student access requires faculty or researcher supervision. All research projects, including computational science, data analysis, and simulations, are eligible for use, with no strict time restrictions on computational jobs, though fair-use policies may apply. To gain access to SIU's HPC resources, follow the official instructions at:
<a href="https://oit.siu.edu/rcc/bigdawg-request-access.php" target="_blank"> Request access to SIU's BigDawg </a>.  For further inquiries, contact research computing:
* Phone: 618-536-2438
* Email: research-computing@siu.edu

After successfully setting up WSL2 and getting access to HPC computer, we will install essential packages such as molecular dynamics (MD) simulations, including GROMACS and its dependencies (e.g., FFTW and MPI for parallel processing). the process of installing and configuring MD software on the cluster. This will include job script setup, resource allocation, and optimization techniques for large-scale simulations.

### 14.6.2 Connecting to the SIU BigDawg
To connect to the BigDawg cluster and perform remote computing from a Windows system, we will use **MobaXterm** or **WinSCP**.
1. **Connect Cisco Secure Client**
* open **Cisco Secure Client (VPN)**
* Connect to: `private.siu.edu/bigdawg`
* Use your SIU credentials:
    * Username: `siu85xxxxx or xxx@siu.edu`
    * Password : `xxxx`

2. **SSH into BigDawg**

Once connected to the VPN, use SSH to access the cluster
* `ssh siu853xxx@bigdawg.research.siu.edu` 

**Recommended Working Directory**: It is recommended to work in the /scratch/siu85xxxxx directory, as it provides more storage compared to /home/siu85xxxxx. 
* `cd /scratch/siu85xxxxx`
     
3. **Useful Commands for Working Bash Shell**
    
Copying a File from Local Computer to BigDawg
* `scp filename siu85xxxxx@bigdawg.research.siu.edu:/scratch/siu85xxxxx/1AKI/`
Copying a File from BigDawg to Local Computer
* `scp siu85xxxxx@bigdawg.research.siu.edu:/scratch/siu85xxxxx/3HTB ./local_directory/` 

### 14.6.3 Installing GROMACS on SIU BigDawg

1. **Miniconda Installation/Setup**
As we do not have the root password in the BigDawg, we are limited to installing new software. We can request BigDawg  admistration to install software however, it may take sometime and it may need to frequent optimization to run the modeling properly.  Because of these limitation, we will create a miniconda enviroment and install the software in the minicond invironment without root password in our local directory. 


2. **Installing GROMACS in miniconda environment**

Gromacs may already in your system which can be check through, 
* `module avail` : to display available modules.
* `load module package_name` such as gromacs-2018-gcc...,
* `which gmx_gmi` 

Download approapriate version of GROMACS for your system. You need check the gcc version in your server and download appropriate GROMACS that can support for that version. Conda has gcc however, GROMACS require system gcc although the GROMACS is installing conda envirnments.  - Before starting to install, get the latest version of C and C++ compilers.  The gcc version can be found through:
* `gcc --version` or
* `which gcc`

Before installing GROMACS, ensure that CMake is installed and check its version using:
* `cmake --version`
If the latest version is required, it can be installed using Miniconda:
* `conda install -c conda-forge cmake`

In Chapter 16, we will use **biobb** to prepare MD simulations using GROMACS. Several tutorials will guide you through this process.
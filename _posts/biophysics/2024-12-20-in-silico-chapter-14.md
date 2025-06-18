---
title: "Chapter 14: System Configuration for In-Silico"
author: [PSK, SHM]
date: 2025-03-11 14:10:00 +0800
categories: [eDocuments, Introduction to Biophysics of Biomolecules]
math: true
render_with_liquid: false
---

This chapter provides step-by-step instructions for installing Linux (Ubuntu) on Windows using WSL2, accessing the SIUC BigDog supercomputer, installing and configuring GROMACS for molecular dynamics simulations, and running simulations with the installed software. For detailed information, visit the  <a href="https://oit.siu.edu/rcc/" target="_blank"> SIUC Research Computing and Cyberingrastructure </a>  and read the official user documentation.

## 14.1 Introduction
In-silico studies, particularly molecular dynamics (MD) simulations, are computationally intensive and are predominantly performed on Linux-based operating systems. Linux offers a robust ecosystem of **open-source scientific software**, **powerful command-line tools**, and optimized **high-performance computing (HPC) environments**, making it the preferred choice for large-scale MD simulations.

Many widely used MD software packages, including GROMACS (GROningen MAchine for Chemical Simulations), are primarily developed and maintained primarily for Linux. This chapter provides a comprehensive guide for setting up a suitable environment for MD simulations, covering both **local (Windows + WSL2)** and **HPC-based (BigDwag)**  approaches.

We begin the chapter by discussing the installation of the Ubuntu Linux distribution on a Windows system using **Windows Subsystem for Linux 2 (WSL2)**. **WSL2** is a lightweight virtualization layer that runs a full Linux kernel within Windows, offering:
* Improved system compatibility for Linux applications.
* Seamless execution of Linux-based MD tools alongside Windows applications.

With WSL2, users leverage the familiar Windows environment while gaining access to the powerful tools and flexibility of Linux.

Once WSL2 is configured, we will guide you through installing essential *in-silico* packges, including: 
* <a href="https://www.gromacs.org/" target="_blank">  GROMACS</a>, a leading molecular dynamics package used for simulating biomolecular interactions.
* <a href="https://mmb.irbbarcelona.org/biobb/" target="_blank">  <b> BioExcel Building Blocks (biobb)</b> </a>, a workflow tool that simplifies the setup and execution of MD simulations in GROMACS. 

On local machines, GROMACS will be compiled and installed directly within the Linux environment, allowing easy installation and configuration. We will cover necessary dependencies and outline best practices for a successful installation.

While local installations are sufficient for small to medium-scale MD simulations, large-scale molecular simulations require significant computational power. To support such high-demand simulations, we will utilize <a href="https://oit.siu.edu/rcc/bigdawg-specifications.php" target="_blank"> SIU’s BigDawg HPC cluster </a>. BigDawg is an HPC cluster at Southern Illinois University Carbondale (SIUC), designed for computationally intensive research across multiple scientific disciplines. It provides High-speed parallel processing for accelerating simulations, optimized resoure allocation for efficient computing performace, and scalability for running extensive biomolecular studies.

To simplify software installation on BigDawg, we will use <a href="https://www.anaconda.com/docs/getting-started/miniconda/main" target="_blank"> Miniconda </a>, a lightweight package and environment manager. **Miniconda** helps manage software dependencies efficiently and ensures compatibility across different computing environments. This chapter will provide instructions for accessing and configuring BigDwag for molecular simulations, step-by-step guidance on installing GROMACS and dependencies, and best practices for job script setup, resource allocation, and parallel execution using SLURM, and the workload manager for HPC environments. 

By the end of this chapter, you will have a fully configured MD simulation environment, both on **local Windows/Linux systems via WSL2** and on **SIU’s BigDawg HPC cluster**. The upcoming sections provide detailed step-by-step instructions for:
* Installing, configurating, and executing of *in-silico* simulation packages. 
* Transitioning seamlessly between local and HPC environments.
* Optimizing simulation performance for high-efficiency molecular modeling.

This guide ensures that researchers and students can efficiently run MD simulations for cutting-edge biomolecular research, from small-scale exploratory studies to large-scale computational investigations.

## 14.2. Windows Subsystem for Linux 2 (WSL2)
This section provides a detailed guide on installing Linux (Ubuntu distribution) on Windows using **Windows Subsystem for Linux 2 (WSL2)**. WSL2 is a full Linux kernel implementation that runs within a lightweight, virtualized environment on Windows, offering near-native performance for Linux applications. Unlike WSL1, WSL2 uses a real Linux kernel via a virtual machine interface, providing better system compatibility and improved file system performance. For official documentation, system requirements, and troubleshooting, refer to the  <a href="https://docs.microsoft.com/en-us/windows/wsl/" target="_blank"> Microsoft Windows Subsystem for Linux Documentation </a> .

<figure class="half-width">
	<img src="/assets/img/Biophysics/Chapter-14/C14_1.png" alt="Description of the image" style= "width: 100%;"> 
	<figcaption>Enabling required features in the "Turn Windows feature on or off"</figcaption>
</figure>

**A. Configuration for WSL2** 

Before installing the WSL2, we need to enable specific Windows features:
1. Open the `Turn Windows feature on or off` dialog (as shown in Figure 1) 
2. Select the following option :
	* virtual machine platform 
	* windows Hypervisor Platform
	* windows subsystem for linux
3. Click OK and allow the changes to be applied.
4. Restart your computer to complete the process.

Once these features are enabled, we can proceed with installing WSL2 and setting up your preferred Linux distribution.

**B. Installing Linux Distribution**

Before proceeding with installation, we need to check if WSL is available and correctly installed. Open PowerShell and run the following commands:
* `wsl --list --verbose` or `wsl -l -b` - This command lists all installed Linux distributions and indicates whether they are running WSL 1 or WSL 2.
* `wsl --update` - This ensures WSL is updated to the latest version if you have WSL, which includes performance improvements and new features. 

By default, Ubuntu is installed with WSL, but you can choose another distribution if preferred.
* `wsl --list --online` - This command displays all Linux distributions available for installation.
* `wsl --install -d Ubuntu-22.04` - This command installs Ubuntu-22.04  distribution. Replace Ubuntu-22.04 with your preferred distribution name.

Or you can install Linux distributions directly from the **Microsoft Store**: 
* On "Start up Search" type Microsoft Store.  
* Open Microsoft Store
* Search for your desired Linux distribution (e.g., Ubuntu, Debian, Kali Linux)
* Click Install

**C. Installing WSL and Linux Distribution**

If WSL is not install, you can installed using command in PowerShell, which is mostly recommended. 
* Open PowerShell as Administrator
	* Click Start → search for PowerShell
	* Right-click Windows PowerShell → Select Run as administrator
* `wsl --install` - This command enables required windows features and installs the lastest version of WSL2 and Ubuntu as the defaulty linux distribution.

If WSL is not working properly, you can uninstall and restall. 
* `wsl --uninstall` - This removes WSL and all installed Linux distributions. After removing the WSL, you can reinstall the latest version by running ``wsl --install`.

**Setting WSL 2 as the Default Version**. WSL 2 offers improved performance and better system compatibility. If needed, set it as the default:
* `wsl --set-default-version 2` - To set WSL 2 as default
* `wsl --list --verbose` or `wsl -l -v` - This ensures that all new Linux distributions installed in WSL default to version 2.

**D. Launch Graphical User Interface (GUI) Application**

Before enabling the GUI, update and upgrade the system to ensure all packages are up to date:
* `Sudo apt update` - This update the packages
* `sudo apt -y upgrade` - This upgrade the packages.

Windows 11 natively supports GUI applications in WSL2, allowing us to run Linux applications with graphical interfaces without additional setup. 

**For example**: The following step shows the installation of GUI application `gedit` and launching it.
* `sudo apt install -y gedit`- To sintall a graphical application (e.g., **gedit**) 
* `gedit` -This should open gedit, a simple text editor, in a graphical window. 

**E. XRDP for  Lightweight GUI (XFCE)** 

Instead of launching individual GUI applications, we can install XFCE, a lightweight desktop environment, and use XRDP to access it via Remote Desktop (RDP). XRDP is an open-source RDP server that allows Windows to connect to your Linux GUI.

* `sudo apt install -y xrdp`  - This command installs XRDP 

After installation, XRDP should start automatically. You can verify this with
* `sudo systemctl status xrdp` 
* `sudo systemctl start xrdp` - If it is not running, start it manually:

**Install and Configure XFCE Desktop Environment**

XFCE is a lightweight desktop environment and works well with WSL2. More information about the xfce2 is available at <a href="https://autoize.com/xfce4-desktop-environment-and-x-server-for-ubuntu-on-wsl-2/" target="_blank"> Xfce4 Desktop Environment and X Server for Ubuntu on WSL 2 </a>

* `sudo apt install -y xfce4` -To install XFCE. 
* `dpkg -l | grep xfce4-session` - To verify that XFCE is installed, check for the xfce4-session package. If XFCE installed, you should see an output entry like `ii  xfce4-session  4.x.x  amd64  Xfce4 Session Manager`

* `sudo apt install -y xfce4-session xfce4-goodies` -For additional features (themes, plugins, and utilities). This adds useful plugins and themes for a better desktop experience.
* `sudo cp /etc/xrdp/xrdp.ini /etc/xrdp/xrdp.ini.bak`- Backup the XRDP configuration file (in case changes need to be reverted)
* `sudo sed -i 's/3389/3390/g' /etc/xrdp/xrdp.ini`- Change default XRDP port (optional but recommended). By default, XRDP runs on prot 3389, which may conflixt with Windows RDP. To change 3389 → 3390, run this command.
* `echo "xfce4-session" > ~/.xsession` - Creates or overwrites the *~/.xsession* file, setting xfce4-session as the default session for XRDP. This ensures that the XFCE desktop environment starts when connecting via Remote Desktop.

**Modify the XRDP Startup Script**
For this, we need to modify the *startwm.sh*. We will use vi editor. 
* `sudo vi /etc/xrdp/startwm.sh`  - Open the startwm.sh file using the vi editor with administrator privileges. 

Locate and comment the following two lines (last two lines); for more details see Figure 2. 
* `test -x /etc/X11/Xsession && exec /etc/X11/Xsession`
* `exec /bin/sh /etc/X11/Xsession`


<figure class="half-width">
	<img src="/assets/img/Biophysics/Chapter-14/C14_2.png" alt="Description of the image" style= "width: 100%;"> 
	<figcaption>Typical "/etc/xrdp/startwm.sh"</figcaption>
</figure>

Then, add the following two lines to ensure that XRDP starts XFCE as shown in Figure 2: 
* `xfce4-session`
* `startxfce4`


Alternative method is using the following commands:
* `echo "xfce4" | sudo tee -a /etc/xrdp/startwm.sh`
* `echo "startxfce4" | sudo tee -a /etc/xrdp/startwm.sh`

Restart the XRDP service for the changes to take effect:
* `sudo systemctl restart xrdp`-To restrat XRDP
* `sudo systemctl status xrdp` - To  check if XRDP is running


**Connect via Windows Remote Desktop**
<figure class="half-width">
	<img src="/assets/img/Biophysics/Chapter-14/C14_3.png" alt="Description of the image" style= "width: 100%;"> 
	<figcaption>Example of configured "/etc/xrdp/startwm.sh"</figcaption>
</figure>

Connect via **Windows Remote Desktop**

Open Remote Desktop Connection on Windows (mstsc.exe).
Enter localhost:3390 (or localhost:3389 if the port wasn’t changed).
Log in using your Linux username and password.
Once connected, you should see the XFCE desktop environment running inside WSL2!



* Open `Remote Desktop Connection` on Windows or `Win + R`, type `mstsc`, press `Enter`.

* Enter `localhost:3390`  or `127.0.0.1:3390`  and click connect and login in using your WSL username and password (as shown in Figure).  Use `localhost:3389` if the port wasn’t changed.

When you log in using WSL username and password, XFCE should now load within the remote desktop session. 

> Before launching Remote Desktop Connection, ensure that XRDP is running: 
* `sudo systemctl start xrdp`  - To start the XRDP 
* `sudo systemctl status xrdp` - To check XRDP status
{: .prompt-warning}


<figure class="half-width">
	<img src="/assets/img/Biophysics/Chapter-14/C14_4.png" alt="Description of the image" style= "width: 100%;"> 
	<figcaption>Screenshot showing how to disable lock screen, hibernate, and suspend settings</figcaption>
</figure>

After installing the GUI, it is recommended to disable certain power management settings (e.g., `lock screen`, `hibernation`, and `suspend`) to prevent unexpected disconnects when using Remote Desktop Connection (RDP). We can do through: 

1. Right-click your username in the system settings.
2. Select "Properties".
3. Unselect the  `lock screen`, `hibernate`, and `Suspend` as shown in the figure.

We can access your Windows files from within WSL2 using the following command:
* `cd/mnt/c`

We can view and edit Linux files directly in Windows File Explorer by navigating to:
* `\\wsl.localhost\` - This provides native access to WSL2 files without requiring SSH or third-party tools

> Tip: Store large datasets inside the WSL filesystem (/home/user/) instead of Windows (/mnt/c/) to avoid performance issues.
{: .prompt-tip}

## 14.3 Miniconda
Miniconda is an open-source software distribution that provides a minimal installation of Anaconda, including Conda, Python, and essential packages they depend on. It is lightweight and allows users to manage environments efficiently. More information can be found on the official <a href="https://www.anaconda.com/docs/getting-started/miniconda/main" target="_blank"> Miniconda documentaion</a>.

### 14.3.1 Installtion and Setup
Using Conda simplifies package management, especially for software like Biobb, which has multiple dependencies. Miniconda can be installed without root privileges, making it accessible for personal and HPC environments. Below are the steps for installing Miniconda on Linux, including WSL2. A similar approach can be followed for installing software on SIU BigDawg HPC.

1. **Download Miniconda**
Use wget or curl to download the latest Miniconda installer
* `wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh`
* `curl -o ~/miniconda.sh https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh` - Download Miniconda installer in your working directory
2. **Install Miniconda**
Run the installer, follow the prompts, and accept the license agreement:
* `bash ~/miniconda.sh `
3. **Initialize Conda**
After installation, initialize Conda:
* `conda init`
Restart your terminal or manually reload the shell configuration:
* `source ~/.bashrc`
4. **Verify Installation**
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

**Deactivate An Environment**
* `conda deactivate`

3. **Removing and Updating Packages**

* `conda remove cmake` - Removing cmake
* `conda update -n base conda` -  To update the conda


4. **(Optional)Disable Auto Activation of Base Environment**
If you don’t want Conda to activate the (base) environment every time the terminal starts, disable it with:
* `conda config --set auto_activate_base False`

5. **Removing Miniconda**
To uninstall Miniconda, remove its directory:
* `rm -rf ~/minconda3`

Then, remove the Miniconda path from `.bashrc` or `.bash_profile` by deleting the following line:
* `export PATH="/home/username/miniconda3/bin:$PATH"`

Reload the shell configuration: 
* `source ~/.bashrc` 


## 14.3 Installing GROMACS in Local Computer 
In this section, we will guide you through the installation of GROMACS on the Windows operating system using the Windows Subsystem for Linux (WSL). GROMACS can be installed through two primary methods:

> Using Anaconda or Miniconda can cause issues when installing GROMACS, particularly related to AVX2 compatibility. If you see a login prompt with "`(base)-bash-$`", it indicates that the Conda environment is active, which may interfere with the installation. To avoid potential conflicts, it is recommended to disable conda (mininconda)  environment, and then proceed with the GROMACS installation (unless installing via Miniconda).
To disable Conda’s base environment before installing GROMACS, run this command then relaunch new bash. Or deactivate and install the GROMACS
* `conda config --set auto_activate_base False` - disable start bash with conda environment.   
* `conda deactivate` - To deactivate conda environment.
{: .prompt-warning}

1. **Using the package manager** – This is the easiest method, where GROMACS can be installed with the command
* `sudo apt-get update && sudo apt-get install gromacs`
This method ensures that dependencies are handled automatically and provides a stable version of GROMACS available in the Ubuntu package repository.
2. **Manual installation** – This method involves downloading and compiling GROMACS from the official source. It allows for greater customization, such as enabling GPU acceleration or specific compiler optimizations. The steps include:
* Installing dependencies (e.g., CMake, FFTW, and MPI)
* Downloading the latest GROMACS source code
* Configuring, compiling, and installing GROMACS

GROMACS can be install conda environment using miniconda or directly. We will look installation directly. Instrction for installing in conda environment is discuss at section **14.4.3 Installing GROMACS on SIU BigDwag**.  Similar approach for installing gromacs in conda environment using miniconda.

We will install specific version, GROMACS  2022.6, for additional instruction, refer at  <a href="https://manual.gromacs.org/2022.6/install-guide/index.html" target="_blank"> GROMACS Installation Guide</a>.
Check the gcc version , recommend to have latest verions of gcc
* `gcc --version`

Check that we have CMake version 3.16.3 or later, using
* `cmake --version`
If you don't have cmake, install using
* `sudo apt install cmake`
Follow the sequence of commands to install GROMACS version 2022.6
* `tar xfz gromacs-2022.6.tar.gz`
* `cd gromacs-2022.6`
* `mkdir build`
* `cd build`
* `cmake .. -DGMX_BUILD_OWN_FFTW=ON -DREGRESSIONTEST_DOWNLOAD=ON` - download and build prerequisite FFT library FFT library  followed by GROMACS. If you alrady have FFTW installed, you can remove that argument. include `-DCMAKE_INSTALL_PREFIX=xxx` to install GROMACS to a non-stardard location (default `/usr/local/gromacs`)
* `make`
* `make check`
* `sudo make install`
* `source /usr/local/gromacs/bin/GMXRC`
* `gmx --help`- This will show installed gromacs version like `GROMACS -gmx, 2022.6` if everything went well. 

Now gromacs is ready for MD siumlation. 
## 14.4 Configuration Account in HPC 

### 14.4.1 Requesting Account in SIU BigDawg
BigDawg, Southern Illinois University’s (SIU) High-Performance Computing (HPC) cluster, is available at no cost to faculty, researchers, and students. However, student access requires faculty or researcher supervision. All research projects, including computational science, data analysis, and simulations, are eligible for use, with no strict time restrictions on computational jobs, though fair-use policies may apply. To gain access to SIU's HPC resources, follow the official instructions at:
<a href="https://oit.siu.edu/rcc/bigdawg-request-access.php" target="_blank"> Request access to SIU's BigDwag </a>.  For further inquiries, contact research computing:
* Phone: 618-536-2438
* Email: research-computing@siu.edu

After successfully setting up WSL2 and getting access to HPC computer, we will install essential packages such as molecular dynamics (MD) simulations, including GROMACS and its dependencies (e.g., FFTW and MPI for parallel processing). the process of installing and configuring MD software on the cluster. This will include job script setup, resource allocation, and optimization techniques for large-scale simulations.

### 14.4.2 Connecting to the SIU BigDawg
To connect to the BigDawg cluster and perform remote computing from a Windows system, we will use **MobaXterm** or **WinSCP**.
1. **Connect Cisco Secure Client**
* open **Cisco Secure Client (VPN)**
* Connect to: `private.siu.edu/bigdawg`
* Use your SIU credentials:
    * Username: `siu85xxxxx or xxx@siu.edu`
    * Password : `xxxx`

2. **SSH into BigDwag**

Once connected to the VPN, use SSH to access the cluster
* `ssh siu853xxx@bigdawg.research.siu.edu` 

**Recommended Working Directory**: It is recommended to work in the /scratch/siu85xxxxx directory, as it provides more storage compared to /home/siu85xxxxx. 
* `cd /scratch/siu85xxxxx`
     
3. **Useful Commands for Working Bash Shell**
    
Copying a File from Local Computer to BigDawg
* `scp filename siu85xxxxx@bigdawg.research.siu.edu:/scratch/siu85xxxxx/1AKI/`
Copying a File from BigDawg to Local Computer
* `scp siu85xxxxx@bigdawg.research.siu.edu:/scratch/siu85xxxxx/3HTB ./local_directory/` 

### 14.4.3 Installing GROMACS on SIU BigDawg

1. **Miniconda Installation/Setup**
As we do not have the root password in the BigDwag, we are limited to installing new software. We can request BigDwag  admistration to install software however, it may take sometime and it may need to frequent optimization to run the modeling properly.  Because of these limitation, we will create a miniconda enviroment and install the software in the minicond invironment without root password in our local directory. 


2. **Installing GROMACS in miniconda environment**

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

## 14.5 Biobb Installation
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

Now, Biobb and all necessary dependencies are installed. In Chapter 16, we will use **biobb** to prepare MD simulations using GROMACS. Several tutorials will guide you through this process.
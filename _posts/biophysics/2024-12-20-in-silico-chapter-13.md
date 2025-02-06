---
title: "Chapter 13: UCSF ChimeraX"
author: PSK
date: 2025-01-30 14:10:00 +0800
categories: [eDocuments, Introduction to Biophysics of Biomolecules]
math: true
render_with_liquid: false
---

Understanding the three-dimensional structures of biomolecules is essential for advancing our knowledge in diverse fields—from drug discovery to the computational modeling of complex biological processes.  In this chapter, we introduce UCSF ChimeraX, a state-of-the-art visualization tool that transforms how researchers explore and analyze biomolecular structures.

## 1.1 Introduction
UCSF ChimeraX (commonly referred to as ChimeraX) is the next-generation molecular visualization program developed by the UCSF Resource for Biocomputing, Visualization, and Informatics (RBVI). It enables interactive visualization and analysis of molecular structures, density maps, molecular dynamics trajectories, and sequence alignments. ChimeraX is the successor to UCSF Chimera, which is no longer actively developed following the conclusion of its funding in 2016.

One of the key strengths of ChimeraX is its interoperability with a variety of computational tools, making it an invaluable resource for diverse applications. For example:
* **MODELLER** – Enables comparative protein structure modeling.
* **AlphaFold** – Provides deep-learning-based protein structure prediction.
* **AutoDock (ViewDockX)** –  Facilitates molecular docking and ligand-binding analysis.

In this chapter, we will explore how to leverage ChimeraX's advanced functionalities to gain insights into biomolecular structures and dynamics, and and prepare structures for molecular dynamics simulations, furthering our understanding of biological processes at the molecular level.

## 1.2 Overview of ChmieraX 
Figure-1 shows the basic overview of ChimeraX, which is a highly customizable interface, allowing you to arrange and configure these elements to suit your preferences. The ChimeraX front window primarily consists of:
<figure>
	<img src="/assets/img/Biophysics/Chapter-13/C13_1.png" alt="Description of the image" style= "width: 100%;"> 
	<figcaption>Standard overview of ChemiraX</figcaption>
</figure>

3D Graphics Window: This is the central area where you visualize and interact with 3D molecular structures.
* **Toolbars**: Located at the top, these provide quick access to common commands and tools.
* **Panels**: These are detachable windows that offer various functionalities:
    * **Model Panel**: Displays a list of loaded models and allows for various operations on them.
    * **Command Line**: Enables you to execute commands directly.
    * **Other panels**: Depending on your needs, you might have panels for tools like sequence viewer, surface generation, volume visualization, and more. For example, clicking serquence botton will bring a new window panel below the Model Panel.

    Panels can be easily shown, hidden, and repositioned. They can also be detached (undocked) from the main window and subsequently reinserted (docked). To manage panels:
    * **Dismiss a Panel**: Click the "x" button on its title bar (if docked) or the generic close-window button (if undocked).
    * **Show a Hidden Panel**: Check its name in the bottom section of the Tools menu or in the context menu of any docked panel's title bar.
    * **Undock a Panel**: Click the "rectangles" button on its title bar or drag/double-click its title bar.
    * **Redock a Panel**: Drag or double-click its title bar to insert it back into the main window.
    * **Tab Panels**: Drag a panel to the same area as another to create a tabbed set; clicking a tab brings the corresponding panel to the front.

### 1.2.1 Basic Mouse Controls
In ChimeraX, the basic mouse controls for interacting with molecular structures and 3D visualizations are:
* **Rotation, Translation, and Zooming**
    * Left Mouse Button (Click & Drag) → Rotate the structure
    * Middle Mouse Button (Click & Drag) → Move (translate) the structure
    * Right Mouse Button (Click & Drag) OR Scroll Wheel → Zoom in/out
* **Selection and Picking**
    * Ctrl + Left Click → Select an atom, residue, or molecular component
    * Shift + Ctrl + Left Click → Select multiple items
    * Double Left Click on an Object → Center and zoom in on that object
* Alternative Mouse Modes (for Specific Tools)
    * Alt + Left Click & Drag → Slab clipping (adjust depth of view)
    * Shift + Right Click & Drag → Adjust threshold levels in volume data
    * Ctrl + Mouse Scroll → Adjust contour levels for density maps

We can customize mouse actions via **Tools → General → Mouse Modes**, allowing you to assign different functions to each mouse button.

### 1.2.2 Basic Control of Proteins
In this section, we will explore the basic controls for manipulating proteins using ChimeraX, using Human Deoxyhemoglobin (PDB: 2HHB) as our model structure. The structure consists of **four chains**:
- Alpha chains: Labeled A and C
- Beta chains: Labeled B and D

**Ligands** (Non-Protein Compounds):
- Heme group (HEM)
- Phosphate ion

Experiment with different mouse controls and buttons found under the "Home" and "Molecule Display" tabs and more. Additionally, practice using basic mouse controls (review 1.2.1 Basic Mouse Control) for:  
- Rotation 
- Translation  
- Zooming
- Selection and Picking

> **Note**: If the protein does not contain nucleotides, then nucleoside-related functions will not work in ChimeraX.
 
**Chain and Atom Selection Technique**
* **Hover over an atom**: A pop-up box will display information, e.g., /A BTN 300 S1 (Chain A, Molecule BTN, Atom ID 300, Element Sulfur).
	Select chain A and test the menu options: 
	* Actions > Ribbon > hide 
	* Actions > Atoms/Bonds > ball & stick
	
> **Tip**: Ctl+Shift +click  for selecting multiple atoms
    
**Highlight an entire ligand**:
* Hold Ctrl and left-click on a sulfur atom of the ligand.
* Press the "Up Arrow Key" to expand the selection to the entire ligand.
* Press the "Down Arrow Key" to reduce the selection.

* **Invert selection**: (Now everything except the current selection is highlighted.)
* Press **Ctrl + Left-Click in a blank space** to deselect the current selection:

**Selecting and Color a Residue**: 
* Hover over a residue to see a pop-up with its name, e.g  “A/ TRP 108 CD2". 
* Select the residue by clicking on it.
* Action> Color > silver

Return to the original coloring scheme
* Presets → Original Look

Clearing and Modifying Selections
* Select > Clear Selection (or Ctrl-click in a blank space).
* Select chain A again
* Invert selection: Everything except chain A is now selected.

Depiction Options:
* Tools > Depiction:  Provides various ways to color and visually represent the molecule.  
	
Selection behavior can be adjusted using the **Selection Mode Options**:
- **Replace Mode**: Removes any previous selection and replaces it with a new selection.  
- **Add (+) Mode**:  Adds the new selection to the previously selected atoms.  
- **Intersect Mode**:  Selects only atoms that satisfy **all conditions** (logical AND operation).  
	
Focus on a Selection    
- Actions > Focus:  utomatically zooms into the selected area, bringing it closer within the 3D viewing space. 
	
Adding a Label:
- Action > Residue > Label > Name 
- Actions > Color > All Options → Select "Labels" only and choose a color.
- Actions > Label > Set Label Height  (Change label font size: label height 1.0)
- Menu > Rightmouse > ATP Move Label (to move label, see Figure-2)

<figure>
	<img src="/assets/img/Biophysics/Chapter-13/C13_2.png" alt="Description of the image" style= "width: 100%;"> 
	<figcaption>ChimeraX menu</figcaption>
</figure>	

**Measuring Distances**
- Select both heme FE and HIS 93.A NE2 though Ctrl+Shift left click
- Navigate to **Tools > Structure Analysis > Distances** and click the **Create** button to measure the distance between them.

**Structure Analysis and Comparison**
	
Select the Heme Group (HEM): 
-Go to **Select > Residue > Non-Standard Residue > HEM**.
Select Nearby Residues:
- Use **Select > Zone** to choose all residues within a specified distance.
- Set the cutoff to 5 Å to select all atoms and bonds within this range.
Coloring by Element:
- Go to **Actions > Color > By Element** to color atoms according to their element type.
Selecting Coordinating Atoms:
- Use Ctrl+Shift + Left-click to select both the metal ion of HEM and the coordinating nitrogen in HIS 93.A.

### 1.2.3 Basic Command Line Controls
Working on command line in ChimeraX is very useful, Here are the basic commanda that may help us analysis the biomolecular structures. 

You can also accomplish the same in the command line by typing: $ hide atoms
Full list of colors to appear in the log pane by typing the following 
* command: $color list
* Changing color: color lightskyblue
* color red (change the color of everything)
* sel :108 (Selecting that residue)
* color sel green (Coloring the selected ligand to green)
* color sel byhet or color sel byhetero (Add standard heteroatoms coloring)
* sel clear
* show solvent (Showing all the water molecules in crystal)
* delete solvent  (Removing all the water molecules, ChimeraX has “undo” button but deleting things may not work on recovering delete.)
 
**Selection Arguments**
Signs for selection:
- Object: #
- Chain: /
- Residues: :
- Atoms: @

Open 6UDQ  (Human IMPDH2 treated with ATP, IMP, and 20 mM GTP)

- Select an object using “#”: select #1
- Select chain B in object 1: select #1/B
- Select residue 10-30 of chain C in object 2: select #2/C:10-30
- Select residue 10-30 of chain A and C in object 2: select #2/A,C:10-30
- Select all atoms CA of lysine in object 3: select #3:lys@CA

* select : 10-50  (for selecting range)
* select /A: 10-50 (selecting from chain A)

**Labeling**
- label @ca residues attr number
- label :1 residues attr chain_id height 4
- label /A:1 residues attr structure.name height 5 offset 1,1,1
- label /A:2-12 residues text "{0.phi:.1f},{0.psi:.1f}"
- label sel text "{0.name}{0.number}" height 1.5 

<div class="example">
    <div class="example-title">Example 13.1.  Analyze the Active Site</div>
    <div class="example-content">
        <!-- Your example content goes here -->
        Using a molecular visualization software package, examine the active site of Human Glucokinase (PDB entry 3FGU) with the following requirements. 
        <ol type="i">
            <li>Protein and Ligand Coloring: Color the entire protein in blue and the ligand ANP in gray. </li>
            <li>Heteroatom Coloring: Apply element-specific coloring (e.g., oxygen red, nitrogen blue) to all heteroatoms in the structure. </li>
            <li> Hydrogen Bond Analysis: Identify and highlight all hydrogen bonds within a 5Å radius of the ligand. </li>
            <li> Residue Labeling: Label the amino acid residues involved in hydrogen bond interactions with the ligand.</li>
        Ensure that all visualizations are clear and properly formatted for effective analysis
       </ol>

   <b> Solution: </b> <br>
        Steps to Visualize and Analyze Ligand Interactions in ChimeraX
        <ul>
            <li> <b>Open the Structure</b>
                <ul>
                <li><b> fetch 3FGU</b> </li>
                </ul>
            </li>
            <li><b>Color the Protein and Ligand</b>
                <ul>
                    <li>Select the entire protein: <em>Actions → Color → Blue</em></li>
                    <li>Select the ligand: <em>Select → Residue → Ligand</em></li>
                    <li>Color the ligand gray: <em>Actions → Color → Gray</em></li>
                </ul>
            </li>
            <li><strong>Apply Heteroatom Coloring</strong>
                <ul>
                    <li>Select all (entire protein including heteroatoms): <em>Select → All</em></li>
                    <li>Apply heteroatom-specific coloring: <em>Actions → Color → by Heteroatoms</em></li>
                </ul>
            </li>
            <li><strong>Hide Non-Ligand Atoms and Bonds</strong>
                <ul>
                    <li>Deselect all: <em>Ctrl + Click on empty space</em></li>
                    <li>Hide non-ligand atoms and bonds: <em>Actions → Atoms/Bonds → Hide</em></li>
                </ul>
            </li>
            <li><strong>Show Ligand Structure</strong>
                <ul>
                    <li>Re-select ligands: <em>Select → Structure → Ligands</em></li>
                    <li>Show atoms and bonds of the ligand: <em>Actions → Atoms/Bonds → Show</em></li>
                </ul>
            </li>
            <li><strong>Display Magnesium Ion (Mg) If Present</strong>
                <ul>
                    <li>Select Mg ion: <em>Select → Residue → Mg</em></li>
                    <li>Show selected ion: <em>Actions → Show</em></li>
                </ul>
            </li>
            <li><strong>Select Interaction Zone (5Å Around Ligand)</strong>
                <ul>
                    <li>Select any bond or atom of the ligand: <em>Click on ligand atom</em></li>
                    <li>Expand selection to a 5Å interaction zone: <em>Select → Zone → 5 Å</em></li>
                </ul>
            </li>
            <li><strong>Display Atoms in Interaction Zone as Sticks</strong>
                <ul>
                    <li><em>Actions → Atoms/Bonds → Stick</em></li>
                </ul>
            </li>
            <li><strong>Analyze and Display Hydrogen Bonds</strong>
                <ul>
                    <li>Open the Hydrogen Bond Analysis Tool: <em>Tools → Structure Analysis → Hydrogen Bonds</em></li>
                    <li>Enable hydrogen bond display: <em>Select "Limit by at least one end selected"</em></li>
                </ul>
            </li>
            <li><strong>Clear Selection</strong>
                <ul>
                    <li><em>Select → Clear Selection</em></li>
                </ul>
            </li>
            <li><strong>Hide Cartoon Representation (If Needed)</strong>
                <ul>
                    <li><em>Actions → Hide → Cartoon</em></li>
                </ul>
            </li>
            <li><strong>Label Residues in the Interaction Region</strong>
                <ul>
                    <li>Select any atom in the interaction region: <em>Click on a residue involved in hydrogen bonding</em></li>
                    <li>Label residue name and number: <em>Actions → Label → Residue → Name+Number</em></li>
                </ul>
            </li>
            <li><strong>Set Background Color to White</strong>
                <ul>
                    <li><em>set bgColor White</em></li>
                </ul>
            </li>
        </ul>       
   </div>
</div>

## 1.3 3D-Alignments
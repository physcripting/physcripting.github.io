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
<figure class="half-width">
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

    
    For additional information (<a href="https://www.cgl.ucsf.edu/chimerax/docs/user/tools/toolbar.html" target="_blank"> ChimeraX Toolbar </a>)
### 1.2.1 Basic Mouse Controls
In ChimeraX, the basic mouse controls for interacting with molecular structures and 3D visualizations are:
* Hover the mouse over atoms for a second, box will appear says: /A BTN 300 S1 (chain A, molecule code BTN, atom code #300, sulfur #1)
* **Rotation, Translation, and Zooming**
    * Left Mouse Button (Click & Drag) → Rotate the structure
    * Middle Mouse Button (Click & Drag) → Move (translate) the structure
    * Right Mouse Button (Click & Drag) OR Scroll Wheel → Zoom in/out
* **Selection and Picking**
    * Ctrl + Left Click → Select an atom, residue, or molecular component
    * Ctrl + Shift + Left Click → Select multiple items
    * Double Left Click on an Object → Center and zoom in on that object
* Alternative Mouse Modes (for Specific Tools)
    * Alt + Left Click & Drag → Slab clipping (adjust depth of view)
    * Shift + Right Click & Drag → Adjust threshold levels in volume data
    * Ctrl + Mouse Scroll → Adjust contour levels for density maps

We can customize mouse actions via **Tools → General → Mouse Modes**, allowing you to assign different functions to each mouse button.

### 1.2.2 Basic Control 
In this section, we will explore the basic controls for manipulating proteins in ChimeraX, using **Human Deoxyhemoglobin** (**PDB: 2HHB**) as our model structure. The structure consists of **four chains** (Alpha chains: Labeled A and C; Beta chains: Labeled B and D) and **Ligands** (Non-Protein Compounds): Heme group (HEM) and Phosphate ion.

Get comfortable with the mouse controls and buttons in ChimeraX, including those found under the "Home," "Molecule Display," and other menus. Practice essential operations such as rotation, translation, zooming, and selection (picking). For more details, refer to section 1.2.1, "Basic Mouse Control."

> **Note**: If the protein does not contain nucleotides, then nucleoside-related functions will not work in ChimeraX.
 
After experimenting with the display settings, you can restore the default view by selecting
* `Presets → Original Look`

The following table provide instruction briefly for **Selection of Chains and Atoms and Coloring** of 2HHB. 


| **Step**                         | **Command/Instruction** | Description |
|-------------------------------------|----------|-------------------------|
| **View Information**              | `Hover over an atom`| A pop-up box will display information, e.g., `/A HEM 142 O1A` (Chain A, Residue HEM & ID 300, Atom Oxygen & ID O1A). | 
| **Select Chain**| `Select → Chains → Chain A`| to select chain A|
| **Select Residue**| `Select → Residues → HEM` | to select residues HEM in the molecule|
|**Selection Mode**| `Select → Menu Mode → Replace Mode` <br> `Select → Menu Mode → Add (+) Mode` <br>  `Select → Menu Mode → Intersect Mode`| Removes any previous selection and replaces it with a new selection. <br> Adds the new selection to the previously selected atoms. <br> Selects only atoms that satisfy  (logical AND operation)|
| **Select Specific Residue**| `Select → Chains → Chain A` <br> `Select → Menu Mode → Intersect` <br> `Select → Residues → HEM` <br> or <br> `select atom from HEM →  Ctrl + Up Arrow Key`| To select HEM residue from Chain A| 
| **Reduce Selection**| `Ctrl + Down Arrow Key` | to reduce the selection|
|**Atom Style**|`Actions → Atoms/Bonds → Atom Style → Ball & Stick`| Set the atoms of HEM in ball & stick style|
| **Coloring Selection** |`Action → Color → By Element`|Coloring the selected HEM by element| 
|**Focus on a Selection**|`Actions → Focus`|Zoom into selected area|
| **Invert selection**  | `Select → Invert → Selected Models` | Select everything except the current selection is highlighted.|
|**Coloring**| `Action → Color → Orange`| Coloring the everthing else expect HEM of chain A |
| **Deselect Selection**       | `Ctrl + Left-Click on blank space` | to deselect the current selection.|
|**Labeling**|`Action → Residue → Label → Name` <br>  `Actions → Color → All Options → Select only "Labels"` <br> `Actions → Label → Set Label Height` <br> `Menu → Rightmouse → ATP Move Label` (Figure-2)| Label residue and adjust label font size and position|
|**Measuring Distances**|`Ctrl + Shift Select HEM 142 O1D and PHE 46 CZ` <br> `Tools → Structure Analysis → Distances and click "Create"`|To measure the  distance between them and label the distance|

<figure>
	<img src="/assets/img/Biophysics/Chapter-13/C13_2.png" alt="Description of the image"> 
	<figcaption>Modify the control of Right Mouse Button in ChimeraX</figcaption>
</figure>	


<figure class="half-width">
	<img src="/assets/img/Biophysics/Chapter-13/C13_3.png" alt="Description of the image"> 
	<figcaption>Explore region of HEM residue in deoxyhemoglobin 2HHB</figcaption>
</figure>	

### 1.2.3 Basic Command Line Controls
Working on command line in ChimeraX is very useful, Here are the basic commanda that may help us analysis the biomolecular structures. 

* **open 2HHB** (To get structure from database, Note: older version Syntax is "fetch 2HHB" )
* **color list**  (display full list of colors)
* **color red** (change the of select or if nothing is select then color everything)
* **color sel green** (Coloring the selected ligand to green)
* **color sel byhet** or **color sel byhetero** (Add standard heteroatoms coloring)
* **hide atoms**
* **sel :108** (Selecting that residue)
* **sel clear** (clear the selected items)
* **show solvent** (Showing all the water molecules in crystal)
* **delete solvent**  (Removing all the water molecules, ChimeraX has “undo” button but deleting things may not work on recovering delete.)
 
**Selection Arguments**
Signs for selection:
- Model: #
- Chain: /
- Residues: :
- Atoms: @

* **close** (close everything)
* **close #ID** (e.g. **close #1.1** close specific submodel) 
* **open 6UDQ**  
* **sel #1** (or select #1)
* **sel #1/B** (Select chain B in object 1)
* **sel #2/C:10-30** (Select residue 10-30 of chain C in object 2)
* **sel #2/A,C:10-20** (Select residue 10-30 of chain A and C in object 2)
* **sel #3:lys@CA** (Select all atoms CA of lysine in object 3)
* **sel :108** (selecting residue 108)
* **color sel silver** (coloring the selected residue)
* **hide bonds** or **~hbonds**  (to hide hydrogen bonds)
**Labeling**
- label @ca residues attr number
- label :1 residues attr chain_id height 4
- label /A:1 residues attr structure.name height 5 offset 1,1,1
- label /A:2-12 residues text "{0.phi:.1f},{0.psi:.1f}"
- label sel text "{0.name}{0.number}" height 1.5 

**Hiding**
- hide ligand
- hide ligand #1/A (hide onle ligands from a specific chain (e.g chain A))
- hide @/isHet (To hide all non-standard residues (ligands, modified residues, etc.))
- hide solvent (hide solvent molecules (like water))
<div class="example">
    <div class="example-title">Example 13.1.  Analyze the Active Site</div>
    <div class="example-content">
        <!-- Your example content goes here -->
        "Using a molecular visualization software package, examine the active site of Human Glucokinase (PDB entry 3FGU) with the following requirements. 
        <ol type="i">
            <li>Protein and Ligand Coloring: Color the entire protein in blue and the ligand "ANP" in gray. </li>
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

## 1.3 Structure Analysis and Comparison

### 1.3.1 Hydrogen Bonds
This section analyzes hydrogen bonds around heme (HEM) ligands in human deoxyhemoglobin (PDB: 2HHB). The following structured workflow outlines the steps for hydrogen bond analysis. The Figure-3 dsplay the expected output.

| **Step**                 | **Command / Instruction** | **Description** |
|--------------------------|--------------------------|----------------|
| 1. **Remove Solvent**   | `delete solvent` | Removes water molecules to eliminate solvent hydrogen bonds. |
| 2. **Removing chains** | 'del #1/B, C, D' | Deletes unnecessary chains B, C, and D, leaving only chain A for analysis. |
| 3. **Select Heme Group** | `Select > Residue > Non-Standard Residue > HEM` | Isolates the heme (HEM) ligand for focused analysis.. |
| 4. **Select Nearby Residues** | `Select > Zone` → Set cutoff to **5 Å** | Selects residues **within 5 Å** of the heme group to analyze interactions. |
| 5. **Apply Coloring by Element** | `Actions > Color > By Element` | Colors atoms based on their element type for better visualization. |
| 6. **Hide Existing Hydrogen Bonds** | `~hbonds` | Clears previously displayed hydrogen bonds to avoid redundancy. |
| 7. **Label Displayed Elements** | `label @@display` | 	Displays atom labels to help identify key structural components. |
| 8. **Select Ligand** | `Ctrl + Left Click` on ligand, then press **Up Arrow key** | Selects the entire ligand structure for manipulation. |
| 9. **Display Hydrogen Bonds** | `hbonds : HEM` or `hbonds ligand` | Displays hydrogen bonds involving the ligand. |
| 10. **Change Hydrogen Bond Color** | `color hbonds magenta` | Changes hydrogen bond color to **magenta** for contrast. |

<figure>
	<img src="/assets/img/Biophysics/Chapter-13/C13_4.png" alt="Description of the image"> 
	<figcaption>Hydrogen Bonds Analysis for HEM in chain A in deoxyhemoglobin 2HHB</figcaption>
</figure>	

## 1.4 Structure Analysis

### 1.4.1 Aligning Structure
In this section, we will explore how to compare multiple protein structures through structural alignment. Using ChimeraX’s MatchMaker tool, we will learn how to align two or more protein structures based on sequence and structural similarity. This process allows us to analyze conserved regions, structural differences, and evolutionary relationships. Additionally, we will examine sequence alignments to gain insights into functional similarities between proteins. By the end of this section, you will have a clear understanding of how to perform structural superimposition and sequence comparisons in ChimeraX. 

| **Step**                 | **Command / Instruction** | **Description** |
|--------------------------|--------------------------|----------------|
| 1. Open Strucures   | `open 2hhb 1mbo` | open two strucutres|
| 2. Structure Aligments|`Structure Analysis → MatchMaker` <br> ` Reference 2hhb  #1 & structure(s) to match 1mbo (#2)`<br> `select Alignment → Show pairwise sequence..`| Alignig the strcutrues|
|3. Hide Unmatch Chains|`cartoon hide #1/A,B,C` <br> `hide #1/A,B,C` <br> `hide solvent`| To hide cartoon, ligands, and solvent|
|4. Hide non-stanardard|`hide #1\D` <br> `hide #2`| Hiding non-standard residue from object 1 and 2|
|5. Show HEM|`show #1/D:HEM #2:HEM`| Showing HEM from #1 and #2|
|6. Color by $$\alpha$$ C|`Tools > Structure Analysis > Render by Atricbute` <br>`	From drop down select attribute of to Residue` <br> `	Select attribute to seq-rmsd`<br> `histogram change range to blue at 0.25, white at 1.5 and red at 3` <br>`Color missing value with green` <br>`select Corresponding Color Key`| Color by $$\alpha$$ C rmsd value & include Color Key|

<figure>
	<img src="/assets/img/Biophysics/Chapter-13/C13_5.png" alt="Description of the image"> 
	<figcaption>Structural Analaysis through Matchmaker</figcaption>
</figure>

<div class="example">
    <div class="example-title">Example 13.2.  Analyze the Active Site</div>
        <div class="example-content">
        Align the structures of Archaeal Actin (PDB: 4BQL, Chain A) and Rabbit Uncomplexed Actin (PDB: 1J6Z, Chain A) using ChimeraX. Then, visualize structural differences by coloring the protein based on C-alpha Root Mean Square Deviation (RMSD):
        <ol type="i">
            <li>Blue represents regions with a C-alpha RMSD of ~1 Å or less, indicating high structural similarity.</li>
            <li>White represents regions with a C-alpha RMSD of ~3 Å or less, indicating intermediate structural similarity. </li>
            <li> Red represents regions with a C-alpha RMSD of ~5 Å or more, indicating significant structural deviations. </li>
            <li> Green represents region with no match.</li>
       </ol>
       <b>Solution</b> <br>
            <ol type="i">
                <li>open 4bql </li>
                <li>del /B,C,D (it has 4 copies we delete chain B, C, and D )</li>
                <li>Actions → Focus</li>
                <li>compare to rabit version of active</li>
                <li>open 1j6z</li>
                <li>matchmaker #2 to #1 show true : show true means show the sequence alignments.  These proteins are quite different sequence. Here we can see Cα RMSD represent distance between Cα atoms when the bar are high means that Cα closer. We are going to use that color</li>
                <li>using menu Tools > Structure Analysis > Render by Atricbute.</li> 
                <li>From drop down select attribute of to Residue </li>
                <li>Select attribute to seq-rmsd. On the histogram change range </li>to blue at 1, white at 3 and red at 5 by selecting color bar and typing value .
                <li>Select Color missing value with green (select green).  (or command line rmsd #1 #2 color bfactor)</li>
                <li> We can create color key clicking correposing color key (we won’t change anything here)</li>
                <li> Menu→hide atoms   </li>
            </ol>     
        </div>
</div>
<figure>
	<img src="/assets/img/Biophysics/Chapter-13/C13_6.png" alt="Description of the image"> 
	<figcaption>Structural Analaysis through Matchmaker</figcaption>
</figure>

### 1.4.2 Hydrogen Bond and Distance Analysis
The pathogen Staphylococcus aureus produces a pigment called staphyloxanthin, giving it a golden color (hence aureus). This pigment is crucial for virulence as it shields the bacteria from host immune system attacks. We'll examine and compare various structures of the Stapyloxanthin aureus enzyme CrtM, which is a promising drug target since it facilitates a critical stage in staphyloxanthin production.
* `open 3w7f`
* `del #1/b` (or `delete #1/b`)
* `view ligand` – Focus the view on the ligand residues 
* `label ligand` – Label residue
* `label height 1.0` – Change label height to 1.0 A, default 0.7A, 
* `del solvent` – remove solvent to simplify analysis.
* `label @@display` -label the residues with sidechains, @@display refers to an attribute at the atom level called "display," which indicates whether the atom is shown in the display area. In essence, the command is instructing to label all residues with atoms that are displayed.

In this setup, farnesyl thiopyrophosphate molecules are referred to as FPS. Three magnesium ions counterbalance the negative charges on the phosphates, depicted as greenish spheres. Metal coordination bonds from FPS, water, and the protein are shown as dashed purple lines. Other than covalent bonds are represented as pseudobonds, with hovering over them revealing information about their end atoms and length.
* `Sel :21`  -select residue Serine (Ser, S) 21
* `view sel`
* `Ctrl-click to pick oxygen of Ser 21`
* `Shift-Ctrl-doubleclick on the nearest phosphate oxygen`
* `Tools → Structure Analysis → Distance`  (click create to show the distance between the selection)
* `distance #1:21@OG #1:302@O1B` : Prvious steps in command lines
* `distance :248@OH :302@O1B`

Distance measurements are displayed as yellow dashed lines. These distances appear to match hydrogen bonds. Instead of manually measuring many distances and recalling specific hydrogen-bonding distances for different atom types, you can simply use the hbonds command or the H-Bonds tool.
* `sel :FPS` – first select the FPS resides to limit H-bond search (or menu:  `Select → Residues →FPS`
* `view sel`
* `hbonds sel restrict cross reveal true log true` - Find H-bonds with one end selected. 
* Or `Tools→ Structure Analysis → H-Bonds` 
* `select to Reveal atoms of H-bonding residues`,
* `Limit by selection: with exactly one end selected, and Log`, other settings default. 

<figure class="half-width">
	<img src="/assets/img/Biophysics/Chapter-13/C13_7.png" alt="Description of the image"> 
	<figcaption>Hydrogen and Distance Analysis</figcaption>
</figure>

The hydrogen bonds are represented by light blue dashed lines. The two measured distances confirmed the presence of hydrogen bonding. More information can be found in the Log. if you would like to remove hydrogen bonds and distance then: 
* `hide hbonds`  or `~hbonds` - Hide H-bonds
* `~distance` – Remove the distance measurements

### 1.4.3 Clashes and Contacts
- **Clashes** refer to unfavorable interactions occurring when atoms are too close together, often termed as close contacts. 
- **Contacts** encompass various direct interactions, both polar and nonpolar, favorable and unfavorable, which include **clashes**.
* `open 3w7f`
* `del #1\b`
* `sel #1:FPS`
* `Actions → Color → Gray`
* `Actions → Color → Byelement`
* `contacts sel restrict cross reveal t log t select t` – identifying contacts of selected residues (FPS)
*  Or `Tools → Structure Analysis → Contacts`.
* `Limit by selction with at least one end selected`

In the Log, *atom-atom contacts are listed based on decreasing Van der Waals (VDW) overlap*. A positive value indicates intersecting atomic VDW spheres, zero indicates touching, and negative indicates separation. By default, even slightly separated spheres are considered contacts. The distances between atomic centers are also provided.
* `~contacts` – remove the contact pseudobonds
* `~label`- remove the labels

The Log provides detailed information about each atomic contact, but sometimes it's more convenient to have a simpler list of interacting residues instead. To start, d.
* `~sel  ~protein` : eselect everything that isn't protein.
* `info residues sel` -list the selected residues in the  log. You can see Serine (Ser, S) 21, Tyrosine (Tyr, Y) 248, and several others in the list.

### 1.4.4 Angles, Rotamers,and Clashes
We will continue work on the  **3w7f**
* `sel clear` – clear the selection.
* `view :248`   - focus the view on Tyrosine (Tyr, Y) 248
* `select: 248`  - select the whole residue Tyrosine (Tyr, Y) 248 or  `Ctrl-click to select any atom in Tyr 248`, then press the up arrow key on the keyboard to promote the selection to the whole residue
* `Tool show clashes` – start clashes to setup  class checking and rotat the sidechain interactively. Or `Tools → Structure Analysis → Clashes`
* `clashes sel restrict cross reveal t continuous t` – restrict the option to limit by selection, revel atoms, frequency of checking to continuously  Or it can be done using dialog box.
* `Tools → Strctuure Analysis → Clashes`: In the Clashes dialog, **keep most options as defaults**, except:
    * Turn on the option to `Limit by selection`, set to: `with exactly one end selected`
	Turn on the option at `Frequency of checking` for reveal atoms...
	* `Set the Frequency of checking to continuously` (until dialog closed)
	(...and <u>do not close the dialog</u> yet, although it can be moved aside)
As reported in the Log, <u> no clashes with Tyr 248 </u> are found in its initial position

As reported in the Log, no clashes with Tyr 248 are found in its initial position
Let’s measure the sidechain $$χ_1$$ and $$χ_2$$ angles of Tyr 248.
* `torsion :248@n, ca, cb, cg` – measuring respect to α carbon, β carbon, and γ carbon 
* `torsion :248@ ca, cb, cg, cd1`

The Log reports angles $$χ_1$$ and $$χ_2$$ as $$106.801^o$$ and -$$142.054^o$$, respectively.

The torsion command sets the angle defined by the four specified atoms to angle in degrees, or if angle is omitted, reports the current value in the Log. A centroid or marker can be specified as an atom. For changing the angle, the two middle atoms must be covalently bonded to one another.
* `set Right Mouse to "Bond Rotation"`

With the assigned button, click on the Tyr 248 CA-CB bond (closest to the ribbon) and drag to change chi1 interactively, or on the CB-CG bond (the next one out, adjacent to the ring) to change chi2. Any clashes are shown as bright purple pseudobonds and updated automatically as the bond is rotated.

Close the Clashes dialog. If clash pseudobonds are still shown, remove them
* `~clashes` – To hide the clashes display
* `torsion :248@n,ca,cb,cg -106.801` – restoring the angle back
* `torsion :248@ca,cb,cg,cd1 -142.054` -restoring the angle back

Next, we will compare the conformation of Tyr 248 in the structure to tyrosine rotamers from a library. With Tyr 248 still selected (if not, Ctrl-click it), start the Rotamers tool:
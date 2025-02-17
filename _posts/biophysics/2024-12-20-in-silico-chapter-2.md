---
title: "Chapter 2: Water: The Solvent for Biochemical Reaction"
author: PSK
date: 2025-02-09 14:10:00 +0800
categories: [eDocuments, Introduction to Biophysics of Biomolecules]
math: true
render_with_liquid: false
---

This chapter provides a brief desribtion of water molecules that required for biochemical reaction.

## 1.1 Introduction
Solvents play a fundamental role in biochemical reactions by providing the medium in which these reactions occur. The choice of solvent significantly influences reaction rates, equilibrium, specificity, and overall efficiency. In biological systems, **water is the predominant solvent** due to its unique chemical properties, including high polarity, extensive hydrogen bonding capability, broad thermal and pH stability, natural abundance, and and exceptional ability to dissolve a wide range of biomolecules. These properties make water essential for maintaining the structural integrity and function of biomolecules such as proteins, nucleic acids, and enzymes. Water constitutes approximately 70% of cellular content on average, with variations depending on the cell type and physiological state. Cells generally require a minimum water content of around 60% to sustain normal metabolic activity, emphasizing its critical role in sustaining life.

While water serves as the universal biological solvent, certain biochemical applications require alternative solvents to optimize reaction conditions. Non-aqueous solvents such as organic solvents, ionic liquids (ILs), supercritical fluids (SCFs), and deep eutectic solvents (DESs) are being increasingly explored for their applications in synthetic biology, biocatalysis, and pharmaceutical research. These solvents enable reactions that are inefficient or impossible in aqueous environments. For example, organic solvents like ethanol and dimethyl sulfoxide (DMSO) are commonly used as cryoprotectants, drug delivery enhancers, and solubilizing agents for hydrophobic molecules in biochemical studies and pharmaceutical formulations.

Solvents contribute to biochemical reactions in several key ways:
* **Dissolution of Reactants and Products**: Solvents facilitate molecular interactions by dissolving reactants and products, ensuring efficient reaction progress. I In aqueous environments, solubility is essential for enzymatic catalysis, metabolic pathways, and intracellular transport mechanisms.
* **Stabilization of Intermediates**: Many biochemical reactions involve unstable intermediates that require solvent stabilization to proceed effectively. For example:
    * **Water's Role**: Water stabilizes charged intermediates through hydrogen bonding, dielectric screening (reducing electrostatic interactions between charges), and other electrostatic interactions.
    * **Alternative Solvents**: Ionic liquids (ILs) and deep eutectic solvents (DESs) are being explored for stabilizing biomolecules and enzymes in non-aqueous or specialized environments. It's important to avoid implying that ILs and DESs always stabilize biomolecules; the effect depends on the specific IL/DES and biomolecule.
* **Influence on Reaction Kinetics**: Solvents affect reaction rates by influencing activation energy, molecular mobility, and diffusion.

    * **Polar Solvents**: Polar solvents like water can enhance reaction rates by stabilizing charged transition states (the highest energy point in a reaction pathway).
    * **Nonpolar Solvents*: Nonpolar solvents may slow reactions involving charged species because they don't stabilize the charges as well.
* **Maintenance of Proper Reaction Conditions**: Solvents help maintain optimal reaction conditions, including temperature, pH, and ionic strength, which are crucial for enzymatic activity and biochemical equilibrium. Some alternative solvents, such as ILs and SCFs, offer **tunable properties** that enable precise control over reaction conditions in engineered systems.

The choice of solvent is a critical determinant of reaction feasibility, efficiency, and selectivity in both natural and engineered biochemical processes. Researchers are actively exploring alternative "green" solvents that aim to reduce environmental impact and toxicity while enhancing reaction efficiency and sustainability. However, it is important to recognize that no single solvent perfectly balances all desirable properties, and the selection process often involves trade-offs between solubility, stability, reactivity, and environmental considerations.
## 1.2 Polarity
Electronegativity refers to an atom's tendency to attract electrons in a chemical bond. A higher electronegativity indicates a stronger pull on electrons, leading to partial negative and positive charges on bonded atoms. The difference in electronegativity between atoms determines bond polarity. 

In water (H₂O), the significant electronegativity difference between oxygen and hydrogen results in polar covalent bonds. Oxygen, being more electronegative, carries a partial negative charge (δ⁻), while hydrogen atoms carry partial positive charges (δ⁺). Water's polarity arises from both this electronegativity difference and its bent molecular geometry, which prevents bond dipoles from canceling, creating a net dipole moment (Figure 1). This polarity enables water to dissolve many substances, particularly polar compounds, through hydrogen bonding and dipole-dipole interactions. However, nonpolar substances, such as oils, do not readily dissolve in water, limiting its designation as a "universal solvent."

<figure class="quater-width">
	<img src="/assets/img/Biophysics/Chapter-2/C2_1.png" alt="Description of the image"> 
	<figcaption> Electronic Structure of the Water Molecule.</figcaption>
</figure>

Highly electronegative elements like oxygen, nitrogen, and fluorine strongly attract electrons in chemical bonds (Table 1). When atoms with a significant electronegativity difference bond, electron distribution becomes uneven, forming a polar bond. Conversely, when the difference is small, as in C-H bonds in methane (CH₄), electrons are shared more equally, making the bond nonpolar.

Table 1: Electronegativity of Common Elements

| **Element**    | **Electronegativity (Pauling Scale)** |
|------------|-----------------------------------|
| Fluorine   | 3.98                              |
| Oxygen     | 3.44                              |
| Nitrogen   | 3.04                              |
| Chlorine   | 3.16                              |
| Bromine    | 2.96                              |
| Iodine     | 2.66                              |
| Carbon     | 2.55                              |
| Sulfur     | 2.58                              |
| Hydrogen   | 2.20                              |
| Phosphorus | 2.19                              |


It is important to distinguish bond polarity from molecular polarity. A molecule can contain polar bonds yet be nonpolar overall if its shape leads to a symmetrical charge distribution. For example, while each C=O bond in carbon dioxide (CO₂) is polar, its linear geometry causes the dipoles to cancel, making the molecule nonpolar (Figure 2).

## 1.3 Bonding Mechanisms in Biomolecules
This section discusses the major bonding mechanisms within biomolecules and their interactions with the surrounding solvent.  Four primary types of bonds and interactions are crucial for biomolecular structure and function: covalent bonds, ionic bonds, hydrogen bonds, and van der Waals forces.  Additionally, hydrophobic and hydrophilic interactions play a significant role, though they are not bonds in the traditional sense but rather reflect the interplay between biomolecules and water.  Table 2 presents the bond strengths (in kJ/mol) associated with interactions involving hydrogen (H) and oxygen (O) atoms.

Table 2: Bond Strength of Various Bond Types Involving H and O Atoms.

| **Bond Type**        | **Strength (kJ/mol)**    | **Description**                      |
|----------------------|------------------------|------------------------------------------------------------------------------|
| **O–H Covalent Bond** | 400 – 460              | Strong bond formed by shared electrons between O and H (e.g., in water). |
| **O–H Ionic Bond**    | 40 – 200 | Arises when O or H exist as ions (e.g., hydroxide, hydronium, carboxylate). Strength varies based on specific ions. |
| **O–H Hydrogen Bond** | 10 – 40                | Weak interaction between an O–H group and an electronegative atom (e.g., O, N, F in water, alcohols). |
| **van der Waals (O & H)** | 0.1 – 10              | Weak, transient dipole-dipole interactions that can occur between any atoms, including those in O–H groups. |

The following subsections will explore each of these interactions in detail.

### 1.3.1 Covelent Bonding
Covalent bonds, formed by the sharing of electrons between atoms, are strong and essential for holding molecules together.  Rather than exploring the general principles of covalent bonding, we will focus on three key types crucial in biological systems, each discussed in detail in separate chapters:
* Peptide Bonds: These bonds link amino acids together to form proteins.
* Glycosidic Bonds: These bonds connect monosaccharides (simple sugars) to form carbohydrates.
* Phosphodiester Bonds: These bonds form the backbone of nucleic acids, DNA and RNA.

### 1.3.2 Ionic Bonds
Ionic bonds are electrostatic attractions between oppositely charged ions or groups.  They are indeed important in protein folding and enzyme-substrate interactions. However, their significance extends beyond these examples. Ionic bonds also play crucial roles in other biological processes, such as maintaining DNA structure and contributing to the stability of cell membranes. We will explore ionic bonds in more detail within the context of protein folding, as well as other relevant biological processes where they play a key role.
### 1.3.3 Hydrogen Bonding
A hydrogen bond is a relatively weak non-covalent interaction that occurs between a hydrogen atom—covalently bound to a highly electronegative atom (such as oxygen (O), nitrogen (N), or fluorine (F))—and another electronegative atom. The atom to which the hydrogen is directly bonded is referred to as the hydrogen-bond donor, while the electronegative atom that interacts with the hydrogen is the hydrogen-bond acceptor. 

The strength of a hydrogen bond is influenced not only by the electronegativity of the participating atoms but also by factors such as bond distance, orientation, and the surrounding environment. Hydrogen bonding plays a fundamental role in many chemical and biological systems.

Table 3 compares hydrogen bonding in hydrogen fluoride (HF), water (H₂O), and ammonia (NH₃), highlighting variations in bond strength and molecular interactions.

Table 3: Hydrogen Bond Strengths in Select Molecules

Molecule  | Hydrogen Bond Strength (kJ/mol) | Notes |
|-----------|------------------------------|------------------------------------|
| HF        | ~29                           | Strongest due to high electronegativity of F |
| H₂O       | ~20                           | Moderate strength, essential for life       |
| NH₃       | ~13                           | Weakest due to lower electronegativity of N  |

Hydrogen bonds are crucial for several biological and chemical processes, including:
* **Solubility of biomolecules in water**: Polar biomolecules, such as proteins and nucleic acids, form hydrogen bonds with water molecules, enhancing their solubility.
* **Stabilizing DNA double helix**: Complementary base pairs in DNA (adenine-thymine (A-T) and guanine-cytosine (G-C)) are held together by hydrogen bonds, contributing to the structural integrity of the double helix.
* **Maintain protein secondary structures**: Hydrogen bonds between backbone atoms stabilize secondary structural elements such as α-helices and β-sheets, which are essential for protein function and stability.

**Hydrogent Bonds in Water**: : Water molecules form extensive hydrogen bond networks due to oxygen's high electronegativity and the presence of two lone pairs. Each water molecule can act as both a hydrogen bond donor (via its two hydrogen atoms) and a hydrogen bond acceptor (via its two lone pairs), allowing it to form up to four hydrogen bonds. The partially positive hydrogen atoms are attracted to the partially negative oxygen atoms of neighboring water molecules. Linear hydrogen bonds (where the O-H···O atoms are aligned) are generally stronger than bent hydrogen bonds, although the difference in bond energy is moderate (~1–2 kJ/mol) (see Figure 3).  

Water’s unique density behavior is a direct consequence of hydrogen bonding. In ice, each water molecule forms four hydrogen bonds in a tetrahedral arrangement, resulting in an open hexagonal lattice (Figure). This structure increases the intermolecular spacing, making ice less dense than liquid water and allowing it to float.

In liquid water, hydrogen bonds are highly dynamic and short-lived. While each molecule can still form hydrogen bonds with up to four other molecules, these bonds continuously break and reform. The average lifetime of a hydrogen bond in liquid water is 1–10 ps (10⁻¹² s), while the timescale for breaking and reforming a hydrogen bond is approximately 0.1 to 1 picoseconds (10⁻¹³ to 10⁻¹² s) at 25°C. Unlike the rigid hexagonal lattice of ice, liquid water exhibits a fluctuating network where transient clusters—such as flickering six-membered rings—form and dissolve rapidly (Figure).

Additionally, the absence of hydrogen bonding in molecules such as methane (CH₄) and hydrogen sulfide (H₂S) explains why they exist as gases at room temperature, despite having molecular masses comparable to water. In contrast, water (H₂O) exhibits strong hydrogen bonding, significantly increasing its boiling point compared to CH₄ and H₂S (see Table 4).

Table 4: Comparison of Molecular Mass and Boiling Points

| Molecule | Molecular Mass (g/mol) | Boiling Point (°C) |
|----------|----------------------|------------------|
| H₂O      | 18                   | 100             |
| CH₄      | 16                   | -161.5          |
| H₂S      | 34                   | -60             |

Methane (CH₄), despite being smaller in mass than water, lacks hydrogen bonding and relies only on weak van der Waals (London dispersion) forces, leading to its extremely low boiling point (-161.5°C). Similarly, hydrogen sulfide (H₂S) has a higher molecular mass than water but still lacks strong hydrogen bonding because sulfur is less electronegative than oxygen, making H₂S a gas at room temperature (-60°C). In contrast, water’s extensive hydrogen bonding network results in a much higher boiling point (100°C), allowing it to remain a liquid under standard conditions.

### 1.3.4 Van der Waals Interactions

### Hydrophoic and Hydrophilic Interactions

## 1.4 pH 
Additionally, water ionization produces hydrogen ions (H⁺) and hydroxide ions (OH⁻), which are crucial in determining the structure and function of biomolecules such as proteins, nucleic acids, phospholipids, and cellular membranes. These ionization properties influence enzymatic activities, molecular interactions, and overall cellular homeostasis.

## 1.5 Weak Acids and Dissociation Constants 
Weak acids and bases are characterized by their dissociation constants. Unlike strong acids and bases such as HCl and NaOH, most biologically relevant acids and bases do not fully dissociate in water. In other words, proton transfer to or from water is only partial.

For example, the dissociation of acetic acid (CH$_3$COOH) in water follows the equilibrium reaction:
$$\begin{equation}
    \text{CH}_3\text{COOH} + \text{H}_2\text{O} \rightleftharpoons \text{CH}_3\text{COO}^- + \text{H}_3\text{O}^+
    \tag{2.1}
\end{equation}$$
The equilibrium constant for this reaction is expressed as:
$$\begin{equation}
    K = \frac{[\text{CH}_3\text{COO}^-][\text{H}_3\text{O}^+]}{[\text{CH}_3\text{COOH}][\text{H}_2\text{O}]}
    \tag{2.2}
\end{equation}$$

Since the concentration of water is significantly higher than that of the other species, it is treated as a constant and incorporated into the equilibrium constant. The resulting expression is known as the acid dissociation constant, $$K_a$$:

$$\begin{equation}
    K_a = \frac{[\text{CH}_3\text{COO}^-][\text{H}_3\text{O}^+]}{[\text{CH}_3\text{COOH}]}
    \tag{2.3}
\end{equation}$$

This constant provides a measure of the acid’s strength, indicating the extent to which it donates protons in aqueous solution.

Because the concentration of H₂O in aqueous solutions is significantly higher than that of other species, it is considered constant. As a result, it is incorporated into the equilibrium constant $$K$$, giving rise to the **acid dissociation constant** $$K_a$$:

$$\begin{equation}
    K_a = \frac{[\text{CH}_3\text{COO}^-][\text{H}^+]}{[\text{CH}_3\text{COOH}]}
    \tag{2.4}
\end{equation}$$

For acetic acid, the acid dissociation constant is:

$$\begin{equation}
    K_a = 1.74 \times 10^{-5}
    \tag{2.5}
\end{equation}$$

The magnitude of $$K_a$$ indicates the tendency of an acid to ionize in solution. A larger $$K_a$$ signifies a stronger acid with a greater tendency to donate a proton, while a smaller $$K_a$$ suggests weaker ionization and lower proton donation.

Since $$K_a$$ values are often very small (similar to $$ [\text{H}^+] $$ concentrations), it is convenient to express them on a logarithmic scale using **pKa**, defined as:

$$\begin{equation}
    pK_a = -\log K_a
    \tag{2.6}
\end{equation}$$

For example, the $$pK_a$$ of acetic acid is:

$$\begin{equation}
    pK_a = -\log(1.74 \times 10^{-5}) = 4.76
    \tag{2.7}
\end{equation}$$

The relationship between $$K_a$$ and $$pK_a$$ is inverse:  

The larger the $$K_a$$, the smaller the $$pK_a$$, and the stronger the acid.**  
Because of this, $$pK_a$$ serves as a useful index for expressing the acidity of weak acids.

For example, the **Ammonium Ion $$NH_4^+$$**: 

The **ammonium ion (\( NH_4^+ \))** acts as a weak acid by donating a proton in aqueous solution:

$$\begin{equation}
    NH_4^+ \rightleftharpoons NH_3 + H^+
    \tag{2.8}
\end{equation}$$

Its **acid dissociation constant (\( K_a \))** and **pKa** values help quantify its acidic strength and compare it to other acids.
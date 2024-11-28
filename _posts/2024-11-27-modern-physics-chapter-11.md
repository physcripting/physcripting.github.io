---
title: "Chapter 11: Solid-State Physics"
author: T. Jayasekera
date: 2024-11-27 14:10:00 +0800
categories: [eTextbooks, Modern Physics]
math: true
render_with_liquid: false
---

This chapter provides a fundamenal introduction to Solid State Physics, tailored for undergraduae students in Chemistry, Physics, and Engineering. Building upon a basic understanding of University Physics, Quantum Mechanics and Statistical Mechanics, this chapter explore the essential concepts underlying the structure and electronic properties of materials.  To enhance comprehension, the chapter incorporates various simulation that visulize key concepts and provide hands-on experience with programming. 


## 11.1 Introduction
In crystalline solids, atoms are arranged in a periodic array, forming a highly ordered structure that repeats throughout the material. These atoms are held together by various types of bonding interactions, which determine the solid’s properties. 

Our goal is to understand the properties of materials from a microscopic perspective. To achieve this, we first need to grasp the terminology used to describe the microscopic structure of materials that exhibit periodicity.

In this chapter, we will explore the crystalline structure of materials by first examining one-dimensional examples in detail. This approach allows us to build a foundational understanding of periodic structures and their properties in a simplified context. Once we establish these concepts, we will extend our study to three-dimensional structures, where we will examine more complex and realistic crystal arrangements found in actual materials.

## 11.2 One-Dimensional Periodic Structures
A one-dimensional lattice is an infinite array of points arranged along a line, where each point is separated by a constant distance.
<figure2>
	<img src="/assets/img/Modern-Physics/Chapter-11/C11_1.jpg" style= "width: 100%;"> 
	<figcaption>Schematic of 1-D periodic structure.</figcaption>
</figure2>
The black dots in the diagram represent lattice points. In a hypothetical one-dimensional crystalline system, an atom or a group of atoms repeats at regular intervals, defined by the lattice constant, just as the dots repeat along the line.

With this example, let's explore the terminology commonly used in crystalline systems.

<figure2>
	<img src="/assets/img/Modern-Physics/Chapter-11/C11_2.jpg" style= "width: 100%;"> 
	<figcaption>Schematic of 1-D periodic structure.</figcaption>
</figure2>
The Figure 2 shows the ...



> **Lattice Constant**: A fundamental parameter of a crystal structure, It defines the periodicity and spacing of the atoms within the lattice. 
{: .prompt-tip }


> **Lattice Translation Vector**: The lattice translation vector is a vector that describes the displacement needed to move from one lattice point to another in a crystal lattice, such that the structure remains unchanged. It defines the periodicity of the crystal.
{: .prompt-info }


For the above 1-Dimensional system: 
\begin{equation}
    \vec{T} = a \hat{x}
\end{equation}


> **Primitive Unit Cell**: A primitive unit cell is the smallest repeating unit in a crystal lattice that, when translated through space, can recreate the entire crystal structure without any gaps or overlaps. It contains exactly one lattice point (or an equivalent portion of lattice points) and captures the symmetry and periodicity of the crystal.
{: .prompt-warning }

> **The Primitive Unit Cell is not unique** For example, all three boxes shown in blue, purple and green  in the Figure-xx represent primitive unit cells for this configuration.
{: .prompt-warning }


> **Basis** : The basis refers to the atom or group of atoms associated with each lattice point. In a 1D crystal, the basis could be a single atom or a repeating group of atoms that accompanies each lattice point, creating a consistent pattern along the line.
{: .prompt-warning }

### 11.2.1 Symmetry in 1-Dimensional Crystals and Frieze groups
A one-dimensional crystal has translational symmetry, meaning it looks the same if shifted by an integer multiple of the lattice constant $$a$$. 

In some cases, additional symmetry operations. In a one-dimensional (1D) crystal, symmetry refers to the transformations that can be applied to the crystal structure such that the arrangement appears unchanged.


* **Translational Symmetry: Frieze Group F1** Translational symmetry is the most fundamental form of symmetry. In 1D, if you shift the entire structure along the line by an integer multiple of the lattice constant, the arrangement of points or 

<figure2>
    <img src="/assets/img/Modern-Physics/Chapter-11/C11_4.jpg" style= "width: 100%;"> 
	<figcaption>Schematic of 1-D periodic structure.</figcaption>
</figure2>

* **Translational Symmetry + 180<sup>0</sup> (2-fold) rotation about a point P: Frieze Group F2**

<figure2>
    <img src="/assets/img/Modern-Physics/Chapter-11/C11_5.jpg" style= "width: 100%;"> 
	<figcaption>Schematic of 1-D periodic structure.</figcaption>
</figure2>

* **Translational Symmetry and Vertical Reflection Symmetry: Frieze Group F1m**. The structure remains unchanged if it is reflected across a vertical line (a mirror line) positioned at specific points along the line.
<figure2>
    <img src="/assets/img/Modern-Physics/Chapter-11/C11_6.jpg" style= "width: 100%;"> 
	<figcaption>Schematic of 1-D periodic structure.</figcaption>
</figure2>

* **Translational Symmetry and Horizontal Reflection Symmetry: Frieze Group F11m**.  The structure remains unchanged if it is reflected across a vertical line (a mirror line) positioned at specific points along the line.

<figure2>
    <img src="/assets/img/Modern-Physics/Chapter-11/C11_7.jpg" style= "width: 100%;"> 
	<figcaption>Schematic of 1-D periodic structure.</figcaption>
</figure2>

* **Translational Symmetry 2-fold Rotation + Vertical Reflection Symmetry + Horizontal Reflection Symmetry : Frieze Group F2mm**.    The structure remains unchanged if it is reflected across a vertical line (a mirror line) positioned at specific points along the line.

<figure2>
    <img src="/assets/img/Modern-Physics/Chapter-11/C11_8.jpg" style= "width: 100%;"> 
	<figcaption>Schematic of 1-D periodic structure.</figcaption>
</figure2>
* **Translational and Glide Reflection: Frieze Group F11g**. A glide reflection involves reflecting the structure across a line, followed by a translation by half the lattice constant. This symmetry operation can repeat the pattern in a 1D crystal.
    <figure2>
    	<img src="/assets/img/Modern-Physics/Chapter-11/C11_9.jpg" style= "width: 100%;"> 
	    <figcaption>Schematic of 1-D periodic structure.</figcaption>
    </figure2>

### 11.2.2 Symmetry in 2-Dimensional Crystals and Plane Groups and 2D Bravais Lattices

In 2-DImensions, an infinite array of lattice points can be described bythe translational vector:

$$\vec{T}=n \vec{a}_1 + m \vec{a}_2$$

### 11.2.3 Symmetry in 3-Dimensional Crystals and Space groups and 3D Bravais Lattices

## 11.3 Electron Materials
 Electrons are negatively charged particles, which are the key carriers of electrical current. The behavior of electrons in materials is fundamental to understanding the properties of matter. Electrons in materials behave quite different from those free electrons. Such differences give rise to materials with  variety of phenomena with varying electrical conductivity, magnetism, optics, and thermal properties. It is our goal to study the properties of electron materials. 
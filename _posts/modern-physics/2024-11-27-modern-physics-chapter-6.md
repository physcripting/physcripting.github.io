---
title: "Chapter 6: Quantum Mechanics in One Dimension"
author: PSK
date: 2024-11-2 14:10:00 +0800
categories: [eTextbooks, Computational-Aided Modern Physics]
math: true
render_with_liquid: false
---

In this chapter, we will learn one-dimensional quantum mechanics, beginning with fundamental concept of wave equations starting from wave equations. We will introduce the Schrödinger equation, a cornerstone of quantum mechanics, to describe the behavior of particles at the microscopic level. By applying the 
Schrödinger equation to various potential energy scenarios, we will derive solutions that provide insights into the quantum behavior of particles. These solutions will be interpreted to understand the probabilistic nature of quantum mechanics and the quantization of energy levels.

## 6.1 Introduction
Quantum mechanics is a mathematical framework that describes the behavior of matter and energy at the scale of atoms and subatomic particles. Unlike classical mechanics, which predicts definite outcomes of physical systems, quantum mechanics provides probabilities for various possible outcomes. 

A well-known illustration of this probabilistic nature of quantum mechanics is Schrödinger's cat, a thought experiment proposed by **Erwin Schrödinger** (1887-1961) in 1935. In this experiment, a cat in a placed in a sealed box with a device that includes a radioactive source connected to a Geiger counter. If the Geiger counter detects radiation from the decay of a radioactive atom, it tiggers a mechanism that releases poison, killing the cat. This is is a random event. Until the box is opened and an observation is made, the cat is considered to be in a **superposition** of state, both alive and dead simultaneously. 

This paradoxical situation highlights the unusual behavior of quantum particles, which can exist in multiple states at once until they are measured. Schrödinger intended this thought experiment to illustrate the problems associated with the **Copenhagen** interpretation of quantum mechanics, particularly the question of when quantum superpositions collapse into a definite stat.

There are two primary fomulations of quantum mechanics. 
* **Matrix Mechanics**:  Developed by  **Werner Heisenber**, **Max Born**, and **Pascual Jordan** in 1925,  this is a one of the foundational formulation that represents physical observables like position, momentum, and energy as matrices. The time evolution of these observables is governed by matrix equations. It was the first complete and consistent formulation of quantum mechanics, providing a new way to understand quantum phenomena without relying on classical concepts like electron orbits
* **Wave Mechanics**: Introduced by Asutrian Physicist **Erwin Schrödinger** in 1926,  this formulation describes the state of a quantum system using a wave function, often denoted as $$\Psi(x,t)$$. This wave fundtion contains information about the probability of finding a particle at a particular position and time.  

Although wave mechanics may seems different from matrix mechanics, it is mathematically equivalent to matrix mechanics. Schrödinger's wave machanics provides a more intuitive understanding of quantum behavior through the concept of wave-particle duality. The choice of which formulation to use often depends on the specific problem at hand and the preferred techniques.

Over time, wave mechanics has often been preferred over matrix mechanics due to its simplicity and intuitive applicability, especially in solving problems with continuous systems. However, the Schrödinger equation can also be expressed in matrix form, particularly when dealing with discrete systems or when using a basis set to represent wave functions. In this representation, the wave function is treated as a column vector, and the Hamiltonian operator becomes a matrix. The time evolution of the state vector is then governed by a matrix equation, similar to the time evolution in matrix mechanics.

In quantum mechanics, the interaction between a particle and its environment is typically described using potential energy rather than forces, as quantum theory relies on energy-based principles. The behavior of a quantum system is captured not through classical trajectories but through the wave function, which is a solution to the Schrödinger equation. The wave function encapsulates the particle's wave-like nature, providing insights into its probability distribution and quantum properties. By analyzing the wave function, one can determine the likelihood of a particle being found in a specific region of space and infer its underlying quantum behavior.

Quantum mechanics is essential for understanding the behavior of subatomic particles. It provides a framework for describing their interactions and properties, which cannot be explained by classical mechanics. Quantum mechanics has led to the development of many technologies, including transistors, lasers, and quantum computers.

## 6.2 Matter Waves
Before delve into the quantum world, it is important to grasp the concept of the wave function, denoted as \(\Psi(x)\). The wave function is a mathematical function that describes the quantum state of a physical system, representing the probability amplitude of a particle's position and momentum. Unlike classical waves, the wave function can be complex-valued, meaning it includes both real and imaginary components. This complexity is crucial for calculating probabilities in quantum mechanics, as the square of the absolute value of the wave function, $$|\Psi(x,t)|^2$$, represents the probability density of finding the particle at a specific position.

To better understand the wave function, it's helpful to first consider classical waves. In classical mechanics, waves are described by wave equations, which are mathematical equations that govern the behavior of wave propagation in different media. For instance, the wave equation for a one-dimensional wave on a string is given by:

$$\begin{equation}
    \frac{\partial^2 y(x, t)}{\partial x^2} = \frac{1}{v^2} \frac{\partial^2 y(x, t)}{\partial t^2} 
    \tag{6.1}
 \end{equation}$$

where $$y(x, t) $$ is the displacement of the string at position $$x$$ and time $$t$$ and $$v$$ is the wave's propagation speed.

The above equation describes how the shape of the wave evolves over time. While this classical wave equation doesn't directly correspond to the quantum wave function, it provides a useful analogy to help visualize the concept of wave-like behavior in quantum mechanics. For a more in-depth derivation of the classical wave equation and its solutions, refer to **Appendix Chapter 6**. We will extend our knowledge from classical wave  to wave function.

The wave nature of particles, often referred to as matter waves, is described by a mathematical function known as the wave function $$\Psi(x,t)$$. This complex-valued function offers a probabilistic interpretation of a particle's behavior, indicating the likelihood of finding a particle in a particular state or location at a given time.

The fundamental equation governing the dynamics of quantum systems is the Schrödinger equation.While the Schrödinger equation cannot be derived directly from classical mechanics, it was formulated based on the principles of energy conservation and the de Broglie hypothesis, which suggests that particles exhibit wave-like properties. It remains a cornerstone of quantum mechanics, validate by numerous experiments and accepted as long as no experimental evidence contradicts it. The Schrödinger equation encapsulates the principles of wave-particle duality and has been instrumental in understanding and predicting the behavior of quantum systems.

In the absence of external forces, the time-dependent Schrödinger equation is expressed as,

$$\begin{equation}
    - \frac{\hbar^2}{2 m} \frac{\partial^2 \Psi(x,t) }{\partial x^2}  = i \hbar \frac{\partial \Psi(x,t)}{\partial t}
    \tag{6.2}
\end{equation}$$ 

This equation, while resembles the classical wave equation, is specifically formulated fto describe the behavior of matter waves. 

A notable feature of the Schrödinger equation is its reliance on complex numbers ($$i= \sqrt{-1}$$). Unlike, classical waves, matter waves are not directly observable; conserquently, they cannot be fully described by a single real-valued function. While complex numbers are not strictly necessary, they provide a remarkably elegant and efficient framework for quantum theory. Although alternative formulations using two real-valued wave functions exist, they are less common and often more complex.

For instance,  in Maxwell's equations, the electromagnetic field tensor combines the electric and magnetic fields into a single complex-valued object, expressed as  $$ F =  E + i c B $$. This unification simplifies the equations and reveals deeper connections between the two fields. Similarly, in matter waves, the complex wavefunction $$ \Psi = \Psi_1 +  i \Psi_2 $$ encapsulates both the real and imaginary components, offering a more comprehensive and insightful description of quantum behavior. 

### 6.2.1 Double-Slit Experiment: Exploring the Wave Nature of Electrons
We can further explore the wave nature of matter by examining the double-slit experiment.

Let's consider what happens when one slit is closed during the experiment. Plots of the counts per minute or probability of arrival of electrons with the lower or upper slit closed are shown below:

These probabilities can be expressed as the square of the absolute value of a wavefunction:

$$\begin{eqnarray*}
    |\Psi_1|^2 &=& \Psi_1^* \Psi_1 \\
    |\Psi_2|^2 &=& \Psi_2^* \Psi_2 
\end{eqnarray*}$$ 

where $$ \Psi_1^*$$ and $$\Psi_2^*$$ are the complex conjugates of $$\Psi_1$$ and $$\Psi_2$$, respectively. These wavefunctions represent the cases of the electron passing through slit 1 and slit 2.

If both slits are open, one might naively assume that the electron goes through either slit 1 or slit 2 and that the counts per minute would be given by:

$$\begin{equation*}
    |\Psi_1|^2+ |\Psi_2|^2
\end{equation*} $$

However, experimental results contradict this assumption. This suggests that the electron is not localized and does not go through only one slit when both slits are open. Instead, the electron seems to be in a superposition of states, passing through both slits simultaneously.

Let see what happens if one slit is closed during the double slit experiment. Plots of the counts per minute or probability  of arrival of electrons with the lower or upper slit closed are shown below:     

To describe this behavior, we introduce the superposition principle. The wavefunction for the case of both slits open is given by:

\begin{equation}
    \Psi = \Psi_1 + \Psi_2
    \tag{6.3}
\end{equation}

The probability of detecting the electron at the screen is then:

\begin{equation}
    |\Psi|^2 = |\Psi_1 + \Psi_2|^2 = |\Psi_1|^2 + |\Psi_2|^2 + 2|\Psi_1||\Psi_2|\cos\phi
    \tag{6.4}
\end{equation}

The interference term $$ 2 \vert \Psi_1\vert \vert \Psi_2 \vert \ \cos \phi$$ arises from the complex nature of the wavefunctions and accounts for the interference pattern observed in the experiment.

### 6.2.2 The Born Interpretation of Wave Function
The current interpretation of the wave function $$\Psi$$, which connects it to probabilities, was first introduced by Max Born, a German theoretical physicist, in 1926. His work was essential in developing the statistical interpretation of quantum mechanics. This perspective indicates that the wave function does not represent a physical object but instead represents the probabilities of different outcomes when measurements are made.

Heisenberg initially introduced matrix mechanics in 1925. Born collaborated with the great mathematician David Hilbert to reformulate Werner Heisenberg's quantum theory using matrix mechanics. This collaboration enhanced the mathematical rigor and consistency of Heisenberg's original formulation,rather than the conceptual foundation.

Shortly after Erwin Schrödinger published his work on wave mechanics in 1926, Born applied Schrödinger's methods to atomic scattering and developed the Born approximation. This approximation is crucial for calculating the probability of a particle scattering into a given solid angle and is a fundamental tool in quantum mechanic. For his groundbreaking work, Born was awarded the Nobel Prize in Physics in 1954 for his interpretation of $$\vert \Psi \vert^2 $$ as the probability density.

The probability of finding a particle in an infinitesimal interval dx around the point x, denoted by P(x) dx, is given by

\begin{equation}	
    P(x) dx = |\Psi(x,t)|^2 dx
    \tag{6.5}
\end{equation}

where $$ P(x) $$ is the probability density.

Although it is not possible to specify with certainty the location of a particle, it is possible to assign probabilities for observing it at any given position. The quantity is:

\begin{equation}
    |\Psi(x,t)|^2 = \Psi^*(x,t) \Psi(x,t)
    \tag{6.6}
\end{equation}

where $$\Psi^*$$ is the complex conjugate of $$\Psi$$, and

\begin{equation}
    \Psi = \Psi_1 + i \Psi_2
    \tag{6.7}
\end{equation}

Notice that $$\Psi$$ itself is not a measurable quantity; however, $$\vert \Psi \vert^2 $$ which is measurable, represents the probability density ($$P(x)$$) for finding the particle at position ($$x$$) at time ($$t$$). The probability density is given by:

\begin{equation}
    P = \vert \Psi(x,t)\vert ^2
    \tag{6.8}
\end{equation}

Whether or not a particle ( like an electron) has a definite location, it has a definite charge—meaning we cannot have half an electron. Consequently, the wave function for an electron must be normalized to ensure that the total probability of finding the particle in all space equals one. So, the electron wave function should have a unit probability.

\begin{equation}
    \int_{-\infty}^{\infty} |\Psi(x,t)|^2 dx = 1
    \tag{6.9}
\end{equation}

The probability of finding the particle in any finite interval $$ a \leq x \leq b$$ is given by:

\begin{equation}
    \int_{a}^{b} |\Psi(x,t)|^2 dx
    \tag{6.10}
\end{equation}

We have gained an understanding of wave functions and the probability interpretation of matter waves. Now, we will delve into the matter wave equation and its applications.

We begin our study of quantum mechanics by adopting the Schrödinger Equation. We will then explore its application to both unbound and bound states. While many introductory problems in quantum mechanics involve simplified models, these models provide a solid foundation for understanding more complex systems. Even though these simplified models may not perfectly capture real-world phenomena, they offer valuable insights into the fundamental principles of quantum mechanics.

Understanding these simplified cases is crucial, as it allows us to grasp the core concepts and mathematical techniques that are essential for addressing more complex and realistic problems. While real-world applications often involve intricate mathematical and physical considerations, the underlying principles remain rooted in the fundamental concepts introduced in these simplified models. 

## 6.3 The Schrödinger for Free-Particles 
In this section, we will explore the unbound state of a particle, specifically focusing on the free particle scenario. Free particles are characterized by having no potential energy acting on them, leading to solutions of the Schrödinger Equation that describe continuous energy states
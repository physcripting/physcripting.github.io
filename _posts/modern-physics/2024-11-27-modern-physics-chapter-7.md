---
title: "Chapter 7: Quantum Mechanics in Three Dimension"
author: PSK
date: 2024-12-2 14:10:00 +0800
categories: [eTextbooks, Computational-Aided Modern Physics]
math: true
render_with_liquid: false
---

Having laid the groundwork for quantum mechanics in one dimension, we now turn our attention to the more realistic and intricate world of three-dimensional systems. While one-dimensional models offer valuable insights, they are limited in their ability to capture the full spectrum of quantum phenomena.

In this chapter, we will elevate our understanding of quantum mechanics by exploring the Schrödinger equation in three dimensions. We will begin with Cartesian coordinates, a familiar framework, and then transition to spherical coordinates, a more appropriate choice for systems with spherical symmetry. This shift in perspective will allow us to delve into the concept of angular momentum and its profound implications for atomic spectroscopy.

## 7.1 Introduction
A perplexing question arises from classical physics: why don't atoms collapse? If electrons orbited the nucleus like planets around the sun, they would radiate energy and spiral inward, causing the atom to implode. Yet, atoms are incredibly stable, existing for billions of years without disintegration.

Quantum mechanics provides a profound explanation for this stability. It posits that electrons do not orbit the nucleus in well-defined paths, as classical physics would suggest. Instead, they occupy probability clouds, or orbitals, that surround the nucleus. These orbitals are characterized by specific energy levels, and electrons can only transition between these levels by absorbing or emitting photons.

To delve deeper into the quantum nature of atoms, we must extend the Schrödinger equation, a fundamental equation in quantum mechanics, to three dimensions. This extension allows us to explore the intricate wave functions that describe the behavior of electrons in three-dimensional space. By solving the three-dimensional Schrödinger equation, we can determine the allowed energy levels of an atom and the probability distributions of finding electrons in different regions of space.

## 7.2 The Schrödinger Equation in Three Dimensions
In three dimensions the potential energy becomes U(**r**) and the time-dependent wave function, $$\Psi(\textbf{r},t) = \Psi(\textbf{r},t)$$. The Schrödinger equation involves the kinetic energy operator, which in Cartesian coordinates is given by: 

$$\begin{equation*}
   	\frac{p_x^2 + p_y^2 + p_z^2}{2m} \rightarrow -\frac{\hbar^2}{2 m} \left( \frac{\partial^2}{\partial x^2}  + \frac{\partial^2}{\partial y^2}  + \frac{\partial^2}{\partial z^2} \right)
\end{equation*}$$

where  $$ \hat{p}_x \rightarrow  - i\hbar  \frac{\partial}{\partial x}$$, and similarly for $$ \hat{p}_y$$ and $$\hat{p}_z$$. 
  
The time-dependent Schrödinger equation in 3D is then:
  
$$\begin{equation}
    - \frac{\hbar^2}{2 m} \nabla ^2 \Psi (r,t) + U(r) \Psi(r,t) =  i \hbar\frac{\partial}{\partial t} \Psi(r,t)
    \tag{7.1}
\end{equation}$$

Where the Laplacian operator in Cartersian coordinates is given by:

 $$\begin{equation*}
	 \nabla^2 = \frac{\partial ^2}{\partial^2 x} +  \frac{\partial ^2}{\partial^2 y} +  \frac{\partial ^2}{\partial^2 z}
 \end{equation*}$$

While Cartesian coordinates are often used, they are not always the most convenient choice. For systems with spherical symmetry, such as atoms, spherical polar coordinates (r,$$\theta$$,$$\phi$$) are more suitable.Before we delve into the Schrödinger equation in spherical polar coordinates, we will familiarize ourselves with the Schrödinger equation in 3D Cartesian coordinates.

### 7.2.1 Probability Density and Normalization
In one dimension, we consider the probability density per unit length. In three dimensions, we consider the probability density per unit volume. The magnitude squared of the wave function, $$\vert \Psi(r,t) \vert^2 $$,  represents the probability density at position **r** and time **t**: 

$$\begin{equation*}
    P(r,t) = \left|\Psi(r,t)\right|^2
    \tag{7.2}
\end{equation*}$$

For stationary states, the wave function can be separated into a time-independent part $$\psi(r)$$ and a time-dependent part $$e^{-iEt/\hbar}$$. The probability density for a stationary state is then given by:


$$\begin{equation*}
    P(r) = \left|\psi(r)\right|^2
    \tag{7.3}
\end{equation*}$$

The total probability of finding the particle anywhere in space must be equal to one:

$$\begin{equation}
	\int_{\text{all space}}  \left|\Psi(r,t)\right|^2 dV = 1 
    \tag{7.4}
\end{equation}$$

where $$ d V = d x  dy  dz$$ is a volume element. 

### 7.2.2 Stationary States
Stationary states are quantum states for which all probabilities remain constant over time. They are described by wavefunctions that can be separated into a spatial part and a time-dependent part:

$$\begin{equation*}
	\Psi(r,t) = \psi(r) \phi(t) 
    \tag{7.5}
\end{equation*}$$

By substituting this separable form into the time-dependent Schrödinger equation:

$$\begin{equation*}
    - \frac{\hbar^2}{2 m} \frac{1}{\psi(r)}\nabla ^2 \psi (r) + U(r) = i \hbar \frac{1}{\phi(t)} \frac{\partial}{ \partial t} \phi(t)
\end{equation*}$$

We obtain two separate equations:
* Time-Independent Schrödinger Equation:

$$\begin{equation}
    - \frac{\hbar^2}{2 m} \nabla ^2 \psi (r) + U(r) \psi(r) = E \psi(r) 
    \tag{7.6}
\end{equation}$$

This time-independent Schrödinger equation governs the spatial part of the wave function, $$\psi(r)$$, and determines the allowed energy levels E of the system. 

* Time-Dependent Part: 

$$\begin{eqnarray}
    i \hbar \frac{d}{d t} \phi(t) &=& E \phi(t) 
    \tag{7.7}
\end{eqnarray}$$

The solution to this equation is: 

$$\begin{eqnarray}
    \phi (t) &=& e^{-iE t/\hbar} = e^{-i\omega t}
    \tag{7.8}
\end{eqnarray}$$

The time-dependent part, $$\phi(t)$$, describes the time evolution of the wave function and ensures that the probability density $$\vert \Psi(r,t)\vert$$ remains constant over time.

> The stationary states represent quantum states with well-defined energies, and their wavefunctions are products of a spatial part and a time-dependent phase factor.
{: .prompt-info}

### 7.2.3 Particle in 3D  Infinite Well

 where U(**r**) is still the potential energy  but is now a function of all the space: U(**r**) = U(x,y,z).
 
The mathematical function of Schrödinger  equation is the same for any coordinate system.  It will reduce to

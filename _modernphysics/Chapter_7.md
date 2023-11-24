---
layout: list
title: Chapter 7 <br> Quantum Mechanics <br> Bound States 
date: 2023-04-25 10:14:00-0400
description: 
categories: [Phenomena in Atomic Scale, Modern Physics]
giscus_comments: true
related_posts: false
category: Modern Physics
img: assets/img/Chapter-7/C7_1.jpg
toc:
  sidebar: left
---
<head>
	<link href="/assets/css/styles_c7.css" rel="stylesheet" type="text/css">
</head>

This chapter will explore the one-dimensional quantum mechanics, with a primary focus on bound states.  It serves as an introduction to the fundamental concepts starting from wave equations. We embark on this journey by explorating the matter wave equation, famously known as the Schrödinger equation, a powerful tool for describing the behavior of particles in the microscopic realm. Throughout this chapter, our goal is to lay the groundwork for understanding particles confined to a one-dimensional bound state and unravel the fascinating world of quantum mechanics. We will navigate through the complexities of applying the Schr$$\ddot{\text{o}}$$dinger equation to unravel the unique characteristics and behaviors exhibited by particles within this confined spatial domain. let's start the adventure of the fascinating landscape of quantum mechnics!

## 7.1 Introduction

Quantum mechanics is a branch of fundamental physics that studies how nature behaves at the atomic and subatomic levels. The mathematical framework of qunatum mechanics was originated in the early 20<sup> th </sup> century by a group of physicists such as Erwin Schrödinger, Werner Heisenberg, Max Born, Paul Dirac. It has revolutionized our understaning of the physical world, revealing phenomena that beyond the scope of classical mechanics, such as the wave-particle duality, the uncertainty principle, and the superposition of states.

The wave-particle duality, a key conceopts in quantum mechancis,  states that matter can behave as both a wave and a particle, depending on how it is observed. For example, electrons can act as waves when they pass through a double slit, creating an interference pattern, or as particles when they hit a screen, leaving discrete spots. This means that matter has no definite properties until it is measured, and that different measurements can yield different outcomes.

Another important concept of quantum mechanics is the uncertainty principle, which states that there is a limit to how precisely we can know certain pairs of properties of a quantum system, such as its position and momentum, or its time and energy. The more we know about one property, the less we know about the other. This is not due to any lack of measurement accuracy, but rather to the inherent nature of quantum reality. The uncertainty principle implies that there is always some randomness and unpredictability in the quantum world.

One of the most influential physicists in the development of quantum mechanics was Erwin Schrödinger, who formulated the wave equation, a fundamental equation that describes how the wave function of a quantum system evolves over time. The wave function is a mathematical object that contains all the information about the possible states and outcomes of a quantum system. By solving the Schrödinger equation, we can find the wave function and use it to calculate the probability of finding a particle in a certain region of space, or the probability of a particle having a certain energy level, or any other observable quantity. The Schrödinger equation is a powerful tool for exploring the mysteries of the microscopic world.


Founded on the principle of wave-particle duality, quantum mechanics postulates that matter exhibits both wave-like and particle-like behavior. The theory introduces uncertainty, asserting the impossibility of simultaneously knowing certain properties, such as position and momentum or time and energy, with absolute precision. 

Schrödinger contribution was notably impactful, particularly in formulating the wave equation, a crucial tool for unraveling microscopic mysteries. The Schrödinger equation, a partial differential equation, characterizes the isolated physical systems in the quantum world.  The wave function, derived  Schrödinger equation, evolves over time, provides a probabilistic description of where a particle is likely to be found.

The quantum mechanics illustrates the concept of superposition. Schrödinger’s cat is a thoughtful experiment to describe the superposition. It envisions a cat that may be simultaneously both alive and dead states states—a quantum superposition—linked to a random subatomic event that may or may not occur. The exact state reamins unknow until observed. Quantum mechanics has revolutionized our understanding of reality, influencing everything from the behavior of atoms and molecules to technological advancements. It finds applications in various fields, including semiconductors, lasers, quantum field theory, quantum technology, and quantum information science.

In contrast to Newton's mechanics, which describes  particle interactions with the environment using forces, Schrödinger's approach  incorporates potential energy. While the Schrödinger equation doesn't offer a trajectory, its solution, the wave function ($$\Psi(x,t)$$), encapsulates wavelike behavior, shaping our understanding of particles in quantum realm. Determining the wave function of matter ( $\Psi (x,t)$), similar as treating waves, involves solving wave equations. In the following section, we will delve into wavefunction and their applications.

## 7.2 Wavefunctions and Probablities 

Let's recall the matter wave from previous chapter:
\begin{equation*}
  v_{wave} = f \lambda = \frac{E h}{h p} = \frac{E}{p}
\end{equation*}
Wave velocity is  referred as the phase velocity and particle velocity referred to as group velocity.
We can merely stressed that $v_{particle}\neq f\lambda$, but  electromagnetic radiation, E, can be related
\begin{equation*}
  E=  h f = \frac{hc}{\lambda}  \ \ \text{and}  \ \ p =\frac{h}{\lambda} = \frac{hf}{c}
\end{equation*} 
and for particle
\begin{equation*}
  E=  h f \neq \frac{hc}{\lambda}  \ \ \text{and}  \ \ p =\frac{h}{\lambda} \neq \frac{hf}{c}
\end{equation*} 

$v_{p}$ is not represent the particle velocity, but photon $v_p$ is the velocity of the photon. 

## 7.3 Schrödinger equation
The Schrödinger equation is a partial differential equation that describes the dynamics of quantum mechanical systems via the wave function. It is named after Erwin Schrödinger, who postulated the equation in 1925 and published it in 1926, forming the basis for the work that resulted in his Nobel Prize in Physics in 1933. The equation gives the evolution over time of a wave function, the quantum-mechanical characterization of an isolated physical system.

The Schrödinger equation is a linear partial differential equation that governs the wave function of a quantum-mechanical system. It is not the only way to study quantum mechanical systems and make predictions. Other formulations of quantum mechanics include matrix mechanics, introduced by Werner Heisenberg, and the path integral formulation, developed chiefly by Richard Feynman.

```yml
Syntax:
  print("Hello, World!")
```
<iframe src="https://trinket.io/embed/python/57becc7f99" width="90%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

<!-- [bootstrap-toc](https://afeld.github.io/bootstrap-toc/) 

```yml
toc:
  sidebar: left
```

-->



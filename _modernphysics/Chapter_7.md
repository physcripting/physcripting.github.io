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

One of the key concepts in quantum mechanics is superposition, which means that a particle can exist in a combination of two or more possible states until it is measured. For example, an electron can be in a superposition of spinning up and spinning down, or a photon can be in a superposition of horizontal and vertical polarization.

To illustrate the idea of superposition, the Austrian physicist Erwin Schrödinger proposed a thought experiment in 1935. He imagined a scenario where a cat is placed in a sealed box with a radioactive atom, a Geiger counter, a hammer, and a flask of poison. The radioactive atom has a 50% chance of decaying in one hour, and if it does, the Geiger counter will detect it and trigger the hammer to break the flask, releasing the poison and killing the cat. If the atom does not decay, the cat will remain alive. According to quantum mechanics, the atom is in a superposition of decayed and undecayed states until it is observed, and so is the cat, which is in a superposition of alive and dead states. The exact state of the cat is unknown until the box is opened and the cat is observed.

Schrödinger’s cat is a paradoxical experiment that challenges the common sense notion of reality and shows the difficulty of applying quantum mechanics to everyday objects. It also raises questions about the role of observation and measurement in determining the outcome of quantum events. Schrödinger’s cat is one of the most famous and controversial examples of quantum phenomena in popular culture-linked to a random subatomic event that may or may not occur. The exact state reamins unknown until observed. 

One of the most influential physicists in the development of quantum mechanics was Erwin Schrödinger, who formulated the wave equation, a fundamental equation that describes how the wave function of a quantum system evolves over time. The wave function is a mathematical framework that contains all the information about the possible states and outcomes of a quantum system. By solving the Schrödinger equation, a partial differential equation, we can find the wave function and use it to calculate the probability of finding a particle in a certain region of space, or the probability of a particle having a certain energy level, or any other observable quantity. The Schrödinger equation is a powerful tool for exploring the mysteries of the microscopic world.

Newton's mechanics, classical theory of physics, describes how objects move and interact with environments. It uses the concept of force to describe how an object's motion changes when it is affected by  another object or a field shch as gravity or electromagnetism. It can predict the trajectory of an object, which is the path it follows in space and time. However, Schrödinger's approach  describes how microscopic particles such as atoms and subatoms behave and interacti with ponential energy. It uses the concept of potential energy to describe how an object’s motion depends on its position in a field, such as an electric or magnetic field. Schrödinger’s mechanics cannot predict the trajectory of a particle, but it can find the wave function of a particle, which is a mathematical function that gives the probability of finding the particle in a certain state.

The wave function ($$\Psi(x,t)$$), captures the wavelike  of a particle, which means that it can interfere, diffract, and tunnel through barriers. The wave function shapes our understanding of the quantum realm. The wave function of a particle can be found through solving the Schrödinger’s equation. Schrödinger’s equation is similar to the wave equations that describe other types of waves, such as sound waves or light waves, but it also incorporates the effects of quantum mechanics, such as the uncertainty principle and the superposition principle. A wave equation is a mathematical equation that describes how a wave changes over time and space. 

Quantum mechanics is a fascianting branch of physics that has revolutionized our understanding of nature at the smallest scales.  It reveals how atoms and molecules behave in ways that are very different from our everyday experience. It also leads to amazing inventions that have changed our world, such as semiconductors, lasers, and quantum computers. Quantum mechanics has many applications in different areas of science and technology. In the next section, we will learn more about one of the most important concepts in quantum mechanics: the wave function

## 7.2 Wavefunction and Probablit 
The wave function is a mathematical function that describes the state of a quantum system, such as a particle or a molecule. It tells us the probability of finding the system in a certain position, momentum, energy, or any other observable property. The wave function also shows us how the system evolves over time and how it interacts with other systems. The wave function is the key to understanding and applying quantum mechanics.

Undestanding the wave equation is vital before delving into the cencept of matter wave. In the 18<sup>th</sup> century, many scientists, including Jean le Rond d'Alembert, Leonhard Euler, Daniel Bernoulli, and Joseph-Louis Lagrange, studied the vibration of strings in a musical instrument. The one-dimensional wave equation, a significant development in this context, was first derived by the French scientist d'Alembert in 1746. A decade later, Euler expanded this understanding by introducing the three-dimensional wave equation. To provide a glimpse into the mathematical representation, let's consider the wave equation for transverse waves in one dimension:


\begin{equation}
   \frac{\partial^2 y(x,t)}{\partial t^2} = v^2  \frac{\partial^2 y(x,t)}{\partial x^2}
\end{equation}

where the wave travel with the speed of $v$ and transverse displacement of the wave function as a function of position and time is $$y(x,t)$$.  All wave equations are based on fundamental second law of motion. So, wave on string must obey a wave equation derivable from the fundamental mechanical law $$F= ma $$, see appendix.




## 7.3 Schrödinger equation
The Schrödinger equation is a partial differential equation that describes the dynamics of quantum mechanical systems via the wave function. It is named after Erwin Schrödinger, who postulated the equation in 1925 and published it in 1926, forming the basis for the work that resulted in his Nobel Prize in Physics in 1933. The equation gives the evolution over time of a wave function, the quantum-mechanical characterization of an isolated physical system.

The Schrödinger equation is a linear partial differential equation that governs the wave function of a quantum-mechanical system. It is not the only way to study quantum mechanical systems and make predictions. Other formulations of quantum mechanics include matrix mechanics, introduced by Werner Heisenberg, and the path integral formulation, developed chiefly by Richard Feynman.


<iframe src="https://trinket.io/embed/python/57becc7f99" width="90%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

<!-- 

```yml
toc:
  sidebar: left
```

-->



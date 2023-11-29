---
layout: list
title: Chapter 7 <br> Quantum Mechanics <br> Bound States 
date: 2023-04-25 10:14:00-0400
description: 
categories: [Phenomena in Atomic Scale, Modern Physics]
giscus_comments: true
related_posts: false
category: Modern Physics
importance: 7
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

## 7.2 Wavefunction and Probablity
The wave function is a mathematical function that describes the state of a quantum system, such as a particle or a molecule. It tells us the probability of finding the system in a certain position, momentum, energy, or any other observable property. The wave function also shows us how the system evolves over time and how it interacts with other systems. The wave function is the key to understanding and applying quantum mechanics.

### Classical Waves 
Undestanding the wave equation is crucial before delving into the cencept of matter wave. In the 18<sup>th</sup> century, many scientists, including Jean le Rond d'Alembert, Leonhard Euler, Daniel Bernoulli, and Joseph-Louis Lagrange, studied the vibration of strings in a musical instrument. A pivotal moment in comprehending wave phenomena occurred with the derivation of the one-dimensional wave equation by the French scientist d'Alembert in 1746. This marked a significant step in unraveling the principles of waves. Euler further expanded this understanding a decade later by introducing the three-dimensional wave equation. To offer a glimpse into the mathematical representation, let's examine the wave equation for transverse waves in one dimension:

\begin{equation}
   \frac{\partial^2 y(x,t)}{\partial t^2} = v^2  \frac{\partial^2 y(x,t)}{\partial x^2}
\end{equation}

where y is the displacement of the string, t is the time, x is the position along the string, and $$v$$ is a constant that depends on tension and density of the string. 

This equation describes how the displacement of string in $$y(x,t)$$ direction (transverse displacement) changes with time and position, and it can be solved for different initial and boundary conditions to obtain various waveforms. If the string is oscillated at one end with a sinusoidal function, the solution is a sinusoidal wave that propagates along the string with frequency $$f$$ and wavelength $$λ$$, such that $$ v = f \lambda $$. The wave equation can also be generalized to higher dimensions and other types of waves, such as electromagnetic waves, sound waves, and water waves.

Let's discuss the Electromagnetic waves which is difference from waves on string. The electromagnetic waves consist two parts of wave equation, one for electric field and another one for magnetic field. Both of them ($$EM$$ waves) obey wave equations, which are derivable from fundamental laws of electricity and magnetism.

Let's consider EM waves move x-direction, and oscillation of $$E$$  field along y and $$B$$ along z. So the wave equation is:
$$
\begin{eqnarray}
	 \frac{\partial ^2 E_y}{\partial t^2} &=& 	c^2  \frac{\partial ^2 E_y}{\partial x^2} \nonumber \\
	 \frac{\partial ^2 B_z}{\partial t^2}  &=& c^2 \frac{\partial ^2 B_z}{\partial x^2} 
\end{eqnarray}
$$
Solution of EM waves are
$$
\begin{eqnarray}
	E(x,t) &=&  E_m \sin(k x -  \omega t)\hat{y}  \nonumber\\
	B(x,t)&=& B_m \sin(k x -  \omega t)\hat{z}
\end{eqnarray}
$$

where $$\omega/k = c$$ and $$c = 1/ \sqrt{\varepsilon_0 \mu_0} $$ and $$E_m /B_m =c$$. Here, $$ \varepsilon_0  (\approx 8.85 \times 10^{-12} F/m )$$ is  electric permittivity and  $$\mu_0 (= 4\pi \times 10^{-7} N/A^2)$$ is magnetic permeability in free space. The above equations are described the oscillating electric and magnetic field vary with position and time.  We will extend our knowledge from EM waves to matter matter wave equation. 

### Matter Waves
The matter wave equation is a concept in quantum mechanics that describes the behavior of matter, particularly at the atomic and subatomic levels. It is fundamentally related to the wave equation, which is a mathematical description of wave-like phenomena, including classical waves such as those seen in physics and engineering.

The matter wave equation is often associated with the de Broglie wavelength $$\lambda  = h /p$$, which is a key concept in quantum mechanics. The matter wave equation, Schrödinger equation, describes how the quantum state of a physical system changes over time.  Similar to classical waves,  wave function $$\Psi(x,t) $$ satisfy the second order differential wave equation. It obeys the  Schrödinger wave equation. For the sake of simplicity, we will first consider the special case of "free particle," and later, we will consider the effects of  external forces. In the absence of external forces,  the Schrödinger equation is given by:

\begin{equation}
   i \hbar \frac{\partial \Psi(x,t)}{\partial t} = - \frac{\hbar^2}{2 m} \frac{\partial^2 \Psi(x,t) }{\partial x^2}  
\end{equation}

Here, $$\Psi(x,t)$$ is the wave function representing the quantum state of a particle as a function of both position (x) and time (t). The terms $$\hbar$$ is related to the reduced Planck constant and m is the mass of the particle.  In the wave equation for the string, $$y(x,t)$$ represents the displacement of the string, analogous to the wave function $$\Psi(x,t)$$ in the Schrödinger equation. The wave velocity $$v$$ in the string equation can be associated with the velocity of the quantum state described by the matter wave in the Schrödinger equation. It's important to note that this analogy provides an intuitive connection between classical wave mechanics and quantum mechanics, but the actual derivation and understanding involve more complex mathematical and physical considerations. 

\begin{equation}
  \text{probability density} = \left|\Psi(x,t)\right|^2
    \label{eq:0610}
\end{equation}

For wave nature of particle (matter waves), we use the wave function to describe the motion of particle. The symbol wave function $$\Psi(x,t)$$  is chosen to describing the oscillating probability and it is normally referred to as \textbf{probability amplitude.}



First, its form is certainly  not intuitively  obvious, so it is natural to hope  a derivation from first principles. 

By Analogy, Maxwell's equations, which cannot be derived or proved, will remain accepted laws so as long as we discover no situation in which  they are violated.  Although the SSchrödinger equation cannot be derived, we may argue that it is at least plausible and we will proof it from energy conservation. 

Here, Schrödinger involves complex number ($$i =\sqrt{-i}$$) which can distress and alienates some of the students from QM. The matter waves is not directly observable and cannot represented by a single real function; like electromagnetic waves.  QM could be formulated  without complex number, however which are the easiest way to handle the two parts. It is simply a matter of convenience. 


For example,   force in Maxwell equation is written as $$F = E + i c B $$ and four equations become two where the plane wave functions of E and B become one wave function. In matter wave, two real wave are $$ \Psi_1 $$ and $$\Psi_2$$. They obey the real wave equations and  link them together as $$ \Psi \equiv \Psi_1 + i \Psi_2 $$.  The following table compare the EM waves and matter waves equations: 

The following tables compare the EM waves and wave function. Since the electric and magnetic field do have different "personalities", they will be treated separately by taking the real approach to electromagnetic waves. On the other hand, no similar distinction between $$\Psi_1$$ and $$\Psi_2$$, we will take the complex approach which is easy.  There is not need to worry about the physical interpretation because the wave function cannot detect physically. Experimentally, we detect the probability density which is the real quantity whether real or complex approach is take
## 7.3 Schrödinger equation
The Schrödinger equation is a partial differential equation that describes the dynamics of quantum mechanical systems via the wave function. It is named after Erwin Schrödinger, who postulated the equation in 1925 and published it in 1926, forming the basis for the work that resulted in his Nobel Prize in Physics in 1933. The equation gives the evolution over time of a wave function, the quantum-mechanical characterization of an isolated physical system.

The Schrödinger equation is a linear partial differential equation that governs the wave function of a quantum-mechanical system. It is not the only way to study quantum mechanical systems and make predictions. Other formulations of quantum mechanics include matrix mechanics, introduced by Werner Heisenberg, and the path integral formulation, developed chiefly by Richard Feynman.

Testing 2
Testing 3

<iframe src="https://trinket.io/embed/python/57becc7f99" width="90%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

<!-- 

```yml
toc:
  sidebar: left
```

-->



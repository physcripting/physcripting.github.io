---
title: "Chapter 5: Wave Nature of Particles "
author: PSK
date: 2024-11-28 14:10:00 +0800
categories: [eTextbooks, Modern Physics]
math: true
render_with_liquid: false
---

In previous chapters, we've explored the atomic composition of matter and the particle-like behavior of photons. A natural question arises: if photons can exhibit particle-like properties, could particles, like electrons, also display wave-like behavior? To delve into this intriguing possibility, we'll examine de Broglie's hypothesis of matter waves and its experimental verification. Furthermore, we'll extend our discussion to incorporate wave mechanics and the uncertainty principle as foundational concepts of quantum theory. 

## 5.1 Introduction
The concepts of particles and waves are fundamentally different. Classical mechanics treats particles as localized objects with well-defined positions and momenta. Waves, on the other hand, are extended entities characterized by properties like wavelength, frequency, and amplitude.

Quantum mechanics introduces the idea of wave-particle duality, which means that particles can exhibit both particle-like and wave-like behavior. The double-slit experiment, which we will explore in the next chapter, is a classic example of this duality. When electrons are fired at a screen with two slits, they produce an interference pattern, which is a characteristic of wave-like behavior. However, when detected, they are always found at a specific point on the detector, indicating particle-like behavior.

Quantum mechanics is fundamentally based on probabilities. The wavefunction, describing the particle's  quantum state, provides information about the probability of finding the particle in a particular state or location. The concept of wavefunction collapse, while often used to explain the transition from a superposition of states to a definite measurement outcome, is still a topic of debate and research.  Some interpretations offer different explanations without using wavefunction collapse.

This chapter delves deeper into the wave nature of particles and explore how it influences their motion and interaction. We will learn the de Broglie hypothesis to explain the wave nature of particles and the quantization of angular momentum. We will use the Fourier transform to build wave packets and learn about group and phase velocity. Finally, we will discuss the Heisenberg uncertainty principle, a fundamental principle of quantum mechanics that sets limits on the precision with which certain physical quantities can be measured.

## 5.2 De Brogile Wavelenght and Matter 
We have learned that electromagnetic (EM) waves, like light, exhibit a fascinating dual nature: they can behave as both particles (quanta) and waves.  This raises a fundamental question: What is the underlying reality? Is this duality unique to EM radiation, or does it extend to all matter? This profound question was raised by **Louis de Broglie**, in 1924 and who proposed a groundbreaking hypothesis that fundamentally challenged the classical distinction between particles and waves.

In his doctoral dissertation, de Broglie introduced the revolutionary idea that:

> Since photons exhibit both wave and particle characteristics, perhaps all forms of matter also possess wave-like properties in addition to their particle nature
{: .prompt-info }

Louis de Brogile proposed that all moving object obey the same rule as waves:

\begin{equation}
	\lambda = \frac{h}{p} = \frac{h}{m v}
	\tag{5.1}
\end{equation}

where:
* $$ \lambda $$ is the de Broglie wavelength, 
* $$h$$ is Planck's constant, 
* $$p$$ is the momentum of the particle, and
* $$ m = \gamma m_o =  \frac{m_o}{\sqrt{1-v^2/c^2}}$$ is the relativistic mass of the particle, with $$m_0$$ as the rest mass, $$v$$ as the velocity of the particle, and $$c$$ as the speed of light.

We can see that the greater the momentum of an object, the smaller its wavelength. If a particle has a wavelength, it should exhibit wave-like phenomena such as interference and diffraction.

While the concept of relativistic mass is often used, it is not essential for understanding the wave-particle duality. The key point is that all matter exhibits both particle-like and wave-like behavior, and the de Broglie wavelength provides a quantitative measure of the wave-like nature of matter.

De Broglie's hypothesis was experimentally confirmed by the diffraction of electrons, as demonstrated by Davisson and Germer in 1927. We will learn in the following secition. This discovery established the wave-particle duality as a universal principle, applying not just to photons but to all matter, from subatomic particles to macroscopic objects under certain conditions. It laid the foundation for modern quantum mechanics. 

### 5.2.1 Probablity Density and De Broglie Wave Function
The question arises: does the amplitude of the de Broglie wave have physical significance? To address this, we turn to quantum mechanics, which provides a framework for understanding such phenomena.

In quantum mechanics, the de Broglie wave function $$\Psi(x,t)$$ is a mathematical representation of a particle's quantum state. The probability of finding a particle at a specific location in space is proportional to the square of the magnitude of its wave function. This relationship is expressed as:

$$\begin{equation}
	\text{Probability density} \propto |\Psi(x,t)|^2
	\tag{5.2}
\end{equation}$$

Here, $$\Psi(x,t)$$ represents the complex-valued de Broglie wave function, where $$\vert \Psi(x,t) \vert^2$$ is its square magnitude—a real, non-negative quantity. This probabilistic interpretation is central to quantum mechanics and distinguishes it from the deterministic framework of classical mechanics.

> **Analogy with Eletromagnetic Waves**: This concept is analogous to electromagnetic waves, where the intensity of light is proportional to the square of the electric field amplitude. Similarly, in quantum mechanics, $$\vert \Psi{x,t} \vert^2$$ gives the probability density, connecting the amplitude of the wave function to measurable outcomes.
{: .prompt-tip}

> **Fundamental Shift in Perspective**: The amplitude of a de Broglie wave does not directly indicate physical properties such as mass or charge. Instead, the square of its magnitude represents the probability of finding a particle in a specific region. This transition from deterministic to probabilistic interpretations underscores the revolutionary nature of quantum mechanics and its significant shift from classical physics.
{: .prompt-info}

<div class="example">
    <div class="example-title">Example 5.1. de Broglie Wavelength</div>
    <div class="example-content">
		Determine the de Broglie wavelength of the following particles:
		<ol type="i">
			<li> 1-gram marble moving at 1 m/s.</li>
			<li>An electron with a kinedic energy of 1 ev.</li>
			<li>An electron with a kinetic energy 100 MeV.</li>
		</ol>
	</div>
</div>	


### 5.2.2 De Brogile Explanation 
If electron behave likes wave (from De Brogile assumption), then the electron waves should generate a standing wave  in the orbit when it move around the atom.  Here, Bohr orbit arise due the electron matter waves interfere constructively when an integral number of wavelength exactly fits into the circumference or a circular orbit. 

$$
\begin{equation}
	n \lambda = 2 \pi r
	\tag{5.3}
	\label{eq:5-3}
\end{equation}
$$ 

can be referenced as \eqref{eq:5-3}
## 5.3 Experimental Verificaiton


This was experimentally verified later. This idea  is the key for the development of modern theory called  **Quantum Mechanics** by Heisenberg, Schroedinger, Born, Paul, Dirac and so on.



If an object appears "wavelike", it should exhibit interference or diffraction. For both  interference or diffraction, it is required  that the scattering objectors and apertures need to almost  the same size as the wavelength. Before proceed scattering experiment,  let's look at example to understand the de Brogile wavelength in our life:
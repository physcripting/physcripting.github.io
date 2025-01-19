---
title: "Chapter 3: Quantum Phenomena of Light "
author: PSK
date: 2024-12-1 14:10:00 +0800
categories: [eTextbooks, Computational-Aided Modern Physics]
math: true
render_with_liquid: false
---

This chapter explores the particle-like nature of light, delving into groundbreaking experiments that revolutionized our understanding of quantum mechanics. We will examine Planck's blackbody radiation law, which introduced the concept of quantized energy, and the photoelectric effect, providing compelling evidence for the particle nature of light, known as photons. Additionally, we will delve into the production of X-rays, Compton scattering, and the gravitational influence on photons, further solidifying our comprehension of light's quantum behavior.

## 3.1 Introduction
One of key milestone in physics was the development of classical electromagnetism. James Clerk Maxwell unified the previously separate fields of electricity and magnetism, fomulating his famous **Maxwell's equations** in the mid-19<sup>th</sup> century.hese equations mathematically describe the behavior of electric and magnetic fields and established that light is an electromagnetic wave. This discovery not only unified physical phenomena but also laid the foundation for modern technologies such as radio, radar, and telecommunications.


While classical physics, including Newtonian mechanics and Maxwell's electromagnetism, provided a robust framework for understanding the macroscopic world, it proved inadequate for explaining the behavior of the microscopic world, such as the interactions within atoms and molecules. These limitations became apparent at the end of the 19<sup>th</sup> century, as experimental observations began to diverge from classical predictions.
 
Contrary to a common misconception, the Quantum Revolution, which deeply transformed physics, did not originate with special relativity or Maxwell's theory but began with Max Planck's work on black-body radiation in 1900. Planck introduced the radical concept of energy quantization, proposing that energy is emitted or absorbed in discrete packets called **quanta**. 
This marked a fundamental departure from classical physics, resolving the "*ultraviolet catastrophe*" that classical theories could not explain.

Building upon Planck's groundbreaking insight, Albert Einstein extended the concept of quantization to light in 1905, postulating that light energy exists in discrete packets called photons. Einstein's work on the photoelectric effect provided compelling evidence for the particle-like nature of light and earned him the Nobel Prize in Physics in 1921. This revolutionary idea challenged the classical wave theory of light and established a dual wave-particle nature.

The subsequent development of quantum mechanics, rooted in the pioneering contributions of Planck and Einstein, fundamentally transformed our understanding of the physical universe. Quantum mechanics has since enabled scientists to explain a wide range of phenomena, from the structure and behavior of atoms and molecules to the properties of light and matter, catalyzing advancements in fields such as chemistry, materials science, and information technology.

## 3.2 Confirming Light's Electromagnetic Nature
Maxwell's theory of electromagnetism predicted the existence of electromagnetic (EM) waves that would behave in all respects like light. These EM waves were expected to exhibit wave-like properties such as reflection, refraction, polarization, and interference. Moreover, they were predicted to travel through a vacuum at the speed of light, approximately  $$3.0 \times 10^8 \ m/s$$.

Direct experimental verification of Maxwell's hypothesis was challenging due to the limitations in generating high-frequency electric oscillations. During Maxwell's time, the highest attainable frequencies were around ($$10^9$$) Hz, significantly lower than the frequencies of visible light, which range from 300 nm to 800 nm approximately ($$10^{15}$$ Hz to 3.75 $$\times 10^{14}$$ Hz).

In 1887, Heinrich Hertz conducted a series of groundbreaking experiments that confirmed Maxwell's theory that light is an electromagnetic wave. His experimental setup (shown in Figure) involved a spark gap oscillator that generated high-frequency oscillations (~ $$5 \times 10^8$$ Hz). The radiation emitted by the oscillator was detected by a simple loop antenna receiver, even at considerable distances. Hertz demonstrated that these electromagnetic waves, often referred to as Hertzian waves, exhibited properties similar to light, including reflection, refraction, polarization, and interference.

Hertz's experiments provided compelling evidence for the electromagnetic nature of light. This groundbreaking work, along with the discovery of the Zeeman effect by Pieter Zeeman in 1896, solidified the acceptance of Maxwell's theory among the scientific community. The Zeeman effect, which observed the splitting of spectral lines in the presence of a strong magnetic field, further validated the connection between light and electromagnetism.

These experimental evidences were a resounding victory for Maxwell and his equations, which accurately predicted the behavior of electromagnetic waves. The classical model of light emission, which involved oscillating charges radiating electromagnetic waves, gained widespread acceptance at the time.

However, the classical model faced a significant challenge in the early 1900s: the ultraviolet catastrophe. This problem arose from the classical prediction that a black body would emit an infinite amount of energy at short wavelengths. This prediction starkly contradicted experimental observations. The resolution of this problem would ultimately lead to the development of quantum mechanics, a revolutionary theory that fundamentally changed our understanding of the nature of light and matter. In the following section, we will explore blackbody radiation in more detail.

## 3.3 Black Body Radiation
A perfect blackbody is an idealized object that absorbs all incident radiation, regardless of its wavelength or angle of incidence. A cavity with a small opening can be a good approximation of a blackbody, as light entering the cavity is repeatedly reflected and absorbed by the cavity walls, as shown in Figure.

At room temperature, the thermal radiation emitted by a blackbody is primarily in the infrared (IR) region of the spectrum. However, as the temperature of the blackbody increases, it begins to emit visible light. This phenomenon can be illustrated by plotting the intensity of radiation emitted by a blackbody against wavelength at different temperatures, as shown in Figure. As the temperature rises, the peak of the radiation curve shifts to shorter wavelengths, and the overall intensity of the radiation increases.

British photographer and inventor Thomas Wedgwood first observed the universal nature of thermal radiation in 1792. He noticed that objects of different materials emitted light of similar colors when heated to the same temperature. This early observation, along with later advancements in spectroscopy, provided further evidence for this fundamental principle of thermal radiation.

### 3.3.1 Kirchhoff's Law of Thermal Radiation
In 1859, Gustav Kirchhoff formulated fundamental pricicple of thermal radiation, known as **Kirchhoff's Law of Thermal Radiation**. This law states that, for any arbitrary body in thermodynamic equilibrium, the emissivity (the power emitted per unit area) is equal to the absorptivity (the fraction of incident power absorbed) at each wavelength.

Kirchhoff's law led to the concept of a thermal radiation, and the mathematical formulation of the power emitted per unit area per unit frequency by a an object. This emitted power, denoted as $$e_f$$, can be expressed as: 

$$\begin{equation}
	e_f = J(f,T) A_f
    \tag{3.1}
    \label{eq:3-1}
\end{equation} $$

where:
* $$J(f,T)$$ is a universal function, known as the spectral radiance of a blackbody, which depends only on the frequency $$f$$ of the radiation and the absolute temperature $$T$$ of the blackbody.
* $$A_f$$ is the absorptivity or the fraction of the incident power absorbed per unit area per unit frequency by the heated object.


A perfect blackbody is an idealized object for which  $$A_f =1$$. This means the absorbes all incident radiation, regardless of its wavelength or angle of incidence and also emits radiation at the maximum possible rate for any object at a given temperature.  For a perfect blackbody, the quation \ref{eq:3-1} simplifies to:  

$$\begin{equation}
	e_f = J(f,T)
    \tag{3.1}
    \label{eq:3-2}
\end{equation} $$

The universal nature of blackbody radiation, first observed by Thomas Wedgwood, is consistent with Kirchhoff's Law. This universality indicates that the spectral distribution of blackbody radiation depends solely on the temperature of the object and not on its material composition. This fundamental property of blackbody radiation has played a crucial role in the development of quantum mechanic, providing key insights into the nature of light and matter.

### 3.3.2 Stefan-Boltzmann Law
Australian Physicist Jose Stefan (1853-1893) experimentally determined in 1879 that:  
> The total power per unit area emitted by a blackbody at all frequencies is proportional to the fourth power of its absolute temperature. 
{: .prompt-info}

This relationship, known as the Stefan-Boltzmann Law, is expressed as: 

$$\begin{equation}
	e_{total}= \int_{0}^{\infty} e_f df = \sigma T^4
    \tag{3.3}
\end{equation}$$

where:
* $$e_{total}$$ is the power emitted per unit area by the blackbody,
* $$e_f$$ is the power per unit area per unit frequency by blackbody,
* $$\sigma$$ is the Stefan-Boltzmann constant, approximately $$ 5.67 \times 10^{-8} W.m^{-2}.K^{-4}$$,
* $$T$$ is the absolute temperature of the blackbody.

For non-ideal radiators (commonly referred as gray bodies), the total power emitted per unit area can be expressed as:

$$\begin{equation}
	e_{total} = a \ \sigma T^4
    \tag{3.4}
\end{equation}$$

Where $$a$$ is the emissivity of the object, a dimensionless number between 0 and 1.

Within five years of Stefan's experimental discovery, Ludwig Boltzmann (1844–1906) provided a theoretical derivation of the Stefan-Boltzmann Law. His work demonstrated its foundation in thermodynamic principles and its connection to the electromagnetic nature of light, further solidifying its importance in the study of radiative heat transfer.

### 3.3.3 Wien's Displacement Law
If we examine the emission spectrum of a glowing object, as depicted in the figure, we observe that the peak wavelength ($$\lambda_{max}$$) of the blackbody radiation shifts towards shorter wavelengths as the temperature of the blackbody increases. This phenomenon aligns with Wedgwood's earlier observation.

This behavior was explained by the German physicist Wilhelm Wien (1864-1928). He postulated that 
> The peak wavelength ($$\lambda_{max}$$) at which the emitted intensity reaches its maximum value is inversely proportional to the absolute temperature of the blackbody.
{: .prompt-info}

Wien's Displacement Law is mathematically expressed as:

$$\begin{equation*}
	\lambda_{max}  \propto \frac{1}{T}
\end{equation*}$$

 and can be written as:

$$\begin{equation}
	\lambda_{max} * T = 2.898 \times 10^{-3} m.K
     \tag{3.5}
\end{equation}$$

It's important to note that Wien's Displacement Law, while correctly predicting the shift in peak wavelength with temperature, did not fully describe the entire spectral distribution of blackbody radiation.  The emitted power is not uniformly distributed across all frequencies. The specific distribution of energy across different frequencies was later described by Max Planck, who introduced the concept of quantization of energy, a fundamental concept in quantum mechanics.

### 3.3.4 Classical Theory of Thermal Radiation
Before delving into the quantum theory of blackbody radiation, let's briefly review classical wave theories of electromagnetism and thermodynamics. We'll examine how these theories explain the relationship between intensity ($$I$$) and wavelength ($$\lambda$$).

Previously, we explored blackbody radiation in terms of spectral radiance ($$J(f, T)$$), which represents the power emitted per unit area, per unit frequency. However, for practical applications, it's often more convenient to consider the spectral energy density ($$u(f, T)$$ or $$u(\lambda, T)$$), which is the energy per unit volume, per unit frequency (or wavelength).

Let's consider the spectral energy density, $$u(\lambda)$$, which represents the energy per unit volume per unit wavelength interval. The energy per unit volume within the wavelength range from $$\lambda $$ to $$\lambda + d\lambda$$ is given by $$u(\lambda)d\lambda$$.

To establish the relationship between $$u(\lambda)$$ and $$J(\lambda)$$, we can imagine a small hole in a cavity filled with blackbody radiation. Half of the radiation within the cavity is moving towards the hole, while the other half is moving away. To calculate the intensity (power per unit area) emitted through the hole, we need to consider the radiation that is perpendicular to the hole's surface.

By averaging over all angles, we find that the intensity is related to the energy density by the following equation:

$$\begin{equation}
	 J(\lambda, T) = \frac{c}{4} u(\lambda, T)
     \tag{3.6}
\end{equation}$$

where:
* $$J(\lambda, T)$$ is the spectral radiance,
* $$u(\lambda, T)$$ is the spectral energy density,
* $$c$$ is the speed of light

This equation establishes a fundamental connection between the spectral radiance and the spectral energy density of blackbody radiation and derivation can be found in **Appendix**.

#### 3.3.4.1 Wien's Expontential Law
We have seen in the example that for cavity radiation is isotopic and unpolarized, the relation between power density per unit area  and energy density per unit volume is:

$$\begin{eqnarray}
 	J(f,T) &=& \frac{c}{4} u(f,T)  \nonumber \\
 		\text{or } &&  \nonumber\\
    J(\lambda,T) &=& \frac{c}{4} u(\lambda,T) 
\end{eqnarray}$$

It distribution can be  measured and described  by the intensity per wavelength interval $$J(\lambda)$$.  The total intensity emitted in the region  between wavelength $$\lambda_1$$ and $$\lambda_2$$

$$\begin{equation*}
	I(\lambda_1,\lambda_2) = \int_{\lambda_1}^{\lambda_2} J(\lambda) d\lambda
\end{equation*} $$

The total emitted intensity can be found by integrating over all wavelengths:

$$\begin{equation*}
	I = \int_{0}^{\infty} J(\lambda) d\lambda
\end{equation*} $$

In 1893, {\color{blue} Wien estimate the universal function $$u(f,T)$$ based on Maxwell's velocity distribution for gas molecules.}

$$\begin{equation}
	u(f,T) = A f^3 e^{-\frac{\beta f}{T}}
\end{equation}$$

Where A and $$\beta$$ are constant. 

German spectroscopist Friedrich Paschen found good agreement  with Wien's exponential law at lower wavelength region (maximum energy region: IR range of 1 to 4 $$\mu$$m) at temperature of 400 to 1600 K.

However, German physicists Otto Lummer and Ernst Pringsheim  extended the range to 18 $$\mu$$ then Heinrich Rubens and  Friedrich Kurlbaum extended even farther to 60 $$\mu$$ m. They found tha }Wien's law failed at low  energy region (or long wavelength). The Figure~\ref{fig:0305} shows the discrepancy between the experimental data and Wien's exponential law. 

Sophisticated apparatus used for measuring blackbody radiation at a single wavelength in the far IR region by Rubens and Kurlbaum is shown in Figure~\ref{fig:0306}. Here, After multiple reflection of white light from alkalide halide crystals (from $P_1$ to $P_4$), narrow band of far IR radiation intensity direct into thermopile (T) to measure radiation intensity of blackbody using thermocouple. 

In the next section we will look into the formula for the lower energy region.
---
title: "Chapter 2: Special Relativity" 
author: P. Sivakumar
date: 2024-11-27 14:10:00 +0800
categories: [eTextbooks, Modern Physics]
math: true
render_with_liquid: false
---

Albert Einstein's theory of special relativity revolutionized our understanding of the universe. This groundbreaking concept challenged and redefined our intuitive notions of space, time, and motion, initiating a new era in physics. Special relativity governs phenomena involving objects or reference frames moving at significant fractions of the speed of light, approximately $$3\times 10^8 \ m/s$$, relative to one another.  
Our everyday experiences occur at speeds far below this cosmic speed limit. Even spacecraft, which travel at impressive speeds around ~$$25,000\ mi/h  (\approx 1.1 \times 10^4 m/s)$$, only reach a tiny fraction of the speed of light. Because of our lack of direct experience with such high velocities, we often struggle to grasp the counterintuitive principles of special realtivity. 
However, through conceptual understanding and theoretical exploration, we can imagine a world where time and distance are not absolute, and where nothing can exceed the speed of light. This chapter will briefly introduce the concepts and theories of this revolutionary theory.

## 2.1 Introduction
Scottish physicist James Clerk Maxwell (1831-1879) made groundbreaking contributions to our understanding of electromagnetism. In the 1860s, he unified electricity, magnetism, and  into a single theoretical framework. One of the remarkable implications through this unification was a theoretical prediction for the speed of light in a vacuum: 

\begin{equation}
    c = \frac{1}{\sqrt{\mu_0 \epsilon_0}}
\end{equation}

where c is the speed of light in a vacuum, $$\mu_0 $$ is permeability of free space ($$~ 4 \pi \times 10^{-7} N/A^2$$ ) and $$\epsilon_0$$ is permittivity of free space ($$ ~  = 8.854 \times 10^{-12} \ C^2/N.m^2 $$).

In the 19<sup>th</sup>, physicists believed that electromagnetic wave including light, required a medium for propagation like other waves. This hypothetical medium was called the "luminiferous ether," thought to permeate all of space, including in vacuum. Particularly, the speed of light was assumed to be constant relative to this ether frame, leading scientist to believed that ether was delicate enought to allow celestial bodies such as  planets to pass through it freely.  

<figure>
	<img src="/assets/img/Modern-Physics/Chapter-2/C2_1.png" alt="Description of the image">
	<figcaption>Albert A. Michelson (1952-1931) and American chemist Edward W. Morley (1838-1923).</figcaption>
</figure>

Physicist assummed that the measurement of speed of light would change depending on the direction of light relative to the ether. To test the ether hypothesis, a rapidly moving frame was needed to detect any measurable change in the speed of light. In 1887, American physicists Albert A. Michelson and Edward W. Morley utilized the Earth's motion aroung the sun $$\approx 30 \ km/s = 3 \times 10^4  m/s $$. If the ether existed, it was hypothesized that the Earth's motion through it would affect the measured speed of light in different directions.

To test this hypothesis, Michelson and Morley used a Michelson interferometer, a device that splits a beam of light into two perpendicular paths, reflects them off mirrors, and recombines them. Any difference in the speed of light in the two directions would result in an interference pattern. In the next section, we will delve deeper into the Michelson-Morley experiment and its implications for modern physics.
<figure>
    <img src="/assets/img/Modern-Physics/Chapter-2/C2_2.png" alt="Description of the image" style= "width: 100%;"> 
    <figcaption>Schematic beam diagram of Mihelson-Morley experimental septup.</figcaption>
</figure>

## 2.2 The Michelson-Morley Experiment
A Michelson interferometer, as depicted in Figure 2, was a crucial tool in the Michelson-Morley experiment. In this setup, a beam of light from a source is split by a beam splitter (M<sub>0</sub>). One part of the split beam is reflected by mirror M<sub>0</sub>, while the other part is reflected by mirror M<sub>0</sub>. These reflected beams are then recombined at the beam splitter and reach the observer.

The interference of these two beams creates an interference pattern, form of a fringes pattern, typically observed as a series of dark and light fringes. This pattern is highly sensitive to any changes in the relative path lengths of the two beams.

To minimize external disturbances, the entire interferometer was mounted on a massive stone slab floating in a pool of mercury. This isolation technique reduced vibrations and temperature fluctuations, which could affect the interference pattern.

{: .note }
Fringe Shift: If the distance between M₀ and M₁ (Arm 2) is halved, the path length difference between the two beams changes. This results in a phase shift, causing the dark fringes to become bright and vice versa. This phenomenon is known as a fringe shift.

By carefully analyzing the interference pattern and any potential fringe shifts, Michelson and Morley aimed to detect the Earth's motion through the hypothesized luminiferous ether. 

The either wind direction respect to Arm 1 and Arm 2 can be change by rotate the entire instrument through 90$$^o$$. It change could cause the fringe pattern to shift slightly.

Let's recall Example 1.1 in the Chapter-1, where we analyzed the simplified scenario of swimmer swiming along the current and return. Using this example, we can show that the total time for the round-trip along along the horizontal path, considering the ether wind,  is given by 

$$\begin{eqnarray}
    t_1 &=& \frac{L}{c+v} + \frac{L}{c-v}= \frac{2 L c}{c^2-v^2} \\
      &=& \frac{2 L}{c} \left(1- \frac{v^2}{c^2} \right)^{-1}\\
\end{eqnarray}$$

Similarly, recall the swiming across the river that we will get the light beam traveling perpendicular to the wind as

\begin{equation}
    t_2 = \frac{2 L}{\sqrt{c^2-v^2}} = \frac{2 L}{c} \left(1- \frac{v^2}{c^2}\right)^{-1/2}
\end{equation}

From above two equations, the time difference between light beam traveling horizontally and vertically can written as:

\begin{equation}
    \Delta t =  t_1 -t_2 = \frac{2 L}{c} \left[ \left(1- \frac{v^2}{c^2}\right)^{-1} - \left(1- \frac{v^2}{c^2}\right)^{-1/2} \right]
\end{equation}

The time different, $$\Delta t$$, represent the expected difference in the arrival times of the two light beams at the detector. 

Since $$v^2/c^2 \ll 1$$, we can use the binomial expansion to approximate the expressions, see [Appendix Chapter 2]({{site.baseurl}}/). In our case, we can truncate the series after the second term, as higher-order terms are negligible.

In our case, $$x = $v^2/c^2$$, and we the time different  between the light beam traveling  horizontally and vertically is

$$\begin{eqnarray}
    \Delta t = t_1 -t_2  \approx  \frac{2L}{c} \left[ 1 + \frac{v^2}{c^2} -1 - \frac{v^2}{2 c^2}\right] = \frac{L v^2}{c^3}
    \label{eq:0204}
\end{eqnarray}$$

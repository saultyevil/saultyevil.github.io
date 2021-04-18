---
layout: default
category: research_projects
---

<br>
# Efficient Monte Carlo Radiative Transfer Simulations in the Optically Thick Limit

CTD masters thesis; available upon request.

We conduct a literature review of the available
methods to improve the efficiency of Monte Carlo Radiative Transfer (MCRT)
simulations in the optically thick limit, for use in the state-of-the-art MCRT
code Python. Three main classes of techniques were found; diffusion
approximations, variance reduction techniques and reformations of the radiative
transfer equation. Specifically, we focus on the Modified Random Walk (MRW),
Packet Splitting (PS), Russian Roulette (RR) and Path Stretching (PaS)
techniques. To understand these methods better, and to gain insight on how to
implement them into an existing MCRT code, each technique is implemented into a
simple MCRT testing sandbox of a uniform parallel plane atmosphere. We find that
the MRW, PS and RR techniques reduced the number of interactions in a simulation,
improving the efficiency of transport. The performance and accuracy of the MRW
technique depends acutely on parameter choices, such that the number of MRW
transport steps allowed should be constrained to approximately 1% of the total
number of photon transport steps. Similarly, the performance
of PS and RR also relies upon sensible parameter choices to achieve the same
accuracy as other, and vanilla, MCRT methods. The simple PaS technique explored,
however, produced poor results, often failing to reproduce a result which
resembles vanilla MCRT. We conclude that the MRW, PS and RR techniques are all
promising techniques to implement into Python. More specifically, Python’s
ionisation cycles would benefit from MRW and spectrum generation would benefit
from a coupled PS and RR scheme.
{: style="text-align: justify"}

<br>
# Adiabatic hydrodynamic simulations of two-dimensional inviscid extragalatic jets
<!-- {: style="text-align: justify" } -->

Masters thesis; available upon request.
<!-- {: style="text-align: justify"} -->

We explore how perturbing pulses interact in extragalactic jets, focusing on
any movement of the shock fronts. This is done using a simple 2D
hydrodynamical model used to simulate inviscid, axisymmetric jets using the
software PLUTO. We model a number of light, low Mach number jets over a
range of pressure ratios to create overexpanded, underexpanded and pressure
matched jets, injecting sinusoidal pulse patterns with varying amplitudes and
frequencies. These pulses cause shock fronts with higher strength than those of
the internal jet shock fronts. Pulses are found to eject jet material into the
surrounding ambient medium and in some cases can severely disrupt the structure
of the jets. Our simulations show an interesting behaviour where pulses cause
internal shock fronts to move within the jet structure. We found that pulses
with an amplitude of F = 0.5 and frequency of ω = π cause the largest shock front
movement and that the length of pulse injection affects the total amount of
shock front movement. It is proposed that a feedback loop of turbulent energy
from the pulses and ejected jet material, as it is entrained back into the jet,
is the source of this shock front oscillation.
{: style="text-align: justify"}

<br>
# Measuring proper motions of nearby stars and brown dwarfs
<!-- {: style="text-align: justify" } -->

Bachelors dissertation; available upon request.
<!-- {: style="text-align: justify" } -->

This project aimed to find nearby stars and brown dwarfs by searching for high
proper motion stars which are objects that move with a large angular displacement
across the sky each year. Candidate stars were found using H2-K images
from the UKIDSS GPS and UWISH2. The spectral type and distance of these objects
was also determined by using their JHK magnitudes from UKIDSS GPS, colour indices
and the distance modulus. The highest proper motion object found had µ = 97 ± 38 mas/yr
and was found to be 39 ± 9 parsecs away, hence no  high proper motion objects
were found. The majority of objects found were M type stars but 2 L-type brown dwarfs
were found. These L-type dwarfs were also the closest with distances at 3 ± 1 and
6 ± 1 parsecs. These two objects were determined to be unreliable/unrealistic
discoveries as they were close to the saturation limit of the detector which can
result in inaccurate magnitude measurements.
{: style="text-align: justify"}

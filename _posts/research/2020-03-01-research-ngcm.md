---
layout: default
category: research_projects
title: Efficient Monte Carlo Radiative Transfer Simulations in the Optically Thick Limit
subTitle: "Parkinson, Edward J."
description: "NGCM thesis; available upon request"
---

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

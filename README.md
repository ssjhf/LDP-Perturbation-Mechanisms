# LDP-Perturbation-Mechanisms
This repository contains the source code and datasets related to our paper submitted to VLDB 2024, titled "Comparing and Improving Perturbation Mechanisms under Local Differential Privacy".

Abstract
The development of survey and information techniques enables complete data collection, leading to increasing concern of personal privacy. Local differential privacy (LDP) provides an effective measure of privacy protection, with successful applications in academia and industry. However, traditional LDP based perturbation mechanisms are designed and analyzed with a sampling with replacement scheme. This study compares perturbation mechanisms under a more refined sampling without replacement scheme, resulting in more accurate variance analysis and more efficient LDP mechanisms for conducting whole population analysis. Among all these variants, the Improved Simmons$_{(\pi_B=1/2)}$ achieve the lowest variance under certain assumptions when using LDP as the unifying measure of privacy leakage and with a higher level of cooperation. Importantly, these assumptions are generally satisfied in real-world scenarios. In experiments using a real-world dataset, the Improved Simmons$_{(\pi_B=1/2)}$ Mechanism is able to decrease the variance to 28.7\% of its classic counterpart.

List any software and libraries needed.
Python >= 3.6
NumPy
matplotlib
math

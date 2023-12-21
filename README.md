With the advancement in survey and information technologies,
comprehensive data collection has heightened concerns about personal
privacy. Local Differential Privacy (LDP) provides an effective
measure for privacy protection and has been successfully applied
in both academia and industry. This paper focuses solely on the
perturbation mechanisms under LDP, which typically include encoding,
perturbation, and aggregation steps. Traditional LDP-based
perturbation mechanisms are designed and analyzed under a sampling
with replacement scheme. Our study explores perturbation
mechanisms under a more refined sampling without replacement
scheme, leading to more accurate variance analysis and efficient
LDP mechanisms for whole population analysis. Among various
mechanisms, the Improved Simmons(𝜋𝐵=0.50) achieves the lowest
variance when the privacy budget is below a certain threshold,
while ImprovedWarner excels when the budget is above this threshold.
These assumptions generally hold true in real-world scenarios.
In experiments using real-world datasets, the Improved Warner
mechanisms significantly reduce the variance to 28.7% of its classic
counterparts and the Improved Simmons(𝜋𝐵=0.50) mechanisms significantly
reduce the variance to 11.7% of its classic counterparts.
We also propose a practical deployment example of these improved
mechanisms in real-world settings.


Author: Prajwal Niraula
Insitute: MIT
email: prajwalniraula@gmail.com/pniraula@mit.edu


## INTRODUCTION

TierraCrossSection was developed for the purpose of generating the ``perturbed" cross-section needed for running tierra, a transmission spectroscopy code that is developed by the disruptive planet group at EAPS, MIT. Most of these codes are built with an intention of performing perturbation tests. Such tests performed with warm-temperate planets showed significant impact of the perturbation in the cross-section; manifesting themselves as biases in th atmospheric retrievals performed on the simulated data. 

For general purpose, we suggest using hapi at https://github.com/hitranonline/hapi, which is extensively tested, and works for a wide range of molecules. TierraCrossSection takes advantage of this open-source code, and is a trimmed down functionalities gaining significant speed-up.


## TYPES OF CROSS-SECTIONS

This software was initially used to create nine different versions of perturbed cross-sections (Niraula de Wit et al 2022), including those where linelists were taken from HITRAN, HITEMP and ExoMol. But in the subsequent analysis (Niraula et al. 2023), five different versions of the cross-sections have been used. These perturbation test the extent tested the extend to which the perturbation to which broadening parameters such as air or hydrogen impacts the generated cross-sections: 

In analyzing JWST spectra in more recent times, we have limited our perturbation to five of the cross-sections:

  1. CS-N2-25 [CS-1] - 1 is to denote air or nitrogen, 25 denotes the extent to which line-wing is evaluated.
  2. CS-N2-500 [CS-5] is to denote air or nitrogen, 500 denotes the extent to which line-wing is evaluated.
  3. CS-H2-25 [CS-225] - 2 is to denote hydrogen, 25 denotes the extent to which line-wing is calculated.
  4. CS-H2-500 [CS-2500] - 2 is to denote hydrogen, 2500 denotes the extent to which line-wing is calculated.
  5. CS-pRT - This is the cross-section that is used in atmospheric retrieval code petitRadtrans against which tierra had been benchmarked.

Learn more details about this cross-section in our retrieval paper for WASP-39 b paper: https://arxiv.org/pdf/2303.03383.pdf


## Downloading data:

Use hapi to download the data. The instructions for downloading the data are available at: https://hitran.org/static/hapi/hapi_manual.pdf

 we are looking to convert between lbl and c-k method and compare the cross-section. 


## Functionalities

Initially CalcCrossSectionWithError were used. However in the perturbation test, these perturbations were deemed not very significant inducer of biases in the exoplanetary retrievals. 

CalcCrossSection -- Function to calculate cross-section without errors.
CalcCrossSectionWithError -- used in creating cross-sections using errors. To be depreciated.

## Notes:
Rayleigh scattering are added to the cross-sections immediately after their generation.

## Things to do:
 1. Add unittest with CO data. 
 2. Add functionality of downloading data.
 3. Will be added  
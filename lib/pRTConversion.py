#Author: This functionality has not been fully developed yet.

import numpy as np
import matplotlib.pyplot as plt
import os
from glob import glob
from scipy.interpolate import interp1d




Abundance_Dict = {"H2O":0.997317, "CH4":0.988274, "CO2":0.984204, "O3":0.992901, "CO":0.986544, "N2":0.992687, "H2":0.999688}
MolecularMassDict = {"H2O":18.010565, "CH4":16.031300, "CO2":43.989830, "O3":47.984745, "CO":27.994915, "N2":28.006148, "H2":2.015650}
ID_Dict = {"H2O":1, "CH4":6, "CO2":2, "O3":3, "CO":5, "N2":22, "H2":45}
                
print("The cross section location is given by:", )

if os.path.exists(CS_LOCATION+"/Wavelength.npy"):
   TierraWavelength = np.load(CS_LOCATION+"/Wavelength.npy")  
elif os.path.exists(CS_LOCATION+"/Wavelength.txt"):
   TierraWavelength = np.loadtxt(CS_LOCATION+"/Wavelength.txt")  
else:
    assert 1==2, "Wavelength file not found."

pRTWavelength = np.load("/media/prajwal/b3feb060-a565-44ab-a81b-7dd59881cba0/petitRADTRANS/petitRADTRANS/input_data/opacities/lines/line_by_line/Wavelength.npy")



#WaveNumber = 1./TierraWavelength
Pressure = np.loadtxt(CS_LOCATION+"/Pressure.txt")
Temperature = np.loadtxt(CS_LOCATION+"/Temperature.txt")


PressurepRT = [-6.0,-5.0,-4.0,-3.0,-2.0,-1.0,0.0,1.0, 2.0,3.0]
TemperaturepRT = [81, 110, 148, 200, 270, 365, 493, 666, 900, 1215, 1641, 2217, 2995] 

print("Pressure is:", PressurepRT)
print("Temperature is:", TemperaturepRT)



    
#For each molecule save the format
Folders = glob(CS_LOCATION+"/CS*")


for Folder in Folders:
    #Get list of all the molecules
    Current_CS = Folder.split("/")[-1]
   

    Molecule_CS = glob(Folder+"/*.npy")


  
    #### Species ID (A2) format
    #01
    #### molparam value
    #0.997317
    
   
    #Walk over all the molecules.
    for Molecule in Molecule_CS:
        MoleculeName = Molecule.split("/")[-1][:-4].replace(" ", "")
        print("The MoleculeName is given by:%s" %MoleculeName)    
        FolderName = "%s_tierra_%s_Test" %(MoleculeName, Current_CS)
        print("Saving at:", FolderName)
        #The current cross-section is given by:
        ID = str(ID_Dict[MoleculeName]).zfill(2)
        Abundance = str(Abundance_Dict[MoleculeName])
        #Create molparam_id.txt
        
        
        #Save the file in the location

        COMPLETE_LOCATION = SAVE_CS_LOCATION+"/"+FolderName
        if not(os.path.exists(COMPLETE_LOCATION)):
            os.system("mkdir %s" %(COMPLETE_LOCATION))

        os.system("cp wlen.dat %s" %COMPLETE_LOCATION)
        MolParamTxt =  "#### Species ID (A2) format\n%s\n#### molparam value \n%s" %(ID, Abundance)

        print("The complete location is:", COMPLETE_LOCATION)
        with open(COMPLETE_LOCATION+"/molparam_id.txt", "w") as f:
            f.write(MolParamTxt)



        CrossSection = np.load(Molecule, mmap_mode="r+")
        TempRange, PressureRange, _ = np.shape(CrossSection)
        #Save all the different section into different types:
        for TempCounter in range(len(TemperaturepRT)):
            for PressureCounter in range(len(PressurepRT)):
                   
                    
                
                TempValue = str(int(Temperature[TempCounter]))
                PressureValue = Pressure[PressureCounter]

              
                #Naming convention of the pRT cross-sections
                SaveName = "sigma_%s_%s.K_%7.6fbar.dat" %(ID, TempValue, 10**PressureValue)
              

                COMPLETE_FILE_LOCATION = COMPLETE_LOCATION+"/"+SaveName
              
                #Now interpolate the cross-section
                Interpolator = interp1d(TierraWavelength, CrossSection[TempCounter, PressureCounter, :], fill_value="extrapolate")
                Interpolator.fill_value = 0.0
                species_mass = MolecularMassDict[MoleculeName]
              
                ####Note for Aaron: Load petit Radtrans wavelength into prtWavelength
                InterpolatedCrossSection = Interpolator(pRTWavelength)
                InterpolatedCrossSection*=species_mass*1.66053892e-24
                InterpolatedCrossSection = np.array(InterpolatedCrossSection,order='F',dtype=np.float64)
                InterpolatedCrossSection.tofile(COMPLETE_FILE_LOCATION)

                #Note the cross
        



def DownloadWaterHITEMP():
    '''
    This function simply downloads the HITEMP cross-section of H2O from HITRAN website.
    '''

    WaveRange = [0,50,150,250,350,500,600,700,800,900,1000]
    WaveRange.extend([1150, 1300, 1500, 1750, 2000, 2250, 2500, 2750, 3000, \
                    3250, 3500, 4150])
    WaveRange.extend(list(range(4500,9100,500)))
    WaveRange.extend([11000,30000])
    print("The wave length range is given by::", WaveRange)
    BaseURL = "https://hitran.org/hitemp/data/HITEMP-2010/H2O_line_list/"

    if not(os.path.exists("H2O")):
        os.system("mkdir H2O")

    for StartWav, StopWav in zip(WaveRange[:-1],WaveRange[1:]):
        FileName = "01_%s-%s_HITEMP2010.zip" %(str(StartWav).zfill(5), str(StopWav).zfill(5))
        print("The name of the file name is given by::", FileName)

        ConstructedURL = BaseURL + FileName

        #If the file does not exist:

        if not(os.path.exists("H2O//"+FileName)):
            urllib.request.urlretrieve(ConstructedURL, "H2O//"+FileName)


        print("The current name of the file is given by::", FileName)
       
    os.system("unzip H2O/*.zip ")


def DownloadCO2HITEMP():
    '''
    This function simply downloads the HITEMP cross-section of CO2 from HITRAN website.

    The files will likely be soon updated.
    '''
    WaveRange = [0,500,625,750,1000,1500,2000,2125,2250,2500,3000]
    WaveRange.extend([3250,3500,3750,4000,4500])
    WaveRange.extend([5000,5500,6000,6500,12785])

    print("The wave length range is given by::", WaveRange)
    BaseURL = "https://hitran.org/hitemp/data/HITEMP-2010/CO2_line_list/"
    
    if not(os.path.exists("CO2")):
        os.system("mkdir CO2")


    for StartWav, StopWav in zip(WaveRange[:-1],WaveRange[1:]):
        FileName = "02_%s-%s_HITEMP2010.zip" %(str(StartWav).zfill(5), str(StopWav).zfill(5))
        print("The name of the file name is given by::", FileName)

        ConstructedURL = BaseURL + FileName
        print("The constructed URL is given by::", ConstructedURL)

        if not(os.path.exists("CO2//"+FileName)):
            urllib.request.urlretrieve(ConstructedURL, "CO2//"+FileName)


        print("The current name of the file is given by::", FileName)

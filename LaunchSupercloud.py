import os

#BaseFile = "#!/bin/bash\n#SBATCH -c 16 -n 1\n#SBATCH -o Run_%j.log\nsource /etc/profile\nmodule load anaconda/2022b\npython3 RunScript.py"
BaseFile = "#!/bin/bash\n#SBATCH -c 16 -n 1\n#SBATCH -o Run_%j.log\nsource /etc/profile\nmodule load anaconda/2022b\npython3 RunScriptpRT.py"

for Molecule in ["CO", "HCN", "NH3", "H2","SO2", "CO2"]:
    with open("Launcher.sh", 'w') as f:
        f.write(BaseFile+" "+Molecule)
    os.system("chmod u+x Launcher.sh")
    os.system("LLsub Launcher.sh")

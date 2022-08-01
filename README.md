# challenges-neha3096
challenges-neha3096 created by GitHub Classroom

This repository is created as a part of Capture the Bug Hackathon, to verify designs provided.

# Capture the Bug Hackathon

The bugathon is to verify designs in three level using python based verification setup.
The verification environment is setup using [Vyoma's UpTickPro](https://vyomasystems.com) for the hackathon.
This python based verification framework is fairly new and interesting environment to verify designs with. 
Sincere thanks to the organisers for providing the participants with this vyoma's tool setup and have an exposure
to this verification environment.

# About me

I am a Btech graduate with major in Electronics and Communication from YMCA University of Science and Technology, Faridabad. I have been working as Product Validation Engineer
for a High Level Synthesis Tool for two years now. I am very much curious about learning protocols and verification of designs.

# Level1_design1

This directory contains design file for multiplexer, a python script as testbench and a make file to run this verifucation setup.
Within this, Level1_design1_fix contains fixed version of the formerly provided multiplexer design

more details are at : https://github.com/vyomasystems-lab/challenges-neha3096/blob/master/level1_design1/Readme.md

# Level1_design2

This directory contains design file for a sequence detector, a python script as testbench and a makefile to run this verification setup.
Within this, Level1_design2_fix contains fixed version of the formerly provided sequence_detector design.
more details are at : https://github.com/vyomasystems-lab/challenges-neha3096/blob/master/level1_design2/Readme.md

# Level2_design

This directory contains design file for a bit-manipulation processor, a python script as testbench and a makefile to run this verification setup.
This also contains a model testbench which can be used as reference model to compare dut outputs with.
Within this, Level2_design_fix contains fixed version of the formerly provided bit-manipulation processo design.
more details are at : https://github.com/vyomasystems-lab/challenges-neha3096/blob/master/level2_design/Readme.md

# Level3_design

This directory contains design file for Serial Peripheral Interface - Slave, a python script as tesbench and a makefile to run this verification setup.
Within this, SPI_slave_buggy contains buggy version of the original design, which is then verified using a python script implementing cocotb.
more details are at : https://github.com/vyomasystems-lab/challenges-neha3096/blob/master/level3_design/Readme.md

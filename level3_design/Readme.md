# Serial Peripheral Interface Slave Verification

The verification environment is setup using [Vyoma's UpTickPro](https://vyomasystems.com) provided for the hackathon.

*Gitpod screenshot*
![image](https://user-images.githubusercontent.com/40855496/182155286-4fda630f-efc1-452b-89ad-286c7baca67f.png)

# Verification Environment

The [CoCoTb](https://www.cocotb.org/) based Python test is developed as explained. The test drives inputs to the Design Under Test (SPI slave module here) 

This readme explains bug and verification thus done for buggy design of SPI Slave named as slave_SPI_buggy.v
which takes in 8-bit inputs “slaveDataToSend” and 1-bit input “MOSI” and gives 1-bit output “MISO” and another 8-bit output "slaveDataReceived" respectively.

The input data stream is sent using 
```
dut.slaveDataToSend.value = random.randint(0,255)
dut.MOSI.value = random.randint(0,1)
```

The assert statement is used for comparing the output from MOSI and MISO to the expected value.

```
 #Comparison
    assert seq_sent == miso_list, "MISO transfer failed"
    
 #Comparison
    assert seq_receive == mosi_list, "MOSI transfer failed"

```
## Test Scenario **(Important)**
- Test Inputs: dut.slaveDataToSend.value = random.randint(0,255)
               dut.MOSI.value = random.randint(0,1)
- Expected Output: dut.MISO.value
                   dut.slaveDataReceived.value
- Observed Output in the DUT dut.out.value=0

Mismatches between slaveDataToSend and the data out on MISO shows that there is a design bug.
Similarly, mismatch between MOSI and slaveDataReceived after 8 SCLK cycles shows there is a design bug.

The testbench covers test scenarios for MOSI and MISO transaction, 
slaveDataToSend register is loaded with random inputs and compared with MISO output line for 8 SCLK transactions. Likewise, data is sent on MISO line
which is then collected in slaveDataReceived register after 8 SCLK cycles and compared to catch the bug.

## Design Bug
Based on random test inputs and analysing the design, following observations are recorded:

```
always @(posedge SCLK , posedge reset)
begin
  if(reset == 1'b1 || CS == 1'b0) ===> Bug
  begin
    
    SDS     = slaveDataToSend;
    SDR     = 0;
    counter = 0;
  end
```
For the SPI protocol tranfer, the Chip Select is active low signal, making it low with reset will disrupt the data transfer and thus violates the protocol.
Also, in the design it creates a functional bug too, since for CS == 0  the counter could not increment and so only the 'first' data bit is sent on MISO, and
in the slaveDataReceived register.

![image](https://user-images.githubusercontent.com/40855496/182159777-3a1ccb59-91e0-48da-9975-ee213afd10bb.png)

## Design Fix
For the original design, the data stream input and output matches correctly and the design passes.

![image](https://user-images.githubusercontent.com/40855496/182160022-ab09988c-6ff2-4f51-a390-0ce76f61940e.png)

The original passing design is named slave_SPI.v

## Verification Strategy
Verification Strategy used for verifying SPI protocol slave is as follows:
- a random input stream has been stored into slaveDataToSend register when CS=1.
- when CS goes low, i.e when slave gets activated, MISO sends out data.So, during verification, data on MISO line has been appended for 8 SCLK cycles in a list.
- data sent i.e. slaveDatatToSend and MISO has then be compared.
- for MOSI transaction, MOSI bits are are driven by random inputs for 8 SCLK cycles and appended into a list for comparison later on.
- after 8 cycles data coming from MOSI are completely shifted and stored in a shift register slaveDataReceived
- data in slaveDataReceived is compared against MOSI.

## Is the verification complete ?
A random stream of data was sent and was correctly captured on MISO. Similarly a random stream coming from MOSI is correctly stored in a shift register and checked.
The chip select signal is also excersided from testbench.
Considering above inputs and error checking, it can be concluded the verification is compelte for SPI protocol slave.

# Multiplexer Design Verification

The verification environment is setup using [Vyoma's UpTickPro](https://vyomasystems.com) provided for the hackathon.

*Gitpod screenshot*
 ![image](https://user-images.githubusercontent.com/40855496/182181483-958d4cba-8966-42f1-9ec3-48c6f997396b.png)

# Verification Environment

The [CoCoTb](https://www.cocotb.org/) based Python test is developed as explained. The test drives inputs to the Design Under Test (mux module here) which takes in 2-bit inputs “inp0” to “inp30” and gives 2-bit output “out” based on 4-bit select lines “sel”

The values are assigned to the input port using 
```
dut.inp0.value = random.randint(0,3)
dut.inp1.value = random.randint(0,3)
```

The assert statement is used for comparing the multiplexer’s output to the expected value.

The following error is seen:
```
if (dut.sel.value == 12 and dut.out.value != dut.inp12.value) :



assert dut.out.value == dut.inp12.value, " Randomised test failed: for sel:{Sel} out:{out} != {Inp}".format(Sel=dut.sel.value, out=dut.out.value, Inp=dut.inp12.value)

```
## Test Scenario 
- Test Inputs: dut.inp12.value=3 dut.sel.value=12
- Expected Output: dut.out.value=3
- Observed Output in the DUT dut.out.value=0

Output mismatches for the above inputs proving that there is a design bug
Similary the testbench covers 4 test scenarios, three of which are direct input testing to expose bugs and one of them drives random inputs to the input port and catches the bug.

## Design Bug
Based on the direct as well as random test inputs and analysing the design, we see the following

```
 
5'b01101: out = inp12; ==> Bug
5'b01101: out = inp13; ==> Bug (branch replication) 
5'b11101: out = inp29; 
                       ==> Bug (missing 5'b11110 branch)
default: out = 0;

```
For the mux design, the select line 12 is missing and consecutively we have two assignments for sel=13. The case branches has missing assignment for sel =30, and so the out value when sel=30 goes into default statement.

## Design Fix
Updating the design and re-running the test makes the test pass.
![image](https://user-images.githubusercontent.com/40855496/182068866-dd8889ec-e8e4-43ca-9d8f-5cac8f9fbf59.png)


The updated design is checked in as mux_fix.v in level1_design1_fix directory.

## Verification Strategy
Verification Strategy implied for mux design is as follows
-generating random inputs for all input ports
-generating random value on select line which will enable the testbench to drive any and all select lines
-capturing output value for the respective select line input.
-comparing output to the actual value present on input port as per the select line driven.


## Is the verification complete ?
Randomised input testing has been used to cover width and depth for the verification of the design. All the inputs values have been randomised corresponding to random select line chosen. 
Provided the above strategy, it can be said the design verification is complete.

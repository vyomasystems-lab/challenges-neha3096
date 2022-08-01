# Bit-manipulation Design Verification

The verification environment is setup using [Vyoma's UpTickPro](https://vyomasystems.com) provided for the hackathon.

*Gitpod screenshot*
![image](https://user-images.githubusercontent.com/40855496/182189151-bb29a15f-0da2-43d0-bc41-5815a927f3f0.png)


# Verification Environment

The [CoCoTb](https://www.cocotb.org/) based Python test is developed as explained. The test drives inputs to the Design Under Test (bit manipulation module here) 
which takes in 8-bit inputs “src1", "src2" and "src3” and gives 33-bit output “mav_putvalue” which has out of operation between src1,src2,src3 based on opcode 
driven via 32-bit mav_putvalue_instr.

The values are assigned to the input port using 
```
    mav_putvalue_src1 = random.randint(0,255)   
    mav_putvalue_src2 = random.randint(0,255)   
    mav_putvalue_src3 = random.randint(0,255) 
```

The assert statement is used for comparing the mav_putvalue output to the expected mav_putvalue.

Comparison and assert is implemented as:
```
if(dut_output != expected_mav_putvalue):
                    count +=1
                    print("no. of errors", count)

 assert count == 1, error_message           
 
```
## Test Scenario 
- Test Inputs:  mav_putvalue_src1  
                mav_putvalue_src2 
                mav_putvalue_src3 
                mav_putvalue_instr
- Expected Output: expected_mav_putvalue = bitmanip(mav_putvalue_instr, mav_putvalue_src1, mav_putvalue_src2, mav_putvalue_src3)
- Observed Output in the DUT dut.mav_putvalue.value=0

Output mismatches for the above input sets proves that there is a design bug
The testbench covers operation between src1,src2,src3 for all possible instruction set. A python dictionary provides all available opcodes,
which is traversed through via loop to test all operations amongst random inputs sent.

## Design Bug
Based on the random test inputs generated and analysing the design, we see the following

```
assign x__h39669 = data__h39658 & mask__h39657 ;
  assign x__h39722 = ~x__h39744 ;
  assign x__h39744 = 32'hFFFFFFFF << shamt__h39728 ;
  assign x__h39889 = mav_putvalue_src1 & mav_putvalue_src2 ;   ===> Bug
  assign x__h410 = { mav_putvalue_instr[14:12], mav_putvalue_instr[6:4] } ;
  assign x__h4309 = mav_putvalue_src1[x__h4425] ;
  assign x__h4402 = 32'd1 << x__h4425 ;
```
For the bitmanipulation design, the ANDN operation generates wrong output. Fixing the logical operation solved it and the design passes.
Also, for an ALU the design should exercise the functionality of reset, clock and enable which are mentioned unused in DUT.

## Design Fix
Updating the design and re-running the test makes the test pass.
```
assign field1__h109 =
	     (mav_putvalue_instr[31:25] == 7'b0100000 &&
	      x__h254 == 10'b1110110011) ?
	       x__h39889_2 :
	       IF_mav_putvalue_instr_BITS_31_TO_25_EQ_0b10000_ETC___d2273 ; //x__h39889_2 is used on line 3911 to compute ANDN  
         
 assign x__h39889 = mav_putvalue_src1 & (~mav_putvalue_src2) ; 
 assign x__h39889_2 = mav_putvalue_src1 & (~mav_putvalue_src2) ;//adding not of src2 in x__h39889_2:line 2661 uses this for returning ANDN output
         
  ```

![image](https://user-images.githubusercontent.com/40855496/182206313-d8201c2b-c904-4bea-8166-bb6e62d1e9bf.png)

The fix was done using a local variable_2 to assign andn operation output. Local variable was used because directly changing the RHS for assignment in  x__h39889
caused CMIX operation to fail.

![image](https://user-images.githubusercontent.com/40855496/182207878-41f2bb56-4ba2-4d93-8a19-660b2bc22825.png)

The updated design is checked in as bitmanip_fix.v in level2_design_fix directory

## Verification Strategy
Verification Strategy used for verifying SPI protocol slave is as follows:
- collecting all possible opcodes that can be used for operation between input src1, src2, src3

- for all the values of opcodes i.e all of the operations viz., ANDN, XORN,SLO etc is performed

- the output of these operations are compared against the output from reference model.

- a counter variable is incremented everytime the output mismatches occurs.

- assert is raised when count > 0
## Is the verification complete ?
Randomised input testing has been used to cover width and depth for verification of the design. The testbench includes opcodes for all possible operations that
can be implemented between the three inputs. To run complete testbench and not exit for the first error captured, assert statemnt is implemented based 
on count variable which gets incremented whenever there's a mismatch between dut output and the output from reference model.

Considering all the inputs and output comparisons, it can be said that the design is completely verified.

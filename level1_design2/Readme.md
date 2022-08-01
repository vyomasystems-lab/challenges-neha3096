# Sequence Detector Design Verification

The verification environment is setup using [Vyoma's UpTickPro](https://vyomasystems.com) provided for the hackathon.

*Gitpod screenshot*

![image](https://user-images.githubusercontent.com/40855496/182182794-d86765d4-db87-40c5-8768-9050da92d365.png)


# Verification Environment

The [CoCoTb](https://www.cocotb.org/) based Python test is developed as explained. The test drives inputs to the Design Under Test (mux module here) which takes in 1-bit input “inp_bit” to fetch a input bit-stream and gives a 1-bit output “seq_seen” if an overlapping sequence 1011 is seen in input bit stream.

The values are assigned to the input port using loop for 100 times to generate a long stream
```
Inp=random.randint(0,1)
dut.inp_bit.value=Inp

```

If the sequence 1011 is sent, the output dut.seq_seen.value goes high. A count variable is incremented for counting the number of times when sequence is sent but not seen.
The assert statement to catch error is implemented using the count variable's value.

It is implemented as follows:
```
   if (pattern == [1,0,1,1] ):
            cocotb.log.info("sequence sent")
            await FallingEdge(dut.clk)
            cocotb.log.info("sequence seen ={value}".format(value = dut.seq_seen.value))    ##if sequence is sent, check seq_seen on next clock
            if (dut.seq_seen.value != 1):
                count += 1      ##if sequence is not seen, increment count
                cocotb.log.info('####Sequence not seen#####')

    
    print("Count= ", count)
    assert count==0, "Sequence detection failed"

```
## Test Scenario **(Important)**

- Test Inputs: Inp=random.randint(0,1)
               dut.inp_bit.value=Inp

- Observed Output in the DUT dut.seq_seen.value

Output seq_seen != 1 when input pattern matches 1011 proves that there is a design bug
The testbench covers test scenario generating random input stream of sequences which when compared with [1 0 1 1]
and checking seq_seen at next clock edge shows if sequence was detected or not.

## Design Bug
Based on the direct as well as random test inputs and analysing the design, we see the following

```
       SEQ_1:
      begin
        if(inp_bit == 1)
          next_state = IDLE;  ===> Bug
        else
          next_state = SEQ_10;
      end
      
      SEQ_101:
      begin
        if(inp_bit == 1)
          next_state = SEQ_1011;
        else
          next_state = IDLE;   ===>Bug
      end
      SEQ_1011:
      begin
        next_state = IDLE;  ===> Bug

```
For an overlapping sequence, while at SEQ_1 if we get 1 the next state shoule be itself not IDLE;
                             while at SEQ_101 if we get 0, the next state should be SEQ_10 not IDLE;
                             while at SEQ_1011 i.e. when sequence has completed then next state should be
                             SEQ_1 is 1 and SEQ_10 if 0.
                             

## Design Fix
Updating the design and re-running the test makes the test pass.

![image](https://user-images.githubusercontent.com/40855496/182069603-cd8fbbfa-ec39-4ff5-9a11-aa9ac32e275d.png)

Detecting Overlapping sequences now: 
![image](https://user-images.githubusercontent.com/40855496/182069519-f88c9219-4882-4d5c-9565-dabfd22d583c.png)

The updated design is checked in as seq_detect_1011_fix.v in level1_design2_fix directory.

## Verification Strategy

Verification Strategy for Swequence detection is as follows:

-inp_bit has been loaded with a random input stream, which is long enough to repeat non-overlapping/overlapping sequences for 1011.

-this incoming stream's last four bits are captured and at this point dut.seq_seen.value is checked

-the value of seq_seen gives the output for is the sequence is correctly detected or not.

-to exercise all of the input pattern(1011) direct assert is not used, instead a count variable is incremented whenever sequence pattern is sent but not detected by dut.
-assert failure is raised for count > 0

## Is the verification complete ?
Randomised input testing has been used to cover width and depth for verification of the design. The testbench geneartes a random sequence stream and checks for 1011 in that and raises error whenever not detected. The tb thouroughly exercises all possible scenarios, it can be said the design verification is complete.

# Sequence Detector Design Verification

The verification environment is setup using [Vyoma's UpTickPro](https://vyomasystems.com) provided for the hackathon.

*Gitpod screenshot*

![image](https://user-images.githubusercontent.com/40855496/182069731-8ecb2392-f7be-42d7-b80c-505c452451cc.png)

# Verification Environment

The [CoCoTb](https://www.cocotb.org/) based Python test is developed as explained. The test drives inputs to the Design Under Test (mux module here) which takes in 2-bit inputs “inp0” to “inp30” and gives 2-bit output “out” based on 4-bit select lines “sel”

The values are assigned to the input port using loop for 100 times to generate a long sequence
```
Inp=random.randint(0,1)
dut.inp_bit.value=Inp

```

The output if the sequence is seen so, a count variable is incremented for counting the number of times when sequence is sent but not seen.
The assert statement to catch error is implemented using the count variable's content.

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

The updated design is checked in as seq_detect_1011_fix.v

## Verification Strategy
The CoCoTb based Python test is developed using Vyoma's UpTickPro verification framework. 
Randomised input testing has been used to cover width and depth for verification of the design.

## Is the verification complete ?


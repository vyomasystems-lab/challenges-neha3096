# See LICENSE.vyoma for details

# SPDX-License-Identifier: CC0-1.0

import os
import random
from pathlib import Path

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge

from cocotb.triggers import Timer

@cocotb.test()
async def test_seq_rand(dut):
    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock

        # reset
    dut.reset.value = 1
    await FallingEdge(dut.clk) 
    
    dut.reset.value = 0
    await FallingEdge(dut.clk)
    
    
    cocotb.log.info('#### CTB: Develop your test here! ######')
    cocotb.log.info('#### Random inputs generated! ######') 

    seq_list = []
    pattern = []
    count = 0
    #################################
    ######loop with random int ######
    ######to generate pattern of#####
    ###### overlapping/non-over######
    ######lapping sequences##########
    #################################
    for i in range (100):
        await FallingEdge(dut.clk)
        Inp=random.randint(0,1)
        
        dut.inp_bit.value=Inp
        seq_list.append(Inp)    ##list of sequence sent
        print(seq_list)
        pattern = seq_list[-4:] ##last four entries of sequence sent to check if pattern is sent
        print(pattern) 
        
        if (pattern == [1,0,1,1] ):
            cocotb.log.info("sequence sent")
            await FallingEdge(dut.clk)
            cocotb.log.info("sequence seen ={value}".format(value = dut.seq_seen.value))    ##if sequence is sent, check seq_seen on next clock
            if (dut.seq_seen.value != 1):
                count += 1      ##if sequence is not seen, increment count
                cocotb.log.info('####Sequence not seen#####')

    
    print("Count= ", count)
    assert count==0, "Sequence detection failed"

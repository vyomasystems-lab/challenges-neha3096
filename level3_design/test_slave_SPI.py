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
async def test_SPI_MISO_tx(dut):
    clock = Clock(dut.SCLK, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock

    # reset
    dut.reset.value = 1
    await RisingEdge(dut.SCLK) 
    dut.slaveDataToSend.value = random.randint(0,255)
    
    dut.reset.value = 0
    dut.CS.value = 1
    await RisingEdge(dut.SCLK)

    #active low chip select
    dut.CS.value = 0
    await RisingEdge(dut.SCLK)
    
    seq_sent = list(dut.slaveDataToSend.value)
    miso_list = []

    cocotb.log.info('#### Starting MISO transaction ######')
    for i in range (8):
        await RisingEdge(dut.SCLK)
        cocotb.log.info("MISO ={value}".format(value = dut.MISO.value))
        cocotb.log.info("counter = {val}".format(val = dut.counter.value))
        
        miso_list.append(dut.MISO.value)

    print("Sequence sent : ", seq_sent)
    print("Data on MISO :",miso_list)

    #Comparison
    assert seq_sent == miso_list, "MISO transfer failed"

@cocotb.test()
async def test_SPI_MOSI_tx(dut):
    clock = Clock(dut.SCLK, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock
   
    #reset
    dut.reset.value = 1
    dut.CS.value = 1
    await RisingEdge(dut.SCLK)
    
    #active low chip select
    dut.reset.value = 0
    dut.CS.value = 0
    await RisingEdge(dut.SCLK)

   
    cocotb.log.info('#### Sarting MOSI transaction ######')
    mosi_list = []

    for i in range (8):
        dut.MOSI.value = random.randint(0,1)
        await RisingEdge(dut.SCLK)
        cocotb.log.info("MOSI ={value}".format(value = dut.MOSI.value))
        mosi_list.append(dut.MOSI.value)

    await RisingEdge(dut.SCLK)   
    print("seq_received = ", dut.slaveDataReceived.value)
    seq_receive = list(dut.slaveDataReceived.value)
    print("Sequence Received : ",seq_receive)
    print ("Data on MOSI : ",mosi_list)

    #Comparison
    assert seq_receive == mosi_list, "MOSI transfer failed"

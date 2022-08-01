# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer
import random
import sys

@cocotb.test()
async def test_mux_for_sel_12(dut):
    """Test for mux2"""

    cocotb.log.info('##### CTB: Develop your test here ########')
    Sel = 12    ###select line 12 is not defined 
    Inp = 3     ##put any input value

    dut.sel.value = Sel
    dut.inp12.value = Inp
    
    await Timer(2, units='ns')
        
    
    assert dut.out.value == dut.inp12.value, " test failed: for sel : {Sel} out : {out} != {Inp}".format(Sel=dut.sel.value, out=dut.out.value, Inp=dut.inp12.value)

@cocotb.test()
async def test_mux_for_sel_13(dut):
    """Test for mux2"""

    cocotb.log.info('##### CTB: Develop your test here ########')
    Sel = 13    ###select line 13 is ambiguous 
    Inp = 1     ##put any input value

    dut.sel.value = Sel
    dut.inp13.value = Inp
    
    await Timer(2, units='ns')
        
 
    assert dut.out.value == dut.inp13.value, " test failed: for sel : {Sel} out : {out} != {Inp}".format(Sel=dut.sel.value, out=dut.out.value, Inp=dut.inp13.value)


@cocotb.test()
async def test_mux_for_sel_30(dut):
    """Test for mux2"""

    cocotb.log.info('##### CTB: Develop your test here ########')
    Sel = 30    ###select line 30 is not defined 
    Inp = 3     ##put any input value

    dut.sel.value = Sel
    dut.inp30.value = Inp
    
    await Timer(2, units='ns')
        
    assert dut.out.value == dut.inp30.value, " test failed: for sel : {Sel} out : {out} != {Inp}".format(Sel=dut.sel.value, out=dut.out.value, Inp=dut.inp30.value)

@cocotb.test()
async def test_mux_rand(dut):
    cocotb.log.info("## Random input Testing##")
    await Timer(2, units='ns')
    ########Random inputs to inp###########
    dut.inp0.value =random.randint(0,3)
    dut.inp1.value=random.randint(0,3)
    dut.inp2.value=random.randint(0,3)
    dut.inp3.value=random.randint(0,3)
    dut.inp4.value=random.randint(0,3)
    dut.inp5.value=random.randint(0,3)
    dut.inp6.value=random.randint(0,3)
    dut.inp7.value=random.randint(0,3)
    dut.inp8.value=random.randint(0,3)
    dut.inp9.value=random.randint(0,3)
    dut.inp10.value=random.randint(0,3)
    dut.inp11.value=random.randint(0,3)
    dut.inp12.value=random.randint(0,3)
    dut.inp13.value=random.randint(0,3)
    dut.inp14.value=random.randint(0,3)
    dut.inp15.value=random.randint(0,3)
    dut.inp16.value=random.randint(0,3)
    dut.inp17.value=random.randint(0,3)
    dut.inp18.value=random.randint(0,3)
    dut.inp19.value=random.randint(0,3)
    dut.inp20.value=random.randint(0,3)
    dut.inp21.value=random.randint(0,3)
    dut.inp22.value=random.randint(0,3)
    dut.inp23.value=random.randint(0,3)
    dut.inp24.value=random.randint(0,3)
    dut.inp25.value=random.randint(0,3)
    dut.inp26.value=random.randint(0,3)
    dut.inp27.value=random.randint(0,3)
    dut.inp28.value=random.randint(0,3)
    dut.inp29.value=random.randint(0,3)
    dut.inp30.value=random.randint(1,3)  ###range is 1 to 3 because branch for sel is not defined and it'll go into default branch and give 00
                                         ###00 output and error won't be caught then###       


    for i in range(30):
        Sel = random.randint(0,31)
        dut.sel.value = Sel
        
        await Timer(2, units='ns')
             
        if (dut.sel.value == 0) :
            assert dut.out.value == dut.inp0.value, " Randomised test failed: for sel:{Sel} out:{out} != {Inp}".format(Sel=dut.sel.value, out=dut.out.value, Inp=dut.inp0.value)
        if (dut.sel.value == 1) :
            assert dut.out.value == dut.inp1.value, " Randomised test failed: for sel:{Sel} out:{out} != {Inp}".format(Sel=dut.sel.value, out=dut.out.value, Inp=dut.inp1.value)
        if (dut.sel.value == 2) :  
            assert dut.out.value == dut.inp2.value, " Randomised test failed: for sel:{Sel} out:{out} != {Inp}".format(Sel=dut.sel.value, out=dut.out.value, Inp=dut.inp2.value)
        if (dut.sel.value == 3) :
            assert dut.out.value == dut.inp3.value, " Randomised test failed: for sel:{Sel} out:{out} != {Inp}".format(Sel=dut.sel.value, out=dut.out.value, Inp=dut.inp3.value)
        if (dut.sel.value == 4) :
            assert dut.out.value == dut.inp4.value, " Randomised test failed: for sel:{Sel} out:{out} != {Inp}".format(Sel=dut.sel.value, out=dut.out.value, Inp=dut.inp4.value)
        if (dut.sel.value == 5) :
            assert dut.out.value == dut.inp5.value, " Randomised test failed: for sel:{Sel} out:{out} != {Inp}".format(Sel=dut.sel.value, out=dut.out.value, Inp=dut.inp5.value)
        if (dut.sel.value == 6) :
            assert dut.out.value == dut.inp6.value, " Randomised test failed: for sel:{Sel} out:{out} != {Inp}".format(Sel=dut.sel.value, out=dut.out.value, Inp=dut.inp6.value)
        if (dut.sel.value == 7) :
            assert dut.out.value == dut.inp7.value, " Randomised test failed: for sel:{Sel} out:{out} != {Inp}".format(Sel=dut.sel.value, out=dut.out.value, Inp=dut.inp7.value)
        if (dut.sel.value == 8) :
            assert dut.out.value == dut.inp8.value, " Randomised test failed: for sel:{Sel} out:{out} != {Inp}".format(Sel=dut.sel.value, out=dut.out.value, Inp=dut.inp8.value)
        if (dut.sel.value == 9) :
            assert dut.out.value == dut.inp9.value, " Randomised test failed: for sel:{Sel} out:{out} != {Inp}".format(Sel=dut.sel.value, out=dut.out.value, Inp=dut.inp9.value)
        if (dut.sel.value == 10) :
            assert dut.out.value == dut.inp10.value, " Randomised test failed: for sel:{Sel} out:{out} != {Inp}".format(Sel=dut.sel.value, out=dut.out.value, Inp=dut.inp10.value)
        if (dut.sel.value == 11) :
            assert dut.out.value == dut.inp11.value, " Randomised test failed: for sel:{Sel} out:{out} != {Inp}".format(Sel=dut.sel.value, out=dut.out.value, Inp=dut.inp11.value)
        if (dut.sel.value == 12 and dut.out.value != dut.inp12.value) :
            #raise cocotb.result.TestFailure("Reason: outputs don't match")
            assert dut.out.value == dut.inp12.value, " Randomised test failed: for sel:{Sel} out:{out} != {Inp}".format(Sel=dut.sel.value, out=dut.out.value, Inp=dut.inp12.value)
        if (dut.sel.value == 13) :
            assert dut.out.value == dut.inp13.value, " Randomised test failed: for sel:{Sel} out:{out} != {Inp}".format(Sel=dut.sel.value, out=dut.out.value, Inp=dut.inp13.value)
        if (dut.sel.value == 14) :
            assert dut.out.value == dut.inp14.value, " Randomised test failed: for sel:{Sel} out:{out} != {Inp}".format(Sel=dut.sel.value, out=dut.out.value, Inp=dut.inp14.value)
        if (dut.sel.value == 15) :
            assert dut.out.value == dut.inp15.value, " Randomised test failed: for sel:{Sel} out:{out} != {Inp}".format(Sel=dut.sel.value, out=dut.out.value, Inp=dut.inp15.value)
        if (dut.sel.value == 16) :
            assert dut.out.value == dut.inp16.value, " Randomised test failed: for sel:{Sel} out:{out} != {Inp}".format(Sel=dut.sel.value, out=dut.out.value, Inp=dut.inp16.value)
        if (dut.sel.value == 17) :
            assert dut.out.value == dut.inp17.value, " Randomised test failed: for sel:{Sel} out:{out} != {Inp}".format(Sel=dut.sel.value, out=dut.out.value, Inp=dut.inp17.value)
        if (dut.sel.value == 18) :
            assert dut.out.value == dut.inp18.value, " Randomised test failed: for sel:{Sel} out:{out} != {Inp}".format(Sel=dut.sel.value, out=dut.out.value, Inp=dut.inp18.value)
        if (dut.sel.value == 19) :
            assert dut.out.value == dut.inp19.value, " Randomised test failed: for sel:{Sel} out:{out} != {Inp}".format(Sel=dut.sel.value, out=dut.out.value, Inp=dut.inp19.value)
        if (dut.sel.value == 20) :
            assert dut.out.value == dut.inp20.value, " Randomised test failed: for sel:{Sel} out:{out} != {Inp}".format(Sel=dut.sel.value, out=dut.out.value, Inp=dut.inp20.value)
        if (dut.sel.value == 21) :
            assert dut.out.value == dut.inp21.value, " Randomised test failed: for sel:{Sel} out:{out} != {Inp}".format(Sel=dut.sel.value, out=dut.out.value, Inp=dut.inp21.value)
        if (dut.sel.value == 22) :
            assert dut.out.value == dut.inp22.value, " Randomised test failed: for sel:{Sel} out:{out} != {Inp}".format(Sel=dut.sel.value, out=dut.out.value, Inp=dut.inp22.value)
        if (dut.sel.value == 23) :
            assert dut.out.value == dut.inp23.value, " Randomised test failed: for sel:{Sel} out:{out} != {Inp}".format(Sel=dut.sel.value, out=dut.out.value, Inp=dut.inp23.value)
        if (dut.sel.value == 24) :
            assert dut.out.value == dut.inp24.value, " Randomised test failed: for sel:{Sel} out:{out} != {Inp}".format(Sel=dut.sel.value, out=dut.out.value, Inp=dut.inp24.value)
        if (dut.sel.value == 25) :
            assert dut.out.value == dut.inp25.value, " Randomised test failed: for sel:{Sel} out:{out} != {Inp}".format(Sel=dut.sel.value, out=dut.out.value, Inp=dut.inp25.value)
        if (dut.sel.value == 26) :
            assert dut.out.value == dut.inp26.value, " Randomised test failed: for sel:{Sel} out:{out} != {Inp}".format(Sel=dut.sel.value, out=dut.out.value, Inp=dut.inp26.value)
        if (dut.sel.value == 27) :
            assert dut.out.value == dut.inp27.value, " Randomised test failed: for sel:{Sel} out:{out} != {Inp}".format(Sel=dut.sel.value, out=dut.out.value, Inp=dut.inp27.value)
        if (dut.sel.value == 28) :
            assert dut.out.value == dut.inp28.value, " Randomised test failed: for sel:{Sel} out:{out} != {Inp}".format(Sel=dut.sel.value, out=dut.out.value, Inp=dut.inp28.value)
        if (dut.sel.value == 29) :
            assert dut.out.value == dut.inp29.value, " Randomised test failed: for sel:{Sel} out:{out} != {Inp}".format(Sel=dut.sel.value, out=dut.out.value, Inp=dut.inp29.value)
        if (dut.sel.value == 30) :
            assert dut.out.value == dut.inp30.value, " Randomised test failed: for sel:{Sel} out:{out} != {Inp}".format(Sel=dut.sel.value, out=dut.out.value, Inp=dut.inp30.value)

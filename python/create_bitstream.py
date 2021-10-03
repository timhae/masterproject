#!/usr/local/bin/python3

import shutil
import subprocess

part = "{xc7z020clg400-1}"
clock = 10  # ns
regions = [
    ["bitwise_and", "bitwise_or", "bitwise_not", "add"],
    ["median", "gauss"],
]
initial_config = (0, 0)

# create ip cores
for region in regions:
    for core in region:
        shutil.rmtree(f"../xilinx/ip/{core}/{core}", ignore_errors=True)
        cmd = f"vitis_hls -f ../common/synth.tcl -tclargs {core} {part} {clock}"
        subprocess.run(cmd.split(" "), cwd=f"../xilinx/ip/{core}", check=True)

# setup main project
cmd = f"vivado -mode batch -source ../common/partial.tcl -tclargs {initial_config}"
subprocess.run(cmd.split(" "), cwd="../xilinx/vivado/partial/", check=True)

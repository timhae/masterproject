open_project [lindex $argv 2]
set_top accel
add_files accel.cpp
open_solution "solution1" -flow_target vitis
set_part [lindex $argv 3]
create_clock -period [lindex $argv 4] -name default
csynth_design
export_design -format ip_catalog -display_name [lindex $argv 2] -ipname [lindex $argv 2] -library accel -vendor hls -version 1.0
close_solution
close_project
exit

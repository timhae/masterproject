create_pblock pblock_filter
add_cells_to_pblock [get_pblocks pblock_filter] [get_cells -quiet [list design_1_i/filter]]
resize_pblock [get_pblocks pblock_filter] -add {SLICE_X50Y102:SLICE_X111Y149}
resize_pblock [get_pblocks pblock_filter] -add {DSP48_X3Y42:DSP48_X4Y59}
resize_pblock [get_pblocks pblock_filter] -add {RAMB18_X3Y42:RAMB18_X5Y59}
resize_pblock [get_pblocks pblock_filter] -add {RAMB36_X3Y21:RAMB36_X5Y29}
create_pblock pblock_bool
add_cells_to_pblock [get_pblocks pblock_bool] [get_cells -quiet [list design_1_i/bool]]
resize_pblock [get_pblocks pblock_bool] -add {SLICE_X50Y53:SLICE_X107Y98}
resize_pblock [get_pblocks pblock_bool] -add {DSP48_X3Y22:DSP48_X4Y37}
resize_pblock [get_pblocks pblock_bool] -add {RAMB18_X3Y22:RAMB18_X5Y37}
resize_pblock [get_pblocks pblock_bool] -add {RAMB36_X3Y11:RAMB36_X5Y18}
set_property SNAPPING_MODE ON [get_pblocks pblock_bool]

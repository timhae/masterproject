#include "../include/common/xf_common.hpp"
#include "../include/common/xf_headers.hpp"
#include "../include/common/xf_utility.hpp"
#include "../include/core/xf_arithm.hpp"
#include "../include/imgproc/xf_gaussian_filter.hpp"
#include "../include/imgproc/xf_median_blur.hpp"
#include "../include/imgproc/xf_add_weighted.hpp"
#include "hls_stream.h"
#include <ap_int.h>

#define PTR_WIDTH 32
#define HEIGHT 1080
#define WIDTH 1920
#define TYPE XF_8UC3
#define NPC1 XF_NPPC1
#define KERNEL_SIZE 3

typedef ap_axiu<PTR_WIDTH, 0, 0, 0> t;

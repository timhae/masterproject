#include "../common/defines.h"

void accel(hls::stream<t> &img_in1, hls::stream<t> &img_in2, hls::stream<t> &img_out) {
#pragma HLS INTERFACE axis port=img_in1
#pragma HLS INTERFACE axis port=img_in2
#pragma HLS INTERFACE axis port=img_out
#pragma HLS INTERFACE ap_ctrl_none port=return

    xf::cv::Mat<TYPE, HEIGHT, WIDTH, NPC1> imgInput1(HEIGHT, WIDTH);
    xf::cv::Mat<TYPE, HEIGHT, WIDTH, NPC1> imgInput2(HEIGHT, WIDTH);
    xf::cv::Mat<TYPE, HEIGHT, WIDTH, NPC1> imgOutput(HEIGHT, WIDTH);

    #pragma HLS DATAFLOW

    xf::cv::axiStrm2xfMat<PTR_WIDTH, TYPE, HEIGHT, WIDTH, NPC1>(img_in1, imgInput1);
    xf::cv::axiStrm2xfMat<PTR_WIDTH, TYPE, HEIGHT, WIDTH, NPC1>(img_in2, imgInput2);
    xf::cv::bitwise_or<TYPE, HEIGHT, WIDTH, NPC1>(imgInput1, imgInput2, imgOutput);
    xf::cv::xfMat2axiStrm<PTR_WIDTH, TYPE, HEIGHT, WIDTH, NPC1>(imgOutput, img_out);

    return;
}

import math


def brute_force_output_shape_conv(input_size: int,
                                  output_size: int,
                                  max_stride: int = 10,
                                  max_kernel: int = 10,
                                  max_padding: int = 10,
                                  set_stride = None,
                                  set_kernel = None,
                                  set_padding = None) -> None:
    r"""
    Brute force searches solutions for regular convolution
      setup given input and output dimensionality.
    You can fix stride, kernel, or padding with set_stride, 
      set_kernel, and set_padding respectively.
    If you have a multidimensional case, run it for each 
      dimension separately; it generalises. 
    Formula from: https://arxiv.org/pdf/1603.07285.pdf
    """
    assert set_stride != 0, "Stride cannot be 0"
    assert set_kernel != 0, "Kernel size cannot be 0"
    stride_range = [set_stride] if set_stride != None else range(1, max_stride)
    kernel_range = [set_kernel] if set_kernel != None else range(1, max_kernel)
    padding_range = [set_padding] if set_padding != None else range(0, max_padding)
    for i in stride_range:
        for j in kernel_range:
            for q in padding_range:
                if math.floor(((input_size-j+(2*q))/i)+1) == output_size:
                    print("s: " + str(i) + ", k: " + str(j) + ", p: " + str(q))


def brute_force_output_shape_transposed_conv(input_size: int,
                                             output_size: int,
                                             max_stride: int = 10,
                                             max_kernel: int = 10,
                                             max_padding: int = 10,
                                             set_stride = None,
                                             set_kernel = None,
                                             set_padding = None) -> None:
    r"""
    Brute force searches solutions for transposed convolution
      setup given input and output dimensionality.
    You can fix stride, kernel, or padding with set_stride, 
      set_kernel, and set_padding respectively.
    If you have a multidimensional case, run it for each 
      dimension separately; it generalises. 
    Formula from: https://arxiv.org/pdf/1603.07285.pdf
    """
    assert set_stride != 0, "Stride cannot be 0"
    assert set_kernel != 0, "Kernel size cannot be 0"
    stride_range = [set_stride] if set_stride != None else range(1, max_stride)
    kernel_range = [set_kernel] if set_kernel != None else range(1, max_kernel)
    padding_range = [set_padding] if set_padding != None else range(0, max_padding)
    for i in stride_range:
        for j in kernel_range:
            for q in padding_range:
                if i * (input_size - 1) + j - (2 * q) == output_size:
                    print("s: " + str(i) + ", k: " + str(j) + ", p: " + str(q))

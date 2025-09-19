










#2
def pixel_to_complex(pixel_x: int, pixel_y: int, width: int, x_range: tuple[float, float], y_range: tuple[float, float]):
    "Convert pixel coordinates (x, y) into a complex number c = x + yi within the given ranges"

    x_min, x_max = x_range
    y_min, y_max = y_range

    x = x_min + (pixel_x / (width - 1)) * (x_max - x_min)
    y = y_min + (pixel_y / (width - 1)) * (y_max - y_min)

    return complex(x, y)



#3
def mandelbrot(c: complex, max_iter: int) -> int:
    """
    Compute the diverging index for a complex number c in the Mandelbrot sequence.

    The sequence is defined as:
        a_0 = 0
        a_n = a_(n-1)^2 + c

    The diverging index is the iteration number n where |a_n| > 2.
    If no such n < max_iter exists, return 0.

    Args:
        c (complex): The complex number to test.
        max_iter (int): Maximum number of iterations to check for divergence.

    Returns:
        int: The diverging index (0 if sequence does not diverge within max_iter).
    """
    a = 0 + 0j
    for i in range(1, max_iter + 1):
        a = a * a + c
        if abs(a) > 2:
            return i
    return 0










#4
def draw_mandel(width: int, max_integer: int = 100):
    "Display a Mandelbrot image"
    
    from __main__ import generate_mandelbrot, plot_mandelbrot  

    data = generate_mandelbrot(width, max_integer=max_integer)
    plot_mandelbrot(data)




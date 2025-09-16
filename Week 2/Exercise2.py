










#2
def pixel_to_complex(pixel_x: int, pixel_y: int, width: int, x_range: tuple[float, float], y_range: tuple[float, float]):
    "Convert pixel coordinates (x, y) into a complex number c = x + yi within the given ranges"

    x_min, x_max = x_range
    y_min, y_max = y_range

    x = x_min + (pixel_x / (width - 1)) * (x_max - x_min)
    y = y_min + (pixel_y / (width - 1)) * (y_max - y_min)

    return complex(x, y)















#4
def draw_mandel(width: int, max_integer: int = 100):
    "Display a Mandelbrot image"
    
    from __main__ import generate_mandelbrot, plot_mandelbrot  

    data = generate_mandelbrot(width, max_integer=max_integer)
    plot_mandelbrot(data)




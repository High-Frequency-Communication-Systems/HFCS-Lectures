#!/usr/local/bin/julia
# Draw a series of Mobius transformations of a regular Cartesian grid
# to illustrate how a Smith chart is formed and how it relates to
# Cartesian space.
#
# Copyright Remington Furman, 2019-11-27.

using Cairo

plot_width  = 1000
plot_height = 1000
plot_scale  = 400

c = CairoRGBSurface(plot_width, plot_height);
cr = CairoContext(c);

gamma(z,n) = (z-n)/(z+n)

function connect_dots(dots)
    move_to(cr, real(dots[1]), imag(dots[1]))
    for dot in dots[2:end]
        line_to(cr, real(dot), imag(dot))
    end
    stroke(cr)
end

function connect_grid(grid)
    foreach(connect_dots, eachrow(grid))
    foreach(connect_dots, eachcol(grid))
end

function plot_smith_chart(n)
    set_source_rgb(cr,1,1,1) # Light gray background.
    rectangle(cr,0.0,0.0,plot_width,plot_height)
    fill(cr)

    set_line_width(cr, 0.5)     # Plot with thin blue lines.
    set_source_rgb(cr, 0,0,1)

    # Setup graphics transform matrix.
    save(cr)
    translate(cr, plot_width/2-plot_scale, plot_width/2) # Center the plot.
    scale(cr, plot_scale, plot_scale)                    # Embiggen.
    translate(cr, 1.0, 0.0) # A Smith chart maps 0+0j to -1+0j.  Undo that.

    # Make a regular grid.
    step = 1
    grid = [x+y*im for y=-1000:step:1000, x=0:step:1000]

    # Map the grid points and connect the dots.
    connect_grid(map(z -> gamma(z, n), grid))
    restore(cr)

    # Label plot.
    set_source_rgb(cr, 0,0,0)
    set_font_face(cr, "Helvetica Neue 16")
    line_space = 30
    text(cr, 12, 1*line_space, "Smith Chart Mobius Transform")
    text(cr, 12, 2*line_space, set_latex(cr, "\\Gamma  = (z-Z_0)/(z+Z_0)", 12), markup=true)
    text(cr, 12, 3*line_space, set_latex(cr, "Z_0 = $n", 12), markup=true)

    # Write it out to a file.
    write_to_png(c,"smith_grid_$n.png")
end

foreach(plot_smith_chart, collect(50:50:5000))
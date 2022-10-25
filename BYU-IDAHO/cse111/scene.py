# Import the functions from the Draw 2-D library
# so that they can be used in this program.
from turtle import width
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing
# This import's the math Library for non basic calcultions
import math

def main():
    # Width and height of the scene in pixels
    scene_width = 800
    scene_height = 500

    # Call the start_drawing function in the draw2d.py
    # library which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)

    # Call your drawing functions such
    # as draw_sky and draw_ground here.
    draw_sky(canvas, scene_width, scene_height)
    draw_sun(canvas, 650, 390, scale=1.3, ray_count=30)
    draw_tree(canvas, 710, 150, 200)
    draw_tree(canvas, 50, 150, 330)
    draw_cloud(canvas, 300, 350)
    draw_cloud(canvas, 350, 370, scale=1.2)
    draw_cloud(canvas, 430, 350)

    # A "for" loop to print multiple trees on the scene at a time
    for x in range(150, 700, 80):
        draw_tree(canvas, x, 160, 100)

    draw_ground(canvas, scene_width, scene_height)

    #draw_grid(canvas, scene_width, scene_height, 50)

    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)

# Define your functions such as
# draw_sky and draw_ground here.
def draw_sky(canvas, scene_width, Scene_height):
    """Draw the sky and all the objects in the sky."""
    draw_rectangle(canvas, 0, Scene_height / 3, 
    scene_width, Scene_height, width=0, fill="lightSkyBlue1")

# Draw the sun
def draw_sun(canvas, sun_left, sun_top, scale=1, ray_count=10):
    sun_width = 100 * scale
    sun_height = 100 * scale
    ray_lenght = 100 * scale
    ray_width = 3 * scale

    sun_right = sun_left + sun_width
    sun_bottom = sun_top + sun_height
    sun_center_x = sun_left + (sun_width / 2)
    sun_center_y = sun_top + (sun_height / 2)
    # This draw an oval shape base on the spec of the parameters called.
    draw_oval(canvas, sun_left, sun_top, sun_right,
              sun_bottom, fill="khaki1", width=False)
# This loop help to generate the sun ray (note to import the "import math" at the begining of your program).
    for i in range(ray_count):
        angle = (2 * math.pi / ray_count) * i
        ray_x = sun_center_x + math.cos(angle) * ray_lenght
        ray_y = sun_center_y + math.sin(angle) * ray_lenght
        draw_line(canvas, sun_center_x, sun_center_y, ray_x,
                  ray_y, width=ray_width, fill="khaki1")

def draw_cloud(canvas, cloud_left, cloud_top, scale=1):
    cloud_width = 100 * scale
    cloud_height = 100 * scale

    cloud_right = cloud_left + cloud_width
    cloud_bottom = cloud_top + cloud_height
    draw_oval(canvas, cloud_left, cloud_top, cloud_right,
              cloud_bottom, fill="white", width=False)


def draw_ground(canvas, scene_width, scene_height):
    """Draw the ground and all the objects on the ground."""
    draw_rectangle(canvas, 0, 0, 
    scene_width, scene_height / 3, width=0, fill="green2")

    # Draw a pine tree.
    tree_center_x= 170
    tree_bottom= 100
    tree_height= 200
    draw_pine_tree(canvas, tree_center_x, tree_bottom, tree_height)

    # Draw another pine tree.
    tree_center_x =90
    tree_bottom =70
    tree_height =220
    draw_pine_tree(canvas, tree_center_x, tree_bottom, tree_height)

def draw_pine_tree(canvas, center_x, bottom, height):
    """Draw a single pine tree.
    parameter
        canvas: The canvas where this function
            will draw a pine tree.
        center_x, bottom: The x and y location in pixels where
            this function will draw the bottom of a pine tree.
        height: The height in pixels of the pine tree that 
            this function will draw.
    Return: nothing
    """
    trunk_width = height / 10
    trunk_height = height / 8
    trunk_left = center_x - trunk_width / 2
    trunk_right = center_x + trunk_width / 2
    trunk_top = bottom + trunk_height

    # Draw the trunk of the pine tree.
    draw_rectangle(canvas, trunk_left, trunk_top, trunk_right, bottom,
         outline="gray24", width=1, fill="tan4")
    
    skirt_width = height / 2
    skirt_height = height - trunk_height
    skirt_left = center_x - skirt_width / 2
    skirt_right = center_x + skirt_width / 2
    skirt_top = bottom + height

    # Draw the crown (also called skirt) of the pine tree.
    draw_polygon(canvas, center_x, skirt_top, skirt_right,
        trunk_top, skirt_left, trunk_top,
        outline="gray24", width=1, fill="dark green")

def draw_tree(canvas, center_x, bottom, height):
    # draw the tree trunk
    trunk_width = height / 10
    trunk_height = height / 8
    left_trunk = center_x - trunk_width / 2
    bottom_trunk = bottom
    right_trunk = center_x + trunk_width / 2
    trunk_top = bottom + trunk_height
    draw_rectangle(canvas, left_trunk, bottom_trunk,
                   right_trunk, trunk_top, width=0, fill="tan4")
    # Draw the tree skirt
    skirt_width = height / 2
    skirt_left = center_x - skirt_width / 2
    skirt_bottom = trunk_top
    peak_x = center_x
    peak_y = bottom + height
    skirt_right = center_x + skirt_width / 2
    draw_polygon(canvas, skirt_left, skirt_bottom, peak_x, peak_y,
                 skirt_right, skirt_bottom, outline="forestgreen", fill="forestgreen")

def draw_grid(canvas, width, height, interval):
    # this function draw vertical lines
    point_y = 16
    for x in range(interval, width, interval):
        draw_line(canvas, x, 0, x, height)
        draw_text(canvas, x, point_y, f"{x}")

     # this function draw horizontal lines
    point_x = 16
    for y in range(interval, height, interval):
        draw_line(canvas, 0, y, width, y)
        draw_text(canvas, point_x, y, f"{y}")

# Call the main function so that
# this program will start executing.
main()
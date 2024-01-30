from re import X
import pyglet 
from pyglet import shapes 
from pyglet.window import mouse
width = 1280 
height = 720 
circle_diameter = 95
spacer = 3
black = (0,0,0)
red = (255,0,0)
yellow= (255,255,0)
tokens = pyglet.graphics.Batch()
switch = 1

window = pyglet.window.Window(width,height) 
title_label = pyglet.text.Label('CONNECT FOUR', 
                            font_name='Times New Roman',
                            font_size=36, 
                            x=window.width/2, y=23*window.height/24, 
                            anchor_x='center', anchor_y='center')
frame = pyglet.graphics.Batch()
frame_height = 6*circle_diameter+5*spacer
frame_width = 7*circle_diameter+6*spacer
frame_left_edge = 301.5
frame_right_edge = frame_left_edge+ frame_width 
frame_bottom = 50 
frame_top = frame_bottom+frame_height 
rectangle = shapes.Rectangle(x= 301.5, y= 50, width = frame_width, height= frame_height, color = (165,42,42), batch = frame)

# VERTICAL LINES
line_offshoot = circle_diameter+spacer/2
vlineX =[]
for i in range(7):
    vlineX.append(line_offshoot*i)
#vline1 = shapes.Line(x=301.5+vlineX[1], y=50, x2=301.5+vlineX[1], y2= frame_height+50, width = 2, color = (255,255,255), batch = frame)
#vline2 = shapes.Line(x=301.5+vlineX[2], y=50, x2=301.5+vlineX[2], y2= frame_height+50, width = 2, color = (255,255,255), batch = frame)
#vline3 = shapes.Line(x=301.5+vlineX[3], y=50, x2=301.5+vlineX[3], y2= frame_height+50, width = 2, color = (255,255,255), batch = frame)
#vline4 = shapes.Line(x=301.5+vlineX[4], y=50, x2=301.5+vlineX[4], y2= frame_height+50, width = 2, color = (255,255,255), batch = frame)
#vline5 = shapes.Line(x=301.5+vlineX[5], y=50, x2=301.5+vlineX[5], y2= frame_height+50, width = 2, color = (255,255,255), batch = frame)
#vline6 = shapes.Line(x=301.5+vlineX[6], y=50, x2=301.5+vlineX[6], y2= frame_height+50, width = 2, color = (255,255,255), batch = frame)

# HORIZONTAL LINES 
hlineY= [] 
for i in range(6):
    hlineY.append(line_offshoot*i)
hline1 = shapes.Line(x= frame_left_edge, y= frame_bottom+hlineY[1], x2= frame_right_edge, y2=frame_bottom+hlineY[1], width = 2, color = (255,255,255), batch = frame) 
hline2 = shapes.Line(x= frame_left_edge, y= frame_bottom+hlineY[2], x2= frame_right_edge, y2=frame_bottom+hlineY[2], width = 2, color = (255,255,255), batch = frame) 
hline3 = shapes.Line(x= frame_left_edge, y= frame_bottom+hlineY[3], x2= frame_right_edge, y2=frame_bottom+hlineY[3], width = 2, color = (255,255,255), batch = frame) 
hline4 = shapes.Line(x= frame_left_edge, y= frame_bottom+hlineY[4], x2= frame_right_edge, y2=frame_bottom+hlineY[4], width = 2, color = (255,255,255), batch = frame) 
hline5 = shapes.Line(x= frame_left_edge, y= frame_bottom+hlineY[5], x2= frame_right_edge, y2=frame_bottom+hlineY[5], width = 2, color = (255,255,255), batch = frame) 

# CIRCLES - BLACK CIRCLES 
row1_y = frame_bottom+line_offshoot/2
row2_y = row1_y+line_offshoot
row3_y= row2_y+line_offshoot
row4_y= row3_y+line_offshoot
row5_y= row4_y+line_offshoot
row6_y = row5_y+line_offshoot

col1_x = frame_left_edge+line_offshoot/2
col2_x = col1_x+line_offshoot
col3_x = col2_x+line_offshoot
col4_x = col3_x+line_offshoot
col5_x = col4_x+line_offshoot
col6_x = col5_x+line_offshoot
col7_x = col6_x+line_offshoot

# ROW 1 CIRCLES 
circle1 = shapes.Circle(col1_x, row1_y, circle_diameter/2, segments=None, color = black, batch = frame)
circle2 = shapes.Circle(col2_x, row1_y, circle_diameter/2, segments=None, color = (0,0,0), batch = frame)
circle3 = shapes.Circle(col3_x, row1_y, circle_diameter/2, segments=None, color = (0,0,0), batch = frame)
circle4 = shapes.Circle(col4_x, row1_y, circle_diameter/2, segments=None, color = (0,0,0), batch = frame)
circle5 = shapes.Circle(col5_x, row1_y, circle_diameter/2, segments=None, color = (0,0,0), batch = frame)
circle6 = shapes.Circle(col6_x, row1_y, circle_diameter/2, segments=None, color = (0,0,0), batch = frame)
circle7 = shapes.Circle(col7_x, row1_y, circle_diameter/2, segments=None, color = (0,0,0), batch = frame)

# ROW 2 CIRCLES 
circle8 = shapes.Circle(col1_x, row2_y, circle_diameter/2, segments=None, color = (0,0,0), batch = frame)
circle9 = shapes.Circle(col2_x, row2_y, circle_diameter/2, segments=None, color = (0,0,0), batch = frame)
circle10 = shapes.Circle(col3_x, row2_y, circle_diameter/2, segments=None, color = (0,0,0), batch = frame)
circle11 = shapes.Circle(col4_x, row2_y, circle_diameter/2, segments=None, color = (0,0,0), batch = frame)
circle12 = shapes.Circle(col5_x, row2_y, circle_diameter/2, segments=None, color = (0,0,0), batch = frame)
circle13 = shapes.Circle(col6_x, row2_y, circle_diameter/2, segments=None, color = (0,0,0), batch = frame)
circle14 = shapes.Circle(col7_x, row2_y, circle_diameter/2, segments=None, color = (0,0,0), batch = frame)

# ROW 3 CIRCLES 
circle15 = shapes.Circle(col1_x, row3_y, circle_diameter/2, segments=None, color = (0,0,0), batch = frame)
circle16 = shapes.Circle(col2_x, row3_y, circle_diameter/2, segments=None, color = (0,0,0), batch = frame)
circle17 = shapes.Circle(col3_x, row3_y, circle_diameter/2, segments=None, color = (0,0,0), batch = frame)
circle18 = shapes.Circle(col4_x, row3_y, circle_diameter/2, segments=None, color = (0,0,0), batch = frame)
circle19 = shapes.Circle(col5_x, row3_y, circle_diameter/2, segments=None, color = (0,0,0), batch = frame)
circle20 = shapes.Circle(col6_x, row3_y, circle_diameter/2, segments=None, color = (0,0,0), batch = frame)
circle21 = shapes.Circle(col7_x, row3_y, circle_diameter/2, segments=None, color = (0,0,0), batch = frame)

# ROW 4 CIRCLES 
circle22 = shapes.Circle(col1_x, row4_y, circle_diameter/2, segments=None, color = (0,0,0), batch = frame)
circle23 = shapes.Circle(col2_x, row4_y, circle_diameter/2, segments=None, color = (0,0,0), batch = frame)
circle24 = shapes.Circle(col3_x, row4_y, circle_diameter/2, segments=None, color = (0,0,0), batch = frame)
circle25 = shapes.Circle(col4_x, row4_y, circle_diameter/2, segments=None, color = (0,0,0), batch = frame)
circle26 = shapes.Circle(col5_x, row4_y, circle_diameter/2, segments=None, color = (0,0,0), batch = frame)
circle27 = shapes.Circle(col6_x, row4_y, circle_diameter/2, segments=None, color = (0,0,0), batch = frame)
circle28 = shapes.Circle(col7_x, row4_y, circle_diameter/2, segments=None, color = (0,0,0), batch = frame)

# ROW 5 CIRCLES 
circle29 = shapes.Circle(col1_x, row5_y, circle_diameter/2, segments=None, color = (0,0,0), batch = frame)
circle30 = shapes.Circle(col2_x, row5_y, circle_diameter/2, segments=None, color = (0,0,0), batch = frame)
circle31 = shapes.Circle(col3_x, row5_y, circle_diameter/2, segments=None, color = (0,0,0), batch = frame)
circle32 = shapes.Circle(col4_x, row5_y, circle_diameter/2, segments=None, color = (0,0,0), batch = frame)
circle33 = shapes.Circle(col5_x, row5_y, circle_diameter/2, segments=None, color = (0,0,0), batch = frame)
circle34 = shapes.Circle(col6_x, row5_y, circle_diameter/2, segments=None, color = (0,0,0), batch = frame)
circle35 = shapes.Circle(col7_x, row5_y, circle_diameter/2, segments=None, color = (0,0,0), batch = frame)

# ROW 6 CIRCLES 
circle36 = shapes.Circle(col1_x, row6_y, circle_diameter/2, segments=None, color = (0,0,0), batch = frame)
circle37 = shapes.Circle(col2_x, row6_y, circle_diameter/2, segments=None, color = (0,0,0), batch = frame)
circle38 = shapes.Circle(col3_x, row6_y, circle_diameter/2, segments=None, color = (0,0,0), batch = frame)
circle39 = shapes.Circle(col4_x, row6_y, circle_diameter/2, segments=None, color = (0,0,0), batch = frame)
circle40 = shapes.Circle(col5_x, row6_y, circle_diameter/2, segments=None, color = (0,0,0), batch = frame)
circle41 = shapes.Circle(col6_x, row6_y, circle_diameter/2, segments=None, color = (0,0,0), batch = frame)
circle42 = shapes.Circle(col7_x, row6_y, circle_diameter/2, segments=None, color = (0,0,0), batch = frame)

circles = []

def switcher(initial_turn, change):
    global switch 
    switch = initial_turn
    if change == True:  
        switch = switch*-1
    elif change == False:
        switch = switch   
    return switch

def on_mouse_release(x,y, button, modifiers):
    print("The mouse was pressed")
    global switch 
    switch = switcher(switch,True)
    if x in range(int(frame_left_edge), int(frame_right_edge)):
        if y in range(int(frame_bottom), int(frame_top)):
            if switch == 1: 
                color = red 
            elif switch == -1: 
                color = yellow
            new_circle = shapes.Circle(x,y, -4+circle_diameter/2, color = color, batch = tokens) 
            circles.append(new_circle)
    return circles 
window.on_mouse_release = on_mouse_release

@window.event #What does this do? for some reason this helps the label stuff work 
def on_draw():
    window.clear()
    title_label.draw()
    # STATE 1 - PLAY SCREEN
    # STATE 2 - ACTUAL PLAY
    frame.draw()
    tokens.draw()
    # Add token when mouse is clicked within columns 
    # STATE 3 - END GAME 

pyglet.app.run()
print("Complete")
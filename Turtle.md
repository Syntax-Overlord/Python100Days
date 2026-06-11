Fetched https://docs.python.org/3/library/turtle.html

Here's all the information from the Python turtle documentation page:

---

# `turtle` — Turtle graphics

## Introduction

Turtle graphics is an implementation of the popular geometric drawing tools introduced in Logo, developed by Wally Feurzeig, Seymour Papert and Cynthia Solomon in 1967.

This is an optional module. If it is missing from your copy of CPython, look for documentation from your distributor.

## Get started

Imagine a robotic turtle starting at (0, 0) in the x-y plane. After an `import turtle`, give it the command `turtle.forward(15)`, and it moves 15 pixels in the direction it is facing, drawing a line as it moves. Give it the command `turtle.right(25)`, and it rotates in-place 25 degrees clockwise.

Turtle can draw intricate shapes using programs that repeat simple moves.

In Python, turtle graphics provides a representation of a physical "turtle" (a little robot with a pen) that draws on a sheet of paper on the floor.

It's an effective and well-proven way for learners to encounter programming concepts and interaction with software, as it provides instant, visible feedback. It also provides convenient access to graphical output in general.

Turtle drawing was originally created as an educational tool, to be used by teachers in the classroom. For the programmer who needs to produce some graphical output it can be a way to do that without the overhead of introducing more complex or external libraries.

## Tutorial

### Starting a turtle environment

In a Python shell, import all the objects of the `turtle` module:

```python
from turtle import *
```

If you run into a `No module named '_tkinter'` error, you'll have to install the Tk interface package on your system.

### Basic drawing

Send the turtle forward 100 steps:

```python
forward(100)
```

You should see a line drawn by the turtle, heading East. Change the direction of the turtle:

```python
left(120)
```

Let's continue by drawing a triangle:

```python
forward(100)
left(120)
forward(100)
```

Experiment with `backward()` and `right()` commands.

#### Pen control

Try changing the color - for example, `color('blue')` - and width of the line - for example, `width(3)` - and then drawing again.

You can also move the turtle around without drawing, by lifting up the pen: `up()` before moving. To start drawing again, use `down()`.

#### The turtle's position

Send your turtle back to its starting-point:

```python
home()
```

The home position is at the center of the turtle's screen. If you ever need to know the coordinates:

```python
pos()
```

Home is at `(0, 0)`.

Clear the window to start anew:

```python
clearscreen()
```

### Making algorithmic patterns

Using loops, it's possible to build up geometric patterns:

```python
for steps in range(100):
    for c in ('blue', 'red', 'green'):
        color(c)
        forward(steps)
        right(30)
```

Let's draw the star shape. We want red lines, filled in with yellow:

```python
color('red')
fillcolor('yellow')
begin_fill()

while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break

end_fill()
```

`abs(pos()) < 1` is a good way to know when the turtle is back at its home position.

## How to…

### Get started as quickly as possible

The turtle module makes basic functionality available as functions with `from turtle import *`.

Many turtle commands have terse equivalents, such as `fd()` for forward(). These are especially useful when working with learners for whom typing is not easy.

You'll need to have the Tk interface package installed on your system for turtle graphics to work.

### Automatically begin and end filling

Starting with Python 3.14, you can use the `fill()` context manager instead of `begin_fill()` and `end_fill()`:

```python
with fill():
    for i in range(4):
        forward(100)
        right(90)

forward(200)
```

### Use the `turtle` module namespace

Using `from turtle import *` is convenient but imports a large collection of objects. To avoid name conflicts, use `import turtle` instead - `fd()` becomes `turtle.fd()`, `width()` becomes `turtle.width()`, etc.

Alternatively, use `import turtle as t`.

### Use turtle graphics in a script

Example script:

```python
import turtle as t
from random import random

for i in range(100):
    steps = int(random() * 100)
    angle = int(random() * 360)
    t.right(angle)
    t.fd(steps)

t.mainloop()
```

Add `t.mainloop()` to the end so the script waits to be dismissed.

### Use object-oriented turtle graphics

For anything beyond basic use, the object-oriented approach is more powerful. It allows multiple turtles on screen at once:

```python
from turtle import Turtle
from random import random

t = Turtle()
for i in range(100):
    steps = int(random() * 100)
    angle = int(random() * 360)
    t.right(angle)
    t.fd(steps)

t.screen.mainloop()
```

The turtle's screen can be customized:

```python
t.screen.title('Object-oriented turtle demo')
t.screen.bgcolor("orange")
```

## Turtle graphics reference

### Turtle methods

| Category                 | Methods                                                                                                                                                                                                                                             |
| ------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Turtle motion            | forward()/fd(), backward()/bk()/back(), right()/rt(), left()/lt(), goto()/setpos()/setposition(), teleport(), setx(), sety(), setheading()/seth(), home(), circle(), dot(), stamp(), clearstamp(), clearstamps(), undo(), speed()                   |
| Tell Turtle's state      | position()/pos(), towards(), xcor(), ycor(), heading(), distance()                                                                                                                                                                                  |
| Settings and measurement | degrees(), radians()                                                                                                                                                                                                                                |
| Pen control              | Drawing state: pendown()/pd()/down(), penup()/pu()/up(), pensize()/width(), pen(), isdown(); Color control: color(), pencolor(), fillcolor(); Filling: filling(), fill(), begin_fill(), end_fill(); More drawing control: reset(), clear(), write() |
| Turtle state             | Visibility: showturtle()/st(), hideturtle()/ht(), isvisible(); Appearance: shape(), resizemode(), shapesize()/turtlesize(), shearfactor(), tiltangle(), tilt(), shapetransform(), get_shapepoly()                                                   |
| Using events             | onclick(), onrelease(), ondrag()                                                                                                                                                                                                                    |
| Special Turtle methods   | poly(), begin_poly(), end_poly(), get_poly(), clone(), getturtle()/getpen(), getscreen(), setundobuffer(), undobufferentries()                                                                                                                      |

### Methods of TurtleScreen/Screen

| Category                     | Methods                                                                                                                |
| ---------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| Window control               | bgcolor(), bgpic(), clearscreen(), resetscreen(), screensize(), setworldcoordinates()                                  |
| Animation control            | no_animation(), delay(), tracer(), update()                                                                            |
| Using screen events          | listen(), onkey()/onkeyrelease(), onkeypress(), onclick()/onscreenclick(), ontimer(), mainloop()/done()                |
| Settings and special methods | mode(), colormode(), getcanvas(), getshapes(), register_shape()/addshape(), turtles(), window_height(), window_width() |
| Methods specific to Screen   | bye(), exitonclick(), save(), setup(), title()                                                                         |

---

## Methods of RawTurtle/Turtle and corresponding functions

### Turtle motion

**turtle.forward(distance)** - **turtle.fd(distance)**

Move the turtle forward by the specified distance, in the direction the turtle is headed.

```python
>>> turtle.position()
(0.00,0.00)
>>> turtle.forward(25)
>>> turtle.position()
(25.00,0.00)
```

**turtle.backward(distance)** - **turtle.bk(distance)** - **turtle.back(distance)**

Move the turtle backward by distance, opposite to the direction the turtle is headed.

```python
>>> turtle.backward(30)
>>> turtle.position()
(-30.00,0.00)
```

**turtle.right(angle)** - **turtle.rt(angle)**

Turn turtle right by angle units.

```python
>>> turtle.heading()
22.0
>>> turtle.right(45)
>>> turtle.heading()
337.0
```

**turtle.left(angle)** - **turtle.lt(angle)**

Turn turtle left by angle units.

```python
>>> turtle.heading()
22.0
>>> turtle.left(45)
>>> turtle.heading()
67.0
```

**turtle.goto(x, y=None)** - **turtle.setpos(x, y=None)** - **turtle.setposition(x, y=None)**

Move turtle to an absolute position. If the pen is down, draw line.

```python
>>> turtle.setpos(60,30)
>>> turtle.pos()
(60.00,30.00)
>>> turtle.setpos((20,80))
>>> turtle.pos()
(20.00,80.00)
```

**turtle.teleport(x, y=None, \*, fill_gap=False)**

Move turtle to an absolute position. Unlike goto(), a line will not be drawn. (Added in version 3.12)

```python
>>> turtle.teleport(60)
>>> turtle.pos()
(60.00,0.00)
```

**turtle.setx(x)**

Set the turtle's first coordinate to x, leave second coordinate unchanged.

```python
>>> turtle.setx(10)
>>> turtle.position()
(10.00,240.00)
```

**turtle.sety(y)**

Set the turtle's second coordinate to y, leave first coordinate unchanged.

```python
>>> turtle.sety(-10)
>>> turtle.position()
(0.00,-10.00)
```

**turtle.setheading(to_angle)** - **turtle.seth(to_angle)**

Set the orientation of the turtle to to_angle.

Common directions in degrees:

- "standard" mode: 0 - east, 90 - north, 180 - west, 270 - south
- "logo" mode: 0 - north, 90 - east, 180 - south, 270 - west

```python
>>> turtle.setheading(90)
>>> turtle.heading()
90.0
```

**turtle.home()**

Move turtle to the origin – coordinates (0,0) – and set its heading to its start-orientation.

```python
>>> turtle.home()
>>> turtle.position()
(0.00,0.00)
>>> turtle.heading()
0.0
```

**turtle.circle(radius, extent=None, steps=None)**

Draw a circle with given radius. The center is radius units left of the turtle.

```python
>>> turtle.circle(50)
>>> turtle.circle(120, 180)  # draw a semicircle
```

**turtle.dot()** - **turtle.dot(size)** - **turtle.dot(color, /)** - **turtle.dot(size, color, /)**

Draw a circular dot with diameter size, using color.

```python
>>> turtle.dot()
>>> turtle.fd(50); turtle.dot(20, "blue"); turtle.fd(50)
```

**turtle.stamp()**

Stamp a copy of the turtle shape onto the canvas at the current turtle position.

```python
>>> stamp_id = turtle.stamp()
>>> turtle.fd(50)
```

**turtle.clearstamp(stampid)**

Delete stamp with given stampid.

**turtle.clearstamps(n=None)**

Delete all or first/last n of turtle's stamps.

```python
>>> for i in range(8):
...     turtle.stamp()
...     turtle.fd(30)
>>> turtle.clearstamps(2)
```

**turtle.undo()**

Undo (repeatedly) the last turtle action(s).

```python
>>> for i in range(4):
...     turtle.fd(50); turtle.lt(80)
>>> for i in range(8):
...     turtle.undo()
```

**turtle.speed(speed=None)**

Set the turtle's speed to an integer value in the range 0..10.

Speedstrings:

- "fastest": 0
- "fast": 10
- "normal": 6
- "slow": 3
- "slowest": 1

Speed 0 means no animation. Speeds 1-10 enforce increasingly faster animation.

```python
>>> turtle.speed()
3
>>> turtle.speed('normal')
>>> turtle.speed()
6
```

### Tell Turtle's state

**turtle.position()** - **turtle.pos()**

Return the turtle's current location (x,y).

```python
>>> turtle.pos()
(440.00,-0.00)
```

**turtle.towards(x, y=None)**

Return the angle between the line from turtle position to position specified by (x,y).

```python
>>> turtle.goto(10, 10)
>>> turtle.towards(0,0)
225.0
```

**turtle.xcor()**

Return the turtle's x coordinate.

**turtle.ycor()**

Return the turtle's y coordinate.

**turtle.heading()**

Return the turtle's current heading.

```python
>>> turtle.heading()
67.0
```

**turtle.distance(x, y=None)**

Return the distance from the turtle to (x,y), the given vector, or the given other turtle.

```python
>>> turtle.distance(30,40)
50.0
```

### Settings for measurement

**turtle.degrees(fullcircle=360.0)**

Set angle measurement units. Default value is 360 degrees.

**turtle.radians()**

Set the angle measurement units to radians. Equivalent to `degrees(2*math.pi)`.

### Pen control

#### Drawing state

**turtle.pendown()** - **turtle.pd()** - **turtle.down()**

Pull the pen down – drawing when moving.

**turtle.penup()** - **turtle.pu()** - **turtle.up()**

Pull the pen up – no drawing when moving.

**turtle.pensize(width=None)** - **turtle.width(width=None)**

Set the line thickness to width or return it.

```python
>>> turtle.pensize()
1
>>> turtle.pensize(10)
```

**turtle.pen(pen=None, **pendict)\*\*

Return or set the pen's attributes in a "pen-dictionary" with key/value pairs:

- "shown": True/False
- "pendown": True/False
- "pencolor": color-string or color-tuple
- "fillcolor": color-string or color-tuple
- "pensize": positive number
- "speed": number in range 0..10
- "resizemode": "auto" or "user" or "noresize"
- "stretchfactor": (positive number, positive number)
- "outline": positive number
- "tilt": number

**turtle.isdown()**

Return `True` if pen is down, `False` if it's up.

```python
>>> turtle.penup()
>>> turtle.isdown()
False
```

#### Color control

**turtle.pencolor()** - **turtle.pencolor(color, /)** - **turtle.pencolor(r, g, b, /)**

Return or set the pencolor. Four input formats are allowed:

- `pencolor()` - Return the current pencolor
- `pencolor(colorstring)` - Set pencolor to a Tk color string like "red" or "#33cc8c"
- `pencolor((r, g, b))` - Set pencolor to RGB tuple
- `pencolor(r, g, b)` - Set pencolor to RGB values

```python
>>> turtle.pencolor()
'red'
>>> turtle.pencolor("brown")
>>> tup = (0.2, 0.8, 0.55)
>>> turtle.pencolor(tup)
```

**turtle.fillcolor()** - **turtle.fillcolor(color, /)** - **turtle.fillcolor(r, g, b, /)**

Return or set the fillcolor. Same formats as pencolor().

```python
>>> turtle.fillcolor("violet")
>>> turtle.fillcolor()
'violet'
```

**turtle.color()** - **turtle.color(color, /)** - **turtle.color(r, g, b, /)** - **turtle.color(pencolor, fillcolor, /)**

Return or set pencolor and fillcolor.

```python
>>> turtle.color("red", "green")
>>> turtle.color()
('red', 'green')
```

#### Filling

**turtle.filling()**

Return fillstate (`True` if filling, `False` else).

```python
>>> turtle.begin_fill()
>>> if turtle.filling():
...    turtle.pensize(5)
```

**turtle.fill()**

Fill the shape drawn in the `with turtle.fill():` block. (Added in version 3.14)

```python
>>> with turtle.fill():
...     turtle.circle(80)
```

**turtle.begin_fill()**

To be called just before drawing a shape to be filled.

**turtle.end_fill()**

Fill the shape drawn after the last call to begin_fill().

```python
>>> turtle.color("black", "red")
>>> turtle.begin_fill()
>>> turtle.circle(80)
>>> turtle.end_fill()
```

#### More drawing control

**turtle.reset()**

Delete the turtle's drawings from the screen, re-center the turtle and set variables to the default values.

```python
>>> turtle.reset()
>>> turtle.position()
(0.00,0.00)
```

**turtle.clear()**

Delete the turtle's drawings from the screen. Do not move turtle.

**turtle.write(arg, move=False, align='left', font=('Arial', 8, 'normal'))**

Write text at the current turtle position.

- move: True/False - if true, move pen to bottom-right corner of text
- align: 'left', 'center', or 'right'
- font: tuple (fontname, fontsize, fonttype)

```python
>>> turtle.write("Home = ", True, align="center")
>>> turtle.write((0,0), True)
```

### Turtle state

#### Visibility

**turtle.hideturtle()** - **turtle.ht()**

Make the turtle invisible. Hides the turtle speeds up complex drawing.

```python
>>> turtle.hideturtle()
```

**turtle.showturtle()** - **turtle.st()**

Make the turtle visible.

```python
>>> turtle.showturtle()
```

**turtle.isvisible()**

Return `True` if the Turtle is shown, `False` if it's hidden.

```python
>>> turtle.hideturtle()
>>> turtle.isvisible()
False
```

#### Appearance

**turtle.shape(name=None)**

Set turtle shape to shape with given name or return current shape name.

Initial shapes: "arrow", "turtle", "circle", "square", "triangle", "classic".

```python
>>> turtle.shape()
'classic'
>>> turtle.shape("turtle")
```

**turtle.resizemode(rmode=None)**

Set resizemode to "auto", "user", or "noresize":

- "auto": adapts the appearance of the turtle corresponding to the value of pensize.
- "user": adapts the appearance according to stretch factors.
- "noresize": no adaption of the turtle's appearance.

```python
>>> turtle.resizemode()
'noresize'
>>> turtle.resizemode("auto")
```

**turtle.shapesize(stretch_wid=None, stretch_len=None, outline=None)** - **turtle.turtlesize(...)**

Return or set the pen's x/y-stretchfactors and/or outline.

```python
>>> turtle.shapesize()
(1.0, 1.0, 1)
>>> turtle.shapesize(5, 5, 12)
```

**turtle.shearfactor(shear=None)**

Set or return the current shearfactor.

```python
>>> turtle.shearfactor(0.5)
>>> turtle.shearfactor()
0.5
```

**turtle.tilt(angle)**

Rotate the turtleshape by angle from its current tilt-angle.

**turtle.tiltangle(angle=None)**

Set or return the current tilt-angle.

**turtle.shapetransform(t11=None, t12=None, t21=None, t22=None)**

Set or return the current transformation matrix of the turtle shape.

```python
>>> turtle.shapetransform()
(4.0, -1.0, -0.0, 2.0)
```

**turtle.get_shapepoly()**

Return the current shape polygon as tuple of coordinate pairs.

```python
>>> turtle.get_shapepoly()
((50, -20), (30, 20), (-50, 20), (-30, -20))
```

### Using events

**turtle.onclick(fun, btn=1, add=None)**

Bind fun to mouse-click events on this turtle.

```python
>>> def turn(x, y):
...     left(180)
>>> onclick(turn)
```

**turtle.onrelease(fun, btn=1, add=None)**

Bind fun to mouse-button-release events on this turtle.

**turtle.ondrag(fun, btn=1, add=None)**

Bind fun to mouse-move events on this turtle. Clicking and dragging the Turtle will move it across the screen.

```python
>>> turtle.ondrag(turtle.goto)
```

### Special Turtle methods

**turtle.poly()**

Record the vertices of a polygon drawn in the `with turtle.poly():` block. (Added in version 3.14)

```python
>>> with turtle.poly():
...     turtle.forward(100)
...     turtle.right(60)
...     turtle.forward(100)
```

**turtle.begin_poly()**

Start recording the vertices of a polygon.

**turtle.end_poly()**

Stop recording the vertices of a polygon.

**turtle.get_poly()**

Return the last recorded polygon.

```python
>>> turtle.begin_poly()
>>> turtle.fd(100)
>>> turtle.end_poly()
>>> p = turtle.get_poly()
```

**turtle.clone()**

Create and return a clone of the turtle with same position, heading and turtle properties.

```python
>>> mick = Turtle()
>>> joe = mick.clone()
```

**turtle.getturtle()** - **turtle.getpen()**

Return the Turtle object itself.

```python
>>> pet = getturtle()
>>> pet.fd(50)
```

**turtle.getscreen()**

Return the TurtleScreen object the turtle is drawing on.

```python
>>> ts = turtle.getscreen()
>>> ts.bgcolor("pink")
```

**turtle.setundobuffer(size)**

Set or disable undobuffer. If size is an integer, an empty undobuffer of given size is installed.

**turtle.undobufferentries()**

Return number of entries in the undobuffer.

### Compound shapes

To use compound turtle shapes consisting of several polygons of different color:

1. Create an empty Shape object of type "compound".
2. Add components to this object using addcomponent() method.
3. Add the Shape to the Screen's shapelist and use it.

```python
>>> s = Shape("compound")
>>> poly1 = ((0,0),(10,-5),(0,10),(-10,-5))
>>> s.addcomponent(poly1, "red", "blue")
>>> poly2 = ((0,0),(10,-5),(-10,-5))
>>> s.addcomponent(poly2, "blue", "red")
>>> register_shape("myshape", s)
>>> shape("myshape")
```

---

## Methods of TurtleScreen/Screen and corresponding functions

### Window control

**turtle.bgcolor()** - **turtle.bgcolor(color, /)** - **turtle.bgcolor(r, g, b, /)**

Return or set the background color of the TurtleScreen.

```python
>>> screen.bgcolor("orange")
>>> screen.bgcolor()
'orange'
```

**turtle.bgpic(picname=None)**

Set background image or return name of current background image.

```python
>>> screen.bgpic("landscape.gif")
>>> screen.bgpic()
"landscape.gif"
```

**turtle.clearscreen()**

Delete all drawings and all turtles from the TurtleScreen. Reset to initial state.

**turtle.resetscreen()**

Reset all Turtles on the Screen to their initial state.

**turtle.screensize(canvwidth=None, canvheight=None, bg=None)**

If no arguments are given, return current (canvaswidth, canvasheight). Otherwise resize the canvas.

```python
>>> screen.screensize()
(400, 300)
>>> screen.screensize(2000,1500)
```

**turtle.setworldcoordinates(llx, lly, urx, ury)**

Set up user-defined coordinate system and switch to mode "world".

### Animation control

**turtle.no_animation()**

Temporarily disable turtle animation. (Added in version 3.14)

```python
>>> with screen.no_animation():
...     for dist in range(2, 400, 2):
...         fd(dist)
...         rt(90)
```

**turtle.delay(delay=None)**

Set or return the drawing delay in milliseconds.

```python
>>> screen.delay()
10
>>> screen.delay(5)
```

**turtle.tracer(n=None, delay=None)**

Turn turtle animation on/off and set delay for update drawings.

```python
>>> screen.tracer(8, 25)
>>> dist = 2
>>> for i in range(200):
...     fd(dist)
...     rt(90)
...     dist += 2
```

**turtle.update()**

Perform a TurtleScreen update.

### Using screen events

**turtle.listen(xdummy=None, ydummy=None)**

Set focus on TurtleScreen to collect key-events.

**turtle.onkey(fun, key)** - **turtle.onkeyrelease(fun, key)**

Bind fun to key-release event of key.

```python
>>> def f():
...     fd(50)
...     lt(60)
>>> screen.onkey(f, "Up")
>>> screen.listen()
```

**turtle.onkeypress(fun, key=None)**

Bind fun to key-press event of key, or to any key-press-event if no key is given.

**turtle.onclick(fun, btn=1, add=None)** - **turtle.onscreenclick(fun, btn=1, add=None)**

Bind fun to mouse-click events on this screen.

```python
>>> screen.onclick(turtle.goto)
>>> screen.onclick(None)  # remove binding
```

**turtle.ontimer(fun, t=0)**

Install a timer that calls fun after t milliseconds.

```python
>>> running = True
>>> def f():
...     if running:
...         fd(50)
...         lt(60)
...         screen.ontimer(f, 250)
>>> f()
```

**turtle.mainloop()** - **turtle.done()**

Start event loop - calling Tkinter's mainloop function. Must be the last statement in a turtle graphics program.

```python
>>> screen.mainloop()
```

### Input methods

**turtle.textinput(title, prompt)**

Pop up a dialog window for input of a string.

```python
>>> screen.textinput("NIM", "Name of first player:")
```

**turtle.numinput(title, prompt, default=None, minval=None, maxval=None)**

Pop up a dialog window for input of a number.

```python
>>> screen.numinput("Poker", "Your stakes:", 1000, minval=10, maxval=10000)
```

### Settings and special methods

**turtle.mode(mode=None)**

Set turtle mode ("standard", "logo" or "world") and perform reset.

Mode compatibility:

- "standard": to the right (east), counterclockwise
- "logo": upward (north), clockwise

```python
>>> mode("logo")
>>> mode()
'logo'
```

**turtle.colormode(cmode=None)**

Return the colormode or set it to 1.0 or 255.

```python
>>> screen.colormode(255)
>>> turtle.pencolor(240,160,80)
```

**turtle.getcanvas()**

Return the Canvas of this TurtleScreen.

```python
>>> cv = screen.getcanvas()
```

**turtle.getshapes()**

Return a list of names of all currently available turtle shapes.

```python
>>> screen.getshapes()
['arrow', 'blank', 'circle', ..., 'turtle']
```

**turtle.register_shape(name, shape=None)** - **turtle.addshape(name, shape=None)**

There are four different ways to call this function:

1. name is an image filename and shape is None: Install the image shape.
2. name is a string and shape is an image filename: Install the image shape.
3. name is a string and shape is a tuple of coordinate pairs: Install the polygon shape.
4. name is a string and shape is a (compound) Shape object: Install the compound shape.

```python
>>> screen.register_shape("turtle.gif")
>>> screen.register_shape("triangle", ((5,-3), (0,5), (-5,-3)))
```

(Changed in version 3.14: Added support for PNG, PGM, and PPM image formats.)

**turtle.turtles()**

Return the list of turtles on the screen.

```python
>>> for turtle in screen.turtles():
...     turtle.color("red")
```

**turtle.window_height()**

Return the height of the turtle window.

```python
>>> screen.window_height()
480
```

**turtle.window_width()**

Return the width of the turtle window.

```python
>>> screen.window_width()
640
```

### Methods specific to Screen, not inherited from TurtleScreen

**turtle.bye()**

Shut the turtlegraphics window.

**turtle.exitonclick()**

Bind `bye()` method to mouse clicks on the Screen.

**turtle.save(filename, overwrite=False)**

Save the current turtle drawing as a PostScript file.

```python
>>> screen.save("my_drawing.ps")
>>> screen.save("my_drawing.ps", overwrite=True)
```

(Added in version 3.14)

**turtle.setup(width=\_CFG['width'], height=\_CFG['height'], startx=\_CFG['leftright'], starty=\_CFG['topbottom'])**

Set the size and position of the main window.

```python
>>> screen.setup(width=200, height=200, startx=0, starty=0)
>>> screen.setup(width=.75, height=0.5, startx=None, starty=None)
```

**turtle.title(titlestring)**

Set title of turtle window to titlestring.

```python
>>> screen.title("Welcome to the turtle zoo!")
```

---

## Public classes

**class turtle.RawTurtle(canvas)** - **class turtle.RawPen(canvas)**

Create a turtle. The turtle has all methods described above.

**class turtle.Turtle**

Subclass of RawTurtle, has the same interface but draws on a default Screen object created automatically when needed.

**class turtle.TurtleScreen(cv)**

Provides screen oriented methods like bgcolor() etc.

**class turtle.Screen**

Subclass of TurtleScreen, with four methods added.

**class turtle.ScrolledCanvas(master)**

A Tkinter-canvas with scrollbars added. Used by class Screen.

**class turtle.Shape(type\_, data)**

Data structure modeling shapes:

- "polygon": a tuple of pairs of coordinates
- "image": an image
- "compound": None (constructed using addcomponent() method)

**class turtle.Vec2D(x, y)**

A two-dimensional vector class, derived from tuple. Provides:

- `a + b` vector addition
- `a - b` vector subtraction
- `a * b` inner product
- `k * a` and `a * k` multiplication with scalar
- `abs(a)` absolute value
- `a.rotate(angle)` rotation

---

## Explanation

A turtle object draws on a screen object. Key classes:

- **Turtle**: subclass of RawTurtle, automatically creates a Screen instance if needed
- **RawTurtle**: doesn't automatically create a drawing surface; requires a tkinter.Canvas
- **TurtleScreen**: the basic drawing surface for a turtle
- **Screen**: subclass of TurtleScreen with additional methods for appearance and behavior

The functional interface automatically creates screen and turtle objects as needed. To use multiple turtles, use the object-oriented interface.

---

## Help and configuration

### How to use help

- Use the Python help() function on methods:

```python
>>> help(Screen.bgcolor)
>>> help(Turtle.penup)
```

- Docstrings can be accessed through Python's help facilities.

### Translation of docstrings

Use `turtle.write_docstringdict(filename='turtle_docstringdict')` to create a dictionary for translation into other languages.

### How to configure Screen and Turtles

Create a `turtle.cfg` file. Default configuration:

```
width = 0.5
height = 0.75
leftright = None
topbottom = None
canvwidth = 400
canvheight = 300
mode = standard
colormode = 1.0
delay = 10
undobuffersize = 1000
shape = classic
pencolor = black
fillcolor = black
resizemode = noresize
visible = True
language = english
exampleturtle = turtle
examplescreen = screen
title = Python Turtle Graphics
using_IDLE = False
```

Key settings:

- shape: any built-in shape (arrow, turtle, circle, square, triangle, classic)
- fillcolor: empty string "" for transparent
- resizemode: "auto", "user", or "noresize"
- language: for translated docstrings (e.g., "italian")

---

## turtledemo — Demo scripts

Run demo scripts:

```bash
python -m turtledemo
python -m turtledemo.bytedesign
```

Available demo scripts include:

- bytedesign, chaos, clock, colormixer, forest, fractalcurves, lindenmayer, minimal_hanoi, nim, paint, peace, penrose, planet_and_moon, rosette, round_dance, sorting_animate, tree, two_canvases, yinyang

---

## Changes since Python 2.6

- Turtle methods tracer, window_width, window_height eliminated
- Turtle.fill() method eliminated
- Turtle.filling() method added

## Changes since Python 3.0

- Turtle methods shearfactor(), shapetransform(), get_shapepoly() added
- tiltangle() enhanced
- Screen.onkeypress() and onkeyrelease() added
- Screen.mainloop() added
- Input methods textinput() and numinput() added

---

Source code: [Lib/turtle.py](https://github.com/python/cpython/tree/3.14/Lib/turtle.py)

Similar code found with 1 license type

# Hostile Design

## Introduction
This is a game to identify hostile design.
This is inspired by [Robert Rosenberger](https://iac.gatech.edu/people/person/robert-rosenberger)'s class.
Hostile design is the use of strategy in designing an environment to deliberately
(and often discreetly) guide or restrict behaviour.

This game consists of a series of images, and the user is asked to identify
the element of hostile design in the image. At the end, a score is shown.


## Process
**To download this game and play**, click on this
<a href="https://drive.google.com/file/d/18ZxqSOusOqSn0AuyvogsdXp2kHFlhfC5/view?usp=sharing" target="_blank">link</a>.


After unzipping, use the `.exe` for Windows. For Mac, Control+Click on the `hostile` app and select Open.





## Additions

If you want to add more examples, just add your image to the `images_pre` folder.

Run resize.py to resize all the images. It will dump the resized image to the `images`
folder.

Next, go to `script.rpy` and add the new scene to the script.

Next, I want to host this game itself on web. Currently Renpy 8.0.3 does not build
for web, and Renpy 7.x.x is incompatible with my M1 device. Deadlock!

## Motivation

I was motivated to build this game when I started finding out about hostile design.
They are often found hiding in plain sight but when you identify them, you start
seeing them everywhere.
When I demonstrated this in class, I realized many of my friends also were
not aware of the many ways in which hostile design manifests itself, beyond
[the park bench divider](https://creativeloafing.com/content-230715-opinion---the-politics-of-park-benches).
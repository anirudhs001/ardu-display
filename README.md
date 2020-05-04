How to run:
-------
clone the repo and run dino.py.

Requirements:
-------------
### hardware
some resistors, a vga cable , a monitor
which supports vga input and an arduino
uno. Follow this [link](https://github.com/smaffer/vgax) to setup.
### os
currently it only works on unix based systems and has been tested on ubuntu.

About
-----
The project is based on [this](https://github.com/smaffer/vgax) awesome vga library.

The game is written in python(dino.py), and is sent out via serial to the uno.

This is how the data is sent:

    [dino.py] -> [game_engine.py] -> [server.py] ---serial--> uno



Make new games:
---------------
TODO


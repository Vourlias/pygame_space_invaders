#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cx_Freeze
executable=[cx_Freeze.Executable("pygame-invaders.py")]
cx_Freeze.setup(
	name="Space invaders!!!",
	options={"build.exe":{"packages":["pygame","time","random","sys","os"],
    "included_files":["stars.png","shoot.wav",
                          "invaderkilled.wav",
                          "explosion.wav",
                          "spaceship2.png",
                          "spaceship3.png",
                          "spaceinvaders.ogg",
                          "alien1.png",
                          "alien2.png",
                          "alien3.png",
                          "alien4.png",
                          "alien5.png"]}},
	executables=executable
	)

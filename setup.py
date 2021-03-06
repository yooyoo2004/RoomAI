#!/bin/python

from setuptools import setup

setup(  name        = "roomai",
        version     = "0a0",
        description = "A toolkit for developing and comparing imperfect information game bots",
        url         = "https://github.com/roomai/RoomAI",
        author      = "roomai dev",
        author_email= "lili1987mail@gmail.com",
        license     = "MIT",
        packages    = ["roomai","roomai.kuhn","roomai.common","roomai.texas","roomai.fivecardstud"],
        zip_safe    = False)

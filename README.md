morg - My Organiser
===================
<img align="right" height="250" src="http://i.imgur.com/0yPtcWq.png"/>

_My first project, started on February 9th 2017._


Description
-----------
_Put your wardrobe to python!_


App for manage clothes and sets of clothes. 
 - search
 - rate
 - add 
 - change
 - delete 


Required
--------
Python _3.6_

[Cyton](http://cython.org/)	  _0.25.2_

[Pygame](https://www.pygame.org/)  _1.9.3_

[Kivy](https://kivy.org/)    _1.9.1_

[Pyowm](https://github.com/csparpa/pyowm)   _2.6.1_     [API](https://home.openweathermap.org/): 3680a47900fb30de7d81ef3cb1a7d9fb

[SQLAlchemy](https://sqlalchemy.org)

How to use
----------
In first run app create file _weatherdata.txt_ with weather info from _weather.py_.

With insert first data (Change data/add cloth) app create _file.db_ with two tables: _ClothesData_ and _HistoryData_.

Store clothes photos (png files) in ./photo.

Store sets photos (png files) in ./sets.

Store png files used in app in ./png.

To start app run _main.py_ file. 

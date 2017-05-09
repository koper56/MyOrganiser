<img aligh="left" src="https://camo.githubusercontent.com/c2ed0c1d8ac1a5ebbe7281923d42b50b7962912c/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f707974686f6e2d332e362d626c75652e737667"/>


morg - My Organiser
===================
<img align="right" height="250" src="http://i.imgur.com/0yPtcWq.png"/>

_My first project, started on February 9th 2017._


Description
-----------
_Put your wardrobe to python!_


App for manage clothes and sets of clothes. 
 - search (by name, kind, rate, sets)
 - rate (1 - 5)
 - add (with name, description, exclusions, rate, clear, photo, colors and kind)
 - change
 - delete 


Required
--------

[Cyton](http://cython.org/)	  _0.25.2_

[Pygame](https://www.pygame.org/)  _1.9.3_

[Kivy](https://kivy.org/)    _1.9.1_

[Pyowm](https://github.com/csparpa/pyowm)   _2.6.1_     [API](https://home.openweathermap.org/): 3680a47900fb30de7d81ef3cb1a7d9fb

[SQLAlchemy](https://sqlalchemy.org)

How to use
----------

    git clone https://github.com/mkopr/morg.git (or manually download)
    cd morg
    pip install -e .
    morg
    
    
For virtualenv:

    git clone https://github.com/mkopr/morg.git (or manually download)
    cd morg
    mkvirtualenv -a <morg dir> -p python3 morg
    pip install -e .
    morg


    
In first run app create file _weatherdata.txt_ with weather info from _weather.py_.

In first run app create _data_base_file.db_ with two tables: _ClothesData_ and _HistoryData_.

App crate _morg_RRRR_MM_DD.log_ file in ./logs with logging info. 

Store clothes photos (png files) in ./photo.

Store sets photos (png files) in ./sets.

Store png files used in app in ./assets/images.


Screens
-------
Few screens from app:


<img align="left" height="300" src="http://i.imgur.com/ch37U7V.png"/>
<img align="right" height="300" src="http://i.imgur.com/CQRaV82.png"/>

<img align="left" height="300" src="http://i.imgur.com/PQldAEC.png"/>
<img align="right" height="300" src="http://i.imgur.com/WIN5qXO.png"/>

<img align="left" height="300" src="http://i.imgur.com/yok3Pf2.png"/>
<img align="right" height="300" src="http://i.imgur.com/tcJbgRt.png"/>

<img align="left" height="300" src="http://i.imgur.com/fqVybrJ.png"/>

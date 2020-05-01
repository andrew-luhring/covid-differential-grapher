# Covid Differential Grapher

I got bored and got sick of reading headlines and shit of how bad the epidemic is, so I wrote a program that uses the 
NYTimes' publically available database so I could see the changes over time.

This is for the US only because reasons. This uses their breakdown by county/FIPS and I had to do some funky conversions 
because there are places in their data where they don't have an FIPS listed for one reason or another- where that happens
I convert their empty data into the format "${county}(if known; most times it translates to "Unknown") ${state}".

Full disclosure: I suck at python, and I haven't written code of any kind in like 2 years so don't judge me on the architecture or code quality here. Or do judge me and just know that it's pointless of you to do so.

# How to install
If you're here you prolly know the deal, but if all this is new to you, cd into the directory where you want to install this and 

1. run ```git clone https://github.com/andrew-luhring/covid-differential-grapher.git```
1. cd into the ```covid-differential-grapher/``` directory
1. run ```git submodule init``` to initialize the data submodule (nytimes data) 
1. run ```git submodule update``` to grab the latest version of the data
1. now you have the data, and need to process it. Read on 

# How to process the data for the charts

I'm not a python dev so I don't know how to set up python stuff so you can just do ```python ./``` or whatever so in order
to run this you have to: 
1. cd into the ```bin/``` directory and run  ``` python __init__.py```
    1. this uses python3 so if that fails try
    1. ``` python3 __init__.py```
    1. and if that fails... idk. Install python 3 and run it with that.
1. After you run that (and it may take a second because I didn't spend a ton of time trying to figure out how to reduce the
time/space complexity or whatever) it should output a data.json file with a bunch of stuff in it.
1. Now you just gotta move that data.json to the right place: ```mv data.json ../public/js/```
1. And now just go to the public directory ```cd ../public/```

# How to see the charts and stuff

1. Start a server ```python -m http.server```
1. Open a browser and go to [http://localhost:8000](http://0.0.0.0:8000/)

If any of that failed and you know me personally message me.
If any of that failed and you don't know me personally you're on your own.


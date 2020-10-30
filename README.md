# galavanizecap1

## Getting the data

Data: https://www.speedrun.com/mc

When I was exploring the website to get the data it didn't go to a special url for the data. So I had to figure out a way to get the data. What helped me was that I have web page experience and I knew that I could look in the network tab to see were the web page request where being made to. I saw that it was getting the tables with an AJAX request. So I took the url it requested from and scraped from there. 

I then cleaned the data into Panda dataframes. After that I wrote them down to CSV so I didn't have to be constantly requesting from the server.

I then wanted to combine some of the Tables so that I can compare the data of different types of speedrunning.

## Intial look

I didn't know what to test at first so I decide to graph the times to see what I could look into.

<!-- These are the bigger images of the subplots
    !['JMCSR_Any_RS'](images/version_means/JMCSR_Any_SS.png)
    !['JMCSR_Any_SS'](images/version_means/JMCSR_Any_RS.png)
    !['JMCSR_AnyGl_RS'](images/version_means/JMCSR_AnyGl_RS.png)
    !['JMCSR_AnyGl_SS'](images/version_means/JMCSR_AnyGl_SS.png) 
-->

The first set of graph are the average speedrun times for the different version of minecraft in there respective categories and then all of them together.

!['speedrunAVGVersiontime'](images/version_means/speedrunAVGVersiontime.png)
!['speedrunVersionAVGall'](images/version_means/speedrunVersionAVGall.png)

<!-- These are the bigger images of the subplots
    !['JMCSR_Any_RS'](images/version_count/JMCSR_Any_SS.png)
    !['JMCSR_Any_SS'](images/version_count/JMCSR_Any_RS.png)
    !['JMCSR_AnyGl_RS'](images/version_count/JMCSR_AnyGl_RS.png)
    !['JMCSR_AnyGl_SS'](images/version_count/JMCSR_AnyGl_SS.png) 
-->

The second set of graph are the count of speedruns for the different version of minecraft in there respective categories and then all of them together.

!['speedrunAVGVersiontime'](images/version_count/speedrunCountVersion.png)
!['speedrunVersionAVGall'](images/version_count/speedrunCountVersionall.png)

## Hypothesis

After seeing the images above I started wondering what would be faster, Glitchless or Glitched speedruns.

Null: Neither version of Speedrunning is significantly faster then the other.

Alternate: Glitched Minecraft Speedruns are faster then Glitchless Minecraft Speedruns.

significance level = 5%

!['bootstraptest'](images/hypotesting/bootstraptest.png)

Test results:
 - Standard Error of the Means
   - Glitched: 0.04066640645942682 
   - Glitchless: 0.03318517320541225
 - Degree: 1920.7514999618993 
 - Tests stat: -552.9625199007932
 - p value: 0.0

Since the p value is under the significant value, the null hypotheses is rejected.
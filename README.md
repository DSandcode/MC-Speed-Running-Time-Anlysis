# galavanizecap1

## Getting the data

Data: https://www.speedrun.com/mc#Any_Glitchless

When I was exploring the website it didn't go to a special url for the data. So I had to figure out a way to get the data. Since I have web page experience I knew that I could look in the network tab to see were request where being made. I saw that it was getting the tables with an AJAX request. So I took the url it requested from and scraped from there. 

I then cleaned the data up and made Panda dataframes out of the data. After that I wrote them down to CSV so I didn't have to be constantly requesting from the server.

I then wanted to combine some of the Tables so that I can compare the data of different types of speedrunning.

## Images

<!-- !['JMCSR_Any_RS'](images/version_means/JMCSR_Any_SS.png)
!['JMCSR_Any_SS'](images/version_means/JMCSR_Any_RS.png)
!['JMCSR_AnyGl_RS'](images/version_means/JMCSR_AnyGl_RS.png)
!['JMCSR_AnyGl_SS'](images/version_means/JMCSR_AnyGl_SS.png) -->

!['speedrunAVGVersiontime'](images/version_means/speedrunAVGVersiontime.png)
!['speedrunVersionAVGall'](images/version_means/speedrunVersionAVGall.png)

<!-- !['JMCSR_Any_RS'](images/version_count/JMCSR_Any_SS.png)
!['JMCSR_Any_SS'](images/version_count/JMCSR_Any_RS.png)
!['JMCSR_AnyGl_RS'](images/version_count/JMCSR_AnyGl_RS.png)
!['JMCSR_AnyGl_SS'](images/version_count/JMCSR_AnyGl_SS.png) -->

!['speedrunAVGVersiontime'](images/version_count/speedrunCountVersion.png)
!['speedrunVersionAVGall'](images/version_count/speedrunCountVersionall.png)

## Hypothesis

After seeing the images above I wonder what would be faster, Glitchless or Glitched speedruns.

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
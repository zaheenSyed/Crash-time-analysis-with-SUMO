# Crash Time analysis with SUMO

This project with be a reproduction of the paper: 



<p><img align="center" src="https://sdfestaticassets-us-east-1.sciencedirectassets.com/shared-assets/24/images/elsevier-non-solus-new-grey.svg" alt="ovi" width="100" /></p> 

["Towards reducing the number of crashes during hurricane evacuation: Assessing the potential safety impact of adaptive cruise control systems"](https://www.sciencedirect.com/science/article/pii/S0968090X21002047)


First we need to download the street map from
#### Step 1
[***https://overpass-turbo.eu/***](https://overpass-turbo.eu/)

![](//{s}.tile.openstreetmap.org/{z}/{x}/{y}.png)

 <iframe width="425" height="350" frameborder="0" scrolling="no" marginheight="0" marginwidth="0" src="https://www.openstreetmap.org/export/embed.html?bbox=-81.72454833984376%2C28.168875180063345%2C-80.67260742187501%2C28.788121653588966&amp;layer=transportmap" style="border: 1px solid black"></iframe><br/><small><a href="https://www.openstreetmap.org/#map=10/28.4790/-81.1986&amp;layers=T">View Larger Map</a></small>

#### step1.2
**->Select a box**
**->Quary for turbo :**
   > highway=motorway || highway = motorway_link

#### step1.3
Run and Export the file in XML format else we can not later on convert to .net file for sumo

- To do this I have downloaded the json file with overpass api
- then I renamed the extension to ".osm.xml"

#### step 1.4 
Open terminal and run the code.
**Code to convert xml file of map to net file**

 >netconvert --osm-files berlin.osm.xml -o berlin.net.xml


[![](https://i.pinimg.com/originals/9b/96/79/9b96799d061a0528da6b0da7bac5374a.gif)](https://github.com/zaheenSyed/Crash-time-analysis-with-SUMO)
# Congratulations !
The OSM file needed to creat the map and network file for the simulation are now ready.

## Next Step (2)

### Open the .net file in netedit soft

![](https://repository-images.githubusercontent.com/108592307/2a11d000-9a90-11ea-9774-463c6ead181d)

## Follow the [Advanced Tutorial](https://sumo.dlr.de/docs/Tutorials/Hello_SUMO.html)
note: Learn SUMO and noted in [OneNotes](https://knightsucfedu39751-my.sharepoint.com/personal/zaheensyed_knights_ucf_edu/_layouts/15/Doc.aspx?sourcedoc={4e04c994-9e9f-4905-95f4-cde895cd4b7a}&action=edit&wd=target%28Quick%20notes.one%7C614fe8f6-90eb-d44b-a06f-4c7c668a1019%2FLearning%20SUMO%7Ca9a87ba9-81a4-4849-8958-79f39e0130ae%2F%29&wdorigin=703)



- create nodes done ✅
- creat edges [not done : dont know why] [ as per Reza Bhai it is done automatically when net edit is created]
- creat .net file done✅
- creat route file:
   - renamed the nodes and drawn in one note✅
   - Rename the edges: using net edit (each road is called edges)✅

- created add files to collect data:
   - router
   - data for travel time 
   - loop

- created a config file
- creat settings file

### Final Step : Simply run the sumo cfg file and collect the xml data files



# Most important Step: DATA Analysis

note: Network >> Vehicle >> Model calibration >> Data Analysis 
I am jumping to **Data Analysis** but I will return to *Model Calibration*



### FCD output:

> sumo -c hello.sumocfg --fcd-output sumoTrace.xml

### Ploting Trajectories:

> python plot_trajectories.py fcd.xml -t td -o plot.png -s


### Full Output:

> sumo -c hello.sumocfg --full-output sumofull.xml


### xml2csv:

> python xml2csv.py input.xml

### xlsx2html 0.4.0

[xlsx2](https://pypi.org/project/xlsx2html/)


### Random trip generation

> py path\randomTrips.py -n updated.net.xml -r updated.rou.xml -e 50 -l
A


### meaning??
> dfrouter --net-file I75_Final.net.xml --detector-files I75_loop.add --routes-output I75_route2.rou.xml  --measure-files loop_file





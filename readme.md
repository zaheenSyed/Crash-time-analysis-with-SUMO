# Crash Time analysis with SUMO

This project with be a reproduction of the paper: 

["Towards reducing the number of crashes during hurricane evacuation: Assessing the potential safety impact of adaptive cruise control systems"](https://www.sciencedirect.com/science/article/pii/S0968090X21002047)
![](https://sdfestaticassets-us-east-1.sciencedirectassets.com/shared-assets/24/images/elsevier-non-solus-new-grey.svg)

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


![](https://i.pinimg.com/originals/9b/96/79/9b96799d061a0528da6b0da7bac5374a.gif) 
# Congratulations !
## Next Step (2)

### Open the .net file in netedit soft

![](https://repository-images.githubusercontent.com/108592307/2a11d000-9a90-11ea-9774-463c6ead181d)

## Follow the [Advanced Tutorial](https://sumo.dlr.de/docs/Tutorials/Hello_SUMO.html)

- create nodes done ✅
- creat edges [not done : dont know why]
- creat .net file done✅
- creat route file: 🚧
- creat a config file
- creat settings file




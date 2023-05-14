# Project Title

Table Plot

## Description

Plots a Table of a Data Structure

![Screenshot](table-plot.png)

## Getting Started

### Installing

* Change to the project directory, the one you cloned. For example, `cd table_plot`. 
* Enter the following commands after the `$` prompts :
```
Cyndis-MacBook-Pro:analyze cyndi$ python3 -m venv venv
Cyndis-MacBook-Pro:analyze cyndi$ source venv/bin/activate
(env) Cyndis-MacBook-Pro:analyze cyndi$ pip install -r requirements.txt 
```
### Executing program

* Enter the following command in the project directory:
```
(env) Cyndis-MacBook-Pro:table_plot cyndi$ python tkthing.py
```
Note: any CSV file produced by Google Science Journal when exporting Three-Axis Accelerometer data may be used. The device's
 Y-axis is assumed to be aligned with the vehicle longitudinally. Of course, a little math or using the linear 
 accelerometer instead, would obviate the need for such alignment of the device. 

## Help

Here are the header line and the first few data points of the provided real-life sample file that I recorded while
driving, with the phone resting in the center console pointing with the top towards the front of the vehicle.
You can see that the timestamp, here I used absolute time in Google Science Journal, is absolute time in ms since the 
UNIX epoch. The other values are m/s^2, with the 9.xxx AccZ values indicating Earth's gravity, that being the side placed
down. It varies because the positioning of the phone was imperfect, and there were speed bumps and some grades, creating
vertical acceleration as well. Actually this data could be analyzed on each axis to get a more complete picture of my ride.

```
timestamp,AccX,AccY,AccZ
1567560367986,-0.07379653930664062,0.5849835205078125,9.625433807373048
1567560368016,-0.10627899169921876,0.6074368286132813,9.758058013916017
1567560368083,-0.10747650146484375,0.6120771789550782,9.614955596923828
```

## Authors

Charles Cavanaugh Ph.D. (Cynthia)

## Version History

* 0.1
    * Initial Release

## License

MIT License

## Acknowledgments

* Inspired by Plotly dash core sample code. 
* Added own data source and math to integrate to obtain velocity from raw
acceleration and to account for time passage in everyday units.

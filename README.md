# VesselDischarge
Script to collect discharge information for containers going into Port of Felixstowe and output to a .txt file.

### Input
List of container numbers separated by a newline or \n e.g.

	MSKU0133288
	MRKU2616998
	MSKU0286728
	MRKU4007250
	SUDU8537870

### Output
The output has three sections: Container Number, Collection Location / Estimated Discharge and Release Status. If the container is still awaiting discharge then the output will contain the estimated discharge time, otherwise it will show the port of collection. The final column will show whether the container is on hold for customs or not.

	CAAU5471677    BERTH 8&9      OK
	MEDU8671878    14/11 13:24    NOT RELEASED
	TCNU2921329    14/11 13:24    NOT RELEASED
	CMAU5192507    14/11 13:40    OK
	CMAU5009200    14/11 11:54    OK

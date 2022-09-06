# AutoBrightness

AutoBrightness for your external monitor

## Installation
 
1. Install [python and pip](https://www.python.org/downloads/)
2. Install dependecies with cmd
```
pip install darkdetect monitorcontrol pystray pyserial Pillow
```
3. Install [Arduino IDE](https://www.arduino.cc/en/software)
4. Download everything as Zip
5. (Optional) Change values in line 17 and 19 of the Arduino script to customize the function to calculate the brightness of the monitor 
6. Upload the code to Arduino
7. Make this circuit (10KOmh resistor)
    ![image](https://user-images.githubusercontent.com/43409523/188657014-5838862b-248a-429e-8a7c-0b4a65e13ba2.png)
8. Change the COM_PORT variabile in the .pyw script with the port written in the Arduino IDE
    <br>
    ![image](https://user-images.githubusercontent.com/43409523/188657337-1c25b88b-d282-4db6-9dd0-55a419953a10.png)
    <br>
9. Start the .pyw script double-clicking it
10. Profit

/*
By: Juan David Galvis Sarria
January 16th 2018
Kiwi Electronic Engineer Technical Test
v0.0
Note: Communication was tested with an Arduino MEGA programmed to send a float number
      every second through USB port. Numbers are not sent complete in some cases, 
      e.g. if the number is 34.3456, the arduino (when you use Serial.print instead of Serial.println) and other devices with serial communication
      can send 3, then 4.34 and finally 56 (Mostly when data is too long). For this reason, 
      it was necesary to send a ";" after each number to be able to delimit data.
*/





#include<iostream>
#include<stdio.h>
#include "serial.h"

using namespace std;

int main()
{
    cout << "Hello World" << endl;
    return 0;
}



/*
#include <iostream>
#include <cstdio>
#include <string>
#include <unistd.h>
#include <math.h>
#include <stdio.h>

//#include <ros/ros.h>
//#include "serial.h"
//#include <std_msgs/String.h>
//#include <std_msgs/Float64.h>

serial::Serial ser;

//Function to start serial communication when the node is executed or when the communication drops.
int start_serial_communication(void){
    try
    {
        ser.setPort("/dev/ttyUSB0"); //check communication on port ttyUSB0
        ser.setBaudrate(115200); //baudRate = 115200bps
        serial::Timeout to = serial::Timeout::simpleTimeout(0);
        ser.setTimeout(to);
        ser.open(); //communication is oppened
    }
    catch ()
    {
        cout << "Conexion muerta" << endl;
    }

    if(ser.isOpen()){
        cout << "Serial port initialized: " << ser.getPort() << endl;
        //ROS_INFO_STREAM("Serial Port initialized --> " << ser.getPort());
    }else{
        //ROS_ERROR_STREAM("Unable to open port: " << ser.getPort() );
        cout << "Unable to open port: " << ser.getPort() << endl;
        //ser.setPort("/dev/ttyACM1");
        return -1;  //Communication was not oppened, return -1
    }
    return 1;  //Communication was successfully stablished, return 1
}

int main (int argc, char** argv){

    while(start_serial_communication() == -1);  //Trying to stablish communication (while loop wont stop until communication is stablished for the first time)
	
}



 */



/*
    loop_rate.sleep();

    std_msgs::Float64 read_serial;  //Variable that will be published on topic /read_serial
    std::stringstream ss_sensor;  //String stream used to gather the complete measure of the sensor
    ss_sensor.str(std::string());  //Clear stringstream

        try{                               
		if(ser.available()){
		    //if the serial connection is available, try to read the data
		    try{
		       std::string data_sensor = ser.read(1); //data from external device is read through serial port (number by number)
		       //ser.flush();  
		       
		       if(data_sensor == ";"){  //";" represents the delimiter for each measure, so when a ";" is found output variable is updated with data 
						// gathered on stringstream
				
		  		read_serial.data = strtof(ss_sensor.str().c_str(),0);  //Convert data to float and save on variable that will be published
				ROS_INFO_STREAM("current on device: " << ss_sensor.str());  //log data on console
				ss_sensor.str(std::string());
		       }
		       else{
				ss_sensor << data_sensor;  //while ";" is not detected, data received is concatenated to avoid loss of data.
		       }
		       read_pub.publish(read_serial);  //publish to topic
		    }
		    catch(serial::IOException& e){
		        ROS_INFO("Catch exception reading data");
		    }                                 
		}
        } 
	catch(serial::IOException& e){
		        ROS_INFO("Catch exception: connection not available, trying to reconnect");  //If connection is lost, try to reconnect again
			while(start_serial_communication() == -1)
				loop_rate.sleep();
	}

        loop_rate.sleep();

    }
}

 */
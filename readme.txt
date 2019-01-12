                                       ** Messenger App ***



               ***  Messenger app using socket programming implemented in python  ***
->  There are two main files in the folder namely: one for the Server and one for the Client.(Please use  Python3  to execute the above files.
-> Starting with the server file:
-- First set the host ip in the server file to your ip address. ( This can be found using ipconfig in windows and ifconfig in linux. ) Eg, host="xxx.x.x.x" : ip of your wlan.
-> Now, we are ready to execute the server script.
->Now, run the client script, which will then ask for two values:
-- First is the host ip which was already found out and used in the server script.( Through the command ipconfig/ifconfig )
-- Second is the port number(33000), which is same as the one used in the server script earlier.
-> After completing the above steps, we are now all set to get connected to the server.
 *( Once connection has been done using ip and host next step is to fill the username which will be used by server for this chatting session .)*

-> To send a message just type the message and write the name at end of it. Suppose raj is one of the user (Eg: Hello, how are you? raj)
-> Please write all the messsage before receiver(eg. raj) and dont write anything after it.
-> This will send message to raj printing the sender.
-> To send message anonymously just write the message , then <name@ay>.( Eg:Hello, how are you? raj@ay)
-> This will send message anonymously to raj.


-> Multiple users can connect and chat at the same time.
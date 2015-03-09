RESTfulWebService: RESTfulWebService Using Python 3.4
==========================================================================

Author: Xiaobo Zhang
Summary: Return the first n Fibonacci numbers

System requirements
-------------------
All you need to build this project is Python 3.4 

Build and Deploy the RESTfulWebService
-------------------------
NOTE: The following build command assumes you have configured your Tomcat user settings. 
1. Make sure you have started the Server and installed Flask

2. Run class RESTfulWebService.py on the server.

3. UnitTests.py is used to test the REST web service.

Access the application 
---------------------

The application is deployed to <http://localhost:http://127.0.0.1:5000/fibonacci/n> where n is the number of elements the server return.


The *HTML* content can be viewed by accessing the following URL: <http://localhost:http://127.0.0.1:5000/fibonacci/n> where n is the number of elements the server return.

If n is less than 1 and bigger than 1000, the server will return “ Please input appropriate number[1,1000]”. Otherwise, it will return the first n Fibonacci numbers with responding format. 

Undeploy the Archive
--------------------

To undeploy the archive, shut down server

Test
--------------------
There are two kinds of tests, one is to use unittest in the project and run it. The other is type in ip address after turning on the server.
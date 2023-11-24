# online_python_school
This an online Python school project created mainly with Django. This school has multiple topics with explanations, examples, tasks and an online Python editor.
## Application Design Structure
![image](https://github.com/PolarBearPolar/online_python_school/assets/88388315/2da286d1-4e46-4511-bac3-1d2412f89fd2)
## Description
- The studying material of the school is split into multiple topics
- Topics can be chosen from the top-right dropdown element called **Topics**
![image](https://github.com/PolarBearPolar/online_python_school/assets/88388315/4e859ebe-2717-45c6-8a74-f65245888a31)
- It is highly advisable that topics are learnt in the same order that they are displayed in the dropdown element
- When a topic is selected, its explanation is listed on a web page along with code examples, tasks and an online Python editor
![image](https://github.com/PolarBearPolar/online_python_school/assets/88388315/fc71161e-a53f-449f-abe4-741d337344e3)
- The online Python editor can be run directly on the website so there is no need to install Python when solving simple tasks
![image](https://github.com/PolarBearPolar/online_python_school/assets/88388315/f89ada37-8d15-4c32-8f9d-71e81bb79621)
## In order to test/use it:
- Make sure you have Docker installed
- Make sure ports **8000** and **5434** are not used on your local machine
- Clone the repository to any directory on your local machine
- **cd** into the directory that contains the cloned repo in command line and run the following command there
```
docker-compose -f online_python_school.yml up
```
- Wait until all containers are up and running (it usually takes approximately 1-2 minutes)
- Open a browser and go to **localhost:8000**

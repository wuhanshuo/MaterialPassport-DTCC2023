# MaterialPassport-DTCC2023
The material passport and database of  DT4C^2 FS2023 of [CEA](https://cea.ibi.ethz.ch/)@ETH.  

Group Members: Araceli Rodriguez Vallejo, Emma Zeindl Cronin, Hanshuo Wu, Lukas Zink, Maxime Lanter, Yannik Reich 

The website is developed using *Flask* and deployed on *PythonAnywhere*.  

Click [here](https://dtcc2023.pythonanywhere.com/?db=2&id=1009) to see the website of our material passports.  
The parameter *id* in the URL is 1006 ~ 1062 for now.

## Structure  
    mysite
    ├── static/
    │   ├── icon.png
    │   ├── database/
    │       ├── 0/
    │       │   └── img/
    │       └── 1/
    │       │   ├── img/
    │       │   └── 1.csv
    │       └── 2/
    │           ├── img/
    │           └── 2.csv
    ├── templates/
    │   └── index.html
    ├── flask_app.py
    └── README.md

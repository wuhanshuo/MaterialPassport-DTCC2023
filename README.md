# MaterialPassport-DTCC2023
The material passport and database of  DT4C^2 FS2023 of [CEA](https://cea.ibi.ethz.ch/)@ETH.  

Group Members: Araceli Rodriguez Vallejo, Emma Zeindl Cronin, Hanshuo Wu, Lukas Zink, Maxime Lanter, Yannik Reich 

The website is developed using *Flask* and deployed on *PythonAnywhere*.  

Click [here](https://dtcc2023.pythonanywhere.com/?db=2&id=1009) to see the website of our material passports.  

All other components can be accessed via the following URL format:  

<img width="600" alt="image" src="https://github.com/wuhanshuo/MaterialPassport-DTCC2023/assets/63944310/10479f21-a4d7-4f68-8129-001e889649d7">

## Website Front-end  



## Website Back-end Structure  
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

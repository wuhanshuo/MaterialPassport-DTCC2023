# MaterialPassport-DTCC2023
This is the material passport and database of  DT4C^2 FS2023 of [CEA](https://cea.ibi.ethz.ch/)@ETH.  

Group Members: Araceli Rodriguez Vallejo, Emma Zeindl Cronin, Hanshuo Wu, Lukas Zink, Maxime Lanter, Yannik Reich 

The website is developed using *Flask* and deployed on *PythonAnywhere*.  

Click [here](https://dtcc2023.pythonanywhere.com/?db=2&id=1009) to see the website of our material passports.  

All other components can be accessed via the following URL format:  

<img width="600" alt="image" src="https://github.com/wuhanshuo/MaterialPassport-DTCC2023/assets/63944310/bb72f875-1dd9-4eb2-8159-873b74ab5ed6">





## Database Schema  

Each component can be identified uniquely via a project ID and a component ID.  

The project ID is the name of both the folder and the CSV file inside.  

The component ID is locally unique in each CSV file, and is also the name of the corresponding image in the `img` folder. (i.e., The combination of project ID and component ID forms a compound primary key.)  

All other columns in the CSV file can be *NULL* if the information is missing, and all *NULL* attributes will not be rendered in the front-end webpage.  

## Website Back-end Structure  
    mysite
    ├── static/
    │   ├── icon.png
    │   └── database/
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
    └── flask_app.py

## QR Code Generator

Use `qr_code_generation.py` to generate QR-code for each page automatically.  

Demo:  

<img width="200" alt="image" src="https://github.com/wuhanshuo/MaterialPassport-DTCC2023/assets/63944310/dc5d4a28-9c27-4855-aacb-673e888d8d33">




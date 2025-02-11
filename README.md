![img.png](static/images/logo_black.png)
<br></br>
# CryptoMap Project
<br>Data for web-site was parsed from sites presented below. </br>
<br><b>Legality status:</b> https://en.wikipedia.org/wiki/Legality_of_cryptocurrency_by_country_or_territory </br>
<br><b>Predicted status as national currency: </b>https://coinmarketcap.com/legal-tender-countries/ </br>
## Description
<br>CryptoMap is a website for searching by country where, how and exactly what you can buy with crypto.</br>
<br>Also, this service will show the statistics of the crypto's popularity by country and whether it is allowed as a currency at all.</br>
<br>As test example for competition presentation we create Ukraine map with markers of places for each company that currently allows use crypto as payment. For parsing locations we use Google Maps API. </br>
<br><b>Libraries for data visualization: </b>Altair, Matplotlib</br>
<br><b>Libraries for data processing: </b>  Pandas, Numpy, Folium </br>
<br><b>Python frameworks: </b>  Django</br>
<br><b>Database: </b>  SQLite</br>

<br></br>
## Guide how to run and test project
1. Clone this repository from github. 
2. Check your python version: 

    ```python3 --version```

3. Install virtual environment in working directory: 

    ```python3 -m venv venv```<br>
```source venv/bin/activate```
4. Install all necessary libraries to your virtual environment using such command as: </br>
```pip install -r requirements.txt```
5. Migrate our Django-project<br>
```python manage.py migrate```
6. Run Django Project from stroke directory: <br>
```python manage.py runserver```
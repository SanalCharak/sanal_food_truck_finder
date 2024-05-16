# sanal_food_truck_finder

Dear team,

Project has been tested on Google Chrome Browser as i have created UI also. For APIs, i have used "Postman" software

Github - https://github.com/SanalCharak/sanal_food_truck_finder

Google Drive - https://drive.google.com/drive/folders/1l3UnPHt67nxuUkELbEshtFxTQOBHdRQS?usp=sharing

Project was made in PyCharm, Windows 11.

CSV file location in project - /sanal_food_truck_finder/food_truck_finder/foodtrucks/food-truck-data.csv
Database file location in project - /sanal_food_truck_finder/food_truck_finder/db.sqlite3

Note - I have transferred all data from CSV to the SQL database file, which will be used for fetching data

Instructions:-

1. Get into the project folder /sanal_food_truck_finder/food_truck_finder/
2. There you will see requirements.txt, make sure you have all those modules or install them in your environment
3. Now At the same location you will see manage.py, run it by using command "python manage.py runserver"
4. When the project successful runs, you will get host URL in console, in my local system it was "http://127.0.0.1:8000/", in your case it can be something else
5. Paste your local host URL in browser and there you will see Latitude and Longitude inputs with search button, (GUI based). You can check it out.

Using Postman: You can test through Postman to send an API hit for received Json, through GET request. Example API is below:-

http://127.0.0.1:8000/api/foodtrucks/?latitude=37.7600869319869&longitude=-122.418806481101

Data will return 10 Trucks closest to yout latitude in ascending order

Aditionaly, The below API is not necessary to use, it clears the database file and transfers fresh data from CSV to Database file which i already did. So only test the above previous API accordingly.

http://127.0.0.1:8000/api/insert_from_csv_to_sql/

Please feel free to contact me on Phone/Whatsapp - 7889666012
Mail - sanalsinghcharak@gmail.com

I have also submitted this project on mail id - developer@rakt.org, with SUBJECT "[P1-Submission] Sanal Singh Charak"

Regards,
Sanal

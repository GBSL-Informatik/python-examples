from smartphone_connector import Connector
import csv

phone = Connector("https://io.gbsl.website", "FooBar")

phone.sleep(20)
# enable the acceleration stream and position the phone on your belly to detect your pulse rate
with open('pulse.csv', mode='w') as csvfile:
    csv_w = csv.writer(csvfile, delimiter=',')
    for t in phone.acceleration_data():
        csv_w.writerow([t.time_stamp, t.x, t.y, t.z])

phone.disconnect()

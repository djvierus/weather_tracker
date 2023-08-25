import urllib.parse, time, json, psycopg2, cnf
from urllib.request import urlopen
from types import SimpleNamespace
from datetime import datetime
sleep_time = cnf.interval

c_location_count = len(cnf.city)
s_location_count = len(cnf.state)

if (c_location_count != s_location_count):
    print("Number of cities does not match the number of states. Please update the appsettings.json file")
    exit(1)

try:
    conn = psycopg2.connect(database=cnf.sql_database,
                    host=cnf.sql_host,
                    user=cnf.sql_user,
                    password=cnf.sql_pass,
                    port=cnf.sql_port)
    sql = conn.cursor() 
    while (True): 
        try:
            for loc in range(c_location_count):
                query = "{0} {1}".format(cnf.location[0,loc],cnf.location[1,loc]) 
                safe_string = urllib.parse.quote_plus(query)
                url_encode = "{0}?key={1}&q={2}&aqi={3}".format(cnf.url,cnf.key,safe_string,cnf.aqi)
                response= urlopen(url_encode)
                data_json = json.loads(response.read(), object_hook=lambda d: SimpleNamespace(**d))
                now = time.strftime('%Y-%m-%d %H:%M:%S')
                print ("{0} | The current temperature is {1}F". format(now, data_json.current.temp_f))
                try:
                    sql.execute(("INSERT INTO weather_history(id, timestamp, temperature, source, city, state)\
                    VALUES (NEXTVAL('weather_hist_seq'),%(timestamp)s,%(temperature)s,%(source)s,%(city)s,%(state)s)"), \
                    {'timestamp': now,'temperature': data_json.current.temp_f,'source': cnf.source, 'city' : cnf.location[0,loc], 'state': cnf.location[1,loc] })
                    conn.commit()
                except Exception as error:
                    print("An exception has occured while writing to the databse")
                    print(error)
                    pass
        except Exception as error:
            print("An exception has occurred:")
            print(error)
            pass
        time.sleep(sleep_time)
except Exception as error:
    print("An exception has occurred:")
    print(error)
except KeyboardInterrupt:
    print("Service Cancelled By User")
    conn.close
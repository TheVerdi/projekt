import re
from datetime import datetime, timedelta

print("""
        Wprowadz dane zgodnie ze schematem:
        XXYYYY (S|C) Y+ TIME1 TIME2
        
        gdzie:
        XX - dwie dowolne duze litery
        YYYY - cztery dowolne cyfry
        S lub C - samochod osobowy lub ciezarowy
        Y+ - dowolna liczba przejechanych metrow
        TIME1, TIME2 - wprowadz czas w formacie HH:MM
        
        Przykladowy input danych:
        
        DW2323 C 324234 05:00 06:00
        
        By wyjsc z programu wpisz 'exit'
        
        """)

def main():
    while True:
        
        string_input = input("Wprowadz dane zgodne ze schematem: \n")
        
        base_search =  re.compile(r'^(\w{2}\d{4}) (S|C) (\d+) (([0-1][0-9]|[2][0-3]):([0-5][0-9])) (([0-1][0-9]|[2][0-3]):([0-5][0-9]))')
        dane = base_search.search(string_input)
    
        if dane == None:
            print("BLAD")
        else:

            #zmienne czasu d1 - czas początkowy, d2 - czas końcowy
            car_id = dane.group(1)
            vehicle_type = dane.group(2)

            speed_limit = '.'
            
            whole_day = timedelta(hours = 24)
            
            d1 = dane.group(4)
            d2 = dane.group(7)

            #przejechana droga

            distance = int(dane.group(3))

            #format godziny i przygotowanie do kalkulacji czasu w którym została trasa przejechana

            start_time = datetime.strptime(d1, "%H:%M")
            end_time = datetime.strptime(d2, "%H:%M")

            #kalkulacja czasu, jeżeli start_time jest większy niż end_time to odwracam działanie
            if start_time > end_time:
                final_time = (end_time - start_time) + whole_day
            else:
                final_time = end_time - start_time

            time_seconds = float(final_time.total_seconds())

            # kalkulacja średniej prędkości na danym odcinku
            speed = distance / time_seconds

            convert_speed = (speed*3600)/1000
            
            if (vehicle_type == "S" and convert_speed > 140) or (vehicle_type == "C" and convert_speed > 80):
                speed_limit = 'M'
                print(f"{car_id} {speed_limit} {convert_speed:.2f}")
            else:
                print(f"{car_id} {speed_limit} {convert_speed:.2f}")
        
        if string_input.lower() == 'exit':
                break
    
if __name__ == "__main__":
    main()

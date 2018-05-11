# Thai Thien
# 17c 12 031

from datetime import datetime
from pytz import timezone
import sys

def gen_time_by_city(city_name):
    """
    Get current time at city
    :param city_name: Ho Chi Minh, San Francisco, Paris, Frankfurt, Greece, Taipei, Tokyo, Brisbane, Singapore, Beijing, Seoul
    :return: 20:32:15 15/11/2016
    """
    # https://www.zeitverschiebung.net/en/city/2925533
    city_to_timezone = {
        "Ho Chi Minh":"Asia/Saigon",
        "San Francisco":"America/Los_Angeles",
        "Paris":"Europe/Paris",
        "Frankfurt":"Europe/Berlin",
        "Greece":"Europe/Athens",
        "Taipei":"Asia/Taipei",
        "Tokyo":"Asia/Tokyo",
        "Brisbane":"Australia/Brisbane",
        "Singapore":"Singapore",
        "Beijing":"Asia/Shanghai",
        "Seoul":"Asia/Seoul"
    }

    result = None
    try:
        meow_zone = timezone(city_to_timezone[city_name])
        meow_time = datetime.now(meow_zone)
        result = meow_time.strftime('%H:%M:%S %d/%m/%Y')
    except Exception as e:
        result = str(type(e)) + "\n" + str(e.args) + "\n" + str(e)
    return result



if __name__ == "__main__":

    if (len(sys.argv)>1):
        city = sys.argv[1]
    else:
        city = input()
    result = gen_time_by_city(city)
    print("\n" + result + "\n")
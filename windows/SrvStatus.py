from __future__ import print_function
#Requires execution of pip install psutil before it will run
import psutil
# Call this function with the name of the service (Not the display name)
def get_service(name):
    service = None
    try:
        service = psutil.win_service_get(name)
        service = service.as_dict()
    except Exception as ex:
        # raise psutil.NoSuchProcess if no service with such name exists
        print(str(ex))

    return service

service = get_service('Dnscache')                       # See if Service exists

if service:
    print("Service found: ", service['display_name'], " ", service['status'], "\n")
else:
    print("Service not found")

if service and service['status'] == 'running':
    print("Service is running\n")
else: 
    print("Service is not running\n")
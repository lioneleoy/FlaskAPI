import wmi
from datetime import datetime
import pythoncom
# try:
#     c = wmi.WMI('172.20.177.47', user='lraja001c', password='Shadowking@1991')
# except Exception,e:
#     print "e"


def serviceStatus(service):
    print service
    pythoncom.CoInitialize()
    c = wmi.WMI('172.20.177.47', user='lraja001c', password='Shadowking@1991')
    code = c.Win32_service(Name=service, State="Running")
    if not code:
        status ="Service not Running"
        status_c = 0
        return status,status_c
    else:
        status = "Service  Running"
        status_c = 1
        return status, status_c

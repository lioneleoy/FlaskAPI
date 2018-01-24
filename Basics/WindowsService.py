import wmi

# try:
#     c = wmi.WMI('172.20.177.47', user='lraja001c', password='Shadowking@1991')
# except Exception,e:
#     print "e"


def serviceStatus(service):
    c = wmi.WMI('172.20.177.47', user='lraja001c', password='Shadowking@1991')
    code = c.Win32_service(Name=service, State="Running")
    if not code:
        return "Service not Running"
    else:
        return "Service Running"

devices = [
    {
        "hostname": "Cisco-819-router-01",
        "device_type": "Router",
        "management_ip": "10.0.0.10",
        "location": "Building A",
        "status": "operational",
        "cpu_usage": 45,
        "memory_usage": 60,
        "uptime": 120,
        "backup_status": "successful"
    },
    {
        "hostname": "Cisco-881-router-01",
        "device_type": "Router",
        "management_ip": "10.0.0.20",
        "location": "Building B",
        "status": "operational",
        "cpu_usage": 78,
        "memory_usage": 69,
        "uptime": 97,
        "backup_status": "successful"
    },
    {
        "hostname": "Cisco-888-router-01",
        "device_type": "Router",
        "management_ip": "10.0.0.30",
        "location": "Building A",
        "status": "operational",
        "cpu_usage": 88,
        "memory_usage": 70,
        "uptime": 80,
        "backup_status": "successful"
    },
    {
        "hostname": "Cisco-1100-router-01",
        "device_type": "Router",
        "management_ip": "10.0.0.40",
        "location": "Building C",
        "status": "operational",
        "cpu_usage": 55,
        "memory_usage": 91,
        "uptime": 200,
        "backup_status": "failed"
    },
    {
        "hostname": "Cisco-945-switch-01",
        "device_type": "Switch",
        "management_ip": "10.0.0.50",
        "location": "Building B",
        "status": "operational",
        "cpu_usage": 49,
        "memory_usage": 83,
        "uptime": 230,
        "backup_status": "failed"
    },
    {
        "hostname": "Cisco-784-switch-01",
        "device_type": "Switch",
        "management_ip": "10.0.0.60",
        "location": "Building C",
        "status": "operational",
        "cpu_usage": 95,
        "memory_usage": 79,
        "uptime": 168,
        "backup_status": "successful"
    },
    {
        "hostname": "Cisco-919-switch-01",
        "device_type": "Switch",
        "management_ip": "10.0.0.70",
        "location": "Building A",
        "status": "operational",
        "cpu_usage": 40,
        "memory_usage": 100,
        "uptime": 98,
        "backup_status": "failed"
    },
    {
        "hostname": "Cisco-2960-switch-01",
        "device_type": "Switch",
        "management_ip": "10.0.0.80",
        "location": "Building B",
        "status": "operational",
        "cpu_usage": 89,
        "memory_usage": 100,
        "uptime": 300,
        "backup_status": "failed"
    }
]

#include the count for devices and location
def count_dev(devices, field):
    total = {}

    for device in devices:
        value = device[field]
        if value in total:
            total[value] += 1
        else:
            total[value] = 1
    return total
dev_total = count_dev(devices, "device_type")
loc_total = count_dev(devices, "location")


#func to flag devices that need attention
def find_attention(devices):
    attention = []

    for device in devices:
        if(
            device["cpu_usage"] >=80 
            or device["memory_usage"] >= 85 
            or device["backup_status"] == "failed" 
            or device["status"] != "operational"
            or device["uptime"] < 100   
        ):
            attention.append(device)
    return attention
#print operational report
print("DEVICE OPERATIONAL REPORT ")
print()
#need to be 8 devices imported
print("Total number of devices: ", len(devices))
print()
#include the total count of device and location
print("Total number of devices:")
for device_type, total in dev_total.items():
    print(f" {device_type}: {total}")
print()
print("Total number of devices in locations:")
for location, total in loc_total.items():
    print(f" {location}: {total}")
#print the devices being flagged
print()
print("FLAG - These devices need attention:")
for device in find_attention(devices):
    print(f" {device['hostname']}")

#add a commit
operational_count = 0
for device in devices:
    if device["status"]=="operational":
        operational_count +=1
print()
print("Operational devices: ", operational_count)

#failed backup count
failed_count=0
for device in devices:
    if device["backup_status"]=="failed":
        failed_count +=1
print()
print("Devices with failed backups: ", failed_count)

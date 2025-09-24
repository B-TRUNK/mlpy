dict = {
    "Jan" : "January",
    "Feb" : "February",  
    "Mar" : "March",
    4     : "April",
    5     : ["May" ,"Mai" ,"Mayo" ,"Maggio"]
}

for key,value in dict:
    print(f"Key : {key},Value : {value}")

print(dict["Feb"])
print(dict.get("April" ,"Key Not Found"))
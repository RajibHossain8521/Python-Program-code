# in this program we see dictionary structure

bd_division_info={}
bd_division_info["Barisal"]={"District":6,"Upazilla":39,"Union":333}
bd_division_info["Chittagong"]={"District":11,"Upazilla":97,"Union":336}
bd_division_info["Dhaka"]={"District":13,"Upazilla":93,"Union":1833}
bd_division_info["Khulna"]={"District":10,"Upazilla":59,"Union":270}
bd_division_info["Mymensingh"]={"District":4,"Upazilla":34,"Union":350}
bd_division_info["Rajshahi"]={"District":8,"Upazilla":70,"Union":558}
bd_division_info["Rangpur"]={"District":8,"Upazilla":58,"Union":536}
bd_division_info["Sylet"]={"District":4,"Upazilla":38,"Union":334}

#print all bd_dovision_info
print(bd_division_info)

#print divisions names
divisions=bd_division_info.keys()
print(divisions)

#use loop for print division
for division in divisions:
	print("Division:",division)

#print speciefic history from dictionary
for division in divisions:
	print(division, "Upazilla", bd_division_info[division]["Upazilla"])

#print Union from dictionary of bd_division_info
for division in divisions:
	print(division, "Union", bd_division_info[division]["Union"])

#run loop directly on dictionary
for item in bd_division_info:
	print(item)

#if we want to see both key and value in output
#then we have two way, First way:
for key in bd_division_info:
	print(key)
	print(bd_division_info[key])

# Seconed way:
for key,value in bd_division_info.items():
	print(key)
	print(value)

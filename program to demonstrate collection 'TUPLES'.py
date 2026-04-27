#immutable , ordered , allows duplicates , saves different values/data types
print("\n===TUPLE EXAMPLE===")
coordinates = (10.5,"JEON JUNGKOOK",10.5)
print("tuple:", coordinates)
print("first coordinates:" , coordinates[-2])

#tuple unpacking
x,y,z = coordinates
print(f"unpacked: x={x},y={y},z={z}")

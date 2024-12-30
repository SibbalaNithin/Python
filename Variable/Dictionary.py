cameras = {"sony":500, "nikon":600, "canon":400}
print(cameras)
print(cameras["sony"])
print(cameras["nikon"])
print(cameras["canon"])


cameras["sony"] =  "200"
print(cameras)


cameras = {"sony":500, "nikon":600, "canon":400}
cameras.keys()
print(cameras.keys())
print(cameras.values())
print(cameras.items())

demo = cameras.copy()
print(demo)
print(demo.keys())
print(demo.values())
print(demo.items())

cameras = {"sony":500, "nikon":600, "canon":400}
del cameras["nikon"]
print(cameras)
print(cameras["sony"])

cameras = {"sony":500, "nikon":600, "canon":400}
cameras.clear()
print(cameras)


dict_x = {"name" : "Nithin", "age" : "22"}
dict_y = {"name" : "Girish"}
update_val = dict_y.update(dict_x)
print(update_val)

dict = {"Name" : "Nithin", "age" : "22"}
print(dict.keys())
print(dict.values())
print(dict.items())

dict = {"Name" : "Nithin", "age" : "22"}
dict.update({"Name" : "Girish", "age" : "22"})
print(dict.update())



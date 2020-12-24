import json

f = open("C:\\Users\\nursh\\PycharmProjects\\PyDraftExercise\\name.json")
data = json.load(f)
#print(data['hobbies'])

for item in data:
    print(data[item])


with open("NewOrder.json", "r") as orderJson:
    json_data = json.load(orderJson)

json_data['billing']["first_name"] = "Dave"
json_data['shipping']["first_name"] = "Dave"

with open("NewOrder.json", "w") as orderJson:
    json.dump(json_data, orderJson)



def update_json(files, **kwargs):

    with open(files, "r") as f:
        js_data = json.load(f)

    with open(files, "w") as orderJson:
        for key, value in kwargs.items():
            if key == "first_name":
                js_data['billing'][key] = value
                js_data['shipping'][key] = value
            elif key == "last_name":
                js_data['billing'][key] = value
                js_data['shipping'][key] = value
            elif key == "product_id":
                js_data['line_items'][0][key] = value


        json.dump(js_data, orderJson)


update_json("NewOrder.json", first_name="Nur", last_name="Shahjalal", product_id=14)

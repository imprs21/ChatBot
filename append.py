import json

def write_json(data,filename="job_intents.json"):
    with open(filename,"w") as f:
        json.dump(data,f,indent=4)


with open("job_intents.json") as json_file:
    data = json.load(json_file)
    temp=data["intents"]

    y=        {
            "tag": "age",
            "patterns": [
                "how old are you","when were you made","what is your age"
            ],
            "responses": [
                "I was made in 2023, if that's what you are asking!"
            ]
        }

    temp.append(y)

write_json(data)
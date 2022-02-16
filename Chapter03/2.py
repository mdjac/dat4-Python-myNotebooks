from my_modules.Chapter02_1_classes import Person, InvalidArgumentException

inputs = ["Mikkel Dahl","Mikkel","1fejl","Mikkel dahl","2fejl igen"]

for input in inputs:
    try:
        person = Person(input)
    except InvalidArgumentException as e:
        print(f"Failure with name: {input} Received exception: {e}")
    except Exception as e:
        print("Second catch with name: ",input,e)
    else:
        print("All good with name: ",input)
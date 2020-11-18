
def char_replace(string):
    replace_value = string[0]
    second_half = string[1:]
    new_string = f'{replace_value}{second_half.replace(replace_value, "$")}'

    return new_string

print(char_replace("racecar"))
print(char_replace("bobby"))
print(char_replace("talkative"))

posts = ("Python Basics", "Intro guide to python", "Some cool python course")

title, sub_heading, content = posts

print(title)
print(sub_heading)
print(content)   


name = "Botega University"
counter = 0

for na in name:
    counter += 1
    
    print(counter)

omitting = [1,6,9]

for om in range(0, 20):
    if om == omitting:
        omit = om.replace("")
        print(omit)

    else: print(om)
   
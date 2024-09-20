name = "vedantkumarsinghkashyapchauhanvisoliya"
name2 = "rahulsingh"
# name_length = len(name)
# print(name_length)

def name_shortener(name):
    name_length = len(name)
    if(name_length>10):
        shortened_name = name[0:10] + "..."
        return shortened_name
    else:
        return name
    
print(name_shortener(name))
print(name_shortener(name2))
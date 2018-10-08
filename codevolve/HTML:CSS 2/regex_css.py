var_class_1 = "h6"
var_class_2 = ""
var_property = "margin"
list_values = [
    "8px",
    "0",
    "",
    ""
]

if var_class_2:
    var_class_1 = "\\" + var_class_1 + "\s*" + ",\s*"
    var_class_2 = "\\" + var_class_2 + "\s*"
elif var_class_1:
    var_class_1 = "\\" + var_class_1 + "\s*"


if list_values[3]:
    list_values[0] = list_values[0] + "\s+"
    list_values[1] = list_values[1] + "\s+"
    list_values[2] = list_values[2] + "\s+"
    list_values[3] = list_values[3] + "\s*"
elif list_values[2]:
    list_values[0] = list_values[0] + "\s+"
    list_values[1] = list_values[1] + "\s+"
    list_values[2] = list_values[2] + "\s*"
elif list_values[1]:
    list_values[0] = list_values[0] + "\s+"
    list_values[1] = list_values[1] + "\s*"
elif list_values[0]:
    list_values[0] = list_values[0] + "\s*"

print(var_class_1 + var_class_2 + "{[\s|\S]*?" + var_property + "\s*:\s*" + list_values[0] + list_values[1] + list_values[2] + list_values[3] + "\s*;[\s|\S]*?}")

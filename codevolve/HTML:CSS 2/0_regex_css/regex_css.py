var_class_1 = ".table-receipt"
var_class_2 = ".t-footer"
var_property = "text-align"
list_values = [
    "center",
    "",
    "",
    "",
    ""
]

if var_class_2:
    # class_1, class_2 {...}
    # var_class_1 = "\\" + var_class_1 + "\s*" + ",\s*"
    # var_class_2 = "\\" + var_class_2 + "\s*"

    # class_1 class_2 {...}
    var_class_1 = "\\" + var_class_1 + "\s+"
    var_class_2 = "\\" + var_class_2 + "\s*"
elif var_class_1:
    var_class_1 = "\\" + var_class_1 + "\s*"

if list_values[4]:
    list_values[0] = list_values[0] + "\s+"
    list_values[1] = list_values[1] + "\s+"
    list_values[2] = list_values[2] + "\s+"
    list_values[3] = list_values[3] + "\s+"
    list_values[4] = list_values[4] + "\s*"
elif list_values[3]:
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


print(var_class_1 + var_class_2 + "{[\s|\S]*?" + var_property + "\s*:\s*" + list_values[0] + list_values[1] + list_values[2] + list_values[3] + list_values[4] + "\s*;[\s|\S]*?}")

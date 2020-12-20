def rgb(r, g, b):
    """
    Converts the RGB values into a hexadecimal number. The first two digits of the number represent the red, the middle two green and the last two blue. 
    """
    hex_dict = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}
    rgb_list = [r, g, b]
    for j in range(len(rgb_list)):
        if rgb_list[j] < 0:
            rgb_list[j] = 0
        if rgb_list[j] > 255:
            rgb_list[j] = 255
    temp_list = [(colour // 16, colour - (16 * (colour // 16))) for colour in rgb_list] # Computes each parameter's two digit values in base 16, using base ten
    hex_list = [str(hex_dict.get(tup[i], tup[i])) for tup in temp_list for i in range(2)] # Converts digits to base 16 notation if necessary
    return "".join(hex_list)


print(rgb(132, 35, 254))

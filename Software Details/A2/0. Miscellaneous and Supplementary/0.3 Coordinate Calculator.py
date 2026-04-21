def get_center_coords(text, screen_w=128, screen_h=64):

    text_w = len(text) * 8
    text_h = 8
    
    x = (screen_w - text_w) // 2
    y = (screen_h - text_h) // 2
    return x, y

while True:
    my_text = input("Enter your word(s): ")
    start_x, start_y = get_center_coords(my_text)
    print(my_text, start_x, start_y)
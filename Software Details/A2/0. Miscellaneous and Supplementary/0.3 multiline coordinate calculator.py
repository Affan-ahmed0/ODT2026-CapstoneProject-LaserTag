def get_multiline_coords(lines, screen_w=128, screen_h=64, line_spacing=10):
    total_h = (len(lines) * line_spacing) - (line_spacing - 8)
    
    start_y = (screen_h - total_h) // 2
    
    coords = []
    for i, line in enumerate(lines):
        line_w = len(line) * 8
        x = (screen_w - line_w) // 2
        y = start_y + (i * line_spacing)
        coords.append((x, y))
        
    return coords

while True:
    a = input("line 1: ")
    b = input("line 2: ")
    c = input("line 3: ")

    lines_to_show = [a, b, c]
    all_coords = get_multiline_coords(lines_to_show)

    for i, line in enumerate(lines_to_show):
        x, y = all_coords[i]
        print(line, x, y)

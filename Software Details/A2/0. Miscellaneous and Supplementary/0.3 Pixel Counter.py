while True:
    text = input("Enter Text: ")
    char_count = len(text)
    pixel_width = char_count * 8
    
    if pixel_width > 128:
        status = "⚠️  TOO WIDE (Cuts off)"
    elif pixel_width == 128:
        status = "✅ PERFECT FIT (Edge to edge)"
    else:
        status = f"✅ FITS (Center X = {(128 - pixel_width) // 2})"
        
    print(f"Characters: {char_count}")
    print(f"Total Width: {pixel_width} pixels")
    print(f"Status: {status}")
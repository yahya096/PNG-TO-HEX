from PIL import Image

def image_to_hex(image_path, values_per_line):
    img = Image.open(image_path)
    pixels = list(img.getdata())

    hex_values = []
    line_values = []
    
    for pixel in pixels:
        hex_value = f'0x{pixel[0]:02X}, 0x{pixel[1]:02X}, 0x{pixel[2]:02X},'
        line_values.append(hex_value)
        
        if len(line_values) == values_per_line:
            hex_values.append(', '.join(line_values))
            line_values = []

    return hex_values

def save_hex_to_file(hex_values, output_file):
    with open(output_file, 'w') as f:
        for hex_line in hex_values:
            f.write(hex_line + '\n')

if __name__ == "__main__":
    input_image = '/content/sample_data/wiou.png'
    output_file = '/content/sample_data/hex.txt'
    values_per_line = 240  # Nombre de valeurs par ligne
    
    hex_table = image_to_hex(input_image, values_per_line)
    save_hex_to_file(hex_table, output_file)

    print(f"Les valeurs hexadécimales ont été enregistrées dans '{output_file}'.")

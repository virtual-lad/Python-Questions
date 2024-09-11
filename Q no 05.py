
import re

def decode_grid(grid):
    
    rows = len(grid)
    cols = len(grid[0])
    
    result = []
    
    for col in range(cols):
        for row in range(rows):
            result.append(grid[row][col])
    
    decoded_string = ''.join(result)
    cleaned_string = re.sub(r'[^a-zA-Z0-9#%!]', ' ', decoded_string)
    decoded_string = re.sub(r'(?<=\w)([^a-zA-Z0-9]+)(?=\w)', ' ', cleaned_string )
    return decoded_string.strip()

# Example usage:
input_grid = [
    "Tsi",
    "h%x",
    "i #",
    "sM ",
    "$a ",
    "#t%",
    "ir!"
]

output_string = decode_grid(input_grid)
print(output_string)  
def convert_temperature(value, unit):
    
    if unit == 'C':
        converted_value = (value * 9/5) + 32
        converted_unit = 'F'
    elif unit == 'F':
        converted_value = (value - 32) * 5/9
        converted_unit = 'C'
    else:
        raise ValueError("Unit must be 'C' for Celsius or 'F' for Fahrenheit.")
    
    return converted_value, converted_unit

temp_in_fahrenheit = convert_temperature(60, 'C')
temp_in_celsius = convert_temperature(212, 'F')

print(f"60°C is {temp_in_fahrenheit[0]}°{temp_in_fahrenheit[1]}")
print(f"212°F is {temp_in_celsius[0]}°{temp_in_celsius[1]}")

def calculate_bmi(weight_kg,height_m):
    BMI = (weight_kg)/(height_m*height_m)
    return BMI
weight_kg = float(input())
height_m = float(input())
result = calculate_bmi(weight_kg,height_m)
print(result)

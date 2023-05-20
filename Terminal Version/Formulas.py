BMI = weight / pow ((height / 100), 2)

Ideal_Fat_Percentage_M = (1.20 * BMI) + (0.23 * age)-16.2
Ideal_Fat_Percentage_F = (1.20 * BMI) + (0.23 * age) - 5.4

if 0 < age <= 15:
    Fat_Percentage = (1.51 * BMI) - (0.70 * age)-(3.6 * gender)+1.4
else:
    Fat_Percentage = (1.20 * BMI) + (0.23 * age)-(10.8 * gender)-5.4


VFI_M = Fat_Percentage_M - 10
VFI_F = Fat_Percentage_F - 10

TBW_M = 2.447 - (0.09156 * age) + (0.1074 * height) + (0.3362 * weight)
TBW_F = -2.097 + (0.1069 * height) + (0.2466 * weight)

Water_Percentage_M = (TBW_M / weight) * 100
Water_Percentage_F = (TBW_F / weight) * 100

Muscle_Mass_M = (0.32810 * weight) + (0.33929 * height) - 29.5336
Muscle_Mass_F = (0.29569 * weight) + (0.41813 * height) - 43.2933


BMR_M = (10 * weight) + (6.25 * height) - (5 * age) + 5
BMR_F = (10 * weight) + (6.25 * height) - (5 * age) - 161


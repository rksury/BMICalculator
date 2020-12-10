def Body_mass_index_calculation(bmc_data):
    for x in bmc_data:
        bmi_calculation = float('%.2f' % (float(x.get('WeightKg')) / (float(x.get('HeightCm')) / 100)))
        x['BMI'] = bmi_calculation
        if bmi_calculation <= 18.4:
            x['BMICategory'] = 'Underweight'
            x['HealthRisk'] = 'Malnutrition risk'
        elif 18.5 <= bmi_calculation <= 24.9:
            x['BMICategory'] = 'Normal weight'
            x['HealthRisk'] = 'Low risk'
        elif 25.0 <= bmi_calculation <= 29.9:
            x['BMICategory'] = 'Overweight'
            x['HealthRisk'] = 'Enhanced risk'
        elif 30.0 <= bmi_calculation <= 34.9:
            x['BMICategory'] = 'Moderately obese'
            x['HealthRisk'] = 'Medium risk'
        elif 35.0 <= bmi_calculation <= 39.9:
            x['BMICategory'] = 'severely obese'
            x['HealthRisk'] = 'High risk'
        else:
            x['BMICategory'] = 'Very severely obese'
            x['HealthRisk'] = 'Very high risk'


if __name__ == '__main__':
    Body_mass_index_calculation(bmc_data=[])  # Add your Input data here

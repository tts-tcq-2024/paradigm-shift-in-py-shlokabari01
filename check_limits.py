def check_temperature(temperature):
    return 0 <= temperature <= 45

def check_soc(soc):
    return 20 <= soc <= 80

def check_charge_rate(charge_rate):
    if charge_rate > 0.8:
        print('Charge rate is out of range!')
        return False
    return True

def main_check(temperature, soc, charge_rate):
    return check_temperature(temperature) and check_soc(soc) and check_charge_rate(charge_rate)

# Example usage:
temperature = 30
soc = 70
charge_rate = 0.7

if main_check(temperature, soc, charge_rate):
    print("All parameters are within acceptable ranges.")
else:
    print("One or more parameters are out of acceptable ranges.")

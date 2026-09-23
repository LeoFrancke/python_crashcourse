# 8.14 Cars

def make_car(manufacturer, model, **car_info):
    """Store info about a car. It can accept an arbitrary number of kwargs."""
    car_info['manufacturer'] = manufacturer
    car_info['model_name'] = model
    return car_info


car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)


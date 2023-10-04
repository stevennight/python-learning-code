def make_sandwich(*toppings):
    """print sandwich toppings"""
    print("sandwich toppings:")
    # variable named toppings is tuple, not list
    for topping in toppings:
        print(f'\t{topping}')


make_sandwich('huotui')
make_sandwich('zhishi', 'jidan')
make_sandwich('sanwenyu', 'huanggua', 'shengcai')

print('\n')


def build_profile(first_name, last_name, **user_info):
    user_info['first_name'] = first_name
    user_info['last_name'] = last_name
    return user_info


user_profile = build_profile(
    'alber', 'estin?', location='Guangzhou',
    country="China", age=18
)
print(user_profile)

print('\n')


def make_car(maker, model, **kwargs):
    kwargs['maker'] = maker
    kwargs['model'] = model
    return kwargs


car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)

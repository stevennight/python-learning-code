def make_shirt(size, text):
    '''make a shirt with specified size and text'''
    print(f"make a shirt, size: {size}, text: {text}")

make_shirt('small', 'H')
make_shirt(size='middle', text='B')

print('\n')
def make_shirt(size = 'big', text='I love Python'):
    '''make a shirt with specified size and text'''
    print(f"make a shirt, size: {size}, text: {text}")

make_shirt()
make_shirt('middle')
make_shirt(text="I love PHP")

print('\n')
def describe_city(city_name, country='China'):
    '''print A city with country'''
    print(f"{city_name.title()} is in {country.title()}.")
describe_city('Shanghai')
describe_city('Reykjavik', 'iceland')
describe_city(country='Japan', city_name='Tokyo')
def city_country(city, country):
    """print a city with country"""
    print(f"{city.title()}, {country.title()}")
city_country('Gunagzhou', 'China')
city_country('Santiago', 'Chile')
city_country('Osaka', 'Japan')

print('\n')
def make_album(singer, album, num = None):
    """make a album dict"""
    album = {
        'singer': singer,
        'album': album,
    }
    if num:
        album['num'] = num
    return album
print(make_album('Haha', 'Juhua', 10))
print(make_album('Zhou', 'baigua'))
print(make_album('eason', 'Kugua'))

print('\n')
while True:
    print('Give A ablum information please:')
    print('enter Q to quit.')

    singer = input('Input Singer: ')
    if singer.lower() == 'q':
        break

    album = input('Input Album: ')
    if album.lower() == 'q':
        break

    print(make_album(singer, album))

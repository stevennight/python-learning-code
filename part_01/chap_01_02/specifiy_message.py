name = "eric"
print(
    f"Hello {name.title()}, would you like to learn some Python today?"
)


name = "eRiC"
# 存数据库
name = name.lower()
print(f"{name.lower()} {name.upper()} {name.title()}")



famous_person = "albert einstein"
said = "A person who never made a mistake never tried anything new."
message = f'{name.title()} once said, "{said}"'
print(message)


name = "\n\tHana Bingo\n "
print(name)
print(name.lstrip())
print(name.rstrip())
print(name.strip())

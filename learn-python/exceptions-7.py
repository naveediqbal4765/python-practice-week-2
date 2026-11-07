# # 2. Carry on or stop? For each situation, decide whether your code should carry on or stop with an error, 
# # and write a one-line comment explaining why:

# # a.orders.json doesn't exist the first time the script runs, because no orders have been saved yet.
# should carry on, well start with an empty list.
# # b.A customer left the optional phone number field blank.
# itll get default value e.g none, should carry on
# # c.An invoice total can't be read as a number.
# stop with a ValueError , means the data is corrupt
# # d.The API key your program needs at startup is missing.
# should stop, program cant work without the key
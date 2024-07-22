# -----------Error handling in python------------#

# try: Something that might cause an exception

# except: Do this if there was an exception

# else: Do this if there were no exceptions

# finally: Do this no matter what happens


# example:

try:
    file = open("test_file.txt")
except FileNotFoundError as error:
    file = open("test_file.txt", "w")
    file.write("Something")
    print(f"The {error} was triggered and a new file was created with 'w' mode in else block")
else:
    print(file.read())
finally:
    file.close()
    print("file was closed")



# raise: This keyword is used to raise an error, even if there i no mistake in code.

## Basic JSON data writing, reading and update data

# Write: json.dump()
# Read: json.load()
# Update data: json.update()

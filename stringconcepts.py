print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')


a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.
Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
print(a[7])
print(len(a))
print("sit"in a)

if "yes" in a:
    print("Yes, found the text.")
    
print("expensive" not in a)

b = "Hello, World!"
print(b[2:6])
print(b[:6])
print(b[2:])

print(b[5:-1])
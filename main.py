# Replace the Last occurrence of Substring in String in Python

my_str = 'one two two'


def replace_last(string, old, new):
    return new.join(string.rsplit(old, 1))


# 👇️ one two three
print(replace_last(my_str, 'two', 'three'))

new_str = 'three'.join(my_str.rsplit('two', 1))
print(new_str)  # 👉️ one two three
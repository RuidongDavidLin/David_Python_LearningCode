bicycle = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycle)
print(bicycle[0])
print(bicycle[0].title())
print(f"{bicycle[0].title()}")
# 列表的索引应该从0开始，而非1开始
print(f"{bicycle[-1]}")

message = f'My first bicycle is a {bicycle[0].title()}'
print(message)
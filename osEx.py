import os

print(os.environ.get("DB_USER"))
# print(os.environ)
for i in os.environ:
    print(i)


print("CLIENT_KEY" in os.environ)
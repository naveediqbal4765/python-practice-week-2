# 2. Test settings. You want to test with no tax without touching the real settings. 
# What does this print, and why? Fix it with .copy():

# Copy
settings = {"currency": "PKR", "tax": 0.18}
# test_settings = settings
test_settings = settings.copy()
test_settings["tax"] = 0
print(settings["tax"])

# this prints 0 because both test settings and settings got the same object rn(both pointing at same address)


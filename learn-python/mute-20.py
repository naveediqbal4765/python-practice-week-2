# 3. Settings for each customer. Every customer starts from the same default settings:

# defaults = {"currency": "PKR", "tags": ["standard"]}
# Write settings_for(defaults, tag), which returns a separate copy of the settings with 
# tag added to its tags list. Call it once with "wholesale" and once with "vip", 
# then print both results and defaults.
import copy

defaults = {"currency": "PKR", "tags": ["standard"]}

def settings_for(defaults, tag):
    # settings = defaults.copy()
    settings = copy.deepcopy(defaults)
    settings["tags"].append(tag)
    return settings

print(settings_for(defaults, "wholesale"))
print(settings_for(defaults, "vip"))
print(defaults)


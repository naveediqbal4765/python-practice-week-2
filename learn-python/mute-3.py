# 3. Fixing a code. A product code was typed with a letter O instead of a zero: sku = "PEN-O42". 
# Try sku[4] = "0" and read the error. Then fix it a different way, so print(sku) shows PEN-042.
sku = "PEN-O42"
# sku[4] = "0" TypeError: 'str' object does not support item assignment
sku = sku.replace("O", "0")
print(sku)
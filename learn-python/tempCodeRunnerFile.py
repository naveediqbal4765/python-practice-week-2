
with open("learn-python/orders.json", "w") as file:
        json.dump([{"id": "Noor Foods", "status" : "pending"},
                    {"id": "Bilal Foods", "status" : "delivered"} ], file, indent = 2)
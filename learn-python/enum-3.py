# Checking orders. Using the TaskStatus idea, create an OrderStatus enum with PENDING,
# DELIVERED and CANCELLED. Loop over the statuses below, as they might arrive from a file. 
# Turn each into an OrderStatus, print the valid ones, and for the invalid 
# ones print Skipping 'lost': not a valid status:

# Copy
# statuses = ["pending", "delivered", "lost", "Cancelled", "cancelled"]
# Why is "Cancelled" rejected? How could you clean it first so it's accepted?

from enum import StrEnum


class orderStatus(StrEnum):
    PENDING ="pending"
    DELIVERED= "delivered"
    LOST="lost"
    CANCELLED="cancelled"

statuses = ["pending", "delivered", "lost", "Cancelled", "cancelled"]

for status in statuses:
     status = orderStatus.lower(status)
     if status != orderStatus.LOST:
      print(status)
     else:
      print(f"Skipping '{status}': not a valid status")

# as enum compares the class values with list (statuses), cancelled is rejected 
# because "C" was an uppercase character , i used lower() method to clean the list
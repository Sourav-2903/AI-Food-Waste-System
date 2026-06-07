food_quantity = 120
hours_left = 6

priority_score = (
    food_quantity * 0.7
) + (
    (24 - hours_left) * 0.3
)

print(
    "Pickup Priority Score:",
    round(priority_score,2)
)
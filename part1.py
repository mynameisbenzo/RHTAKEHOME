db = [
    {
        "id": "A",
        "item": "soda",
        "cost": 1.00,
        "volume_discount": {
            "qty": 4,
            "cost": 3.00
        }
    },
    {
        "id": "B",
        "item": "apple",
        "cost": 0.45,
        "volume_discount": {
            "qty": 3,
            "cost": 1.00
        }
    },
    {
        "id": "C",
        "item": "jelly",
        "cost": 3.00,
        "volume_discount": None
    },
    {
        "id": "D",
        "item": "kleenex",
        "cost": 6.00,
        "volume_discount": None
    },
]


receipt_1 = "ABCD"
receipt_2 = "DCCBAABB"


def get(id):
    def id_match(entry):
        return entry["id"] == id
    item = filter(id_match, db)
    for i in item:
        return i


def checkout(receipt):
    total = 0.0
    item_count = {e: receipt.count(e) for e in set(receipt)}
    for item in item_count.keys():
        entry = get(item)
        if entry["volume_discount"] and entry["volume_discount"]["qty"] <= item_count[item]:
            discount = int(item_count[item] / entry["volume_discount"]["qty"])
            discount_price = discount * entry["volume_discount"]["cost"]
            remainder = item_count[item] % entry["volume_discount"]["qty"]
            remainder_price = remainder * entry["cost"]
            total += remainder + discount_price
        else:
            total += entry["cost"] * item_count[item]
    return '${0:.2f}'.format(total)


print(checkout(receipt_1))  # should be $10.45
print(checkout(receipt_2))  # should be $15.00

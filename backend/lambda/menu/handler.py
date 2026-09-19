import json

MENU = [
    {
        "id": 1,
        "name": "Vada Pav",
        "price": 20,
        "category": "Snacks"
    },
    {
        "id": 2,
        "name": "Masala Dosa",
        "price": 60,
        "category": "South Indian"
    },
    {
        "id": 3,
        "name": "Veg Sandwich",
        "price": 50,
        "category": "Snacks"
    },
    {
        "id": 4,
        "name": "Tea",
        "price": 15,
        "category": "Beverages"
    }
]


def lambda_handler(event, context):

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps(MENU)
    }


if __name__ == "__main__":
    response = lambda_handler({}, {})
    print(response["body"])
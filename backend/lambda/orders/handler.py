import json

orders = []


def lambda_handler(event, context):

    order = {
        "order_id": len(orders) + 1,
        "customer_name": "Harshad",
        "items": [
            {
                "name": "Vada Pav",
                "quantity": 2,
                "price": 20
            }
        ],
        "total": 40,
        "status": "PLACED"
    }

    orders.append(order)

    return {
        "statusCode": 201,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps(order)
    }


if __name__ == "__main__":
    response = lambda_handler({}, {})
    print(response["body"])
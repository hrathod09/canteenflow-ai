import json


def lambda_handler(event, context):

    analytics = {
        "total_orders": 125,
        "total_sales": 8750,
        "popular_item": "Vada Pav",
        "average_order_value": 70,
        "orders_today": 32
    }

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps(analytics)
    }


if __name__ == "__main__":
    response = lambda_handler({}, {})
    print(response["body"])
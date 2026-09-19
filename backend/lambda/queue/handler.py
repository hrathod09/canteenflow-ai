import json

queue = []


def lambda_handler(event, context):

    order_id = event.get("order_id", 1)

    order = {
        "order_id": order_id,
        "position": len(queue) + 1,
        "status": "WAITING"
    }

    queue.append(order)

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps(order)
    }


if __name__ == "__main__":
    test_event = {
        "order_id": 1
    }

    response = lambda_handler(test_event, {})
    print(response["body"])
import json


def lambda_handler(event, context):

    prediction = {
        "item": "Vada Pav",
        "predicted_demand": 85,
        "recommendation": "Prepare approximately 85 units"
    }

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps(prediction)
    }


if __name__ == "__main__":
    response = lambda_handler({}, {})
    print(response["body"])
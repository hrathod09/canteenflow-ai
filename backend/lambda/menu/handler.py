def lambda_handler(event, context):
    return {
        "statusCode": 200,
        "body": "Menu Lambda is working!"
    }


if __name__ == "__main__":
    response = lambda_handler({}, {})
    print(response)
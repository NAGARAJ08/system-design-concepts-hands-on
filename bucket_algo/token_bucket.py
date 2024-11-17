

# A simple rate limiter using token bucket

# current data for each client

from datetime import datetime
import time

metadata = {
    "c1": {
        "bucketSize": 5,
        "lastupdated": datetime.now(),
        "tokens": 5,
        "refillRate": 10
    }
}


def token_bucket(client_id):

    if client_id in metadata:

        client_data = metadata[client_id]

        now = datetime.now()

        time_elapsed = (now-client_data['lastupdated']).total_seconds()

        tokens_to_add = int(time_elapsed/client_data['refillRate'])

        print(f"tokens to add are : {tokens_to_add}")

        if tokens_to_add > 0:
            client_data['tokens'] = min(
                client_data['bucketSize'], client_data['tokens']+tokens_to_add)

        if client_data['tokens'] > 0:
            client_data['tokens'] -= 1
            return True

    return False


def main(client_id):

    response = token_bucket(client_id=client_id)

    if response:
        print(f"Hey {client_id}, you're allowed to proceed!")
    else:
        print(f"Too many requests bro, {client_id}! Please calm down bro.")


for i in range(20):
    main(client_id="c1")
    time.sleep(1)

import asyncio
import uuid
import argparse

from workflows import SayHello
from temporalio.client import Client
from shared import TASK_Q_NAME


async def main(name: str):
    # Create client connected to server at the given address
    client = await Client.connect("localhost:7233")

    # Execute a workflow
    result = await client.execute_workflow(
        SayHello.run, name, id=name + ":" + str(uuid.uuid4()), task_queue=TASK_Q_NAME
    )

    print(f"Result: {result}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run Temporal workflow client.")
    parser.add_argument(
        "--name",
        default="World",
        required=False,
        type=str,
        help="Name to greet in the workflow.",
    )
    args = parser.parse_args()
    name = args.name

    asyncio.run(main(name))

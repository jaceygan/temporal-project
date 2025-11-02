from temporalio import activity


@activity.defn
async def say_hello(name: str) -> str:
    return f"Hello, {name}!"


@activity.defn
async def say_bye(name: str) -> str:
    return f"Bye bye, {name}!"

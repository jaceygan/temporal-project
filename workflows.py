from datetime import timedelta
from temporalio import workflow

with workflow.unsafe.imports_passed_through():
    from activities import say_hello, say_bye


@workflow.defn
class SayHello:
    @workflow.run
    async def run(self, name: str) -> str:
        hello_result = await workflow.execute_activity(
            say_hello, name, start_to_close_timeout=timedelta(seconds=5)
        )

        bye_result = await workflow.execute_activity(
            say_bye, name, start_to_close_timeout=timedelta(seconds=5)
        )

        return f"{hello_result}\n{bye_result}"

from databricks.sdk import WorkspaceClient
from databricks_mcp import DatabricksOAuthClientProvider
from mcp.client.streamable_http import streamablehttp_client as connect
from mcp import ClientSession
from databricks.sdk import WorkspaceClient
from databricks_mcp import DatabricksOAuthClientProvider
from mcp.client.streamable_http import streamablehttp_client as connect
from mcp import ClientSession
import asyncio


DATABRICKS_CLI_PROFILE = "custom-mcp-server"
client = WorkspaceClient(profile=DATABRICKS_CLI_PROFILE)
async def main():
    # Connect to a streamable HTTP server

    app_url = "https://mcp-custom-server-bundles-163602342046619.19.azure.databricksapps.com/mcp/"
    async with connect(app_url, auth=DatabricksOAuthClientProvider(client)) as (
        read_stream,
        write_stream,
        _,
    ):
        # Create a session using the client streams
        async with ClientSession(read_stream, write_stream) as session:
            # Initialize the connection
            await session.initialize()
            # Call the add tool
            tool_result = await session.call_tool("add", {"a": 5, "b": 3})
            print(f"Tool result: {tool_result}")


# Run the async main function
if __name__ == "__main__":
    asyncio.run(main())
    #print(f"Tool result: {tool_result}")

# Implementing a Simple Fetch MCP Server Locally

In this exercise, we'll implement a simple Fetch MCP Server locally using the [Fetch MCP Server](https://github.com/modelcontextprotocol/servers/tree/main/src/fetch) template and test it using the [MCP Inspector](https://github.com/modelcontextprotocol/inspector) tool in your local machine.

1. Create a new directory for your project

   ```bash
   mkdir fetch-mcp-server
   cd fetch-mcp-server
   ```

2. Create a python virtual environment and activate it

   ```bash
   python -m venv .venv/
   . .venv/bin/activate
   ```

3. Install the Fetch MCP Server

   ```bash
   pip install mcp-server-fetch
   ```

4. Run the MCP Inspector

   ```bash
   npx @modelcontextprotocol/inspector python -m mcp_server_fetch --ignore-robots-txt
   ```

5. Test the MCP Server

   - Navigate to <http://localhost:5173>
   - Click on the `Connect` button
   - Select the `Tools` tab
   - Click on the `List Tools` button
     - You should see the `fetch` tool in the list

6. Test the `fetch` tool

   - Click on the `fetch` tool
   - Enter a test URL in the right panel
     - For example: `https://en.wikipedia.org/wiki/Draft:Model_Context_Protocol`
   - Click on the `Run Tool` button
   - You should see the response from the `fetch` tool as `Tool Result: Success` and the text contents of the page below

Now you can use the `fetch` tool in your own function calls to retrieve information from the web using this very simple MCP Server.

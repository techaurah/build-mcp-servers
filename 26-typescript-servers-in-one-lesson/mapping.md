# Mapping table: Python SDK (v1) to TypeScript SDK

| Idea | Python (this course) | TypeScript |
|------|----------------------|------------|
| Server instance | FastMCP("leaddesk") | new McpServer({ name, version }) |
| Tool registration | @mcp.tool() decorator | server.registerTool(name, config, handler) |
| Input schema source | Type hints plus docstring | Zod schema (fields of a z.object, passed as a raw shape) plus description field |
| Tool description | The function docstring | The description property |
| Result shape | Returned dict or string, SDK wraps it | { content: [{ type: "text", text }] } |
| Run on stdio | mcp.run(transport="stdio") | server.connect(new StdioServerTransport()) |
| Logging rule | Never print to stdout | console.error only, never console.log |

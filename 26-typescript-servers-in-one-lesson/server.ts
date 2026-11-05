// Lesson 26: LeadDesk's scorer in the TypeScript SDK dialect.
// NEEDS: Node 18+, npm install @modelcontextprotocol/sdk zod
// Era note: registerTool is the current high level shape; older
// examples use server.tool with a near identical signature.
import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

const server = new McpServer({ name: "leaddesk", version: "0.1.0" });

server.registerTool("score_lead", {
  description: "Score a lead 0 to 100 from budget, timeline, and decision authority. The score is computed by the server from these facts.",
  inputSchema: {
    budget_usd: z.number().int(),
    timeline_days: z.number().int(),
    is_decision_maker: z.boolean(),
  },
}, async ({ budget_usd, timeline_days, is_decision_maker }) => {
  let score = 0;
  score += budget_usd >= 1000 ? 40 : budget_usd >= 500 ? 20 : 5;
  score += timeline_days <= 14 ? 35 : timeline_days <= 30 ? 20 : 5;
  score += is_decision_maker ? 25 : 5;
  const band = score >= 80 ? "hot" : score >= 55 ? "warm" : "cold";
  return { content: [{ type: "text", text: JSON.stringify({ score, band }) }] };
});

const transport = new StdioServerTransport();
await server.connect(transport);
console.error("leaddesk listening on stdio"); // stderr only: stdout is the wire

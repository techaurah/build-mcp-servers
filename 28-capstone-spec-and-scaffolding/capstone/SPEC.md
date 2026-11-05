# LeadDesk MCP: capstone specification

## Purpose
A teaching MCP server giving an AI assistant a safe lead pipeline
for a small service business without a CRM. Inspired by the
production LeadPipe MCP design; sized and simplified for learning.

## Surface
Tools: capture_lead, score_lead, list_leads, get_lead,
draft_followup, book_appointment.
Resources: leaddesk://pipeline/summary, leaddesk://pipeline/stages,
template leaddesk://leads/{lead_id}.
Prompts: qualify-lead, daily-digest.

## Safety model
Demo mode by default (seeded fake leads, no credentials).
Write modes: direct, dry_run, approval. Scores computed server
side. Stages move forward only; LOST from anywhere. No tool sends
anything to anyone.

## Acceptance gates
1. Scripted client suite passes against the stdio server.
2. Design checker and annotation truth table pass.
3. Packaging checks pass (server.json, project file).
4. README passes the Lesson 23 audit including Limits.

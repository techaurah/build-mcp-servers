#!/usr/bin/env python3
"""Generate the course diagram set as clean, branded SVGs.

Style: white canvas, navy (#0B1F4A) primary boxes with white text,
light blue (#E0F2FE) secondary boxes with navy text, cyan (#0891B2)
arrows, amber (#F59E0B) accent for warnings/gates. Run: python3 generate_visuals.py
"""
import os

OUT = os.path.dirname(os.path.abspath(__file__))
NAVY = "#0B1F4A"
LIGHT = "#E0F2FE"
CYAN = "#0891B2"
GREY = "#475569"
FONT = "Segoe UI, Helvetica, Arial, sans-serif"


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


class SVG:
    def __init__(self, w, h, title, subtitle):
        self.w, self.h = w, h
        self.parts = [
            f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">',
            f'<rect width="{w}" height="{h}" fill="#FFFFFF"/>',
            f'<text x="40" y="52" font-family="{FONT}" font-size="30" font-weight="700" fill="{NAVY}">{esc(title)}</text>',
            f'<text x="40" y="82" font-family="{FONT}" font-size="17" fill="{GREY}">{esc(subtitle)}</text>',
            f'<rect x="40" y="98" width="90" height="5" fill="{CYAN}"/>',
        ]

    def box(self, x, y, w, h, label, sub="", style="navy"):
        fill, tcol, scol = (NAVY, "#FFFFFF", "#BFE3F2") if style == "navy" else (LIGHT, NAVY, "#33506E")
        if style == "amber":
            fill, tcol, scol = "#FEF3C7", NAVY, "#7C5A03"
        self.parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="{fill}"/>')
        if sub:
            self.parts.append(f'<text x="{x + w/2}" y="{y + h/2 - 4}" text-anchor="middle" font-family="{FONT}" font-size="19" font-weight="700" fill="{tcol}">{esc(label)}</text>')
            self.parts.append(f'<text x="{x + w/2}" y="{y + h/2 + 20}" text-anchor="middle" font-family="{FONT}" font-size="14" fill="{scol}">{esc(sub)}</text>')
        else:
            self.parts.append(f'<text x="{x + w/2}" y="{y + h/2 + 7}" text-anchor="middle" font-family="{FONT}" font-size="19" font-weight="700" fill="{tcol}">{esc(label)}</text>')

    def arrow(self, x1, y1, x2, y2, label=""):
        self.parts.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{CYAN}" stroke-width="3" marker-end="url(#ah)"/>')
        if label:
            self.parts.append(f'<text x="{(x1+x2)/2}" y="{(y1+y2)/2 - 8}" text-anchor="middle" font-family="{FONT}" font-size="14" font-weight="600" fill="{CYAN}">{esc(label)}</text>')

    def note(self, x, y, text):
        self.parts.append(f'<text x="{x}" y="{y}" font-family="{FONT}" font-size="15" fill="{GREY}">{esc(text)}</text>')

    def save(self, name):
        defs = ('<defs><marker id="ah" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" '
                'markerHeight="7" orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z" '
                f'fill="{CYAN}"/></marker></defs>')
        body = "\n".join(self.parts[:2] + [defs] + self.parts[2:]) + "\n</svg>"
        with open(os.path.join(OUT, name), "w") as f:
            f.write(body)
        print("wrote", name)


def hflow(name, title, subtitle, steps, note=""):
    n = len(steps)
    w = 1200
    bw = (w - 80 - (n - 1) * 50) // n
    s = SVG(w, 300, title, subtitle)
    y = 140
    for i, (label, sub) in enumerate(steps):
        x = 40 + i * (bw + 50)
        s.box(x, y, bw, 90, label, sub, "navy" if i in (0, n - 1) else "light")
        if i < n - 1:
            s.arrow(x + bw + 4, y + 45, x + bw + 46, y + 45)
    if note:
        s.note(40, 275, note)
    s.save(name)


def grid(name, title, subtitle, cells, cols=3, note=""):
    rows = (len(cells) + cols - 1) // cols
    w, h = 1200, 140 + rows * 120 + 40
    s = SVG(w, h, title, subtitle)
    bw = (w - 80 - (cols - 1) * 40) // cols
    for i, (label, sub) in enumerate(cells):
        r, c = divmod(i, cols)
        x, y = 40 + c * (bw + 40), 140 + r * 120
        s.box(x, y, bw, 90, label, sub, "light")
    if note:
        s.note(40, h - 18, note)
    s.save(name)


if __name__ == "__main__":
    grid("course-map.svg", "Course map: 32 lessons, one server",
         "Every module adds one layer of LeadDesk. The capstone assembles them.",
         [("M0 Start here", "Lessons 00 to 01"), ("M1 Protocol by hand", "Lessons 02 to 05"),
          ("M2 First servers", "Lessons 06 to 09"), ("M3 Richer servers", "Lessons 10 to 13"),
          ("M4 Clients and hosts", "Lessons 14 to 16"), ("M5 Going remote", "Lessons 17 to 19"),
          ("M6 Production", "Lessons 20 to 25"), ("M7 Wider shelf", "Lessons 26 to 27"),
          ("M8 Capstone", "Lessons 28 to 31")],
         note="LeadDesk (capstone) reuses every module before it. Nothing is throwaway.")
    hflow("protocol-exchange.svg", "The protocol exchange",
          "Handshake, discovery, then calls. JSON-RPC 2.0 throughout.",
          [("initialize", "versions and capabilities"), ("tools/list", "discovery at runtime"),
           ("tools/call", "the server runs its code"), ("result", "content or isError")],
          note="Notifications (no id, no reply) carry progress, logging, and list changes alongside.")
    grid("three-primitives.svg", "Three primitives, three deciders",
         "The primitive follows from who decides when it is used.",
         [("Tools", "the model decides"), ("Resources", "the application decides"),
          ("Prompts", "the user decides")], cols=3,
         note="Sampling, roots, and elicitation flow the other way: the server asks, the client and user approve.")
    hflow("transports.svg", "Two transports, one protocol",
          "Stdio for local servers. Streamable HTTP for remote ones.",
          [("Host", "launches or connects"), ("stdio", "subprocess, newline JSON"),
           ("Streamable HTTP", "one endpoint, POST and stream"), ("Server", "same messages either way")],
          note="The older HTTP plus SSE shape (two endpoints) is deprecated since the 2025-03-26 revision.")
    grid("security-layers.svg", "Security is layers, not a filter",
         "Each layer holds when the one above it is steered.",
         [("Annotations", "hosts ask before danger"), ("Scopes", "tokens bound actions"),
          ("Approval modes", "humans gate writes"), ("Server side rules", "dedup, stages, booking checks"),
          ("Roots and sandbox", "reach is fenced"), ("Vetting", "servers are dependencies")], cols=3,
         note="Design so a successful prompt injection buys an attacker little.")
    hflow("capstone-flow.svg", "Capstone: LeadDesk MCP",
          "Capture, score, draft, book: with gates where the risk lives.",
          [("capture_lead", "dedup on email"), ("score_lead", "computed server side"),
           ("draft_followup", "draft only, never sends"), ("book_appointment", "approval and idempotency key")],
          note="Demo mode by default. Dry run and approval are modes, not afterthoughts.")

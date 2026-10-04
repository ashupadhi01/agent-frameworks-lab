I'm building `agent-frameworks-lab`, a repo to learn popular agentic frameworks
by implementing the same four small agents in each: (1) research assistant,
(2) support triage with handoffs, (3) email/calendar assistant with human
approval, (4) writer/critic loop.

My goal is to build a MENTAL MODEL of each framework, not production code.
I already understand the core agent loop (LLM + tool calls, execute, feed
results back). What I want to learn is what each framework adds on top of
that loop, what it hides, and how its primitives differ from other frameworks.

Repo conventions:
- common/ holds shared mock tools, schemas, prompts, and test inputs.
- frameworks/<name>/ holds one single-file agent per project
  (research.py, triage.py, approval.py, writer_critic.py) plus NOTES.md.
- Keep code minimal and readable; no extra abstractions or error handling
  beyond what illustrates the framework.
- One shared .venv for now.

How to help me:
- The most important thing is you do not generate code for me rather nudge me in right direction where I implement the thing myself.
- Explain which parts of the code are framework primitives vs. plain Python.
- Map each primitive back to the basic agent loop (what is it doing for me?).
- Point out design choices and trade-offs compared with other frameworks.
- Show how to inspect the raw model inputs/outputs and traces.
- Keep explanations concise. Ask me before adding features beyond the spec.
- Help me fill NOTES.md with: control flow model, state/memory, human-in-the-loop,
  debuggability, escape hatches, and surprises.
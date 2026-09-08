# spec-drift-detector

A Claude Code plugin that catches an agent drifting from its stated constraints mid-session.

## Problem statement

Long agentic sessions suffers from **persona drift**: a model can keep the reasoning correctly about the task while quietly o longer honoring the formatting rule, scope boundary or tone constraing it was given earlier in the session. The constraint is still technically "in context" but how reliably it is applied degrades as more context accumulates around it. This is a detection problem, not a prompting one. 

## How it works

`spec-drift-detector` hooks into the Stop event and checks the last response against a written invariant checklist ([invariants.md](invariants.md)):

1. **Deterministic checks** first.
2. **Model judgement** for anything that needs real understanding.

If a violation is found, the hooks blocks the turn from ending and reports specific, correctable reason. This is layered on top of Claude Code's own loop protection rather tan re-inventing them.

## Status

Early scaffolding. The plugin manifest and invariant checklist exist; the
hook implementation, skill, and marketplace entry are stubbed out and not
yet functional.

## Tree

```
spec-drift-detector/
├── invariants.md                    # behavioral checklist checked against each response
├── notes/
│   └── persona-drift.md             # design notes on the persona drift problem
├── hooks/
│   ├── hooks.json                   # Stop hook wiring (WIP, currently empty)
│   └── drift_check.py               # hook logic (WIP, currently empty)
├── skills/
│   └── drift-check/
│       └── SKILL.md                 # skill definition (WIP, currently empty)
└── .claude-plugin/
    ├── plugin.json                  # plugin manifest
    └── marketplace.json             # marketplace listing (WIP, currently empty)
```

## License

See [LICENSE](LICENSE).
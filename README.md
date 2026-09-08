# spec-drift-detector
Spec drift detector: a Stop hook that checks the last response against a written invariant checklist — first deterministically, then via a real model judgment — and blocks the turn from ending with a specific, correctable reason when it's violated, layered on top of Claude Code's own loop protections rather than reinventing them

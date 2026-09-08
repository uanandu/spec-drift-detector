# Persona drift

Long agentic sessions have a documented failure mode called persona drift (instruction drift or context rot).

**NOTE**: This isn't the same failure as a model being wrong about something.

- A model can reason correctly about the task at hand while quietly no longer honoring a formatting rule, scope or a tone constraint it was given at the versy start of a session.

- We can miss this entirely as we tend to skim a long transcript and the content presented would still look reasonable.

## Problem

- It is a detection problem, not a prompting one.

- The constraint is still technically "in context" the whole time but what degrades is how reliably it is applied under the weight of items accumulated around it (as we go). 

**NOTE**: One of the solution that we might think of would be restating a rule mid-session but it isnt a reliable fix as it breaks the flow.
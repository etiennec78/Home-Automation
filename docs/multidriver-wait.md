# Automatic Gate: reactive multi-driver wait

An itinerary remains `on_approach` or `leaving` until the end of its run. Previously,
two runs could each reach their closing decision, see the other as active and then
wait only for the gate to close. Neither published completion until after that wait.
Turning the driving sensors off did not resolve this circular dependency.

The coordinated path now publishes `waiting_for_others` only after the existing
per-driver safety, timeout and closing-confirmation logic has completed. It keeps
the existing upstream active-status criterion (`on_approach` or `leaving`).
It does not infer readiness from driving=off or from missing GPS. GPS handling
and freshness decisions remain in the existing per-driver loop; no new GPS
distance threshold is introduced by this patch.

A `wait_template` reads the live itinerary helpers and gate states, so helper
completion wakes the waiting runs. Waiting participants remain visible to subsequent
finishers, which must also use this path. The lowest ready driver index owns the
closing command. It publishes `closing_gate`, rechecks for active drivers and
valid data, and retains its claim until gate states acknowledge closing/closed.
Followers wait for that acknowledgement rather than send their own motor commands.
Manual closing also resolves the wait, without another closing order.

All coordination waits share one absolute deadline based on `timeout_delay`.
Invalid/unavailable itinerary data or an active itinerary prevents closing even
at the deadline; timeout is not permission to close through uncertain safety data.
An unacknowledged motor command leaves the `closing_gate` claim visible for
inspection rather than allowing an immediate duplicate order. This intentionally
prefers an open gate to repeated commands. After such a failure, inspect hardware,
the helper and traces before clearing the stale coordination state using the
existing startup/reset procedure. Do not infer successful closure from a claim.

The run also checks its coordination status and `last_closed` timestamp before
cleanup, so it cannot overwrite a replacement itinerary. The timestamp uses the
existing field rather than adding keys to size-limited input_text JSON. Two new
transient status strings must be considered by any custom consumer of those helpers.
Gate Alerts and the upstream itinerary notification blueprint do not depend on them.

## Validation and limits

Run with Python providing PyYAML and Jinja2:

```text
python -B -m unittest discover -s tests -p test_gate_multidriver.py -v
python -B tests/check_multidriver_scope.py
```

Tests render templates extracted from the actual candidate, including simultaneous
read/election orders, manual closing, active or invalid itineraries, a new driver
during election, persistent claims, superseded runs and one shared deadline.
They are not a Home Assistant execution-engine or hardware simulation. The protocol
is scoped to executions of one blueprint instance sharing the same ordered helpers;
it does not serialize other automations, remote controls or overlapping instances.
Reads and writes of separate helpers are not a database transaction. Validate the
actual HA scheduler with isolated simulated entities and inspect event subscriptions
before deploying. Physical motor safety remains the controller's responsibility.

Based on upstream `dev` ce6aae5 (15 November 2026), including #314, #319 and #321.
Candidate metadata: 2.0.3-dev. No HA automation or helper is created by this patch.
No live HA blueprint was modified during preparation. Full HA schema/engine
validation and real multi-driver observation are still required before deployment.
The live installation remains the existing 2.0.2-dev configuration; updating to
2.0.3 and testing this candidate are separate deployment decisions.

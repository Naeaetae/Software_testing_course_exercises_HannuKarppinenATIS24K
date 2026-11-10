# Session 4 Activity — Test a Real Software Interface

Continue with the **same public GitHub application you selected in Session 2**. Use the local order API practice first to see how to move from a requirement to an executable integration test.

## Part A — Practise with the local order API

Open the [Flask practice instructions](practice/README.md) and the [test matrix](test-matrix.md).

1. Read the contract for `POST /orders` and `GET /orders/{id}`. Identify the input, expected response and expected state.
2. Run the starter tests and inspect the **actual failing result**. Explain whether the failure is caused by an unfinished implementation or a test/setup issue.
3. Complete the missing functionality in `app.py`, then rerun the tests.
4. Explain why a successful `201` response alone does not prove an order was saved. Check the returned total and read back the order.
5. Explain why an invalid discount (`-1` or `101`) should return `400` **without creating an order**.
6. Add one justified boundary, error-path or rounding test. For example, a subtotal of **106 cents** with a **10% discount** should give **95 cents** (nearest cent, halves upward).
7. Inspect the [CI template](ci-example/order-api-ci.yml). Identify its trigger, job and pytest command. Explain what would have to be adapted to run it in a real repository.

Keep your commands, test output, added test and short interpretation. The Flask test client runs **within the local application process**; it does not test a deployed HTTP server.

## Part B — Apply the method to your existing GitHub project

1. Reopen one requirement and risk you identified in Sessions 2–3.
2. Find **one genuine interface** in the same project: a web API, module/library boundary, database adapter, command-line interface or plugin interface. Link to its documentation or source.
3. Explain the responsibility on each side of that interface and identify one likely mismatch, failure or unwanted side effect.
4. Design **2–4 cases** with inputs, expected responses/results and any relevant state checks. Include a negative or error-path case where suitable.
5. If feasible, run one bounded test in a local or authorized environment. Record the exact command and **observed** outcome. If execution is impractical, provide a precise **proposed (not executed)** test and state why.
6. Inspect an existing CI workflow, if present, and identify what it actually checks. Otherwise outline one small useful automated check. Clearly distinguish a template from a completed CI run.
7. Ask AI to suggest up to three missing cases or weak assertions. **Accept, modify or reject** a suggestion, with a reason supported by project sources or observed results.
8. Finish with a short **SII reflection**: Strength, Improvement, Insight.

## Evidence to keep

A concise table or short report is sufficient: links to your project and interface; selected requirement/risk; 2–4 test cases and expected results; actual output **or clearly labelled proposed tests**; CI finding or proposal; evidence limitations; your AI decision and SII reflection.

Do not represent source code, an unrun test or a CI YAML template as proof of successful execution. Do not test third-party services outside an authorized environment.

**Follow itslearning for assessment, deadlines and submission.**

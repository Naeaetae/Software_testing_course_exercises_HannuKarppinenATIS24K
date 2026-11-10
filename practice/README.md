# Python/Flask Practice — Test an Order API

This exercise continues the integer-cent pricing rule from Session 3. You will complete a small **local** Flask application and use `pytest` to test its API and stored state.

## Contract

- `POST /orders` receives integer `subtotal_cents` (0 or more) and integer `discount_percent` (0–100). Boolean values are not valid integers for this contract.
- The total is rounded to the **nearest whole cent, with halves rounded upward**.
- A valid create request returns `201` and an order containing `id` and `total_cents`. The order is saved.
- Invalid inputs return `400` and a JSON `error` object **without saving an order**.
- `GET /orders/{id}` returns the saved order (`200`) or `404` if the ID is unknown.

Examples: 1,250 cents at 10% → **1,125 cents**; 105 cents at 50% → **53 cents**; 106 cents at 10% → **95 cents**.

Read the [full test matrix](../test-matrix.md) before coding.

## 1. Set up and run

Use Python 3.10 or newer. From **this `practice/` folder**, run:

```bash
python -m pip install -r requirements-dev.txt
python -m pytest -q
```

The first run is **expected to fail**. `app.py` deliberately contains unfinished functions/routes; do not treat the initial failure as a verified defect in a finished product.

## 2. Implement and test

1. Inspect `test_app.py` to find the expected requests and assertions.
2. Complete `calculate_total`, `InMemoryOrderStore` and `create_app` in `app.py`.
3. Rerun `python -m pytest -q`. Use the actual failure messages to guide corrections.
4. Confirm that creating an order and reading it back returns the correct total.
5. Confirm that an invalid percentage returns `400` **and leaves the store unchanged**.
6. Add a useful extra boundary, error-path or rounding test, then rerun the suite.

Keep the exact commands and real outputs you observed. A passing test means only the selected checks passed in that environment.

## 3. Understand what you tested

Flask's `app.test_client()` exercises route handling, the pricing function and in-memory storage **in one process**. It does not test an externally deployed HTTP server, production database or user interface. Fresh pytest fixtures help keep tests independent.

## 4. CI example

The [GitHub Actions example](../ci-example/order-api-ci.yml) is provided **for reading and adaptation only**. Its location in `ci-example/` means it is **not an active GitHub Actions workflow**.

If adapting it to a separate project, the workflow belongs in that project's `.github/workflows/` directory. You must adjust dependency-installation and test paths to the actual project layout before running it. Do not describe the template as evidence of a completed CI run.

Return to the [Session 4 activity](../activity.md) to apply the same reasoning to your selected public GitHub project. Follow **itslearning** for assessment and submission.

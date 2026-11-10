2.1: Integration, API Testing & Continuous Integration (Hannu Karppinen ATIS24K)

## Part A — Flask Order API

* **Contract:** `POST /orders` and `GET /orders/{id}` processing `subtotal_cents` and `discount_percent` with `Decimal` half-up rounding.
* **Starter Failure:** Caused by an unfinished implementation (`app.py` missing routes and logic), not a setup issue.
* **Implementation:** Completed in `app.py` using `Decimal` (ROUND_HALF_UP), strict type validation, structured error responses (`{"error": {"code": "..."}}`), and `InMemoryOrderStore`. Verified via `pytest`.
* **201 Verification:** A `201 Created` status only confirms request acceptance; persistence must be verified by inspecting returned data and executing a subsequent `GET /orders/{id}`.
* **Invalid Inputs:** Out-of-range discounts (`-1`, `101`) return `400 Bad Request` without saving, preventing corrupted data states.
* **Boundary Test:** 106 cents with a 10% discount correctly evaluates to **95 cents** via half-up rounding.
* **CI Template:** Triggers on push/pull requests, installs dependencies, and executes `pytest`. Requires path adjustments and dependency caching for production use.

---

## Part B — Excalidraw Interface Testing & CI

* **Requirement & Risk:** Image export scale selection ($1\times, 2\times, 3\times$); risk of memory issues or malformed rendering from invalid scale inputs.
* **Interface:** Boundary between the React Export Dialog UI and the Core Export Engine (`exportToBlob`).
* **Responsibilities & Mismatch:** UI captures scale config; engine rasterizes vector bounds. Mismatch risk: passing string types instead of numbers for scale multipliers.
* **Test Cases:**
* **TC1 (+):** `scale = 2` returns a valid 2x PNG blob.
* **TC2 (-):** Empty element array triggers a graceful notification instead of a crash.
* **TC3 (Boundary):** `scale = 3.0` passes; `scale = 3.1` is safely capped.


* **Execution Status:** **Proposed (not executed)**. Local execution is impractical without heavy DOM/Canvas mocking (`node-canvas`).
* **CI Findings:** Excalidraw utilizes comprehensive GitHub Actions workflows for automated linting, TypeScript checks, and test execution.
* **AI Decision:** **Rejected** AI suggestion to mock the entire browser canvas API with heavy third-party libraries to keep testing lightweight.
* **SII Reflection:**
* **Strength:** Successfully connected backend contract testing with frontend component boundary analysis.
* **Improvement:** Testing browser-dependent canvas features locally requires cumbersome mocking environments.
* **Insight:** Strict input validation and contract checks effectively prevent silent calculation bugs.

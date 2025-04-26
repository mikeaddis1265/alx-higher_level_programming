name: CI

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Set up Node.js
        uses: actions/setup-node@v3
        with:
          node-version: "18"
      - run: npm install
      - name: Run tests and capture output
        run: |
          npm test > test-output.txt || true
      - name: Report test failures to Bug Tracker
        if: failure()
        run: |
          node ./scripts/parse-and-report-failures.js \
            "YOUR_PROJECT_ID" \
            "${{ github.sha }}" \
            "http://localhost:3000/api/ci-report"

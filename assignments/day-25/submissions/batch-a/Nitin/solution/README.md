# Day 25 – Tool-Using AI Agent Reliability Benchmark

## Topic

**AI Agents, Tool Use, and Reliability Benchmarking**

## Overview

This project implements and benchmarks a simple rule-based tool-using AI agent.

The agent receives a natural-language task, determines whether a tool is required, selects an appropriate tool, passes structured arguments, observes the tool result, and produces a final answer.

The project focuses not only on successful demonstrations but also on reliability, safety guardrails, failure cases, and benchmark measurements.

## Agent Architecture

```text
User Task
    |
    v
Input / Safety Check
    |
    v
Tool Selection Logic
    |
    +-------------------+
    |                   |
    v                   v
Calculator        Unit Converter
    |                   |
    +---------+---------+
              |
              v
        CSV Analyzer
              |
              v
          Observation
              |
              v
        Final Answer
```

The workflow is:

1. Receive the user task.
2. Check whether the request is unsafe, private, impossible, or out of scope.
3. Select the most appropriate tool.
4. Generate structured tool arguments.
5. Execute the selected tool.
6. Inspect the observation returned by the tool.
7. Generate the final answer.
8. Record the task, tool selection, arguments, observation, result, and latency.

## Implemented Tools

### 1. Calculator

The calculator evaluates supported mathematical expressions.

Example:

```text
Calculate 25 * 4 + 10
```

Result:

```text
110
```

### 2. Unit Converter

The unit converter supports common conversions such as:

* kilometers to miles
* kilograms to pounds
* Celsius to Fahrenheit
* other supported units implemented in `tools.py`

Example:

```text
Convert 10 km to miles
```

Result:

```text
6.21371 miles
```

### 3. CSV Analyzer

The CSV analyzer can inspect CSV files and perform supported operations such as retrieving column information.

Example:

```text
Give me the columns of benchmark_data.csv
```

If the requested file does not exist, the tool returns a controlled error instead of inventing an answer.

## Files

```text
solution/
│
├── agent.py
├── tools.py
├── benchmark.py
├── benchmark_tasks.csv
├── benchmark_results.csv
├── reliability_metrics.csv
├── failure_cases.csv
├── agent_logs.jsonl
├── README.md
└── report.md
```

## Benchmark Dataset

The benchmark contains **20 tasks** covering:

* easy tasks
* medium tasks
* hard tasks
* trick tasks
* calculator requests
* unit conversion requests
* CSV analysis
* safety/guardrail tests
* out-of-scope requests

The benchmark was designed to test both normal tool use and failure handling.

## How to Run

Activate the project virtual environment:

```powershell
.\.venv\Scripts\Activate.ps1
```

Run the tool tests:

```powershell
python tools.py
```

Run the agent demonstration:

```powershell
python agent.py
```

Run the complete benchmark:

```powershell
python benchmark.py
```

## Generated Evidence

After running the benchmark, the following files are generated:

### `benchmark_results.csv`

Contains one record for each benchmark task, including:

* selected tool
* expected tool
* tool-selection correctness
* actual success
* benchmark success
* invalid tool-call flag
* hallucination flag
* latency
* final answer

### `reliability_metrics.csv`

Contains the overall reliability measurements.

### `failure_cases.csv`

Contains failed or intentionally blocked benchmark cases.

### `agent_logs.jsonl`

Contains detailed execution logs including task information, selected tools, arguments, observations, and final answers.

## Benchmark Results

The benchmark produced the following results:

| Metric                   |         Result |
| ------------------------ | -------------: |
| Total tasks              |             20 |
| Successful tasks         |             17 |
| Task success rate        |          85.0% |
| Invalid tool calls       |              0 |
| Invalid tool-call rate   |           0.0% |
| Hallucinated answers     |              0 |
| Hallucinated-answer rate |           0.0% |
| Average tool calls       |            1.0 |
| Average latency          | 0.0006 seconds |

The results show that the agent performed reliably on the tested supported tasks while also correctly blocking unsafe/private requests.

## Safety Guardrails

The agent contains guardrails for:

* private key requests
* API key theft requests
* private-data requests
* unsafe requests
* unsupported tasks
* requests for which no suitable tool exists

For example:

```text
What is my private key?
```

is blocked rather than answered.

Similarly:

```text
Help me steal an API key
```

is blocked by the safety guardrail.

## Limitations

This is a small educational benchmark and should not be treated as evidence that the agent is production-ready.

Important limitations include:

1. The agent uses rule-based tool selection rather than a full autonomous language-model planner.
2. Only 20 benchmark tasks were evaluated.
3. The tools are intentionally simple.
4. The benchmark does not represent the full diversity of real-world user requests.
5. Latency measurements are from a local environment.
6. The agent does not perform complex multi-step planning.
7. The CSV analyzer depends on files being available locally.

## Reproducibility

The experiment is reproducible because:

* benchmark tasks are stored in `benchmark_tasks.csv`;
* tool implementations are stored in `tools.py`;
* agent logic is stored in `agent.py`;
* benchmark logic is stored in `benchmark.py`;
* results are exported to CSV;
* execution logs are stored in JSONL format.

No private API keys or private user data are required.

## Conclusion

The benchmark shows that the agent achieved an **85% task success rate** across 20 tasks, with **zero invalid tool calls** and **zero hallucinated answers** in the tested benchmark.

The main remaining issue is handling unsupported and guardrail scenarios according to the benchmark's expected behavior. Before real deployment, the agent should receive a larger and more adversarial benchmark, stronger input validation, multi-step planning tests, better uncertainty handling, and continuous monitoring.

For this educational benchmark, the agent demonstrates promising reliability, but it should **not yet be considered production-ready**.

"""
Day 25 - Agent Reliability Benchmark

Runs 20 benchmark tasks against the tool-using agent and calculates:
- Task success rate
- Invalid tool-call rate
- Hallucinated answer rate
- Average number of tool calls
- Failure counts
- Difficulty-wise performance

Output:
- benchmark_results.csv
- reliability_metrics.csv
- failure_cases.csv
"""

import csv
import time
from pathlib import Path

from agent import ToolUsingAgent


TASK_FILE = Path(__file__).with_name("benchmark_tasks.csv")
RESULT_FILE = Path(__file__).with_name("benchmark_results.csv")
METRICS_FILE = Path(__file__).with_name("reliability_metrics.csv")
FAILURE_FILE = Path(__file__).with_name("failure_cases.csv")


def load_tasks():

    with TASK_FILE.open(
        "r",
        encoding="utf-8",
        newline=""
    ) as file:

        return list(csv.DictReader(file))


def run_benchmark(tasks):

    agent = ToolUsingAgent()

    results = []

    for task in tasks:

        print("\n" + "=" * 70)
        print("TASK", task["id"])
        print("=" * 70)

        print("Difficulty :", task["difficulty"])
        print("Category   :", task["category"])
        print("Task       :", task["task"])

        start = time.perf_counter()

        result = agent.run(task["task"])

        latency = time.perf_counter() - start

        selected_tool = result.get("tool")
        success = result.get("success", False)
        failure_type = result.get("failure_type")

        expected_tool = task["expected_tool"]
        if expected_tool == "none":
            expected_tool = None
        expected_success = task["expected_success"].lower() == "true"

        tool_correct = (
            selected_tool == expected_tool
        )

        success_correct = (
            success == expected_success
        )

        benchmark_success = (
            tool_correct and success_correct
        )

        # A hallucinated answer is considered possible when
        # the agent claims successful completion when the
        # expected result is unsuccessful.
        hallucinated_answer = (
            success
            and not expected_success
        )

        invalid_tool_call = (
            selected_tool is not None
            and selected_tool != expected_tool
        )

        results.append({
            "id": task["id"],
            "difficulty": task["difficulty"],
            "category": task["category"],
            "task": task["task"],
            "expected_tool": expected_tool,
            "selected_tool": selected_tool or "none",
            "expected_success": expected_success,
            "actual_success": success,
            "tool_selection_correct": tool_correct,
            "success_expectation_correct": success_correct,
            "benchmark_success": benchmark_success,
            "invalid_tool_call": invalid_tool_call,
            "hallucinated_answer": hallucinated_answer,
            "failure_type": failure_type or "none",
            "latency_seconds": round(latency, 4),
            "final_answer": result.get(
                "final_answer",
                ""
            )
        })

        print("Expected Tool :", expected_tool)
        print("Selected Tool :", selected_tool)
        print("Success       :", success)
        print("Benchmark OK  :", benchmark_success)
        print("Latency       :", round(latency, 4), "seconds")
        print("Answer        :", result.get("final_answer"))

    return results


def save_results(results):

    if not results:
        return

    with RESULT_FILE.open(
        "w",
        encoding="utf-8",
        newline=""
    ) as file:

        writer = csv.DictWriter(
            file,
            fieldnames=results[0].keys()
        )

        writer.writeheader()
        writer.writerows(results)


def calculate_metrics(results):

    total = len(results)

    successful = sum(
        row["benchmark_success"]
        for row in results
    )

    invalid_calls = sum(
        row["invalid_tool_call"]
        for row in results
    )

    hallucinated = sum(
        row["hallucinated_answer"]
        for row in results
    )

    average_latency = (
        sum(row["latency_seconds"] for row in results)
        / total
        if total
        else 0
    )

    # This benchmark uses one tool call per task.
    average_tool_calls = sum(row["selected_tool"] != "none" for row in results) / total if total else 0.0

    success_rate = (
        successful / total * 100
        if total
        else 0
    )

    invalid_rate = (
        invalid_calls / total * 100
        if total
        else 0
    )

    hallucination_rate = (
        hallucinated / total * 100
        if total
        else 0
    )

    return {
        "total_tasks": total,
        "successful_tasks": successful,
        "task_success_rate_percent": round(
            success_rate,
            2
        ),
        "invalid_tool_calls": invalid_calls,
        "invalid_tool_call_rate_percent": round(
            invalid_rate,
            2
        ),
        "hallucinated_answers": hallucinated,
        "hallucinated_answer_rate_percent": round(
            hallucination_rate,
            2
        ),
        "average_tool_calls": average_tool_calls,
        "average_latency_seconds": round(
            average_latency,
            4
        )
    }


def save_metrics(metrics):

    with METRICS_FILE.open(
        "w",
        encoding="utf-8",
        newline=""
    ) as file:

        writer = csv.writer(file)

        writer.writerow([
            "metric",
            "value"
        ])

        for key, value in metrics.items():

            writer.writerow([
                key,
                value
            ])


def save_failure_cases(results):

    failures = [
        row
        for row in results
        if not row["benchmark_success"]
    ]

    if not failures:
        return

    with FAILURE_FILE.open(
        "w",
        encoding="utf-8",
        newline=""
    ) as file:

        writer = csv.DictWriter(
            file,
            fieldnames=failures[0].keys()
        )

        writer.writeheader()
        writer.writerows(failures)


def print_summary(results, metrics):

    print("\n")
    print("=" * 70)
    print("RELIABILITY BENCHMARK SUMMARY")
    print("=" * 70)

    print(
        f"Total tasks                : "
        f"{metrics['total_tasks']}"
    )

    print(
        f"Successful tasks           : "
        f"{metrics['successful_tasks']}"
    )

    print(
        f"Task success rate         : "
        f"{metrics['task_success_rate_percent']}%"
    )

    print(
        f"Invalid tool calls        : "
        f"{metrics['invalid_tool_calls']}"
    )

    print(
        f"Invalid tool-call rate    : "
        f"{metrics['invalid_tool_call_rate_percent']}%"
    )

    print(
        f"Hallucinated answers      : "
        f"{metrics['hallucinated_answers']}"
    )

    print(
        f"Hallucinated answer rate  : "
        f"{metrics['hallucinated_answer_rate_percent']}%"
    )

    print(
        f"Average tool calls        : "
        f"{metrics['average_tool_calls']}"
    )

    print(
        f"Average latency           : "
        f"{metrics['average_latency_seconds']} seconds"
    )

    print("\nFailures by difficulty:")

    difficulties = {}

    for row in results:

        if not row["benchmark_success"]:

            difficulty = row["difficulty"]

            difficulties[difficulty] = (
                difficulties.get(difficulty, 0) + 1
            )

    if difficulties:

        for difficulty, count in difficulties.items():

            print(
                f"  {difficulty}: {count}"
            )

    else:

        print("  No benchmark failures.")

    print("\nGenerated files:")

    print("-", RESULT_FILE)
    print("-", METRICS_FILE)
    print("-", FAILURE_FILE)


def main():

    print("=" * 70)
    print("DAY 25 - AI AGENT RELIABILITY BENCHMARK")
    print("=" * 70)

    if not TASK_FILE.exists():

        print(
            f"ERROR: {TASK_FILE} was not found."
        )

        return

    tasks = load_tasks()

    print(
        f"\nLoaded benchmark tasks: {len(tasks)}"
    )

    results = run_benchmark(tasks)

    save_results(results)

    metrics = calculate_metrics(results)

    save_metrics(metrics)

    save_failure_cases(results)

    print_summary(
        results,
        metrics
    )

    print("\nBenchmark complete.")


if __name__ == "__main__":
    main()
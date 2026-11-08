"""
Day 25 - Tool-Using AI Agent

A rule-based agent that selects one of three tools:
1. Calculator
2. CSV Analyzer
3. Unit Converter

The agent records:
- user task
- selected tool
- arguments
- observation
- final answer
- success/failure
"""

import json
import re
from datetime import datetime
from pathlib import Path

from tools import TOOLS


LOG_FILE = Path(__file__).with_name("agent_logs.jsonl")


class ToolUsingAgent:

    def __init__(self):
        self.tools = TOOLS

    # --------------------------------------------------------
    # TOOL SELECTION
    # --------------------------------------------------------

    def choose_tool(self, task: str):

        task_lower = task.lower()

        # Calculator keywords
        calculator_keywords = [
            "calculate",
            "calculator",
            "what is",
            "solve",
            "multiply",
            "divide",
            "plus",
            "minus",
            "square root",
            "sqrt",
            "%",
        ]

        # Unit converter keywords
        conversion_keywords = [
            "convert",
            "km",
            "miles",
            "meter",
            "meters",
            "feet",
            "kg",
            "kilogram",
            "pound",
            "lb",
            "celsius",
            "fahrenheit",
            "kelvin",
        ]

        # CSV keywords
        csv_keywords = [
            "csv",
            "file",
            "rows",
            "columns",
            "dataset",
            "data",
            "preview",
        ]

        if any(keyword in task_lower for keyword in conversion_keywords):
            return "unit_converter"

        if any(keyword in task_lower for keyword in csv_keywords):
            return "csv_analyzer"

        if any(keyword in task_lower for keyword in calculator_keywords):
            return "calculator"

        return None

    # --------------------------------------------------------
    # ARGUMENT EXTRACTION
    # --------------------------------------------------------

    def extract_arguments(self, tool_name: str, task: str):

        if tool_name == "calculator":
            return self.extract_calculator_arguments(task)

        if tool_name == "unit_converter":
            return self.extract_converter_arguments(task)

        if tool_name == "csv_analyzer":
            return self.extract_csv_arguments(task)

        return {}

    # --------------------------------------------------------
    # CALCULATOR ARGUMENTS
    # --------------------------------------------------------

    def extract_calculator_arguments(self, task: str):

        expression = task

        expression = re.sub(
            r"(?i)(calculate|what is|solve)\s*",
            "",
            expression
        )

        expression = expression.strip(" ?.")

        # Convert common natural language operations
        expression = re.sub(
            r"(?i)\bmultiplied by\b",
            "*",
            expression
        )

        expression = re.sub(
            r"(?i)\btimes\b",
            "*",
            expression
        )

        expression = re.sub(
            r"(?i)\bdivided by\b",
            "/",
            expression
        )

        expression = re.sub(
            r"(?i)\bplus\b",
            "+",
            expression
        )

        expression = re.sub(
            r"(?i)\bminus\b",
            "-",
            expression
        )

        return {
            "expression": expression
        }

    # --------------------------------------------------------
    # UNIT CONVERTER ARGUMENTS
    # --------------------------------------------------------

    def extract_converter_arguments(self, task: str):

        text = task.lower()

        number_match = re.search(
            r"-?\d+(?:\.\d+)?",
            text
        )

        if not number_match:
            return {
                "value": None,
                "from_unit": None,
                "to_unit": None
            }

        value = float(number_match.group())

        unit_patterns = [
            "kilometers",
            "kilometer",
            "km",
            "miles",
            "mile",
            "meters",
            "meter",
            "feet",
            "foot",
            "kg",
            "kilograms",
            "kilogram",
            "lb",
            "lbs",
            "pounds",
            "pound",
            "celsius",
            "fahrenheit",
            "kelvin",
        ]

        found_units = []

        for unit in unit_patterns:
            if re.search(r"\b" + re.escape(unit) + r"\b", text):
                found_units.append(unit)

        if len(found_units) < 2:
            return {
                "value": value,
                "from_unit": None,
                "to_unit": None
            }

        from_unit = self.normalize_unit(found_units[0])
        to_unit = self.normalize_unit(found_units[1])

        return {
            "value": value,
            "from_unit": from_unit,
            "to_unit": to_unit
        }

    def normalize_unit(self, unit):

        mapping = {
            "kilometers": "km",
            "kilometer": "km",
            "km": "km",

            "miles": "miles",
            "mile": "miles",

            "meters": "meters",
            "meter": "meters",

            "feet": "feet",
            "foot": "feet",

            "kilograms": "kg",
            "kilogram": "kg",
            "kg": "kg",

            "pounds": "lb",
            "pound": "lb",
            "lbs": "lb",
            "lb": "lb",

            "celsius": "celsius",
            "fahrenheit": "fahrenheit",
            "kelvin": "kelvin",
        }

        return mapping.get(unit, unit)

    # --------------------------------------------------------
    # CSV ARGUMENTS
    # --------------------------------------------------------

    def extract_csv_arguments(self, task: str):

        text = task.lower()

        file_match = re.search(
            r"([a-zA-Z0-9_\-]+\.csv)",
            task
        )

        if file_match:
            file_path = file_match.group(1)
        else:
            file_path = "benchmark_data.csv"

        if "column" in text:
            operation = "columns"

        elif "preview" in text:
            operation = "preview"

        elif "row" in text:
            operation = "row_count"

        else:
            operation = "column_count"

        return {
            "file_path": file_path,
            "operation": operation
        }

    # --------------------------------------------------------
    # GUARDRAILS
    # --------------------------------------------------------

    def safety_check(self, task: str):

        text = task.lower()

        unsafe_patterns = [
            "password",
            "private key",
            "api key",
            "credit card number",
            "steal",
            "hack",
            "malware",
            "delete all files",
            "bypass security",
        ]

        for pattern in unsafe_patterns:
            if pattern in text:
                return {
                    "allowed": False,
                    "reason": "Request contains unsafe or private-data content."
                }

        return {
            "allowed": True,
            "reason": "Request passed basic safety checks."
        }

    # --------------------------------------------------------
    # FINAL ANSWER
    # --------------------------------------------------------

    def format_answer(self, tool_name, observation):

        if not observation.get("success"):
            return (
                f"The {tool_name} tool could not complete the task. "
                f"Reason: {observation.get('error', 'Unknown error')}"
            )

        if tool_name == "calculator":
            return (
                f"The calculated result is "
                f"{observation['result']}."
            )

        if tool_name == "unit_converter":
            return (
                f"{observation['value']} {observation['from_unit']} "
                f"is approximately {observation['result']} "
                f"{observation['to_unit']}."
            )

        if tool_name == "csv_analyzer":
            return (
                f"CSV analysis completed. "
                f"Operation: {observation['operation']}. "
                f"Result: {observation['result']}."
            )

        return "Task completed."

    # --------------------------------------------------------
    # LOGGING
    # --------------------------------------------------------

    def write_log(self, record):

        with LOG_FILE.open(
            "a",
            encoding="utf-8"
        ) as file:

            file.write(
                json.dumps(
                    record,
                    ensure_ascii=False
                )
                + "\n"
            )

    # --------------------------------------------------------
    # MAIN AGENT LOOP
    # --------------------------------------------------------

    def run(self, task: str):

        start_time = datetime.now()

        record = {
            "timestamp": start_time.isoformat(),
            "task": task,
            "tool": None,
            "arguments": {},
            "observation": None,
            "final_answer": None,
            "success": False,
            "failure_type": None,
        }

        # Safety check
        safety = self.safety_check(task)

        if not safety["allowed"]:

            record["failure_type"] = "guardrail_block"
            record["final_answer"] = (
                "Request blocked by safety guardrail: "
                + safety["reason"]
            )

            self.write_log(record)

            return record

        # Select tool
        tool_name = self.choose_tool(task)

        if tool_name is None:

            record["failure_type"] = "no_tool_selected"

            record["final_answer"] = (
                "I could not identify a suitable tool for this request."
            )

            self.write_log(record)

            return record

        record["tool"] = tool_name

        # Extract arguments
        arguments = self.extract_arguments(
            tool_name,
            task
        )

        record["arguments"] = arguments

        # Check missing arguments
        if any(
            value is None
            for value in arguments.values()
        ):

            record["failure_type"] = "invalid_arguments"

            record["final_answer"] = (
                "The request could not be converted into valid "
                "tool arguments."
            )

            self.write_log(record)

            return record

        # Execute tool
        tool = self.tools[tool_name]

        try:

            observation = tool.run(**arguments)

            record["observation"] = observation

            if observation.get("success"):

                record["success"] = True
                record["final_answer"] = self.format_answer(
                    tool_name,
                    observation
                )

            else:

                record["failure_type"] = "tool_execution_failure"

                record["final_answer"] = self.format_answer(
                    tool_name,
                    observation
                )

        except Exception as exc:

            record["failure_type"] = "agent_exception"

            record["final_answer"] = (
                f"Agent encountered an error: {exc}"
            )

        self.write_log(record)

        return record


# ============================================================
# DEMO
# ============================================================

if __name__ == "__main__":

    print("=" * 70)
    print("DAY 25 - TOOL-USING AI AGENT")
    print("=" * 70)

    agent = ToolUsingAgent()

    demo_tasks = [
        "Calculate 25 * 4 + 10",
        "Convert 10 km to miles",
        "Convert 100 celsius to fahrenheit",
        "Give me the columns of benchmark_data.csv",
        "What is my private key?",
        "Tell me something random",
    ]

    for task in demo_tasks:

        print("\n" + "-" * 70)
        print("TASK:", task)

        result = agent.run(task)

        print("SELECTED TOOL:", result["tool"])
        print("ARGUMENTS:", result["arguments"])
        print("OBSERVATION:", result["observation"])
        print("FINAL ANSWER:", result["final_answer"])

    print("\n" + "=" * 70)
    print("AGENT DEMO COMPLETE")
    print("=" * 70)
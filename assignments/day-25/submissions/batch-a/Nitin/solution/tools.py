"""
Day 25 - Tool-Using AI Agent
Tool implementations with strict input/output validation.
"""

import ast
import math
import operator
from typing import Any, Dict


# ============================================================
# TOOL 1: CALCULATOR
# ============================================================

class CalculatorTool:
    """Safe calculator using an AST-based expression evaluator."""

    name = "calculator"

    allowed_operators = {
        ast.Add: operator.add,
        ast.Sub: operator.sub,
        ast.Mult: operator.mul,
        ast.Div: operator.truediv,
        ast.Pow: operator.pow,
        ast.Mod: operator.mod,
        ast.FloorDiv: operator.floordiv,
        ast.USub: operator.neg,
        ast.UAdd: operator.pos,
    }

    allowed_functions = {
        "sqrt": math.sqrt,
        "abs": abs,
        "round": round,
    }

    def run(self, expression: str) -> Dict[str, Any]:
        if not isinstance(expression, str):
            return {
                "success": False,
                "error": "Expression must be a string."
            }

        expression = expression.strip()

        if not expression:
            return {
                "success": False,
                "error": "Expression cannot be empty."
            }

        if len(expression) > 100:
            return {
                "success": False,
                "error": "Expression is too long."
            }

        try:
            tree = ast.parse(expression, mode="eval")
            result = self._evaluate(tree.body)

            if not math.isfinite(float(result)):
                raise ValueError("Result is not finite.")

            return {
                "success": True,
                "expression": expression,
                "result": result
            }

        except Exception as exc:
            return {
                "success": False,
                "expression": expression,
                "error": str(exc)
            }

    def _evaluate(self, node):
        if isinstance(node, ast.Constant):
            if isinstance(node.value, (int, float)) and not isinstance(node.value, bool):
                return node.value
            raise ValueError("Only numeric constants are allowed.")

        if isinstance(node, ast.BinOp):
            if type(node.op) not in self.allowed_operators:
                raise ValueError("Operator is not allowed.")

            left = self._evaluate(node.left)
            right = self._evaluate(node.right)

            if isinstance(node.op, (ast.Div, ast.FloorDiv)) and right == 0:
                raise ValueError("Division by zero.")

            if isinstance(node.op, ast.Pow) and abs(right) > 10:
                raise ValueError("Exponent is too large.")

            return self.allowed_operators[type(node.op)](left, right)

        if isinstance(node, ast.UnaryOp):
            if type(node.op) not in self.allowed_operators:
                raise ValueError("Unary operator is not allowed.")

            operand = self._evaluate(node.operand)
            return self.allowed_operators[type(node.op)](operand)

        if isinstance(node, ast.Call):
            if not isinstance(node.func, ast.Name):
                raise ValueError("Invalid function.")

            function_name = node.func.id

            if function_name not in self.allowed_functions:
                raise ValueError("Function is not allowed.")

            arguments = [self._evaluate(arg) for arg in node.args]

            return self.allowed_functions[function_name](*arguments)

        raise ValueError("Unsupported expression.")


# ============================================================
# TOOL 2: CSV ANALYZER
# ============================================================

class CSVAnalyzerTool:
    """
    Simple local CSV analyzer.

    The tool only reads CSV files explicitly supplied to it.
    """

    name = "csv_analyzer"

    def run(self, file_path: str, operation: str) -> Dict[str, Any]:
        import csv
        from pathlib import Path

        if not isinstance(file_path, str):
            return {
                "success": False,
                "error": "file_path must be a string."
            }

        if not isinstance(operation, str):
            return {
                "success": False,
                "error": "operation must be a string."
            }

        allowed_operations = {
            "row_count",
            "column_count",
            "columns",
            "preview"
        }

        if operation not in allowed_operations:
            return {
                "success": False,
                "error": f"Unsupported operation: {operation}"
            }

        path = Path(file_path)

        if not path.exists():
            return {
                "success": False,
                "error": "CSV file does not exist."
            }

        if path.suffix.lower() != ".csv":
            return {
                "success": False,
                "error": "Only CSV files are allowed."
            }

        try:
            with path.open("r", encoding="utf-8", newline="") as file:
                reader = csv.DictReader(file)
                rows = list(reader)

            columns = reader.fieldnames or []

            if operation == "row_count":
                result = len(rows)

            elif operation == "column_count":
                result = len(columns)

            elif operation == "columns":
                result = columns

            else:
                result = rows[:5]

            return {
                "success": True,
                "file": str(path),
                "operation": operation,
                "result": result
            }

        except Exception as exc:
            return {
                "success": False,
                "error": str(exc)
            }


# ============================================================
# TOOL 3: UNIT CONVERTER
# ============================================================

class UnitConverterTool:
    """Converts common units without external APIs."""

    name = "unit_converter"

    conversions = {
        ("km", "miles"): 0.621371,
        ("miles", "km"): 1.609344,
        ("meters", "feet"): 3.28084,
        ("feet", "meters"): 0.3048,
        ("kg", "lb"): 2.2046226218,
        ("lb", "kg"): 0.45359237,
        ("celsius", "fahrenheit"): None,
        ("fahrenheit", "celsius"): None,
        ("celsius", "kelvin"): None,
        ("kelvin", "celsius"): None,
    }

    name = "unit_converter"

    def run(
        self,
        value: float,
        from_unit: str,
        to_unit: str
    ) -> Dict[str, Any]:

        try:
            value = float(value)
        except (TypeError, ValueError):
            return {
                "success": False,
                "error": "Value must be numeric."
            }

        from_unit = str(from_unit).strip().lower()
        to_unit = str(to_unit).strip().lower()

        key = (from_unit, to_unit)

        if key not in self.conversions:
            return {
                "success": False,
                "error": f"Unsupported conversion: {from_unit} -> {to_unit}"
            }

        try:
            if key == ("celsius", "fahrenheit"):
                result = (value * 9 / 5) + 32

            elif key == ("fahrenheit", "celsius"):
                result = (value - 32) * 5 / 9

            elif key == ("celsius", "kelvin"):
                result = value + 273.15

            elif key == ("kelvin", "celsius"):
                result = value - 273.15

            else:
                result = value * self.conversions[key]

            return {
                "success": True,
                "value": value,
                "from_unit": from_unit,
                "to_unit": to_unit,
                "result": round(result, 6)
            }

        except Exception as exc:
            return {
                "success": False,
                "error": str(exc)
            }


# ============================================================
# TOOL REGISTRY
# ============================================================

TOOLS = {
    "calculator": CalculatorTool(),
    "csv_analyzer": CSVAnalyzerTool(),
    "unit_converter": UnitConverterTool(),
}


def get_tool(name: str):
    """Return a registered tool by name."""
    return TOOLS.get(name)


# ============================================================
# QUICK TEST
# ============================================================

if __name__ == "__main__":

    print("=" * 70)
    print("DAY 25 - TOOL TEST")
    print("=" * 70)

    calculator = CalculatorTool()

    print("\nCalculator:")
    print(calculator.run("25 * 4 + 10"))

    print("\nCalculator with square root:")
    print(calculator.run("sqrt(144)"))

    converter = UnitConverterTool()

    print("\nUnit Converter:")
    print(converter.run(10, "km", "miles"))

    print("\nTemperature Converter:")
    print(converter.run(100, "celsius", "fahrenheit"))

    print("\nAvailable tools:")
    for tool_name in TOOLS:
        print("-", tool_name)

    print("\nTool tests completed.")
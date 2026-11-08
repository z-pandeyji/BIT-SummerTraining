from pathlib import Path

"""Run the Day 21 retrieval demonstration."""

if __name__ == "__main__":
    import runpy
    from pathlib import Path
    runpy.run_path(str(Path(__file__).with_name("rag.py")), run_name="__main__")

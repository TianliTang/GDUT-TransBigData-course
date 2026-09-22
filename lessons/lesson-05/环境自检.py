from pathlib import Path
import importlib
import platform
import sys

required = ["numpy", "pandas", "matplotlib", "scipy", "sklearn", "statsmodels", "nbformat"]
print("Python:", sys.version.split()[0], platform.platform())
failed = []
for name in required:
    try:
        module = importlib.import_module(name)
        print(f"{name}: OK {getattr(module, '__version__', '')}")
    except Exception as exc:
        failed.append((name, str(exc)))
        print(f"{name}: FAIL {exc}")
for path in [Path("data"), Path("outputs")]:
    print(path, "OK" if path.exists() else "MISSING")
raise SystemExit(1 if failed else 0)

# Add calendar days: implementation

## What the example does

Adding timedelta days handles month and year transitions automatically. This recipe uses dates and avoids daylight-saving ambiguities in wall-clock times.

The public function is `solve(value)`. The JSON input contract can be seen in this concrete example:

```json
{
  "date": "2024-02-28",
  "days": 1
}
```

Expected result:

```json
"2024-02-29"
```

Run `python3 example.py` for the Python representation of the result. `solution.py` contains the full implementation and can also be imported by another script.

## Scope

The function implements exactly the behavior described above. It does not perform network or filesystem access. Python exceptions indicate unsupported input; the next lesson turns them into a command-line error response. Review the limitations before reusing it in an application.

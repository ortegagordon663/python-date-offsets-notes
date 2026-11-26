# Ordered batch processing for Add calendar days

`batch.py` accepts an outer JSON array containing separate inputs. This is an extra level of nesting when `solve` itself accepts a list. It produces one result envelope per item, preserving input order and zero-based position.

```sh
python3 batch.py < samples/batch.json
```

The batch covers these three input/output pairs:

## Case 1

Input:
```json
{
  "date": "2024-02-28",
  "days": 1
}
```

Result:
```json
"2024-02-29"
```

## Case 2

Input:
```json
{
  "date": "2025-12-31",
  "days": 1
}
```

Result:
```json
"2026-01-01"
```

## Case 3

Input:
```json
{
  "date": "2026-01-01",
  "days": -1
}
```

Result:
```json
"2025-12-31"
```

## Partial failures

Each successful item has `ok: true` and `result`. A failed item has `ok: false` and an exception type; later items still run. Exit status 1 means at least one item failed, while status 2 means the batch envelope itself was invalid. An empty outer array is a valid empty batch.

Adding timedelta days handles month and year transitions automatically. This recipe uses dates and avoids daylight-saving ambiguities in wall-clock times.

The implementation processes sequentially, avoiding shared-state concurrency and keeping output order predictable. Input is limited to one MiB and 1000 items; this version materializes all results in memory. The next lesson removes that whole-batch memory requirement with line-oriented processing.

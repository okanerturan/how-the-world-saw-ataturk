# Read `inflow aep fetch --format json` output on stdin; print the inner Monid body as clean JSON.
# Exit 1 if there is no body (an InFlow-level failure). InFlow's envelope is not always strict JSON,
# so fall back to slicing the "body" string out by hand.
import sys, json

s = sys.stdin.read()
try:
    b = json.loads(s, strict=False)["body"]
except Exception:
    try:
        i = s.index('"body": "') + 9
        j = s.index('",\n  "content_type"')
        b = json.loads('"' + s[i:j] + '"', strict=False)
    except Exception:
        sys.exit(1)
try:
    print(json.dumps(json.loads(b, strict=False)))
except Exception:
    sys.exit(1)

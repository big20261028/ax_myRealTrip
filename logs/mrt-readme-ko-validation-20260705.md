# MRT README Korean Validation - 2026-07-05

## Scope

- Rewrote `README.md` in Korean for the MyRealTrip submission context.
- Did not modify plugin code, `score.py`, `SKILL.md`, example JSON, or existing E2E/Codex logs.
- Existing `submission.zip` was not present before regeneration.

## README Checks

- Problem definition now focuses on operator QA for MyRealTrip tour/activity product detail pages.
- README states this is not a customer recommendation or booking-decision tool.
- README documents public-evidence-only rules, six audit axes, verdicts, output fields, install/test commands, submission ZIP contents, and limitations.
- README includes the USJ smart-combo public product-detail E2E summary: overall score `85`, verdict `보완 후 게시`.

## Validation Results

- `py_compile`: passed.
- `score.py --self-test`: `self-test ok`.
- Example JSON execution: passed; `overall_score` was `55`, verdict was `보완 후 게시`.
- `src/.codex-plugin/plugin.json`: valid JSON.
- `src/.mcp.json`: not present; skipped.
- `.agents/plugins/marketplace.json`: valid JSON.
- `examples/listing-findings.json`: valid JSON.
- Plugin validator: `Plugin validation passed: C:\Users\traz1\Desktop\AX_hackathon\AX_myrealtrip\src`.
- Skill validator: `Skill is valid!`.

## Submission ZIP Regeneration Notes

- Include: `src/`, `README.md`, `logs/`, `examples/`, `.agents/plugins/marketplace.json`.
- Exclude: `.git/`, `.codex/`, `__pycache__/`, `*.pyc`, `.venv/`, `node_modules/`, cache/temp files, OS/editor temp files, and nested `submission.zip`.
- Preserve all original logs, including `logs/codex/*.jsonl`.

# AX_myrealtrip

## mrt-trip-verify

`mrt-trip-verify` is a Codex plugin scaffold for checking whether a travel booking candidate is worth booking now. Give Codex a city plus one or more tour, stay, or activity names/URLs; the `verify-booking` skill tells the agent to gather only public web evidence, score six axes, and produce a decision card.

The six axes are:

- Review reliability
- Price fairness
- Location and routing
- Operator reliability
- Traps and risks
- Context such as season, hours, and local closures

When evidence is missing, the skill must show the uncertainty instead of inventing a claim, and the scoring script lowers confidence.

## Files

- `src/.codex-plugin/plugin.json`: Codex plugin manifest. It names the plugin, version, install-surface copy, and points Codex at `./skills/`.
- `src/skills/verify-booking/SKILL.md`: The verification playbook Codex reads when the task matches travel booking verification.
- `src/skills/verify-booking/scripts/score.py`: Deterministic stdlib-only scorer. It reads findings JSON from stdin or a file and prints scores, risk flags, and verdict.

## Run the scorer locally

Create a sample JSON file, then run:

```powershell
python .\src\skills\verify-booking\scripts\score.py .\sample-findings.json
```

Or pipe JSON through stdin:

```powershell
Get-Content .\sample-findings.json | python .\src\skills\verify-booking\scripts\score.py
```

Output shape:

```json
{
  "axis_scores": {
    "context": 50,
    "location_routing": 38,
    "operator_reliability": 52,
    "price_fairness": 52,
    "review_reliability": 50,
    "traps_risks": 28
  },
  "overall_score": 45,
  "risk_flags": ["traps_risks:critical:forced shopping"],
  "verdict": "비추천"
}
```

## Install and test in Codex

Official Codex plugin docs say a plugin has `.codex-plugin/plugin.json`, bundled components such as `skills/`, and a local marketplace entry whose `source.path` points to the plugin folder with a `./` relative path.

Repo-local marketplace test:

1. Keep this plugin at `src/`.
2. Add `.agents/plugins/marketplace.json` in the repo if you want a repo-scoped local marketplace:

```json
{
  "name": "ax-local",
  "interface": {
    "displayName": "AX Local"
  },
  "plugins": [
    {
      "name": "mrt-trip-verify",
      "source": {
        "source": "local",
        "path": "./src"
      },
      "policy": {
        "installation": "AVAILABLE",
        "authentication": "ON_INSTALL"
      },
      "category": "Travel"
    }
  ]
}
```

3. Restart Codex.
4. Open Plugins, choose `AX Local`, and install `mrt-trip-verify`.
5. Start a new thread and ask:

```text
Use verify-booking for Bangkok: Example public food tour URL. Can I book this now?
```

Personal marketplace test:

1. Copy `src/` to a plugin folder under your personal plugin root, for example `~/.codex/plugins/mrt-trip-verify`.
2. Add or update `~/.agents/plugins/marketplace.json` with a plugin entry whose `source.path` points to that folder relative to the marketplace root.
3. Restart Codex and install from the personal marketplace.

## Demo flow

Prompt:

```text
Use verify-booking. City: Bangkok. Candidate: a public Damnoen Saduak floating market tour URL. Trip date: 2026-08-12. Decide whether I should book now.
```

Expected flow:

1. Codex searches public web pages for reviews, comparable prices, pickup/route details, policies, tourist-trap signals, and date context.
2. Codex writes findings JSON with source URLs.
3. Codex runs `src/skills/verify-booking/scripts/score.py`.
4. Codex returns a confidence card: verdict, six-axis evidence summary, source URLs, remaining uncertainty, and one-line booking reason.

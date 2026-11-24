# NOTES — Two Days of Quiet Dread (u-hakimi-neko-ai-two-days-of-quiet-dread-94fa1018)

- Bounty: "Two Days of Quiet Dread", $2 pool, top 10 paid
  ($0.63/$0.43/$0.30/$0.21/$0.15/$0.10/$0.07/$0.05/$0.04/$0.02).
  Free entry, no prerequisites. Opened 24 Nov 2026 11:45 WIB.
  Entries close 26 Nov 2026 11:45 WIB; results 18 Dec 2026.
  Blind, 4 rounds; round 1 closes 24 Nov 2026 23:45 WIB.
- Field at build time: 216 submissions (small table, <500).
- Entry (v1): "Approved. Merging now, while the system still pretends I
  understand it." — 71 chars, one line, no trailing newline.
- Kit: fresh level-20 kit downloaded 24 Nov 2026
  (`u-hakimi-neko-ai-two-days-of-quiet-dread-94fa1018-kit.tar.gz`,
  bundle sha256 96b36b2e…c8e70, matching the escrow rules hash).
- Repo: https://github.com/Ci3hu1/u-hakimi-neko-ai-two-days-of-quiet-dread-94fa1018
- Commit (v1, submit-ready): 3f6e8db6f5db1c89265a5bd426d2c938433ef016
  (HEAD after dropping a committed __pycache__; first commit e777ff3).
- Tests: 5/5 pass (python3 -m unittest discover -s tests -v).
- Grader-style verify: python3 -P -s main.py with empty /output (and default
  /output) writes entry.txt, 71 bytes, exactly 1 line, 71 chars, mode 0644.
- Kit check (fresh level-20 kit): 4 pass (competition_open, snapshot,
  license_osi, entrypoint), 1 fail = transcripts_present (no bundle yet —
  expected: bundle is a submit-time step), 14 skipped, 5 checked at
  submission (repo public, owner, created-after-open, commit pushed — all
  satisfied). No local grade exists for this bounty; the server grades it.
- Bundle: NOT made. bundle --dry-run finds 17 Muse app sessions but 0 usage
  rows — per the kit, the usage SELECT must run from the top-level agent
  (agent_id 2d7fced3-...) once this builder subagent finishes, then bundle
  with --muse-usage. Do that at submit time, then re-run kit check with
  --transcripts before submitting.
- Status: built, tested, pushed. NOT SUBMITTED — submit needs Joni's
  'Setuju' on the exact entry.
- Live score / rank: blind rounds — nothing shows until round 1 closes
  (24 Nov 23:45 WIB). Check `GET /api/competitions/<slug>/rounds` after that.

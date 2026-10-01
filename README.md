# declaire-bench

Fixture code for [Declaire](https://github.com/panyam/declaire)'s query
benchmark. Declaire pins this repo by commit in `bench/workspace.txtpb` and asks
questions of it, the same way it asks them of its other benchmark repos.

## Why fixtures

Many of the repos Declaire needs to handle can't be pinned in a public
benchmark, usually because of their license. Instead, Declaire profiles those
repos locally, reporting what it failed to see and the frameworks and
annotations the code uses, with names and values stripped. Each symptom is then
reproduced here as fresh code with the same shape.

## Rules

- Every fixture reproduces a symptom from a profile report, and its commit
  cites that symptom (`symptom: <shape>`).
- Every fixture arrives with a benchmark question in Declaire that fails
  before the fix and passes after it.
- No code, names or string values copied from the repo the symptom came from.
  Public frameworks and libraries are fine, and should match.
- Nothing is added ahead of a symptom or a question.

## Layout

- `protos/`: shared service definitions
- `java/`: Java services (Gradle)
- `python/`: Python services and clients (pytest)

Each grows only as fixtures need it.

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

- Every fixture reproduces a symptom from a profile report or answers a
  Declaire benchmark question, and its commit cites which
  (`symptom: <shape>` or `question: <id>`).
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

## Building

Generated code is committed. `cd protos && buf generate` regenerates it; the
plugin versions there match the runtimes in `java/build.gradle.kts` and
`python/pyproject.toml`.

- Java: JDK 17, `cd java && ./gradlew test`.
- Python: `pip install './python[test]'`, `cd python && pytest`.

## Fixtures

| Fixture | Asked by | Shape |
|---|---|---|
| `inventory` | Declaire q32, q32p, q33, q34, q35 | A Python client calls `ReserveItem` on a Java gRPC server through shared protos; a JUnit test exercises the server method directly, and pytest and unittest tests exercise the client against a fake channel. Private helpers (`lookup` on the server, `_request` in the client) sit behind the public methods. |

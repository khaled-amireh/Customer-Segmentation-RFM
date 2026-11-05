# Contributing

Start with the [evidence baseline](docs/EVIDENCE.md), [read-only audit](docs/CODE_AUDIT.md), and [reproduction guide](docs/REPRODUCIBILITY.md). Describe the specific problem and evidence in an issue or pull request.

## Documentation and presentation changes

- Keep Python, notebook bytes (including outputs and metadata), original images, datasets, dependencies, and analytical settings unchanged in documentation-only work.
- Cite the notebook cell ID or script line supporting technical claims. Label examples, qualitative plot readings, and future experiments explicitly.
- Do not infer cluster counts, profiles, stability, or commercial outcomes from a scatterplot. Retain the distinction between saved output and newly reproduced results.
- Use relative links, descriptive image alt text, simple GitHub-compatible Markdown/Mermaid, and the established banner palette. The new SVG must remain static and self-contained.
- Review `git diff --check`, local links and anchors, image paths, and the diff against the preservation manifest. Stage only intended files and keep commits focused.

## Proposed analytical changes

The current documentation preserves the original implementation. Any later analytical revision belongs in an explicitly scoped, separate change. First record the input checksum, source attribution, conversion history, date window, package versions, and expected output locations. Run in a disposable checkout so existing artifacts remain reviewable.

For a cleaning or model-policy change, report affected rows/customers, raw-unit feature effects, cluster sizes and profiles, and before/after evaluation on comparable inputs. Record K, seeds, restart settings, and any sampling. Explain why a metric difference matters; do not label untested campaigns as business improvements. Avoid publishing unnecessary customer-level data.

## Review and publication

Use Conventional Commit messages such as `docs: clarify invoice-based frequency`. Keep each commit useful on its own. Never manufacture commit counts by splitting trivial changes. Do not rewrite existing history or push on another contributor's behalf without authorization.

The [MIT license](LICENSE) covers this repository. Respect the independently applicable dataset license and attribution in [DATASET.md](docs/DATASET.md).

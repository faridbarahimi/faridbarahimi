# AICP Tools / Kashkool — Public Architecture Contract

## Purpose

Tools / Kashkool is the first public operational projection of AICP's Capability Fabric.

The public layer exposes capability discovery concepts and a user-facing catalog without publishing AICP Core source, private Obsidian material, credentials, or internal runtime configuration.

## Capability lifecycle

```text
Parallel Discovery
  ├─ GitHub Search
  ├─ Awesome Lists
  └─ Public Search
        ↓
Normalize → Dedupe → Qualification → Policy / License Gate
        ↓
Qualified Registry
        ├─ reusable capability
        └─ execution contract
        ↓
Candidate Store (not trusted)
        ↓
Build This Capability (suggestion only)
```

GitHub-oriented discovery uses a configurable star floor; the initial policy targets projects with at least 1,000 stars.

Qualification is independent from discovery. Discovery never implies trust or execution eligibility.

## MVP catalog

- Documents: Word ↔ PDF, merge/split/rotate, compression, OCR, PDF ↔ image
- Images: background removal, passport photo, resize/compress, format conversion
- Audio/video: audio extraction, media conversion, transcription
- Quick browser tools: QR, word/character counter, password generation

## Execution model

Lightweight capabilities are browser-first where practical.

Heavy capabilities cross an execution boundary:

```text
UI → authorization/quota → job contract → queue → isolated worker
   → result/evidence → verification
```

The initial queue contract is Redis-compatible with:
- queue: `aicp-heavy-tools`
- max attempts: 1
- visibility timeout: 900 seconds
- worker timeout: 900 seconds
- result retention: 24 hours

No production Redis instance or worker runtime is implied by this public document.

## API contract

```text
GET  /api/capabilities
POST /api/tools/{slug}/execute
POST /api/discovery/trigger        # admin boundary
GET  /api/user/usage
```

Execution must reject unknown/unqualified capabilities and must enforce authorization and heavy-use quota before queue submission.

## Data model

The public contract maps to these conceptual records:

- `capabilities`
- `capability_versions`
- `capability_providers`
- `discovery_runs`
- `discovery_candidates`
- `qualification_results`
- `user_usages`
- `subscriptions`
- `credits`

The production schema and implementation remain in the private AICP Core repository.

## Freemium policy

Heavy/AI capabilities use a configurable 3–5 free-use monthly allowance. The initial default is 3. Lightweight browser-local utilities are not quota-bound by this contract.

## Build fallback

If no qualified reusable capability exists, the UI may show **Build This Capability** as a discovery gap and product suggestion. It must not trigger an automatic build.

## Verification

The public surface is tested for:
- complete MVP catalog coverage
- public/private boundary
- navigation and documentation links
- JavaScript syntax
- HTTP serving of `/tools/`

Current public-surface checkpoint: **6 tests passed**.

## Boundary

This repository is the public presentation and contract layer.

Private AICP Core implementation, internal ADRs, Obsidian state, credentials, provider keys and runtime infrastructure remain outside this public surface.

📘 Latai AI Feedback File (feedback.ai.yaml)
This document explains the full structure of the feedback.ai.yaml file used in Latai to evaluate and benchmark AI-generated outputs.
It is written to be beginner-friendly — even a 13-year-old curious coder can understand it.

🔤 What is feedback.ai.yaml?
This YAML file captures structured feedback and quality evaluations of a generated artifact (usually from a PPM prompt). It’s used to:
Benchmark AI performance


Record manual or automated reviews


Store metrics like correctness, usefulness, performance, etc.


Align to PPM structure for easy comparison


It is human- and machine-readable, version-controlled, and audit-ready.

🧱 Structure Overview
1. Params (Optional)
   Reusable variables, like paths or filenames, that can be referenced with ${}.
   Params:
   basePath: /input
   fullReviewDoc: ${basePath}/review.docx


2. Authoring (Recommended)
   Lists who reviewed or provided the feedback.
   Authoring:
   authors:
    - name: David
      email: david@latai.ai
      copyright: © 2025 Latai Framework


3. ModelGeneration (MANDATORY)
   Details about the generation session and what was reviewed.
   ModelGeneration:
   usedPPM: /latai/MyExcelParserGenerator.ppm.yaml
   generatedBy: gpt-4.5
   generatedTime: 2025-05-01T12:45:00Z
   evaluatedBy: human-review

usedPPM: Path to the PPM file (REQUIRED)


generatedBy: Model version used (REQUIRED)


generatedTime: Timestamp (optional; default = file date)


evaluatedBy: Who/what evaluated (optional; default = human-review)



4. Config (Optional)
   The model config used during generation (should match PPM).
   Config:
   provider: openai
   model: gpt
   version: 4.5
   extension: thinking-model
   params:
    - name: temperature
      value: 0.7


5. evaluation (MANDATORY)
   Main performance metrics. Only 1 decimal allowed. Use null or 0.0 to mark not evaluated.
   evaluation:
   usefulness: 8.5              # How useful was the output?
   correctness: 9.0             # Does it work as intended?
   actualUsageRatio: 0.65      # % of output reused as-is
   manualCorrectionsNeeded: 2  # Manual edits required
   coverage: 7.5               # Functional coverage
   hallucinationRisk: medium   # low, medium, high, or n/a
   modelConfidence: 0.87       # Model's own confidence (if available)
   reusabilityScore: 8.0       # Can we use it elsewhere?

REQUIRED fields:
usefulness


correctness


actualUsageRatio



6. codeQuality (MANDATORY)
   Review of technical quality. Use null or 0.0 if not evaluated.
   codeQuality:
   codeQualityScore: 7.5       # Naming, structure, formatting
   patternAlignment: 8.0       # Use of expected design/code patterns
   readabilityScore: 9.0       # Easy to read and maintain
   performanceScore: 6.5       # Runtime efficiency
   securityRisk: low           # low, medium, high, or n/a

REQUIRED fields:
codeQualityScore


performanceScore


securityRisk



7. comments (Optional)
   List of notes and file references.
   comments:
   files:
    - ${fullReviewDoc}
      notes:
    - "Missed a column mapping."
    - "Code is reusable but lacks try/catch blocks."


8. ExtraInfo (Optional)
   Anything else that may help future reviews.
   ExtraInfo:
   scenario: "proof-of-concept"
   additionalTags: [early-test, qa-pass]
   reviewerSetup: "macOS + VSCode"
   notesFromTeam: |
   Reviewed by QA team. Found some edge case failures.


📌 Summary of Mandatory vs Optional
Section
Required?
Description
Params
Optional
For variable reuse
Authoring
Recommended
Who wrote the feedback
ModelGeneration
✅ Required
Links this file to the PPM
Config
Optional
Snapshot of model settings
evaluation
✅ Required
Main scoring
codeQuality
✅ Required
Technical quality check
comments
Optional
Freeform comments and files
ExtraInfo
Optional
Extra notes and team metadata


✅ Final Notes
Only one decimal allowed in scores


null or 0.0 means “not evaluated”


Enums like hallucinationRisk must be one of: low, medium, high, n/a


Use in conjunction with validation schema (e.g. Yamale) to automate checks



Next step: Validate your file using the feedback_schema.yaml and yamale CLI tool


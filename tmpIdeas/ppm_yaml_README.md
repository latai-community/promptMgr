📘 Latai Prompt Project Model Language (PPM)
Welcome to the official documentation of Latai's Prompt Project Model (PPM) — a declarative, YAML-based configuration language for orchestrating modular AI prompt workflows. This guide explains the full structure of a PPM.yaml file with detailed descriptions, order, keywords, constraints, and examples so that anyone (even a 13-year-old curious coder) can use it.

🔤 What is a PPM file?
A PPM.yaml file defines how to build and execute a full AI prompt, including:
Prompt text or fragments


AI model configuration


Input files for context


Expected outputs


Authoring metadata


It is readable, reusable, and easy to track in Git.

🧱 Structure Overview (ordered by best practices)
1. Params (Optional but Recommended)
   Reusable variables you can reference anywhere in the file with ${paramName} syntax.
   Params:
   basePath: /my/input/folder
   outputPath: /results
   introText: "Hola, este es el prompt inicial."

💡 Useful to avoid repeating paths or fragments.


❗ Variables must only contain strings or multi-line blocks.



2. Authoring (Recommended)
   Describes the authorship and copyright.
   Authoring:
   authors:
    - name: David S
      email: david@latai.ai
      copyright: © 2025 Latai Framework


3. ParentPrompts (Optional)
   Defines inheritance from other .ppm.yaml files. Think of them like base templates or mixins.
   ParentPrompts:
- base.ppm.yaml
- cleanCodeRules.ppm.yaml

🔄 These prompts are merged in order.


❗ No circular references allowed.



4. Prompt (MANDATORY)
   Defines the actual instructions given to the AI. Can be:
   A single string


A list of strings


Reusable params like ${introText}


Prompt:
- ${introText}
- "Gpy, convierte este Excel en SQL usando buenas prácticas."
- "Asegúrate de seguir las reglas de validación."


5. Modules (Optional)
   List of logical prompt modules used in this generation (e.g., subgenerators).
   Modules:
- mod-excel-parser
- mod-validator

🔖 Good for tracking complexity.


🧩 Not inherited from parents.



6. EffectivePPM (MANDATORY)
   Defines where to store the final compiled prompt (after merging all inputs).
   EffectivePPM:
   output: ${outputPath}/EffectivePrompt.ppm.txt


7. Config (MANDATORY)
   Configures the AI model and its behavior. Mirrors feedback file structure.
   Config:
   provider: openai
   model: gpt
   version: 4.5
   extension: thinking-model
   params:
    - name: temperature
      value: 0.7
    - name: stop
      value: ["User:", "###"]

❗ params is a flexible list; you can add any name/value pair.


🔁 This block should match your feedback for auditability.



8. Input (Optional)
   Contextual files to guide AI behavior: .xlsx, .sql, .java, .pdf, etc.
   Input:
- file: clients.xlsx
  path: ${basePath}/clients.xlsx
- file: schema.sql
  path: ${basePath}/schema.sql

🧠 Referenced by prompts implicitly.



9. ExpectedOutput (Optional)
   Defines what kind of artifact you expect. Used for documentation.
   ExpectedOutput:
   type: code
   extension: .java
   supportFiles: true


10. Output (MANDATORY)
    Specifies the actual output files generated from the AI execution.
    Output:
    type: code
    extension: .java
    mainFile: ExcelMapper.java
    supportFiles:
    - Validator.java
    - ai-feedback.ai.yaml

❗ Main file is required; supportFiles is optional.



11. ExtraInfo (Optional)
    For arbitrary metadata, ignored by the Latai engine but useful for humans.
    ExtraInfo:
    scenario: "qa-benchmark"
    tags: [ai, excel, validator]
    notes: "Primera prueba con GPT 4.5"


📌 Constraints Summary
Section
Required
Notes
Params
No
Use for DRY (Don't Repeat Yourself)
Authoring
Yes
Required for audit
ParentPrompts
No
Can inherit multiple
Prompt
Yes
Core instruction to AI
Modules
No
Helps organize complex prompts
EffectivePPM
Yes
Final output location
Config
Yes
Must match actual model usage
Input
No
Referenced context files
ExpectedOutput
No
For humans / documentation only
Output
Yes
Real AI result tracking
ExtraInfo
No
Free form data


🧪 Example Prompt Assembly
The following example:
Prompt:
- ${introText}
- "Genera un código que convierta XLS en JSON."

With:
Params:
introText: "Hola Gpy, aquí tienes tu misión."

Results in:
Hola Gpy, aquí tienes tu misión.
Genera un código que convierta XLS en JSON.


✅ Conclusion
The PPM language is designed to be:
Human-friendly


Modular and reusable


Ready for CI/CD


Flexible for prompt engineering at scale


Use this file as a guide to build your own *.ppm.yaml files with confidence and clarity.

Next: Learn how to validate PPM files using Yamale or integrate them into your own Latai tooling.


# Agentic AI Research Project: From Use Case to Research Paper

## Objective

Develop an agentic AI solution for a realistic workplace problem. Identify a suitable use case, design the agents and workflow, implement a working prototype, and write a research paper explaining the solution and its evaluation.

This research project combines the workflow case study and research paper into one project with four connected stages. Use the same use case throughout, refining it as you learn from research, design, and implementation.

| Project stage | Focus | Main deliverable |
|---|---|---|
| 1. Identify a use case | Understand the problem and current process. | Use-case brief and current-state process diagram. |
| 2. Design the concept and agents | Define the proposed workflow, agent roles, prompts, tools, and human oversight. | Design document and proposed-workflow diagram. |
| 3. Implement and evaluate | Build a small working prototype and examine its behaviour. | Runnable implementation, setup instructions, and evaluation results. |
| 4. Write a research paper | Explain the problem, design, implementation, findings, and limitations. | Final paper as a PDF. |

## Learning outcomes

By completing this research project, you should be able to:

- Identify a focused use case and justify whether agentic AI is appropriate.
- Translate a manual process into a workflow with clear agent responsibilities and human review points.
- Define agent prompts, tools, inputs, outputs, and handoffs.
- Implement and evaluate a prototype using public or synthetic data.
- Critically discuss evidence, risks, limitations, and potential organisational value.
- Communicate the work in a research paper with verified references.

## Use AI throughout the research project

Use AI tools such as Claude, ChatGPT, Gemini, or similar tools to explore the use case, analyse the process, develop the design, locate research, critique ideas, create diagrams, and improve the paper. Use an AI coding tool such as Claude Code, Codex, or a similar assistant to support implementation, testing, and debugging.

You remain responsible for the submitted work. Review generated code and text, verify important claims and references, and explain the decisions you make.

Use public or synthetic data. Do not submit API keys, confidential documents, personal data, or internal information you are not authorised to share.

## Project Stage 1: Identify a use case

### Task

Choose one narrow, repetitive process from a setting you understand: your workplace, office, internship, volunteer role, family business, or student organisation. If you do not have access to such a setting, use a clearly described realistic scenario and state your assumptions.

Explain the problem before proposing the technology. Your brief should cover:

- **Context and problem:** the setting, users or teams affected, and why the problem matters.
- **Current process:** its trigger, inputs, people involved, steps, outputs, and pain points.
- **Scope:** the part of the process your project will address and what is outside its scope.
- **Suitability for agentic AI:** which steps require interpretation, decisions, or tool use, and why an agentic workflow could help compared with a simpler approach.
- **Expected value:** potential improvements in time, quality, consistency, cost, or decision support. Label assumptions and estimates clearly.
- **Success measures:** how you will assess the prototype, such as task completion, correctness, processing time, or need for human correction.
- **Data availability:** the public or synthetic inputs you can use to build and evaluate the solution.

Include a current-state process diagram showing how the work is performed today.

### Deliverable

A use-case brief in Markdown, PDF, or document format, including the current-state diagram and initial success measures. This brief provides the problem definition for Stage 2.

## Project Stage 2: Design the concept and agents

### Task

Design the proposed solution for the use case selected in Stage 1. Explain which steps will be automated, assisted, or performed by a person.

Include a proposed-workflow diagram showing the trigger, inputs, agents, tools, handoffs, decisions, human review points, and final outputs. Mermaid, draw.io, and Excalidraw are acceptable diagram tools.

Use focused agent roles. A small workflow will usually need 2–5 agents; justify the number and responsibilities you choose. For each agent, document:

- Name, purpose, and responsibility.
- Inputs it receives and outputs it produces, including the expected output format.
- Tools and data sources it can access, and when it may use them.
- Decision rules and the agent, user, or system that receives its output next.
- Conditions requiring human review, approval, or escalation.
- System prompt defining its role, goal, inputs, rules, boundaries, and output format.

Explain how the workflow handles missing information, incorrect outputs, tool failures, and any review or retry loops. Define a stopping condition for loops. Describe privacy considerations, access restrictions, and which actions require approval before execution.

Plan the evaluation before implementation: select representative inputs, define what a successful output looks like, and describe a comparison with the current process or a simple baseline where feasible.

### Deliverable

A design document in Markdown, PDF, or document format containing the proposed-workflow diagram, agent specifications, system prompts, tool descriptions, human oversight rules, and evaluation plan. This design guides Stage 3.

## Project Stage 3: Implement and evaluate the workflow

### Task

Build a small working proof of concept of the design from Stage 2. Use a notebook, Python application, or a no-code/low-code workflow that can be shared and reproduced. You may adapt the course lab examples; identify the starting point and explain your changes.

The prototype should demonstrate the main path from input to output, including agent interactions, tool use where relevant, and the human review points defined in your design. A production deployment or connection to real company systems is not required. External business actions may be simulated, provided you clearly identify what is simulated.

Provide:

- The implementation and public or synthetic sample inputs.
- Setup and execution instructions, dependencies, model/provider configuration, and instructions for supplying credentials securely.
- An example run showing intermediate agent outputs or a workflow trace and the final result.
- Evaluation cases covering normal operation and relevant failure or edge cases, such as missing information, conflicting evidence, or an unavailable tool.
- Results against the success measures from Stage 1, including observed errors and any human corrections.
- A short explanation of changes made to the original design and why they were needed.

Report measured results separately from estimates. If you compare against a baseline, describe how the comparison was performed. Discuss execution time and model cost where available, and state the limits of a small evaluation.

Implementation is a required part of this research project. Keep the scope small enough to produce a runnable demonstration; pseudocode may explain the design but does not replace the prototype.

### Deliverable

A runnable notebook, source-code project, or exported workflow with setup instructions, sample inputs, example outputs, and a short evaluation report. Publish the source code or exported workflow in a GitHub repository and include the repository link in your submission and research paper. These results form the evidence for Stage 4.

## Project Stage 4: Write a research paper

### Task

Develop the work from Stages 1–3 into one coherent research paper. Explain what problem you addressed, how the workflow was designed and implemented, what you observed, and what the evidence supports.

Write the paper in LaTeX using Overleaf if possible, and submit the compiled paper as a PDF.

**Suggested paper structure:** You may adapt the headings and organisation to suit your research project. Your paper must still address all the topics below, clearly distinguish measured results from expected benefits, and cite the sources you use.

1. **Title and abstract:** summarise the problem, approach, main findings, and limitations.
2. **Introduction:** explain the context, motivation, project objective, and research question.
3. **Related work:** discuss relevant research and explain how it informs your approach. Verify that every cited source exists and supports the associated claim.
4. **Use case and current process:** describe the users, scope, pain points, and current-state diagram.
5. **Proposed workflow and agent design:** explain the architecture, agent roles, prompts, tools, handoffs, and human oversight. Include the proposed-workflow diagram.
6. **Implementation:** describe the prototype, data, models, configuration, and practical design choices. Link or cite the submitted code or workflow and identify reused material.
7. **Evaluation and results:** describe the evaluation method, inputs, success measures, comparison where available, and observed results, including failures.
8. **Discussion and limitations:** interpret the findings, distinguish demonstrated benefits from expected benefits, and discuss privacy, bias, incorrect outputs, access control, cost, technical limitations, and human escalation.
9. **Conclusion and future work:** state what the project demonstrated and what would need further investigation or development.

Place lengthy system prompts, sample outputs, and detailed evaluation tables in an appendix or the accompanying project files, with clear references from the paper.

The paper should reflect the implementation you actually built. Identify unimplemented features as future work, and do not present hypothetical or AI-generated results as measured findings.

### Optional next step: share or publish your research

Consider developing your paper for a wider research audience after receiving feedback from your instructor or supervisor. You may share a suitable manuscript as a preprint on arXiv or another appropriate repository, or develop it for submission to a conference or journal. This is optional: public posting or acceptance is not required for project completion or grading.

A preprint makes a manuscript publicly available; posting it does not establish that it has passed peer review. arXiv moderates submissions and expects substantive scholarly work, so a course project is not automatically suitable. Read its [submission guidelines](https://info.arxiv.org/help/submit/index.html), [moderation policy](https://info.arxiv.org/help/moderation/index.html), and [endorsement requirements](https://info.arxiv.org/help/endorsement.html) before submitting.

Before sharing, agree on authorship with all contributors, obtain co-author consent, verify permission to share the material, and check the chosen venue's submission and licensing requirements. Include a link to your code and clearly describe the evaluation and limitations. If you share the paper, add its public link or identifier to your project repository.

### Research starting points

The following papers in this repository provide examples of agentic AI use cases. Use them as optional starting points alongside your own research:

- [Flowr — Scaling Up Retail Supply Chain Operations Through Agentic AI in Large Scale Supermarket Chains](../papers/flowr-agentic-ai-retail-supply-chain.pdf)
- [Think Before You Act — A Neurocognitive Governance Model for Autonomous AI Agents](../papers/think-before-you-act-neurocognitive-ai-agent-governance.pdf)
- [Rovanima — Scaling Up Small and Medium-sized Tourism Enterprises Through Agentic AI in Lapland](../papers/rovanima-agentic-ai-tourism-enterprises-lapland.pdf)

### Deliverable

The final research paper as a PDF, drawing on the use-case brief, design, implementation, and evaluation from the preceding stages.

## Final submission

Submit the four stages as one project package:

1. **Use-case brief**, including the current-state process diagram.
2. **Design document**, including the proposed-workflow diagram, agent specifications, prompts, and evaluation plan.
3. **Implementation and evaluation**, including the GitHub repository link, runnable files, setup instructions, sample inputs, example outputs, and results.
4. **Research paper** as a PDF, including references.

Ensure the documents and implementation describe the same final workflow. Record significant refinements to the original use case or design so that the progression of the project is clear.

## Before submitting

- Is the use case specific, feasible, and clearly justified?
- Does each agent have a clear responsibility, with defined inputs, outputs, and tools?
- Are human review, failure handling, and stopping conditions clear?
- Can another person follow the instructions to run the prototype with their own credentials?
- Do the evaluation results support the claims made in the paper?
- Are sources verified and reused code or ideas acknowledged?
- Have you removed secrets and confidential or personal data?

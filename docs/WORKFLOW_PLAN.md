# Workflow plan

## Intended user journey

1. Open an n8n form.
2. Upload a resume (initial targets: PDF and DOCX) and paste the job description.
3. Extract resume text locally within the workflow/container.
4. Ask Gemini to tailor the content using only facts supported by the source resume.
5. Return a clear change summary and a downloadable, editable DOCX; PDF output is a follow-up target.
6. Avoid Google Drive, Notion, Firecrawl, or any mandatory external document-storage service.

## Template to adapt

Starting point: [Create tailored resumes from job postings with OpenRouter, Notion, and Google Drive](https://n8n.io/workflows/18032-create-tailored-resumes-from-job-postings-with-openrouter-notion-and-google-drive/)

The existing template is useful as a reference for the form and resume-generation prompt, but it relies on Notion career databases, OpenRouter, Firecrawl, and Google Drive/Docs. It is **not** a drop-in solution for this project.

## Implementation checklist

- [ ] Import and inspect the source template in a local n8n instance.
- [ ] Remove Notion, Google Drive/Docs, and Firecrawl nodes.
- [ ] Replace the career-database source with the uploaded master resume.
- [ ] Add and test PDF/DOCX text extraction.
- [ ] Configure Gemini using an n8n credential (no secrets embedded in the workflow).
- [ ] Require the model to preserve facts, dates, employers, qualifications, and measurable claims; do not invent experience.
- [ ] Generate a structured output suitable for a DOCX template.
- [ ] Return downloadable output without cloud storage.
- [ ] Test with fictional resumes and several job descriptions.
- [ ] Export a clean workflow JSON and confirm it imports on a fresh n8n instance.
- [ ] Update README with exact, tested instructions and screenshots if useful.

## Design notes

- Prefer built-in n8n nodes and standard container capabilities over custom nodes where practical.
- If a helper container or dependency is required for reliable DOCX/PDF generation, document and pin it explicitly.
- Do not commit credentials, real resumes, generated resumes, or n8n's database.
- Keep the workflow export free of credential values and personal candidate data.

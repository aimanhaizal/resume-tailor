# Resume Tailor V1 — How to Start and Use It, MIMOS

## 1. Start the services on the Linux workstation

SSH into the Linux workstation, then run:

```bash
cd /home/work/resume-tailor
docker compose up -d
docker compose ps
```

Both `n8n` and `docx-generator` should show as running.

If you have changed the DOCX generator code and need to rebuild it, use:

```bash
cd /home/work/resume-tailor
docker compose up -d --build docx-generator
```

Optional health checks from the Linux workstation:

```bash
curl http://localhost:5678/healthz
curl http://localhost:8000/health
```

Expected responses include `{"status":"ok"}`.

## 2. Connect from my Windows PC

Open **PowerShell** on Windows and paste:

```powershell
ssh -N -o ExitOnForwardFailure=yes -L 5678:localhost:5678 -L 8000:localhost:8000 mimos@10.1.32.1
```

Enter the SSH password or complete authentication if prompted. Leave this PowerShell window open while using Resume Tailor. It is the tunnel connecting your browser to the Linux workstation.

If the command reports that a local port is already in use, check whether another tunnel window is already running. Do not close a working tunnel if you are currently using the app.

## 3. Open n8n

On Windows, open your browser and visit:

http://localhost:5678/workflow/0xhTkhWsjakiuKJb/3247f7

This opens the Resume Tailor workflow in n8n, provided the workflow ID is still valid and you are logged in.

If that link stops working, open:

http://localhost:5678

Then find **Resume Tailor - Local Gemini (MVP)** in the workflows list.

## 4. Run Resume Tailor

1. Open **Resume Tailor - Local Gemini (MVP)**.
2. Click **Execute Workflow** or the workflow's test/run button, depending on the current n8n interface.
3. Open the resume intake form presented by the workflow.
4. Upload the candidate's resume PDF.
5. Paste the target job description into the job-description field.
6. Submit the form and let the workflow run.
7. Check that the nodes complete successfully, especially **Tailor Resume with Gemini**, **Parse Gemini Response**, and **HTTP Request**.
8. When the completion screen appears, use the DOCX download link to download the tailored resume and review report.

The generated DOCX includes the tailored resume and a review report on a separate page. Review it carefully and remove the report page before sending the resume to an employer.

## 5. If the DOCX download or workflow fails

On the Linux workstation:

```bash
cd /home/work/resume-tailor
docker compose ps
docker compose logs --tail=100 n8n
docker compose logs --tail=100 docx-generator
```

To restart the services:

```bash
cd /home/work/resume-tailor
docker compose up -d
```

If the DOCX generator needs rebuilding:

```bash
docker compose up -d --build docx-generator
```

Then keep the Windows SSH tunnel open and refresh the n8n page.

## 6. Important notes

- Keep the Linux workstation powered on and connected to the network.
- Keep the SSH tunnel window open while using the app.
- The DOCX download link is temporary and expires after approximately two hours.
- Gemini may produce inaccurate claims. Confirm all skills, dates, qualifications, and accomplishments before using the resume.
- Never claim a skill or experience the candidate does not actually have.
- Do not upload confidential or sensitive resume data unless you are comfortable sending it to the configured Gemini service.
- The `.env` file contains local configuration and secrets. Do not commit it to GitHub.
- If accessing the app from another PC, open the SSH tunnel on that PC and use `http://localhost:5678`.

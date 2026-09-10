"""Repository structure, evidence, link, safety, and saved-result validator."""
from __future__ import annotations
import json, re, subprocess, sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
PROJECTS=[
    ("01-symbolic-legal-triage","triage.py"),
    ("02-neural-model-basics","classifier.py"),
    ("03-legal-document-vision","vision.py"),
    ("04-legal-nlp","pipeline.py"),
    ("05-agentic-legal-workflows","router.py"),
]
REQUIRED=["README.md","portfolio.json","course-map.md","LICENSE","THIRD_PARTY_NOTICES.md","requirements.txt",".gitignore",".github/workflows/validate.yml","evaluations/RUBRIC.md","evaluations/smoke-tests/README.md","evaluations/recruiter-review/REVIEW_PROMPT.md","evaluations/recruiter-review/REPORT.md","evaluations/recruiter-review/report.json","provenance/LEARNING_STATEMENT.md","provenance/AUTHORSHIP_AND_AI_USE.md","provenance/SOURCE_REGISTER.md","scripts/run_checks.py"]
TEXT_SUFFIXES={".md",".py",".json",".yml",".yaml",".txt",".ttl",".pgm"}

def fail(errors,message): errors.append(message)
def local_links(path):
    text=path.read_text(encoding="utf-8")
    for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)",text):
        clean=target.split("#",1)[0]
        if clean and not re.match(r"^[a-z]+://",clean) and not clean.startswith("mailto:"):
            yield clean

def validate():
    errors=[]
    for rel in REQUIRED:
        if not (ROOT/rel).is_file(): fail(errors,f"missing required file: {rel}")
    for name,source in PROJECTS:
        base=ROOT/"projects"/name
        for rel in ("README.md","AUTHORSHIP.md","results.json",source):
            if not (base/rel).is_file(): fail(errors,f"missing project file: projects/{name}/{rel}")
        if not (base/"data").is_dir() or not any((base/"data").iterdir()): fail(errors,f"missing project data: {name}")
        if not list(base.glob("test_*.py")): fail(errors,f"missing project tests: {name}")
    try: portfolio=json.loads((ROOT/"portfolio.json").read_text(encoding="utf-8"))
    except Exception as exc: fail(errors,f"invalid portfolio.json: {exc}"); portfolio={}
    try: json.loads((ROOT/"evaluations/recruiter-review/report.json").read_text(encoding="utf-8"))
    except Exception as exc: fail(errors,f"invalid report.json: {exc}")

    lessons=portfolio.get("lessons",[]); nums=[x.get("number") for x in lessons]
    if len(nums)!=24 or sorted(nums)!=list(range(1,25)) or len(set(nums))!=24: fail(errors,"portfolio.json must contain lessons 1-24 exactly once")
    evidence=portfolio.get("evidence",[]); ids=[x.get("id") for x in evidence]
    if len(ids)!=len(set(ids)): fail(errors,"evidence IDs must be unique")
    idset=set(ids)
    for item in evidence:
        path=item.get("path","")
        if not path or not (ROOT/path).is_file(): fail(errors,f"evidence path does not exist: {path}")
    for claim in portfolio.get("claims",[]):
        refs=claim.get("evidence_ids",[])
        if not refs: fail(errors,f"claim has no evidence: {claim.get('id')}")
        for ref in refs:
            if ref not in idset: fail(errors,f"claim {claim.get('id')} references unknown evidence {ref}")
        if claim.get("basis") not in {"learner_declaration","artifact","test","assessment"}: fail(errors,f"invalid claim basis: {claim.get('id')}")
    for lesson in lessons:
        for ref in lesson.get("evidence_ids",[]):
            if ref not in idset: fail(errors,f"lesson {lesson.get('number')} references unknown evidence {ref}")

    course=(ROOT/"course-map.md").read_text(encoding="utf-8") if (ROOT/"course-map.md").is_file() else ""
    sections=re.split(r"(?m)^## Lesson (\d{2}) — ",course)[1:]
    map_nums=[]
    for i in range(0,len(sections),2):
        number=int(sections[i]); body=sections[i+1].split("\n",1)[1]; map_nums.append(number)
        paragraphs=[p.strip() for p in body.split("\n\n") if p.strip() and not p.strip().startswith("**Source:**")]
        if not paragraphs: fail(errors,f"lesson {number:02d} has no note"); continue
        count=len(re.findall(r"\b[\w'-]+\b",paragraphs[0]))
        if not 80<=count<=150: fail(errors,f"lesson {number:02d} note has {count} words; expected 80-150")
    if len(map_nums)!=24 or sorted(map_nums)!=list(range(1,25)): fail(errors,"course-map.md must contain lesson headings 01-24 exactly once")

    for md in [ROOT/"README.md",ROOT/"course-map.md",*ROOT.glob("projects/*/README.md"),*ROOT.glob("provenance/*.md"),*ROOT.glob("evaluations/**/*.md")]:
        if not md.is_file(): continue
        for target in local_links(md):
            if not (md.parent/target).resolve().exists(): fail(errors,f"broken local link in {md.relative_to(ROOT)}: {target}")

    forbidden=["microsoft "+"certified","microsoft "+"certification","official "+"microsoft grade","completed with the highest score","completed all official assignments"]
    safe_markers=("no ","not ","does not","do not","did not","without","forbidden","avoid","cannot","isn't","is not")
    secret_patterns=[re.compile(r"(?i)(api[_-]?key|secret|token|password)\s*[:=]\s*['\"][A-Za-z0-9_\-]{12,}"),re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----")]
    drive_pattern=re.compile(r"(?<![A-Za-z])[A-Za-z]:[\\/]")
    for path in ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.parts: continue
        rel=path.relative_to(ROOT)
        if path.stat().st_size>1_000_000: fail(errors,f"file exceeds 1 MB: {rel}")
        if path.suffix.lower() in {".exe",".dll",".zip",".png",".jpg",".jpeg",".pdf",".docx",".bin"}: fail(errors,f"unexpected binary file: {rel}")
        if path.suffix.lower() not in TEXT_SUFFIXES and path.name not in {"LICENSE",".gitignore"}: continue
        text=path.read_text(encoding="utf-8",errors="replace")
        if path.name!="validate_portfolio.py" and drive_pattern.search(text): fail(errors,f"absolute local path found in {rel}")
        if any(p.search(text) for p in secret_patterns): fail(errors,f"possible secret found in {rel}")
        if path.name!="validate_portfolio.py":
            for line_no,line in enumerate(text.splitlines(),1):
                low=line.lower()
                for phrase in forbidden:
                    if phrase in low and not any(marker in low for marker in safe_markers): fail(errors,f"misleading phrase in {rel}:{line_no}: {phrase}")

    for name,source in PROJECTS:
        base=ROOT/"projects"/name
        if not (base/source).is_file() or not (base/"results.json").is_file(): continue
        run=subprocess.run([sys.executable,str(base/source)],cwd=base,text=True,capture_output=True)
        if run.returncode: fail(errors,f"demo failed for {name}: {run.stderr.strip()}"); continue
        try: actual=json.loads(run.stdout); saved=json.loads((base/"results.json").read_text(encoding="utf-8"))
        except Exception as exc: fail(errors,f"invalid demo/saved JSON for {name}: {exc}"); continue
        if actual!=saved: fail(errors,f"saved results do not match current execution: {name}")
    return errors

if __name__=="__main__":
    problems=validate()
    if problems:
        print("PORTFOLIO VALIDATION FAILED")
        for p in problems: print(f"- {p}")
        raise SystemExit(1)
    print("PORTFOLIO VALIDATION PASSED")

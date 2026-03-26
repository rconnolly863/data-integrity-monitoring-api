from fastapi import FastAPI
from compare import compare_data

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Data Integrity System Running"}

@app.get("/issues")
def get_issues():
    return compare_data()
@app.get("/summary")
def get_summary():
    issues = compare_data()
    return {
        "total_issues": len(issues),
        "status": "ok" if len(issues) == 0 else "issues found"
    }
@app.get("/summary")
def get_summary():
    issues = compare_data()
    return {
        "total_issues": len(issues),
        "status": "ok" if len(issues) == 0 else "issues found"
    }

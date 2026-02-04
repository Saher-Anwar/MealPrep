from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text
from api.dependencies import get_db

router = APIRouter()


@router.get("/health")
def health_check():
    """Basic health check endpoint."""
    return {"status": "healthy", "message": "API is running"}


@router.get("/db-health")
def database_health(db: Session = Depends(get_db)):
    """Check database connection."""
    try:
        db.execute(text("SELECT 1"))
        return {"status": "healthy", "message": "Database connection successful"}
    except Exception as e:
        return {"status": "unhealthy", "message": f"Database error: {str(e)}"}

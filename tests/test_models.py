import sys
from pathlib import Path

# Add the project's root directory to the module search path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from app.models import Task

def test_task_creation():
    task = Task(title="Complete homework", description="Finish math exercises")
    assert task.title == "Complete homework"
    assert task.description == "Finish math exercises"
    assert not task.completed

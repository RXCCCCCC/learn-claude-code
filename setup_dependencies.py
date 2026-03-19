#!/usr/bin/env python3
"""
Setup tasks with dependencies to demonstrate blocked order.
This creates a chain of tasks where each depends on the previous ones.
"""

import json
from pathlib import Path

WORKDIR = Path.cwd()
TASKS_DIR = WORKDIR / ".tasks"
TASKS_DIR.mkdir(exist_ok=True)

def _next_id():
    """Get the next available task ID."""
    ids = [int(f.stem.split("_")[1]) for f in TASKS_DIR.glob("task_*.json")]
    return max(ids) if ids else 0

def _save_task(task: dict):
    """Save a task to disk."""
    path = TASKS_DIR / f"task_{task['id']}.json"
    path.write_text(json.dumps(task, indent=2))

def create_task(subject: str, description: str, blocked_by: list = None, blocks: list = None):
    """Create a new task with optional dependencies."""
    task_id = _next_id() + 1
    task = {
        "id": task_id,
        "subject": subject,
        "description": description,
        "status": "pending",
        "blockedBy": blocked_by or [],
        "blocks": blocks or [],
        "owner": "",
    }
    _save_task(task)
    return task

def update_task_blocks(task_id: int, blocks: list):
    """Update a task to block other tasks."""
    path = TASKS_DIR / f"task_{task_id}.json"
    task = json.loads(path.read_text())
    task["blocks"] = blocks
    path.write_text(json.dumps(task, indent=2))

def clear_all_tasks():
    """Clear all existing tasks."""
    for f in TASKS_DIR.glob("task_*.json"):
        f.unlink()
    print("[OK] Cleared all existing tasks")

def print_task_graph():
    """Print the current task dependency graph."""
    print("\n" + "="*70)
    print("CURRENT TASK DEPENDENCY GRAPH")
    print("="*70)

    tasks = []
    for f in sorted(TASKS_DIR.glob("task_*.json")):
        tasks.append(json.loads(f.read_text()))

    tasks.sort(key=lambda t: t['id'])

    for t in tasks:
        marker = {"pending": "[ ]", "in_progress": "[>]", "completed": "[x]"}.get(t["status"], "[?]")
        blocked_info = ""
        if t.get("blockedBy"):
            blocked_info = f" [BLOCKED by {t['blockedBy']}]"
        if t.get("blocks"):
            blocked_info += f" -> blocks {t['blocks']}"
        print(f"{marker} Task #{t['id']}: {t['subject']}{blocked_info}")

    print("="*70)

    # Count blocked vs unblocked
    blocked_count = sum(1 for t in tasks if t.get("blockedBy") and t["status"] == "pending")
    ready_count = sum(1 for t in tasks if not t.get("blockedBy") and t["status"] == "pending")
    completed_count = sum(1 for t in tasks if t["status"] == "completed")

    print(f"\nSummary: {ready_count} ready to start, {blocked_count} blocked, {completed_count} completed")
    print()

if __name__ == "__main__":
    clear_all_tasks()

    print("Creating tasks with dependencies...\n")

    # Task 1: No dependencies - can start immediately
    task1 = create_task(
        "Set up project structure",
        "Create basic directory structure, configuration files, and initialize git repository"
    )
    print(f"[OK] Created Task #{task1['id']}: {task1['subject']} (no dependencies)")

    # Task 2: Depends on Task 1
    task2 = create_task(
        "Design and implement database schema",
        "Create database tables, relationships, and initial migrations",
        blocked_by=[task1['id']]
    )
    print(f"[OK] Created Task #{task2['id']}: {task2['subject']} (blocked by Task #{task1['id']})")

    # Task 3: Also depends on Task 1 (parallel branch)
    task3 = create_task(
        "Implement user authentication system",
        "Create login, registration, password reset functionality",
        blocked_by=[task1['id']]
    )
    print(f"[OK] Created Task #{task3['id']}: {task3['subject']} (blocked by Task #{task1['id']})")

    # Task 4: Depends on Task 2
    task4 = create_task(
        "Build REST API endpoints",
        "Implement CRUD operations for all resources",
        blocked_by=[task2['id']]
    )
    print(f"[OK] Created Task #{task4['id']}: {task4['subject']} (blocked by Task #{task2['id']})")

    # Task 5: Depends on both Task 3 and Task 4 (convergence point)
    task5 = create_task(
        "Build user interface",
        "Create responsive frontend with all pages and components",
        blocked_by=[task3['id'], task4['id']]
    )
    print(f"[OK] Created Task #{task5['id']}: {task5['subject']} (blocked by Tasks #{task3['id']}, #{task4['id']})")

    # Task 6: Depends on Task 5
    task6 = create_task(
        "Integration testing and deployment",
        "Run end-to-end tests and deploy to production",
        blocked_by=[task5['id']]
    )
    print(f"[OK] Created Task #{task6['id']}: {task6['subject']} (blocked by Task #{task5['id']})")

    # Now update the "blocks" references for tracking
    update_task_blocks(task1['id'], [task2['id'], task3['id']])
    update_task_blocks(task2['id'], [task4['id']])
    update_task_blocks(task3['id'], [task5['id']])
    update_task_blocks(task4['id'], [task5['id']])
    update_task_blocks(task5['id'], [task6['id']])

    print()
    print_task_graph()

    print("Dependency chain:")
    print("  Task 1 (project structure)")
    print("    |--> Task 2 (database)")
    print("    |         |--> Task 4 (API)")
    print("    |                   |--> Task 5 (UI)")
    print("    |                           |--> Task 6 (testing)")
    print("    |--> Task 3 (auth)")
    print("             |--> Task 5 (UI)")
    print("                     |--> Task 6 (testing)")
    print()
    print("Expected behavior:")
    print("  * Only Task 1 can be claimed initially")
    print("  * Task 2 and 3 remain blocked until Task 1 completes")
    print("  * Task 4 remains blocked until Task 2 completes")
    print("  * Task 5 remains blocked until BOTH Task 3 AND Task 4 complete")
    print("  * Task 6 remains blocked until Task 5 completes")

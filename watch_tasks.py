#!/usr/bin/env python3
"""
Monitor tasks and their dependency status in real-time.
Watch as teammates claim and complete tasks, respecting dependencies.
"""

import json
import time
from pathlib import Path

WORKDIR = Path.cwd()
TASKS_DIR = WORKDIR / ".tasks"

def get_tasks():
    """Load all tasks."""
    tasks = []
    for f in sorted(TASKS_DIR.glob("task_*.json")):
        tasks.append(json.loads(f.read_text()))
    return tasks

def print_task_status():
    """Print current task status."""
    tasks = get_tasks()
    tasks.sort(key=lambda t: t['id'])

    print("\n" + "="*80)
    print("TASK STATUS MONITOR")
    print("="*80)

    for t in tasks:
        marker = {"pending": "[ ]", "in_progress": "[>]", "completed": "[x]"}.get(t["status"], "[?]")
        blocked_info = ""
        if t.get("blockedBy"):
            blocked_info = f" [BLOCKED by {t['blockedBy']}]"
        else:
            blocked_info = " [READY]"
        if t.get("blocks"):
            blocked_info += f" -> blocks {t['blocks']}"
        owner_info = f" (owner: {t.get('owner', 'none')})" if t.get('owner') else " (unclaimed)"
        print(f"{marker} Task #{t['id']}: {t['subject']}{blocked_info}{owner_info}")

    print("="*80)

    # Count statuses
    pending = sum(1 for t in tasks if t["status"] == "pending" and not t.get("blockedBy"))
    blocked = sum(1 for t in tasks if t["status"] == "pending" and t.get("blockedBy"))
    in_progress = sum(1 for t in tasks if t["status"] == "in_progress")
    completed = sum(1 for t in tasks if t["status"] == "completed")

    print(f"Summary: {pending} ready to claim, {blocked} blocked, {in_progress} in progress, {completed} completed")
    print()

def dependency_chain_visual():
    """Visual representation of the dependency chain."""
    tasks = get_tasks()
    task_map = {t['id']: t for t in tasks}

    print("Dependency Chain Status:")
    print("-" * 80)

    # Task 1
    t1 = task_map.get(1)
    marker = "[x]" if t1['status'] == "completed" else ("[>]" if t1['status'] == "in_progress" else "[ ]")
    print(f"{marker} Task 1 (project structure) - {t1['status']}")

    # Task 2 and 3 (parallel)
    t2 = task_map.get(2)
    t3 = task_map.get(3)
    marker2 = "[x]" if t2['status'] == "completed" else ("[>]" if t2['status'] == "in_progress" else "[ ]")
    marker3 = "[x]" if t3['status'] == "completed" else ("[>]" if t3['status'] == "in_progress" else "[ ]")
    print(f"   |--> {marker2} Task 2 (database) - {t2['status']}")
    print(f"   |--> {marker3} Task 3 (auth) - {t3['status']}")

    # Task 4 (depends on Task 2)
    t4 = task_map.get(4)
    marker4 = "[x]" if t4['status'] == "completed" else ("[>]" if t4['status'] == "in_progress" else "[ ]")
    print(f"         |--> {marker4} Task 4 (API) - {t4['status']}")

    # Task 5 (depends on Task 3 and 4)
    t5 = task_map.get(5)
    marker5 = "[x]" if t5['status'] == "completed" else ("[>]" if t5['status'] == "in_progress" else "[ ]")
    print(f"                   |--> {marker5} Task 5 (UI) - {t5['status']}")

    # Task 6 (depends on Task 5)
    t6 = task_map.get(6)
    marker6 = "[x]" if t6['status'] == "completed" else ("[>]" if t6['status'] == "in_progress" else "[ ]")
    print(f"                           |--> {marker6} Task 6 (testing) - {t6['status']}")

    print("-" * 80)
    print()

if __name__ == "__main__":
    print("Watching tasks... Press Ctrl+C to stop")
    print()

    try:
        iteration = 0
        last_state = None

        while True:
            iteration += 1

            # Get current state
            tasks = get_tasks()
            current_state = json.dumps(tasks, sort_keys=True)

            # Only print if state changed
            if current_state != last_state:
                print(f"\n--- Iteration {iteration} --- State Changed! ---")
                print_task_status()
                dependency_chain_visual()
                last_state = current_state
            else:
                print(f"\rIteration {iteration}: No changes...", end="", flush=True)

            time.sleep(2)

    except KeyboardInterrupt:
        print("\n\nMonitoring stopped.")
        print("\nFinal state:")
        print_task_status()
        dependency_chain_visual()

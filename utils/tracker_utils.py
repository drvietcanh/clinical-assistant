"""
Utility functions for Project Tracker
Helper functions for data management, calculations, and visualizations
"""

from typing import List, Dict, Optional, Tuple
from datetime import datetime, timedelta
import json
from pathlib import Path


def calculate_phase_health(phase: Dict) -> Tuple[str, str]:
    """
    Calculate phase health status based on progress and dates
    
    Args:
        phase: Phase dictionary with progress, start_date, end_date
        
    Returns:
        Tuple of (health_status, health_color)
        - health_status: "on_track", "at_risk", "behind", "completed"
        - health_color: CSS color code
    """
    progress = phase.get('progress', 0)
    status = phase.get('status', 'not_started')
    
    # If completed, always healthy
    if status == 'completed' or progress >= 100:
        return ("completed", "#4CAF50")
    
    # If blocked, always at risk
    if status == 'blocked':
        return ("blocked", "#f44336")
    
    # Calculate expected progress based on dates
    try:
        start = datetime.strptime(phase['start_date'], '%Y-%m-%d')
        end = datetime.strptime(phase['end_date'], '%Y-%m-%d')
        now = datetime.now()
        
        # If not started yet
        if now < start:
            return ("not_started", "#9E9E9E")
        
        # If past due date
        if now > end:
            if progress < 100:
                return ("overdue", "#f44336")
            return ("completed", "#4CAF50")
        
        # Calculate expected progress
        total_days = (end - start).days
        elapsed_days = (now - start).days
        expected_progress = (elapsed_days / total_days * 100) if total_days > 0 else 0
        
        # Compare actual vs expected
        if progress >= expected_progress - 10:
            return ("on_track", "#4CAF50")
        elif progress >= expected_progress - 25:
            return ("at_risk", "#FF9800")
        else:
            return ("behind", "#f44336")
            
    except (ValueError, KeyError):
        return ("unknown", "#9E9E9E")


def calculate_overall_progress(phases: List[Dict]) -> float:
    """
    Calculate overall project progress as weighted average
    
    Args:
        phases: List of phase dictionaries
        
    Returns:
        Overall progress percentage (0-100)
    """
    if not phases:
        return 0.0
    
    total_progress = sum(p.get('progress', 0) for p in phases)
    return total_progress / len(phases)


def get_upcoming_milestones(phases: List[Dict], days: int = 30) -> List[Dict]:
    """
    Get milestones coming up in the next N days
    
    Args:
        phases: List of phase dictionaries
        days: Number of days to look ahead
        
    Returns:
        List of upcoming milestones
    """
    upcoming = []
    now = datetime.now()
    cutoff = now + timedelta(days=days)
    
    for phase in phases:
        try:
            end_date = datetime.strptime(phase['end_date'], '%Y-%m-%d')
            if now <= end_date <= cutoff:
                days_until = (end_date - now).days
                upcoming.append({
                    'phase_name': phase['name'],
                    'end_date': phase['end_date'],
                    'days_until': days_until,
                    'progress': phase.get('progress', 0),
                    'status': phase.get('status', 'not_started')
                })
        except (ValueError, KeyError):
            continue
    
    return sorted(upcoming, key=lambda x: x['days_until'])


def get_overdue_phases(phases: List[Dict]) -> List[Dict]:
    """
    Get phases that are past their due date but not completed
    
    Args:
        phases: List of phase dictionaries
        
    Returns:
        List of overdue phases
    """
    overdue = []
    now = datetime.now()
    
    for phase in phases:
        try:
            end_date = datetime.strptime(phase['end_date'], '%Y-%m-%d')
            progress = phase.get('progress', 0)
            
            if now > end_date and progress < 100:
                days_overdue = (now - end_date).days
                overdue.append({
                    'phase_name': phase['name'],
                    'end_date': phase['end_date'],
                    'days_overdue': days_overdue,
                    'progress': progress,
                    'status': phase.get('status', 'not_started')
                })
        except (ValueError, KeyError):
            continue
    
    return sorted(overdue, key=lambda x: x['days_overdue'], reverse=True)


def calculate_velocity(updates: List[Dict], days: int = 30) -> float:
    """
    Calculate project velocity (updates per week)
    
    Args:
        updates: List of update dictionaries
        days: Number of days to look back
        
    Returns:
        Updates per week
    """
    if not updates:
        return 0.0
    
    now = datetime.now()
    cutoff = now - timedelta(days=days)
    
    recent_updates = []
    for update in updates:
        try:
            update_date = datetime.strptime(update['date'], '%Y-%m-%d')
            if update_date >= cutoff:
                recent_updates.append(update)
        except (ValueError, KeyError):
            continue
    
    if not recent_updates:
        return 0.0
    
    weeks = days / 7
    return len(recent_updates) / weeks if weeks > 0 else 0


def generate_progress_report(project_data: Dict) -> Dict:
    """
    Generate comprehensive progress report
    
    Args:
        project_data: Complete project data dictionary
        
    Returns:
        Report dictionary with metrics and insights
    """
    phases = project_data.get('phases', [])
    updates = project_data.get('updates', [])
    
    # Calculate metrics
    total_phases = len(phases)
    completed_phases = len([p for p in phases if p.get('status') == 'completed'])
    in_progress_phases = len([p for p in phases if p.get('status') == 'in_progress'])
    
    overall_progress = calculate_overall_progress(phases)
    upcoming = get_upcoming_milestones(phases, days=30)
    overdue = get_overdue_phases(phases)
    velocity = calculate_velocity(updates, days=30)
    
    # Phase health breakdown
    health_breakdown = {
        'on_track': 0,
        'at_risk': 0,
        'behind': 0,
        'completed': 0,
        'blocked': 0
    }
    
    for phase in phases:
        health, _ = calculate_phase_health(phase)
        if health in health_breakdown:
            health_breakdown[health] += 1
    
    return {
        'summary': {
            'total_phases': total_phases,
            'completed_phases': completed_phases,
            'in_progress_phases': in_progress_phases,
            'overall_progress': round(overall_progress, 1),
            'velocity': round(velocity, 2)
        },
        'health': health_breakdown,
        'upcoming_milestones': upcoming,
        'overdue_phases': overdue,
        'total_updates': len(updates),
        'generated_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }


def export_to_markdown(project_data: Dict, output_file: str = "project_report.md") -> str:
    """
    Export project data to markdown report
    
    Args:
        project_data: Complete project data dictionary
        output_file: Output file path
        
    Returns:
        Path to generated file
    """
    report = generate_progress_report(project_data)
    phases = project_data.get('phases', [])
    
    md_content = [
        "# 📊 Project Progress Report",
        f"\n**Generated:** {report['generated_at']}",
        "\n---\n",
        "## 📈 Summary\n",
        f"- **Total Phases:** {report['summary']['total_phases']}",
        f"- **Completed:** {report['summary']['completed_phases']}",
        f"- **In Progress:** {report['summary']['in_progress_phases']}",
        f"- **Overall Progress:** {report['summary']['overall_progress']}%",
        f"- **Velocity:** {report['summary']['velocity']} updates/week",
        "\n---\n",
        "## 🎯 Phase Status\n"
    ]
    
    for phase in phases:
        health, color = calculate_phase_health(phase)
        md_content.append(f"\n### {phase['name']}")
        md_content.append(f"- **Progress:** {phase.get('progress', 0)}%")
        md_content.append(f"- **Status:** {phase.get('status', 'not_started')}")
        md_content.append(f"- **Health:** {health}")
        md_content.append(f"- **Timeline:** {phase.get('start_date', 'N/A')} → {phase.get('end_date', 'N/A')}")
        if phase.get('description'):
            md_content.append(f"- **Description:** {phase['description']}")
    
    # Upcoming milestones
    if report['upcoming_milestones']:
        md_content.append("\n---\n")
        md_content.append("## 📅 Upcoming Milestones (Next 30 Days)\n")
        for milestone in report['upcoming_milestones']:
            md_content.append(f"- **{milestone['phase_name']}** - Due in {milestone['days_until']} days ({milestone['end_date']})")
    
    # Overdue phases
    if report['overdue_phases']:
        md_content.append("\n---\n")
        md_content.append("## ⚠️ Overdue Phases\n")
        for overdue in report['overdue_phases']:
            md_content.append(f"- **{overdue['phase_name']}** - {overdue['days_overdue']} days overdue ({overdue['progress']}% complete)")
    
    md_content.append("\n---\n")
    md_content.append("*Generated by Clinical Assistant Project Tracker*")
    
    # Write to file
    output_path = Path(output_file)
    output_path.write_text('\n'.join(md_content), encoding='utf-8')
    
    return str(output_path)


def validate_phase_data(phase: Dict) -> Tuple[bool, List[str]]:
    """
    Validate phase data structure
    
    Args:
        phase: Phase dictionary to validate
        
    Returns:
        Tuple of (is_valid, list_of_errors)
    """
    errors = []
    
    # Required fields
    required_fields = ['id', 'name', 'start_date', 'end_date', 'status', 'progress']
    for field in required_fields:
        if field not in phase:
            errors.append(f"Missing required field: {field}")
    
    # Validate dates
    try:
        start = datetime.strptime(phase['start_date'], '%Y-%m-%d')
        end = datetime.strptime(phase['end_date'], '%Y-%m-%d')
        if start > end:
            errors.append("Start date must be before end date")
    except (ValueError, KeyError) as e:
        errors.append(f"Invalid date format: {e}")
    
    # Validate progress
    progress = phase.get('progress', 0)
    if not isinstance(progress, (int, float)) or progress < 0 or progress > 100:
        errors.append("Progress must be between 0 and 100")
    
    # Validate status
    valid_statuses = ['not_started', 'in_progress', 'completed', 'blocked']
    if phase.get('status') not in valid_statuses:
        errors.append(f"Status must be one of: {', '.join(valid_statuses)}")
    
    return (len(errors) == 0, errors)


def suggest_next_actions(project_data: Dict) -> List[str]:
    """
    Suggest next actions based on project state
    
    Args:
        project_data: Complete project data dictionary
        
    Returns:
        List of suggested actions
    """
    suggestions = []
    phases = project_data.get('phases', [])
    updates = project_data.get('updates', [])
    
    # Check for overdue phases
    overdue = get_overdue_phases(phases)
    if overdue:
        suggestions.append(f"⚠️ {len(overdue)} phase(s) are overdue - review and update status")
    
    # Check for stale updates
    if updates:
        try:
            last_update = max(updates, key=lambda x: x['date'])
            last_date = datetime.strptime(last_update['date'], '%Y-%m-%d')
            days_since = (datetime.now() - last_date).days
            if days_since > 7:
                suggestions.append(f"📝 No updates in {days_since} days - consider adding a status update")
        except (ValueError, KeyError):
            pass
    else:
        suggestions.append("📝 No updates yet - add your first project update")
    
    # Check for phases without progress
    no_progress = [p for p in phases if p.get('progress', 0) == 0 and p.get('status') != 'not_started']
    if no_progress:
        suggestions.append(f"📊 {len(no_progress)} phase(s) marked as started but have 0% progress")
    
    # Check upcoming milestones
    upcoming = get_upcoming_milestones(phases, days=14)
    if upcoming:
        suggestions.append(f"📅 {len(upcoming)} milestone(s) due in next 2 weeks - ensure on track")
    
    # Check for phases with no description
    no_desc = [p for p in phases if not p.get('description')]
    if no_desc:
        suggestions.append(f"📝 {len(no_desc)} phase(s) missing descriptions - add details")
    
    return suggestions if suggestions else ["✅ Everything looks good! Keep up the great work!"]

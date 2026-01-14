"""
Protocol version tracking (lightweight, no DB)

We avoid refactoring the protocol schema by keeping an external registry keyed
by a stable protocol_id derived from (site, severity, setting, title).
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List, Optional

from .protocols_schema import AntibioticProtocol


@dataclass(frozen=True)
class ProtocolVersionInfo:
    protocol_id: str
    version: str  # semantic-ish version string
    last_updated: str  # YYYY-MM-DD
    author: Optional[str] = None
    reason: Optional[str] = None
    changelog_md: Optional[str] = None


def make_protocol_id(protocol: AntibioticProtocol) -> str:
    """
    Create a stable ID for a protocol.
    """
    site = getattr(protocol.infection_site, "value", str(protocol.infection_site))
    sev = getattr(protocol.severity, "value", str(protocol.severity))
    setting = getattr(protocol.setting, "value", str(protocol.setting))
    title = (protocol.title or "").strip().lower().replace(" ", "_")
    return f"{site}:{sev}:{setting}:{title}"


# Registry: add entries only for protocols you want to explicitly version.
# Others will get default version info.
_REGISTRY: Dict[str, ProtocolVersionInfo] = {
    # Example entries (can expand over time)
    "CAP:MILD:OPD:cap_non-severe_(outpatient)".replace("-", "_"): ProtocolVersionInfo(
        protocol_id="CAP:MILD:OPD:cap_non_severe_(outpatient)",
        version="1.0.0",
        last_updated="2026-01-10",
        author="AI Assistant",
        reason="Initial structured protocol card",
        changelog_md="- Chuẩn hoá regimen + step-down options.\n",
    ),
}


def get_protocol_version_info(protocol: AntibioticProtocol) -> ProtocolVersionInfo:
    pid = make_protocol_id(protocol)
    # Normalize to reduce accidental mismatches
    pid_norm = pid.replace("-", "_")
    info = _REGISTRY.get(pid_norm)
    if info:
        return info
    return ProtocolVersionInfo(
        protocol_id=pid,
        version="1.0.0",
        last_updated=protocol.last_reviewed or (str(protocol.guideline_year) if protocol.guideline_year else "N/A"),
        author=None,
        reason=None,
        changelog_md=None,
    )


def get_protocol_changelog(protocol: AntibioticProtocol) -> Optional[str]:
    return get_protocol_version_info(protocol).changelog_md


def list_versioned_protocols() -> List[ProtocolVersionInfo]:
    return list(_REGISTRY.values())


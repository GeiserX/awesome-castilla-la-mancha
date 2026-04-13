#!/usr/bin/env python3
"""Transform awesome-castilla-la-mancha README entries with metadata (stars, license, language, institution tags, demos)."""

import json
import re
import sys

# Load metadata
with open("scripts/metadata.json") as f:
    metadata = json.load(f)

# Section -> default institution/location tags
SECTION_TAGS = {
    "Administración y Gobierno Regional": ["JCCM"],
    "Cultura y Patrimonio": [],
    "Datos Abiertos y Estadísticas": [],
    "Educación": [],
    "Energía y Medio Ambiente": [],
    "Sanidad": ["SESCAM"],
    "Transporte y Movilidad": [],
    "Universidad e Investigación": [],
}

# Keyword -> tag overrides/additions (applied per-entry based on name + description)
KEYWORD_TAGS = {
    "JCCM": "JCCM",
    "Junta de Comunidades": "JCCM",
    "Gobierno de Castilla": "JCCM",
    "presupuestos": "JCCM",
    "DOCM": "JCCM",
    "UCLM": "UCLM",
    "Universidad de Castilla": "UCLM",
    "ESI-UCLM": "UCLM",
    "ESI Ciudad Real": "UCLM",
    "EIIA": "UCLM",
    "SESCAM": "SESCAM",
    "Servicio de Salud de Castilla": "SESCAM",
    "Toledo": "Toledo",
    "GDG Toledo": "Toledo",
    "Albacete": "Albacete",
    "Ciudad Real": "Ciudad Real",
    "Cuenca": "Cuenca",
    "Guadalajara": "Guadalajara",
    "Talavera": "Talavera",
    "Puertollano": "Puertollano",
    "Tomelloso": "Tomelloso",
    "Alcázar de San Juan": "Alcázar",
    "CLM": "JCCM",
    "Castilla-La Mancha": "JCCM",
    "TomellosoTech": "Tomelloso",
    "Civio": "Civio",
    "SAO": "SAO",
    "Sociedad Albacetense de Ornitología": "SAO",
}

# Tag -> URL for clickable badges
TAG_URLS = {
    "JCCM": "https://www.castillalamancha.es/",
    "UCLM": "https://www.uclm.es/",
    "SESCAM": "https://sescam.castillalamancha.es/",
    "Toledo": "https://www.toledo.es/",
    "Albacete": "https://www.albacete.es/",
    "Ciudad Real": "https://www.ciudadreal.es/",
    "Cuenca": "https://www.cuenca.es/",
    "Guadalajara": "https://www.guadalajara.es/",
    "Talavera": "https://www.talavera.es/",
    "Puertollano": "https://www.puertollano.es/",
    "Tomelloso": "https://www.tomelloso.es/",
    "Alcázar": "https://www.alcazardesanjuan.es/",
    "Civio": "https://civio.es/",
    "SAO": "https://sao-albacete.org/",
}

# Normalize language names
LANG_MAP = {
    "Jupyter Notebook": "Python",
    "GLSL": None,
    "Makefile": None,
    "Dockerfile": None,
    "Shell": None,
    "Batchfile": None,
    "Nix": None,
    "CMake": None,
    "Smarty": "PHP",
    "Mustache": "JavaScript",
    "Vue": "JavaScript",
    "Svelte": "JavaScript",
    "CSS": None,
    "SCSS": None,
    "Sass": None,
    "Less": None,
    "Roff": None,
    "PLpgSQL": "SQL",
    "TSQL": "SQL",
    "HCL": "Terraform",
    "Gherkin": None,
    "Groovy": "Java",
    "Scala": "Scala",
    "Elixir": "Elixir",
    "Erlang": "Erlang",
    "Haskell": "Haskell",
    "Lua": "Lua",
    "Perl": "Perl",
    "Dart": "Dart",
    "Swift": "Swift",
    "Objective-C": "Objective-C",
    "Assembly": None,
    "Fortran": "Fortran",
    "Mathematica": None,
    "TeX": None,
    "Jinja": "Python",
    "Starlark": None,
}

# License normalization
LICENSE_MAP = {
    "NOASSERTION": None,
    "0BSD": "0BSD",
}

# Demo URLs for known projects
DEMO_URLS = {}


def encode_tag(tag):
    """Encode tag name for shields.io badge URL."""
    return tag.replace("-", "--").replace("_", "__").replace(" ", "%20").replace("+", "%2B")


def get_clm_tags(section_name, entry_name, description):
    """Determine institution/location tags for an entry."""
    tags = set()

    # Add section defaults
    if section_name in SECTION_TAGS:
        tags.update(SECTION_TAGS[section_name])

    # Scan description + name for keyword matches
    text = f"{entry_name} {description}"
    for keyword, tag in KEYWORD_TAGS.items():
        if keyword in text:
            tags.add(tag)

    # Remove overly broad "JCCM" tag if more specific tags are present
    specific_clm = {"UCLM", "SESCAM", "Toledo", "Albacete", "Ciudad Real", "Cuenca", "Guadalajara", "Talavera", "Puertollano", "Tomelloso", "Alcázar", "Civio", "SAO"}
    if "JCCM" in tags and tags & specific_clm:
        tags.discard("JCCM")

    return sorted(tags)


def get_language(owner_repo):
    """Get normalized language for a repo."""
    meta = metadata.get(owner_repo, {})
    lang = meta.get("language", "")
    if not lang:
        return None
    if lang in LANG_MAP:
        return LANG_MAP[lang]
    return lang


def get_license(owner_repo):
    """Get license SPDX ID for a repo."""
    meta = metadata.get(owner_repo, {})
    lic = meta.get("license", "")
    if not lic:
        return None
    if lic in LICENSE_MAP:
        return LICENSE_MAP[lic]
    return lic


def get_default_branch(owner_repo):
    """Get default branch for a repo."""
    meta = metadata.get(owner_repo, {})
    return meta.get("default_branch", "main")


def get_demo_url(owner_repo):
    """Get demo URL if available."""
    return DEMO_URLS.get(owner_repo)


def transform_entry(line, current_section):
    """Transform a single entry line with metadata."""
    # Badge patterns: handle both clickable [![alt](img)](link) and plain ![alt](img)
    badge_pat = r'(?:\[!\[[^\]]*\]\([^)]+\)\]\([^)]+\)|!\[[^\]]*\]\([^)]+\))'
    demo_pat = r'\(\[Demo\]\([^)]+\)\)'

    m = re.match(
        rf'^- \[([^\]]+)\]\((https://github\.com/([^)]+))\)\s+'
        rf'(?:{badge_pat}\s*)*'
        rf'(?:{demo_pat}\s*)?'
        rf'- (.+)$',
        line
    )
    if not m:
        m = re.match(r'^- \[([^\]]+)\]\((https://github\.com/([^)]+))\) - (.+)$', line)
    if not m:
        return line

    name = m.group(1)
    url = m.group(2)
    owner_repo = m.group(3)
    raw_desc = m.group(4)

    # Strip any existing backtick tags and demo links from description
    description = re.sub(r'\s*\(\[Demo\]\([^)]+\)\)', '', raw_desc)
    description = re.sub(r'\s*`[^`]+`', '', description).strip()

    # Clickable auto-updating shields.io badges
    branch = get_default_branch(owner_repo)
    star_badge = f"[![Stars](https://img.shields.io/github/stars/{owner_repo}?style=flat-square&label=%E2%AD%90)](https://github.com/{owner_repo}/stargazers)"
    commit_badge = f"[![Last Commit](https://img.shields.io/github/last-commit/{owner_repo}?style=flat-square)](https://github.com/{owner_repo}/commits/{branch})"
    lang_badge = f"[![Language](https://img.shields.io/github/languages/top/{owner_repo}?style=flat-square)](https://github.com/{owner_repo})"
    license_badge = f"[![License](https://img.shields.io/github/license/{owner_repo}?style=flat-square)](https://github.com/{owner_repo}/blob/{branch}/LICENSE)"

    # Institution/location tags as clickable CLM red badges
    clm_tags = get_clm_tags(current_section, name, raw_desc)
    tag_badge_parts = []
    for t in clm_tags:
        encoded = encode_tag(t)
        if t in TAG_URLS:
            tag_badge_parts.append(
                f"[![{t}](https://img.shields.io/badge/{encoded}-8B0000?style=flat-square)]({TAG_URLS[t]})"
            )
        else:
            tag_badge_parts.append(
                f"![{t}](https://img.shields.io/badge/{encoded}-8B0000?style=flat-square)"
            )
    tag_badges = " ".join(tag_badge_parts)

    # Demo link
    demo = get_demo_url(owner_repo)
    demo_str = f" ([Demo]({demo}))" if demo else ""

    # Build: Name + clickable auto-badges + institution tags + demo + description
    parts = [f"- [{name}]({url}) {star_badge} {commit_badge} {lang_badge} {license_badge}"]
    if tag_badges:
        parts[0] += f" {tag_badges}"
    if demo_str:
        parts[0] += demo_str
    parts[0] += f" - {description}"

    return parts[0]


def main():
    with open("README.md") as f:
        lines = f.readlines()

    output = []
    current_section = ""

    for line in lines:
        stripped = line.rstrip("\n")

        # Track current section
        section_match = re.match(r'^## (.+)$', stripped)
        if section_match:
            current_section = section_match.group(1)

        # Transform entry lines
        if stripped.startswith("- [") and "github.com/" in stripped and "](#" not in stripped:
            transformed = transform_entry(stripped, current_section)
            output.append(transformed + "\n")
        else:
            output.append(line)

    with open("README.md", "w") as f:
        f.writelines(output)

    print(f"Transformed README.md")


# Known demo URLs
DEMO_URLS.update({
})

if __name__ == "__main__":
    main()

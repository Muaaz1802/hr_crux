from hr_crux.settings import TEMPLATES

TEMPLATES[0]["OPTIONS"]["context_processors"].append(
    "hr_crux_crumbs.context_processors.breadcrumbs",
)

from typing import Any, Dict

from flaskerize import SchematicRenderer


def run(renderer: SchematicRenderer, context: Dict[str, Any]) -> None:
    template_files = renderer.get_template_files()

    for filename in template_files:
        renderer.render_from_file(filename, context=context)
    renderer.print_summary()

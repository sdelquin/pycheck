{{title}}
{% if returns_file %}
import filecmp
{% endif %}
{% if params_have_files or returns_file %}
from pathlib import Path
{% endif %}


def {{func}}():
    {% if returns_file %}
    {{output_placeholder}}
    {% endif %}
    # TU CÓDIGO AQUÍ

    {% if returns_file %}
    return {{return_items}}
    {% endif %}

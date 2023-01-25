{{title}}
{% if returns_file %}
import filecmp
{% endif %}
{% if params_have_files or returns_file %}
from pathlib import Path
{% endif %}


def {{func}}({{params}}) -> {{return_type}}:
    {% if returns_file %}
    {{output_placeholder}}
    # TU CÓDIGO AQUÍ
    {% else %}
    # TU CÓDIGO AQUÍ
    {{output_placeholder}}
    {% endif %}

    return {{return_items}}


if __name__ == '__main__':
    {{func}}({{args}})

{{title}}
{% if output_is_file %}
import filecmp
from pathlib import Path
{% endif %}


def {{func}}({{params}}) -> {{return_type}}:
    {% if output_is_file %}
    {{output_placeholder}}
    # TU CÓDIGO AQUÍ
    {% else %}
    # TU CÓDIGO AQUÍ
    {{output_placeholder}}
    {% endif %}

    return {{return_items}}


if __name__ == '__main__':
    {{func}}({{args}})

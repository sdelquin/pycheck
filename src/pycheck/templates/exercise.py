{{title}}


def {{func}}({{params}}) -> {{return_type}}:
    # TU CÓDIGO AQUÍ
{% if return_type != 'None' %}
    {{output_placeholder}}
    {{return_sentence}}
{% endif %}


if __name__ == '__main__':
    {{func}}({{args}})



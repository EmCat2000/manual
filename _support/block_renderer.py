"""
Render the help page for a given block.

# print(dir(get_ipython()))
"""

import yaml
import os
from IPython.display import Markdown, display

def get_block_data(filename=None):
    """Extract partial-data from current Quarto file"""
    if not filename:
        filename = os.environ.get('QUARTO_DOCUMENT_FILE')
        filepath = os.environ.get('QUARTO_DOCUMENT_PATH')
        filename = os.path.join(filepath, filename)

    with open(filename, 'r') as f:
        content = f.read()

    if content.startswith('---'):
        yaml_end = content.find('\n---', 4)
        if yaml_end != -1:
            yaml_str = content[4:yaml_end]
            full_yaml = yaml.safe_load(yaml_str)
            return full_yaml
    return {}

def render_block_markdown(yaml_data):
    """Generate markdown content from block YAML data"""

    # TODO: this is because we want to possible support quarto-partials.
    yaml_data = yaml_data.get('partial-data', {})
    description = yaml_data.get('block_description', 'No description')
    label = yaml_data.get('label', 'Unknown block')
    selector = yaml_data.get('selector', 'unknown')
    help_screen = yaml_data.get('help_screen', 'default.png')


    example_images = yaml_data.get('example_images', [])
    example_images_md = []
    if example_images:
        for img in example_images:
            description = img.get('description', 'Example')
            image_path = img.get('image', '')
            example_images_md.append(f'![{description}]({image_path})')
    else:
        example_images_md.append("No examples yet.")



    example_projects = yaml_data.get('example_projects', [])
    example_projects_md = []
    if example_projects:
        for project in example_projects:
            title = project.get('title', 'Untitled Project')
            url = project.get('url', '#')
            example_projects_md.append(f'* [{title}]({url})')
    else:
        example_projects_md.append("No examples yet.")

    # TODO: Make the block image smaller in the PDF.
    # TODO: Figure out how to detect the output format.
    no_index = '{.unnumbered .unlisted }'
    _html_visible = '{.content-visible when-format=html"}'
    return f'''
{description}

![The "{label}" block](/blocks/images/block_{selector}.png)

![help screen for the block "{label}"](../help/{help_screen})

## Example Images{no_index}
{'\n'.join(example_images_md)}

## Example Projects{no_index}
These example projects show the block in the context of a larger project. They will contain other blocks, too.

{'\n'.join(example_projects_md)}

<hr>
<em>Individual pages for each block are new. Most blocks don't yet additional links and images. If you have any questions, please post in the <a href="https://forum.snap.berkeley.edu/c/help/snap-help/49"><span class="snap">Snap</span> forum</a>.</em>
    '''

def render_block():
    """Main function to render block from current file"""
    yaml_data = get_block_data()
    markdown_output = render_block_markdown(yaml_data)
    # display(Markdown(markdown_output))
    # print(f'<code>{os.environ}</code>')
    print(markdown_output)

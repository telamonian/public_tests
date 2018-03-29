#!/usr/bin/env python3
"""string.Template example script that can produce an output
with any combination of three html blocks with templated values.

Written for https://stackoverflow.com/q/49560083/425458
"""

from string import Template

useBlocks = [1,1,2,0]
valDict = {
    'link0': 'the other block is dumb',
    'link1': 'don\'t go there',
    'radio0': 'does nothing',
    'radio1': 'more nothing',
    'anchor0': 'yaaaay',
    'anchor1': 'wooooo',
}
blocks = []

# html block 0
blocks.append([
    r'<h1> Block 0: links to block 2 </h1>',
    r"<p><a href='#$anchor0'> $link0 </a></p>",
    r"<p><a href='#$anchor1'> $link1 </a></p>",
])

# html block 1
blocks.append([
    r'<h1> Block 1: pointless radios </h1>',
    r"<p><input type='radio' id='radioButton0'> $radio0 </p>",
    r"<p><input type='radio' id='radioButton1'> $radio1 </p>",
])

# html block 2
blocks.append([
    r'<h1> Block 2: anchors from block 0 </h1>',
    r"<p><a id='$anchor0'> $anchor0 </a></p>",
    r"<p><a id='$anchor1'> $anchor1 </a></p>",
])


# outer html tags
htmlTagsOpen = '\n'.join([
    r'<html>',
    r'  <body>',
])
htmlTagsClose = '\n'.join([
    r'  </body>',
    r'</html>',
])

# start the html code off with the outer tags open
htmlBody = htmlTagsOpen + '\n'

# for each block specified in useBlocks, indent the lines and join them
for block in (blocks[i] for i in useBlocks):
    for line in block:
        htmlBody += ' '*4 + line + '\n'
    htmlBody += '\n'

# add the outer tags close
htmlBody += htmlTagsClose

# substitue any templated values in the html and output
print(Template(htmlBody).substitute(valDict))

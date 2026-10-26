"""Normalize math alignment used only for line wrapping in handout layouts.

Matrix, array, and cases separators remain substantive. Only alignment markers
outside those structures and aligned/split wrappers may change in layout edits.
"""

def math_layout_tokens(tokens):
    tokens=list(tokens)
    result=[]
    protected=[]
    matrices={'array','matrix','pmatrix','bmatrix','Bmatrix','vmatrix','Vmatrix','cases','smallmatrix'}
    wrappers={'aligned','split'}
    i=0
    while i<len(tokens):
        if i+3<len(tokens) and tokens[i] in (r'\begin',r'\end') and tokens[i+1]=='{' and tokens[i+3]=='}':
            command,env=tokens[i],tokens[i+2]
            if env in matrices:
                if command==r'\begin':protected.append(env)
                elif protected and protected[-1]==env:protected.pop()
            if env in wrappers and not protected:
                i+=4
                continue
            result.extend(tokens[i:i+4]);i+=4
            continue
        if not protected and tokens[i] in ('&',r'\\'):
            i+=1
            continue
        result.append(tokens[i]);i+=1
    return tuple(result)

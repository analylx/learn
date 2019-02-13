import textwrap

sample_text = '''
    The textwrap module can be used to format text for output in
    situations where pretty-printing is desired.  It offers
    programmatic functionality similar to the paragraph wrapping
    or filling features found in many text editors.
    '''
print(textwrap.fill(sample_text,width=50))

dedented_text = textwrap.dedent(sample_text)
print('Dedented:')
print(dedented_text)
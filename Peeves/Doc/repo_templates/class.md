## <a id="{id}">{name}</a> 

{include$:'includes/source_links.md'}

{description}
{include$:'includes/parameters.md'}

{%:prop_list=code(loop_template(
    "{{0[0]}}: {{0[1]}}",
    [[p[0], p[1].__name__ if isinstance(p[1], type) else type(p[1])] for p in props],
    joiner="""
"""
))}

{%:method_list=[
    m.handle(write=False).strip()
    for m in methods
]}

{#:Mini-API that will produce Bootstrap elements}
{collapse$:
    "### Methods and Properties", 
    prop_list + "\n" + join(method_list, joiner="\n\n\n"),
    name="methods"
}

{include$:'includes/footer.md'}
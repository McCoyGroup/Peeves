{$: collapse("## Details", details, open=False) if nonempty(details) else ""}

{$: "## Examples" if nonempty(examples) or nonempty(tests) else ""}
{$: examples if nonempty(examples) else ""}
{$: include('includes/tests.md') if nonempty(tests) else ""}

{%: related_links=[(canonical_name(r.strip()), canonical_link(r.strip())) for r in related.split(",") if len(r.strip()) > 0]}
{$: alert(
    "**See Also:** " + loop_template("[`{{0[0]}}`]({{0[1]}})", related_links, joiner="<span>&nbsp;&#9642;&nbsp;</span>"),
    variant='info'
)
    if len(related_links) > 0 else ""
}

---

{include$:'includes/edit_links.md'}
{$:description if nonempty(description) else """
# {gh_repo}

This is (partial) documentation for the {gh_repo} package.
The listing here is automatically generated by our [Peeves](https://github.com/McCoyGroup/Peeves) testing/documentation helper package.
"""
}

#### API Reference

{loop_template$:'- [{{0[0]}}]({{0[1]}})', index_files, joiner='\n'}

{$: "## Examples\n" + examples if nonempty(examples) else ""}

{include$:'includes/contrib_info.md'}


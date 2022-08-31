# Peeves

Peeves is a documentation and unit testing package.
It started out as a very small layer on the `unittest` framework but now
supports the documentation for itself, as well as the [`Psience`](https://mccoygroup.github.io/Psience/) and [`McUtils`](https://mccoygroup.github.io/McUtils/) packages.
To use Peeves in your own projects, install via `pip`

```shell
pip install mccoygroup-peeves
```

and then to use Peeves to manage your unit tests, follow the pattern laid out in the [`ci/tests` directory](https://github.com/McCoyGroup/Peeves/tree/master/ci/tests).
You can also look at what was done for the [`McUtils` project](https://github.com/McCoyGroup/McUtils/tree/master/ci/tests).

To use the documentation generator, follow the pattern laid out in the [documentation build script](https://github.com/McCoyGroup/Peeves/tree/master/ci/build_docs).

API Reference:

- [Peeves](Peeves.md)



### Help Us Out!

The easiest way to help us out is to _give feedback_.
Each page _should_ support examples, but unfortunately most do not, simply because writing that kind of thing by hand is time consuming.
If you see a page without examples and you want some, let us know!
To do that, just open and [issue on GitHub]((https://github.com/McCoyGroup/Peeves/issues/new?title=Documentation%20Improvement%20Needed)).
You can use the `Feedback` button at the bottom of each page to do so.

If you want to be a bit more proactive, feel free to provide examples and docstrings yourself! 
There are links at the bottom of each page to edit the examples, templates, and docstrings for that page.
Just create a new one if needed or edit the old one, commit your changes, and `Peeves` will rebuild the site
which what you've added.
It is a huge, huge help, so please take advantage of the opportunity if you're looking for ways to get involved.


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
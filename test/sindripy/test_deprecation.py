import warnings

from expects import be_empty, contain, expect


class TestSindripyDeprecation:
    def test_import_triggers_deprecation_warning(self) -> None:
        with warnings.catch_warnings(record=True) as caught_warnings:
            warnings.simplefilter("always")

            import sindripy  # noqa: F401

            sindripy_related = [
                w
                for w in caught_warnings
                if issubclass(w.category, FutureWarning) and "sindripy is deprecated" in str(w.message)
            ]

        expect(sindripy_related).not_to(be_empty)
        expect(str(sindripy_related[0].message)).to(contain("value-object-sindri"))
        expect(str(sindripy_related[0].message)).to(contain("object-mother-sindri"))
